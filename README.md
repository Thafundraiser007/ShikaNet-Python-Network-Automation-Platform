# 🚀 ShikaNet — Python Network Automation Platform

> **A Multi-Vendor Network Automation & Administration Platform built with Python**

[![ShikaNet Application Screenshot](https://private-user-images.githubusercontent.com/164267146/614266988-00458cd0-e0f9-4b25-8a61-d0d0cba9a7fc.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODgyMjYxNjQsIm5iZiI6MTc4ODIyNTg2NCwicGF0aCI6Ii8xNjQyNjcxNDYvNjE0MjY2OTg4LTAwNDU4Y2QwLWUwZjktNGIyNS04YTYxLWQwZDBjYmE5YTdmYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwOTAxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDkwMVQwMTI0MjRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zYWY5MGE5OWMzYWI5YWUzMDU3N2EyNzkzN2ZiNDY5ZGQ5ZWY2MjE2Y2U4N2Q5MTk2Y2ZmMDE3YzkzOGUzYTk4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Y3TNhsrtv030kJK6H53-FOKq0_00x_OeUINGGtMwlrc)](https://private-user-images.githubusercontent.com/164267146/614266988-00458cd0-e0f9-4b25-8a61-d0d0cba9a7fc.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODgyMjYxNjQsIm5iZiI6MTc4ODIyNTg2NCwicGF0aCI6Ii8xNjQyNjcxNDYvNjE0MjY2OTg4LTAwNDU4Y2QwLWUwZjktNGIyNS04YTYxLWQwZDBjYmE5YTdmYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwOTAxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDkwMVQwMTI0MjRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zYWY5MGE5OWMzYWI5YWUzMDU3N2EyNzkzN2ZiNDY5ZGQ5ZWY2MjE2Y2U4N2Q5MTk2Y2ZmMDE3YzkzOGUzYTk4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Y3TNhsrtv030kJK6H53-FOKq0_00x_OeUINGGtMwlrc)

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://img.shields.io/badge/Python-3.11-blue) [![Platform](https://img.shields.io/badge/Platform-Windows-success)](https://img.shields.io/badge/Platform-Windows-success) [![GUI](https://img.shields.io/badge/GUI-ttkbootstrap-orange)](https://img.shields.io/badge/GUI-ttkbootstrap-orange) [![Automation](https://img.shields.io/badge/Automation-Netmiko-red)](https://img.shields.io/badge/Automation-Netmiko-red) [![License](https://img.shields.io/badge/License-MIT-brightgreen)](https://img.shields.io/badge/License-MIT-brightgreen)

A Python-based desktop platform for automating repetitive network administration tasks across multiple vendors, built around a graphical interface, secure credential handling, automated reporting, configuration backup, and AI-assisted troubleshooting.

The project demonstrates an end-to-end network automation tool build — from a single-vendor CLI script through to a multi-vendor desktop application with over 4,000 lines of Python — including the real design decisions and problems solved along the way.

---

## Project Overview

**ShikaNet** simplifies repetitive network administration work by giving engineers a single desktop application to connect to, automate, back up, and report on infrastructure across multiple vendors, instead of repeating the same CLI operations device by device.

It's built for:

- Network Engineers and Administrators
- NOC Engineers and IT Support Engineers
- Networking and Cybersecurity Students
- Python Developers learning network automation

The project was developed around several core objectives:

- Automate repetitive network administration tasks
- Support multiple network vendors from one interface
- Provide a user-friendly graphical interface
- Improve configuration backup workflows and generate structured reports
- Provide secure, encrypted credential handling
- Keep the GUI responsive during long-running network operations
- Ship as a standalone Windows application requiring no Python install
- Explore practical uses of AI inside network administration workflows

---

## Environment & Technology Stack

| Component | Details |
|---|---|
| Language | Python 3.11 |
| GUI Framework | Tkinter + ttkbootstrap |
| Network Automation | Netmiko (SSH) |
| Security | Cryptography, hashlib, Base64 |
| Data Handling | JSON, CSV |
| Email | SMTP, `email.mime` |
| Concurrency | Python `threading` |
| Packaging | PyInstaller (standalone `.exe`) |
| Development Environment | VS Code, Git, GitHub, Windows |
| Supported Vendors | Cisco IOS / IOS-XE / NX-OS, Juniper, Arista |

---

## Architecture

```
                    ShikaNet GUI
                  Tkinter / ttkbootstrap
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
       ▼                  ▼                  ▼
Device Management     Automation         Reporting
       │                  │                  │
       └──────────────────┼──────────────────┘
                          │
                          ▼
                    Network Layer
                       Netmiko
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
       ▼                  ▼                  ▼
     Cisco             Juniper            Arista
```

The architecture continues to evolve as new automation and administration capabilities are introduced.

---

# 1. Network Automation Engine

ShikaNet handles device interaction over SSH via **Netmiko**, providing:

- SSH connectivity and device reachability testing
- Single and batch command execution across multiple devices
- Configuration retrieval
- Reusable automation workflows for repeated administration tasks

# 2. Graphical User Interface

The application uses **Tkinter and ttkbootstrap** for a modern desktop interface, with structured navigation across device management, the automation console, and reporting — designed so administrators don't need to touch a CLI directly for routine tasks.

# 3. Credential & Application Security

ShikaNet separates application-level authentication from network-device credentials, and adds:

- Application login authentication with password hashing
- Encrypted credential storage
- Clear separation between ShikaNet's own login and the credentials used to reach routers, switches, and firewalls

> **Security Note:** Never commit real network credentials, API keys, passwords, or other secrets to the repository.

# 4. Reporting & Logging

Automation runs produce structured output for documentation and troubleshooting:

- Device reports and CSV exports
- Session logs
- Automation and configuration-backup records

# 5. Email Reporting

Reports, session logs, configuration backups, and automation results can be distributed automatically over SMTP, so results don't have to be manually collected from the application after each run.

# 6. Configuration Backup

ShikaNet retrieves and stores device running configurations, with backup documentation and export functionality — laying the groundwork for future configuration versioning and comparison features.

# 7. AI-Assisted Network Administration

An AI assistant tab (using the Anthropic API) explores AI-assisted troubleshooting, interpretation of network information, and configuration analysis as part of the day-to-day automation workflow. This is an evolving part of the platform and will keep expanding as it develops.

# 8. Background Processing

Network operations vary in response time depending on the device and network conditions. ShikaNet runs these operations on background threads using Python's `threading` module so the GUI stays responsive instead of freezing while automation tasks run.

# 9. Standalone Windows Packaging

ShikaNet is packaged with **PyInstaller** into a standalone `ShikaNet.exe`, so end users can run it without installing Python or setting up a development environment.

---

## Installation

### Option 1 — Standalone Application

The recommended method for most users — download the latest Windows executable from the repository's **Releases** section, then run:

```
ShikaNet.exe
```

No Python installation is required.

### Option 2 — Run From Source

```
git clone https://github.com/Thafundraiser007/ShikaNet-Python-Network-Automation-Platform.git
cd ShikaNet-Python-Network-Automation-Platform
pip install -r requirements.txt
python ShikaNet.py
```

### Default Application Login

If running with the default development credentials:

```
Username: admin
Password: admin
```

> **Important:** These credentials are for the ShikaNet application login only — they are not used to access routers, switches, firewalls, or other network devices. Change the defaults before any production use.

---

# Design Decisions & Challenges Addressed

A few practical problems shaped how ShikaNet is built:

### GUI Freezing During Long-Running Network Operations

SSH operations across multiple devices can take noticeably longer than a typical UI action, and running them on the main thread would freeze the interface mid-automation. This was addressed by moving network operations onto background threads with Python's `threading` module, keeping the GUI responsive while automation runs.

### Credential Exposure Risk

Storing plaintext device credentials alongside automation scripts is a common and risky shortcut. ShikaNet addresses this by encrypting stored credentials and hashing the application's own login password, and by keeping application credentials and network-device credentials in clearly separate stores.

### Multi-Vendor Command Differences

Cisco IOS, IOS-XE, NX-OS, Juniper, and Arista don't share a single CLI syntax. Netmiko's vendor-aware driver model was used as the automation layer so the same higher-level ShikaNet workflows can target different platforms without rewriting the automation logic per vendor.

### Keeping Results Accessible After the Fact

Automation output that only lives inside the GUI session is easy to lose. Structured CSV/report exports and optional SMTP email delivery were added so results, logs, and configuration backups persist and can be shared outside the application itself.

---

# What This Project Demonstrates

This project demonstrates practical experience with:

- Python desktop application development (Tkinter, ttkbootstrap)
- Network automation with Netmiko over SSH
- Multi-vendor CLI automation (Cisco IOS/IOS-XE/NX-OS, Juniper, Arista)
- Secure credential handling (encryption, password hashing)
- Multithreaded GUI design for responsive long-running operations
- Structured reporting (CSV export, session logging)
- SMTP email integration
- Configuration backup workflows
- AI API integration into a practical operational tool
- Standalone application packaging and distribution (PyInstaller)
- Iterative software architecture growth across multiple versions

---

# Project Evolution

ShikaNet didn't start out as a full network administration platform — it grew through several stages.

### Version 1 — Cisco Automation

The original project (`Cisco-Network-Automation-with-Python-Netmiko-Cisco-DevNet-`) focused on basic Cisco automation: SSH connectivity, simple command execution, and a basic Tkinter interface.

### Version 2+ — ShikaNet

The project was progressively rebuilt into a multi-vendor platform, adding a redesigned ttkbootstrap GUI, Cisco IOS/IOS-XE/NX-OS + Juniper + Arista support, application authentication, credential encryption, automated email reporting, CSV exporting, configuration backup, AI-assisted functionality, background multithreading, and standalone Windows packaging.

The project has grown from a basic Cisco automation script into a multi-vendor network automation and administration platform containing **4,000+ lines of Python code**.

---

# Testing

ShikaNet is developed and tested against lab-based network environments, focusing on:

- SSH connectivity and device authentication
- Command execution (single and multi-device)
- Configuration retrieval and backup
- Report generation
- GUI responsiveness under load
- Error handling

---

# Future Roadmap

- [ ] SSH Terminal
- [ ] Network Topology Mapping
- [ ] REST API Integration
- [ ] Configuration Comparison
- [ ] Scheduled Automation Tasks
- [ ] Inventory Management
- [ ] Real-Time Alerts
- [ ] Performance Analytics
- [ ] Plugin Architecture
- [ ] Multi-User Authentication
- [ ] Cloud Integration
- [ ] Expanded AI Network Troubleshooting
- [ ] Additional Vendor Support

---

# Contributing

Contributions, suggestions, bug reports, and feature requests are welcome.

```
Issue → Feature Branch → Development → Testing → Pull Request → Review → Merge
```

1. Open an **Issue** describing the problem or proposed feature
2. Create a branch for your changes
3. Submit a **Pull Request**

---

# AI-Assisted Development

AI tools were used during development as productivity and learning assistants:

- **ChatGPT (OpenAI)** — feature brainstorming, Python development assistance, debugging, code review, networking guidance, documentation, and release notes
- **Claude (Anthropic)** — Python integration ideas, feature implementation assistance, GUI development, code organization, logic refinement
- **Replit AI** — GUI design ideas, layout suggestions, UX recommendations

**Transparency statement:** ShikaNet was designed, developed, tested, integrated, debugged, and maintained by the project author. AI tools were used as development assistants for brainstorming, debugging, documentation, implementation suggestions, and learning — the project author remains responsible for integrating, testing, and maintaining the resulting software.

---

# Repository Structure

```
ShikaNet-Python-Network-Automation-Platform/
│
├── README.md
│
└── ShikaNet v9/
    │
    ├── ShikaNet V9.py
    │
    ├── Requirments for python.txt
    │
    ├── Reports received via Email option in ShikaNet/
    │
    └── screenshots/
```

- **`ShikaNet v9/ShikaNet V9.py`** — the primary Python application containing the ShikaNet v9 desktop network automation platform
- **`ShikaNet v9/Requirments for python.txt`** — Python packages required to run the application from source
- **`ShikaNet v9/Reports received via Email option in ShikaNet/`** — supporting material demonstrating the email reporting functionality
- **`ShikaNet v9/screenshots/`** — screenshots and visual documentation of the application interface

---

# Screenshots

## Application Interface

![ShikaNet Interface](https://private-user-images.githubusercontent.com/164267146/614266988-00458cd0-e0f9-4b25-8a61-d0d0cba9a7fc.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODgyMjYxNjQsIm5iZiI6MTc4ODIyNTg2NCwicGF0aCI6Ii8xNjQyNjcxNDYvNjE0MjY2OTg4LTAwNDU4Y2QwLWUwZjktNGIyNS04YTYxLWQwZDBjYmE5YTdmYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwOTAxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDkwMVQwMTI0MjRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zYWY5MGE5OWMzYWI5YWUzMDU3N2EyNzkzN2ZiNDY5ZGQ5ZWY2MjE2Y2U4N2Q5MTk2Y2ZmMDE3YzkzOGUzYTk4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.Y3TNhsrtv030kJK6H53-FOKq0_00x_OeUINGGtMwlrc)

Additional screenshots will be added as the interface and functionality continue to develop. Planned: login screen, main dashboard, device manager, automation console, network reports, configuration backup, email reporting, monitoring functionality.

---

# License

This project is licensed under the **MIT License**.

---

# Acknowledgements

ShikaNet makes use of and was developed with the help of: Python, Netmiko, Tkinter, ttkbootstrap, Cryptography, GitHub, Cisco DevNet, OpenAI, Anthropic, and Replit.

---

# Author

**Jamil Naipao**
Aspiring Network Engineer | Python Developer | Network Automation Enthusiast

Building practical networking and infrastructure projects focused on automation, administration, and enterprise network technologies.

---

# Support ShikaNet

If you find ShikaNet useful:

⭐ Star the repository · 🍴 Fork the project · 🐛 Report bugs · 💡 Suggest features · 🤝 Contribute improvements

Your feedback helps guide the continued development of ShikaNet.
