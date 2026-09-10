#!/usr/bin/env python3

import os
import re
import sys
import time
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed


# ============================================================
# SHADOWSCAN OSINT
# Public Username Footprint Scanner
# Version 3.0
# Developer: Dhannjay Uphade
# ============================================================

VERSION = "3.0"

DEVELOPER = "Dhannjay Uphade"
WEBSITE = "https://dhannjayuphade.github.io/"
GITHUB = "https://github.com/dhannjayuphade/shadowscan-osint"
EMAIL = "dhannjayuphade5@gmail.com"


# ============================================================
# PUBLIC PLATFORMS
# ============================================================

PLATFORMS = {
    "Instagram": "https://www.instagram.com/{u}/",
    "Facebook": "https://www.facebook.com/{u}",
    "YouTube": "https://www.youtube.com/@{u}",
    "X / Twitter": "https://x.com/{u}",
    "TikTok": "https://www.tiktok.com/@{u}",
    "Reddit": "https://www.reddit.com/user/{u}/",
    "GitHub": "https://github.com/{u}",
    "GitLab": "https://gitlab.com/{u}",
    "LinkedIn": "https://www.linkedin.com/in/{u}/",
    "Pinterest": "https://www.pinterest.com/{u}/",
    "Twitch": "https://www.twitch.tv/{u}",
    "Medium": "https://medium.com/@{u}",
    "Dev.to": "https://dev.to/{u}",
    "Telegram": "https://t.me/{u}",
    "Snapchat": "https://www.snapchat.com/add/{u}",
    "ShareChat": "https://sharechat.com/profile/{u}",
    "Codeberg": "https://codeberg.org/{u}",
    "PyPI": "https://pypi.org/user/{u}/",
    "Gravatar": "https://gravatar.com/{u}",
}


TIMEOUT = 8

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Linux; Android 13) "
        "AppleWebKit/537.36 "
        "Chrome/120.0 Mobile Safari/537.36 "
        "ShadowScan/3.0"
    )
}


# ============================================================
# TERMINAL COLORS
# ============================================================

RESET = "\033[0m"

BLACK = "\033[30m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"

BOLD = "\033[1m"


def color(text, colour):
    return f"{colour}{text}{RESET}"


# ============================================================
# TERMINAL CONTROL
# ============================================================

def clear_screen():

    os.system(
        "clear"
        if os.name != "nt"
        else "cls"
    )


def hide_cursor():

    print("\033[?25l", end="")


def show_cursor():

    print("\033[?25h", end="")


# ============================================================
# TYPING EFFECT
# ============================================================

def type_text(text, delay=0.01, colour=WHITE):

    print(colour, end="")

    for char in text:

        print(char, end="", flush=True)
        time.sleep(delay)

    print(RESET, end="")


# ============================================================
# STARTUP ANIMATION
# ============================================================

def startup():

    clear_screen()
    hide_cursor()

    try:

        print()

        type_text(
            " [ SYSTEM INITIALIZING... ]",
            0.025,
            CYAN
        )

        time.sleep(0.25)

        type_text(
            " [ LOADING OSINT ENGINE... ]",
            0.025,
            YELLOW
        )

        time.sleep(0.25)

        type_text(
            " [ CONNECTING PUBLIC DATA MODULES... ]",
            0.02,
            MAGENTA
        )

        time.sleep(0.25)

        type_text(
            " [ SYSTEM READY ]",
            0.025,
            GREEN
        )

        time.sleep(0.4)

        clear_screen()

    finally:

        show_cursor()


# ============================================================
# BANNER
# ============================================================

