#!/usr/bin/env python3

import re
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

# ============================================================
# ShadowScan OSINT
# Public Username Footprint Scanner
# Version: 1.0
# ============================================================

VERSION = "1.0"

SITES = {
    "GitHub": "https://github.com/{u}",
    "GitLab": "https://gitlab.com/{u}",
    "Reddit": "https://www.reddit.com/user/{u}/",
    "Codeberg": "https://codeberg.org/{u}",
    "Dev.to": "https://dev.to/{u}",
    "Medium": "https://medium.com/@{u}",
    "Twitch": "https://www.twitch.tv/{u}",
    "Pinterest": "https://www.pinterest.com/{u}/",
    "Gravatar": "https://gravatar.com/{u}",
    "PyPI": "https://pypi.org/user/{u}/",
}

TIMEOUT = 8

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Linux; Android) "
        "AppleWebKit/537.36 "
        "Chrome/120.0 Mobile Safari/537.36 "
        "ShadowScan/1.0"
    )
}


# ------------------------------------------------------------
# Colors
# ------------------------------------------------------------

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
GRAY = "\033[90m"
BOLD = "\033[1m"


def color(text, colour):
    return f"{colour}{text}{RESET}"


# ------------------------------------------------------------
# Banner
# ------------------------------------------------------------

def banner():

    print()

    print(color(
        r"""
 ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
 ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
 ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
 ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝

              SHADOWSCAN OSINT
        PUBLIC USERNAME FOOTPRINT SCANNER
        """,
        CYAN
    ))

    print(color(f"Version {VERSION}", GRAY))
    print()


# ------------------------------------------------------------
# Username validation
# ------------------------------------------------------------

def validate_username(username):

    if not username:
        return False

    # Common username characters.
    # Maximum length is kept conservative.
    pattern = r"^[A-Za-z0-9._-]{1,39}$"

    return bool(re.fullmatch(pattern, username))


# ------------------------------------------------------------
# HTTP checker
# ------------------------------------------------------------

def check_site(site):

    name, template = site

    url = template.format(u=USERNAME)

    request = urllib.request.Request(
        url,
        headers=HEADERS,
        method="GET"
    )

    try:

        with urllib.request.urlopen(
            request,
            timeout=TIMEOUT
        ) as response:

            status = response.status

            # Any successful HTTP response is only a lead.
            if 200 <= status < 400:

                return {
                    "name": name,
                    "url": url,
                    "status": "FOUND",
                    "http": status
                }

            return {
                "name": name,
                "url": url,
                "status": "UNKNOWN",
                "http": status
            }

    except urllib.error.HTTPError as error:

        code = error.code

        # These responses can occur for protected,
        # rate-limited or otherwise special pages.
        if code in (401, 403, 429):

            return {
                "name": name,
                "url": url,
                "status": "UNKNOWN",
                "http": code
            }

        if code == 404:

            return {
                "name": name,
                "url": url,
                "status": "NOT FOUND",
                "http": code
            }

        return {
            "name": name,
            "url": url,
            "status": "UNKNOWN",
            "http": code
        }

    except urllib.error.URLError as error:

        return {
            "name": name,
            "url": url,
            "status": "ERROR",
            "http": str(error.reason)
        }

    except Exception as error:

        return {
            "name": name,
            "url": url,
            "status": "ERROR",
            "http": type(error).__name__
        }


# ------------------------------------------------------------
# Display result
# ------------------------------------------------------------

def display_result(result):

    name = result["name"]
    url = result["url"]
    status = result["status"]
    http = result["http"]

    if status == "FOUND":

        icon = color("[+]", GREEN)
        state = color("FOUND", GREEN)

    elif status == "NOT FOUND":

        icon = color("[-]", RED)
        state = color("NOT FOUND", RED)

    elif status == "UNKNOWN":

        icon = color("[?]", YELLOW)
        state = color("UNKNOWN", YELLOW)

    else:

        icon = color("[!]", RED)
        state = color("ERROR", RED)

    print(
        f"{icon} "
        f"{name:<12} "
        f"{state:<20} "
        f"{url}"
    )

    print(
        f"    {color('HTTP:', GRAY)} {http}"
    )


