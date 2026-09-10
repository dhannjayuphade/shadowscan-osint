# shadowscan-osint
A privacy-focused OSINT username scanner for discovering publicly available profile footprints.

🔎 ShadowScan OSINT

«Explore the public footprint of a username.»

ShadowScan is a lightweight, privacy-focused OSINT tool that checks whether a username has a publicly accessible profile URL on selected online platforms.

It is designed for cybersecurity learning, OSINT education, and authorized security research.

---

✨ Features

- 🔍 Username footprint scanning
- 🌐 Multi-platform public profile checking
- ⚡ Concurrent scanning for faster results
- 📊 Clear FOUND / NOT FOUND / UNKNOWN results
- 📝 Automatic text report generation
- 📱 Works in Termux
- 💻 Works on Linux, Windows and macOS with Python
- 📦 No third-party Python packages required

---

🌐 Platforms

ShadowScan currently checks public URLs on:

- GitHub
- GitLab
- Reddit
- Codeberg
- Dev.to
- Medium
- Twitch
- Pinterest
- Gravatar
- PyPI

The platform list can be expanded in future versions.

---

🔎 ShadowScan OSINT

«Explore the public footprint of a username.»

A lightweight, privacy-focused OSINT username scanner for checking publicly accessible profile URLs.

📱 Installation — Termux

1. Update Termux

pkg update && pkg upgrade -y

2. Install Git and Python

pkg install git python -y

3. Clone ShadowScan

git clone https://github.com/dhannjayuphade/shadowscan-osint.git

4. Open the project

cd shadowscan-osint

5. Check the files

ls

You should see:

LICENSE
README.md
requirements.txt
osint.py
.gitignore

6. Install dependencies

ShadowScan uses only Python's standard library, so no external packages are required.

pip install -r requirements.txt

7. Start ShadowScan

python osint.py

⚡ Quick Installation

You can also use:

pkg update -y && pkg install git python -y && git clone https://github.com/dhannjayuphade/shadowscan-osint.git && cd shadowscan-osint && python osint.py

🚀 Usage

Interactive mode:

python osint.py

Then enter:

Enter username: example123

Or directly:

python osint.py example123

⚠️ Disclaimer

ShadowScan checks only publicly accessible profile URLs.

It does not bypass authentication, access private profiles, collect passwords, or retrieve hidden personal information.

Use this project only for lawful educational and authorized security research.

📄 License

MIT License.

📱 Termux Installation

Install Python:

pkg update
pkg install python

Clone the repository:

git clone https://github.com/dhannjayuphade/shadowscan-osint.git

Enter the project:

cd shadowscan-osint

Run ShadowScan:

python osint.py

---

🚀 Usage

Run interactively:

python osint.py

Then enter a username:

Enter username: example123

You can also provide the username directly:

python osint.py example123

You can enter either:

example123

or:

@example123

---

📊 Example

╔══════════════════════════════════════════════╗
║              SHADOWSCAN OSINT               ║
║      PUBLIC USERNAME FOOTPRINT SCANNER       ║
╚══════════════════════════════════════════════╝

[*] Target username: example123
[*] Checking public profile URLs...
[*] No login or private-data access is performed.

[+] GitHub       FOUND
[-] GitLab       NOT FOUND
[?] Reddit       UNKNOWN
[+] Dev.to       FOUND

===========================================================

SCAN SUMMARY

Checked     : 10
Found       : 2
Not Found   : 6
Unknown     : 2
Errors      : 0

---

📝 Reports

After a scan, ShadowScan automatically creates a text report:

shadowscan_example123.txt

The report contains:

- Username
- Platform
- Public profile URL
- HTTP response status
- Scan result

---

🔐 Privacy & Security

ShadowScan does not:

- ❌ Request passwords
- ❌ Bypass login systems
- ❌ Access private profiles
- ❌ Extract private messages
- ❌ Find hidden phone numbers
- ❌ Find passwords
- ❌ Track a person's live location
- ❌ Bypass platform security
- ❌ Access private account information

It only checks publicly accessible profile URLs.

---

⚠️ Important Disclaimer

ShadowScan is provided for educational and authorized OSINT/security research purposes.

A "FOUND" result only means that the requested public URL returned a response. It does not prove that the profile belongs to a particular person.

Always verify information independently and respect applicable laws, platform terms, privacy rights, and authorization requirements.

The developer is not responsible for misuse of this software.

---

🛠️ Requirements

- Python 3.9 or newer
- Internet connection

No external Python libraries are required.

---

📂 Project Structure

shadowscan-osint/
│
├── osint.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore

---

📜 License

ShadowScan is released under the MIT License.

See ""LICENSE"" (LICENSE) for details.

---

👨‍💻 Developer

Dhannjay Uphade

GitHub:

https://github.com/dhannjayuphade

Instagram 
https://www.instagram.com/dhannjayuphade?igsh=YzljYTk1ODg3Zg==

Website 
https://dhannjayuphade.github.io/

---

⭐ Support

If you find ShadowScan useful for learning cybersecurity and OSINT, consider giving the repository a ⭐ on GitHub.
