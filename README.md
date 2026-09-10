# 🔎 ShadowScan OSINT

> Explore the public footprint of a username.

ShadowScan is a lightweight, privacy-focused OSINT tool that checks publicly accessible profile URLs for a given username.

Designed for cybersecurity learning, OSINT education, and authorized security research.

---

## ✨ Features

- 🔍 Username OSINT scanning
- 🌐 Multi-platform public profile checking
- ⚡ Fast concurrent scanning
- 📊 FOUND / NOT FOUND / UNKNOWN results
- 📝 Automatic scan report
- 📱 Termux support
- 💻 Linux / Windows / macOS support
- 📦 No third-party Python dependencies

---

## 🌐 Platforms Checked

ShadowScan currently checks public profile URLs on:

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

More platforms may be added in future versions.

---

# 📱 Installation — Termux

## 1. Update Termux

```bash
pkg update && pkg upgrade -y
```

## 2. Install Git and Python

```bash
pkg install git python -y
```

## 3. Clone ShadowScan

```bash
git clone https://github.com/dhannjayuphade/shadowscan-osint.git
```

## 4. Enter the project directory

```bash
cd shadowscan-osint
```

## 5. Check project files

```bash
ls
```

Expected files:

```text
osint.py
README.md
LICENSE
requirements.txt
.gitignore
```

## 6. Install requirements

```bash
pip install -r requirements.txt
```

> ShadowScan currently uses only Python's standard library, so no external packages are required.

## 7. Run ShadowScan

```bash
python osint.py
```

---

# ⚡ Quick Installation

Copy and run:

```bash
pkg update -y && pkg install git python -y && git clone https://github.com/dhannjayuphade/shadowscan-osint.git && cd shadowscan-osint && python osint.py
```

---

# 🚀 Usage

Run ShadowScan:

```bash
python osint.py
```

Enter a username when asked:

```text
Enter username: example123
```

You can also provide the username directly:

```bash
python osint.py example123
```

Using `@username` also works:

```bash
python osint.py @example123
```

---

# 📊 Example

```text
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
[-] Medium       NOT FOUND

===========================================================

SCAN SUMMARY

Checked     : 10
Found       : 2
Not Found   : 6
Unknown     : 2
Errors      : 0
```

---

# 📝 Scan Reports

After a scan, ShadowScan creates a local text report.

Example:

```text
shadowscan_example123.txt
```

The report contains:

- Username
- Platform
- Public profile URL
- HTTP response status
- Scan result

Generated reports are ignored by Git using `.gitignore`.

---

# 🔐 Privacy & Security

ShadowScan does **NOT**:

- ❌ Access private profiles
- ❌ Bypass login systems
- ❌ Collect passwords
- ❌ Extract private messages
- ❌ Find hidden phone numbers
- ❌ Track live location
- ❌ Bypass platform security
- ❌ Access private account information

ShadowScan only checks publicly accessible profile URLs.

---

# ⚠️ Disclaimer

ShadowScan is intended for:

- Cybersecurity education
- OSINT learning
- Authorized security research
- Public-profile discovery

A `FOUND` result does **not** prove that a profile belongs to a particular person.

Always respect privacy, applicable laws, platform terms, and authorization requirements.

The developer is not responsible for misuse of this software.

---

# 🛠️ Requirements

- Python 3.9+
- Git
- Internet connection
- Termux / Linux / Windows / macOS

No third-party Python packages are currently required.

---

# 📂 Project Structure

```text
shadowscan-osint/
│
├── osint.py
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# 👨‍💻 Developer

## Dhannjay Uphade

🌐 Website:

https://dhannjayuphade.github.io/

📧 Email:

dhannjayuphade5@gmail.com

📸 Instagram:

https://www.instagram.com/dhannjayuphade/

---

# ⭐ Support

If you find ShadowScan useful for learning cybersecurity and OSINT:

⭐ Star the repository  
🍴 Fork the repository  
🐛 Report bugs  
💡 Suggest new features

---

# 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

**ShadowScan — Public Footprint. Privacy First.**