# ------------------------------------------------------------
# Save report
# ------------------------------------------------------------

def save_report(results):

    filename = f"shadowscan_{USERNAME}.txt"

    try:

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write("SHADOWSCAN OSINT REPORT\n")
            file.write("=" * 60 + "\n\n")

            file.write(
                f"Username: {USERNAME}\n"
            )

            file.write(
                f"Version: {VERSION}\n\n"
            )

            for result in results:

                file.write(
                    f"{result['name']}: "
                    f"{result['status']} | "
                    f"{result['url']} | "
                    f"HTTP {result['http']}\n"
                )

            file.write("\n")
            file.write(
                "NOTE: Results indicate public URL responses only.\n"
            )
            file.write(
                "They do not prove that a profile belongs to a "
                "particular person.\n"
            )

        return filename

    except Exception as error:

        print(
            color(
                f"[!] Could not save report: {error}",
                RED
            )
        )

        return None


# ------------------------------------------------------------
# Scanner
# ------------------------------------------------------------

def scan_username(username):

    global USERNAME

    USERNAME = username

    print(
        color(
            f"[*] Target username: {USERNAME}",
            WHITE
        )
    )

    print(
        color(
            "[*] Checking public profile URLs...",
            CYAN
        )
    )

    print(
        color(
            "[*] No login or private-data access is performed.",
            GRAY
        )
    )

    print()
    print(color("-" * 75, GRAY))
    print()

    results = []

    # Parallel requests make the scanner considerably faster.
    with ThreadPoolExecutor(max_workers=6) as executor:

        futures = [
            executor.submit(
                check_site,
                site
            )
            for site in SITES.items()
        ]

        for future in as_completed(futures):

            try:

                result = future.result()

                results.append(result)

            except Exception as error:

                print(
                    color(
                        f"[!] Scanner error: {error}",
                        RED
                    )
                )

    # Keep output in the same order as SITES.
    order = {
        name: index
        for index, name in enumerate(SITES.keys())
    }

    results.sort(
        key=lambda item: order.get(
            item["name"],
            999
        )
    )

    for result in results:

        display_result(result)

        print()

    # Statistics
    found = sum(
        1 for result in results
        if result["status"] == "FOUND"
    )

    not_found = sum(
        1 for result in results
        if result["status"] == "NOT FOUND"
    )

    unknown = sum(
        1 for result in results
        if result["status"] == "UNKNOWN"
    )

    errors = sum(
        1 for result in results
        if result["status"] == "ERROR"
    )

    print(color("=" * 75, GRAY))

    print(
        color(
            "SCAN SUMMARY",
            BOLD + CYAN
        )
    )

    print()

    print(
        f"Checked     : {len(results)}"
    )

    print(
        color(
            f"Found       : {found}",
            GREEN
        )
    )

    print(
        color(
            f"Not Found   : {not_found}",
            RED
        )
    )

    print(
        color(
            f"Unknown     : {unknown}",
            YELLOW
        )
    )

    print(
        color(
            f"Errors      : {errors}",
            RED
        )
    )

    print()

    # Save report
    report = save_report(results)

    if report:

        print(
            color(
                f"[+] Report saved: {report}",
                GREEN
            )
        )

    print()

    print(
        color(
            "Important: A FOUND result does not prove ownership.",
            YELLOW
        )
    )

    print(
        color(
            "Verify identity independently using lawful public sources.",
            YELLOW
        )
    )

    print()


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

def main():

    banner()

    if len(sys.argv) > 1:

        username = sys.argv[1].strip()

    else:

        username = input(
            color(
                "Enter username: ",
                WHITE
            )
        ).strip()

    # Remove @ if user enters @username.
    username = username.lstrip("@")

    if not validate_username(username):

        print()

        print(
            color(
                "[!] Invalid username.",
                RED
            )
        )

        print(
            color(
                "Use letters, numbers, '.', '_' or '-'.",
                GRAY
            )
        )

        print()

        sys.exit(1)

    try:

        scan_username(username)

    except KeyboardInterrupt:

        print()

        print(
            color(
                "[!] Scan cancelled.",
                YELLOW
            )
        )

        print()

        sys.exit(0)


# ------------------------------------------------------------

if __name__ == "__main__":
    main()