def banner():

    logo = r"""
 ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
 ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
 ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
 ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
 ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
 ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝
"""

    print(color(logo, CYAN))

    print(
        color(
            "             [ S H A D O W S C A N ]",
            BOLD + MAGENTA
        )
    )

    print(
        color(
            "          PUBLIC USERNAME OSINT TOOL",
            YELLOW
        )
    )

    print()
    print(color("═" * 68, CYAN))

    print(
        color("  Developer : ", GRAY) +
        color(DEVELOPER, WHITE)
    )

    print(
        color("  Website   : ", GRAY) +
        color(WEBSITE, BLUE)
    )

    print(
        color("  GitHub    : ", GRAY) +
        color(GITHUB, BLUE)
    )

    print(
        color("  Email     : ", GRAY) +
        color(EMAIL, WHITE)
    )

    print(
        color("  Version   : ", GRAY) +
        color(VERSION, GREEN)
    )

    print(color("═" * 68, CYAN))

    print()

    print(
        color(
            " [✓] PUBLIC OSINT ENGINE ONLINE",
            GREEN
        )
    )

    print(
        color(
            " [✓] PROFILE URL CHECKER READY",
            GREEN
        )
    )

    print(
        color(
            " [✓] PRIVACY MODE ENABLED",
            GREEN
        )
    )

    print()


# ============================================================
# USERNAME VALIDATION
# ============================================================

def valid_username(username):

    pattern = r"^[A-Za-z0-9._-]{1,39}$"

    return bool(
        re.fullmatch(
            pattern,
            username
        )
    )


# ============================================================
# PLATFORM CHECK
# ============================================================

def check_platform(item):

    name, template = item

    url = template.format(
        u=USERNAME
    )

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

            code = response.status

            if 200 <= code < 400:

                return {
                    "name": name,
                    "url": url,
                    "status": "FOUND",
                    "code": code
                }

            return {
                "name": name,
                "url": url,
                "status": "UNKNOWN",
                "code": code
            }


    except urllib.error.HTTPError as error:

        code = error.code

        if code == 404:

            return {
                "name": name,
                "url": url,
                "status": "NOT FOUND",
                "code": code
            }

        if code in (401, 403, 429):

            return {
                "name": name,
                "url": url,
                "status": "UNKNOWN",
                "code": code
            }

        return {
            "name": name,
            "url": url,
            "status": "UNKNOWN",
            "code": code
        }


    except urllib.error.URLError:

        return {
            "name": name,
            "url": url,
            "status": "ERROR",
            "code": "NETWORK"
        }


    except Exception:

        return {
            "name": name,
            "url": url,
            "status": "ERROR",
            "code": "ERROR"
        }


# ============================================================
# ANIMATED SCAN BAR
# ============================================================

def scan_animation(total):

    width = 32

    for i in range(width + 1):

        percent = int(
            (i / width) * 100
        )

        filled = "█" * i
        empty = "░" * (width - i)

        print(
            f"\r {color('[SCAN]', CYAN)} "
            f"[{color(filled, GREEN)}"
            f"{color(empty, GRAY)}] "
            f"{percent:3d}%",
            end="",
            flush=True
        )

        time.sleep(0.015)

    print()
    print()


# ============================================================
# RESULT DISPLAY
# ============================================================

def display_result(result):

    name = result["name"]
    url = result["url"]
    status = result["status"]
    code = result["code"]

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
        f"{name:<15} "
        f"{state:<18} "
        f"HTTP {code}"
    )

    if status == "FOUND":

        print(
            f"    {color('↳', GRAY)} "
            f"{color(url, BLUE)}"
        )


# ============================================================
# REPORT
# ============================================================

def save_report(results):

    filename = (
        f"shadowscan_"
        f"{USERNAME}.txt"
    )

    try:

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "SHADOWSCAN OSINT REPORT\n"
            )

            file.write(
                "=" * 68 + "\n\n"
            )

            file.write(
                f"Developer : {DEVELOPER}\n"
            )

            file.write(
                f"Website   : {WEBSITE}\n"
            )

            file.write(
                f"Username  : {USERNAME}\n"
            )

            file.write(
                f"Version   : {VERSION}\n\n"
            )

            for result in results:

                file.write(
                    f"{result['name']} | "
                    f"{result['status']} | "
                    f"HTTP {result['code']} | "
                    f"{result['url']}\n"
                )

            file.write("\n")
            file.write(
                "Public URL checks only.\n"
            )

            file.write(
                "A FOUND result does not prove account ownership.\n"
            )

        return filename

    except Exception:

        return None


# ============================================================
# SCANNER
# ============================================================

def scan(username):

    global USERNAME

    USERNAME = username

    clear_screen()
    banner()

    print(
        color(
            " TARGET INFORMATION",
            BOLD + CYAN
        )
    )

    print(
        color(" ├─ Username : ", GRAY) +
        color(USERNAME, WHITE)
    )

    print(
        color(" ├─ Platforms: ", GRAY) +
        color(str(len(PLATFORMS)), WHITE)
    )

    print(
        color(" └─ Mode     : ", GRAY) +
        color("PUBLIC OSINT", GREEN)
    )

    print()
    print(
        color(
            "Starting public profile scan...",
            YELLOW
        )
    )

    print()

    # Progress animation
    scan_animation(
        len(PLATFORMS)
    )

    results = []

    with ThreadPoolExecutor(
        max_workers=8
    ) as executor:

        futures = [
            executor.submit(
                check_platform,
                item
            )
            for item in PLATFORMS.items()
        ]

        for future in as_completed(
            futures
        ):

            try:

                results.append(
                    future.result()
                )

            except Exception:

                pass


    # Preserve platform order

    order = {
        name: index
        for index, name
        in enumerate(
            PLATFORMS.keys()
        )
    }

    results.sort(
        key=lambda x:
        order.get(
            x["name"],
            999
        )
    )


    print(
        color(
            " PLATFORM RESULTS",
            BOLD + CYAN
        )
    )

    print(
        color(
            "─" * 72,
            GRAY
        )
    )

    print()

    for result in results:

        display_result(
            result
        )

        print()


    # ========================================================
    # SUMMARY
    # ========================================================

    found = sum(
        x["status"] == "FOUND"
        for x in results
    )

    not_found = sum(
        x["status"] == "NOT FOUND"
        for x in results
    )

    unknown = sum(
        x["status"] == "UNKNOWN"
        for x in results
    )

    errors = sum(
        x["status"] == "ERROR"
        for x in results
    )


    print(
        color(
            "═" * 72,
            CYAN
        )
    )

    print(
        color(
            "                    SCAN COMPLETE",
            BOLD + GREEN
        )
    )

    print(
        color(
            "═" * 72,
            CYAN
        )
    )

    print()

    print(
        f" {color('Total Platforms', GRAY)} : "
        f"{len(results)}"
    )

    print(
        f" {color('FOUND', GREEN)}          : "
        f"{found}"
    )

    print(
        f" {color('NOT FOUND', RED)}      : "
        f"{not_found}"
    )

    print(
        f" {color('UNKNOWN', YELLOW)}        : "
        f"{unknown}"
    )

    print(
        f" {color('ERROR', RED)}          : "
        f"{errors}"
    )

    print()


    # ========================================================
    # REPORT
    # ========================================================

    report = save_report(
        results
    )

    if report:

        print(
            color(
                f"[+] Report saved → {report}",
                GREEN
            )
        )

    print()

    print(
        color(
            "─" * 72,
            GRAY
        )
    )

    print(
        color(
            " DEVELOPED BY DHANNJAY UPHADE",
            MAGENTA
        )
    )

    print(
        color(
            f" {WEBSITE}",
            BLUE
        )
    )

    print(
        color(
            "─" * 72,
            GRAY
        )
    )

    print()

    print(
        color(
            "[!] Public information only.",
            YELLOW
        )
    )

    print(
        color(
            "[!] FOUND does not prove account ownership.",
            YELLOW
        )
    )

    print()


# ============================================================
# MAIN
# ============================================================

def main():

    startup()

    banner()

    try:

        if len(sys.argv) > 1:

            username = (
                sys.argv[1]
                .strip()
                .lstrip("@")
            )

        else:

            username = input(
                color(
                    " TARGET USERNAME ➜ ",
                    BOLD + WHITE
                )
            ).strip().lstrip("@")


        if not valid_username(
            username
        ):

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

            return


        scan(
            username
        )


    except KeyboardInterrupt:

        print()

        show_cursor()

        print(
            color(
                "[!] Scan interrupted.",
                YELLOW
            )
        )

        print()


    finally:

        show_cursor()


# ============================================================

if __name__ == "__main__":
    main()
