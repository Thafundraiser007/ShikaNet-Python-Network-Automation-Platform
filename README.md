# 🚀 ShikaNet — Python Network Automation Platform

> **A Multi-Vendor Network Automation & Administration Platform built with Python**

<img width="1357" height="981" alt="ShikaNet Application Screenshot" src="https://github.com/user-attachments/assets/00458cd0-e0f9-4b25-8a61-d0d0cba9a7fc" />

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-success)
![GUI](https://img.shields.io/badge/GUI-ttkbootstrap-orange)
![Automation](https://img.shields.io/badge/Automation-Netmiko-red)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

# 📖 Project Overview

**ShikaNet** is a Python-based desktop network automation platform designed to simplify repetitive network administration tasks through automation.

The project began as a basic Cisco network automation script and gradually evolved into a multi-vendor network administration platform with a graphical interface, secure credential management, automated reporting, configuration backups, email integration, AI-assisted functionality, and standalone Windows deployment.

ShikaNet is designed for:

* Network Engineers
* Network Administrators
* NOC Engineers
* System Administrators
* IT Support Engineers
* Networking Students
* Cybersecurity Students
* Python Developers learning network automation

The primary goal is to provide a practical interface for interacting with network infrastructure without requiring administrators to manually repeat the same CLI operations across multiple devices.

---

# 🎯 Project Objectives

The project was developed around several key objectives:

* Automate repetitive network administration tasks
* Support multiple network vendors
* Provide a user-friendly graphical interface
* Reduce repetitive CLI configuration work
* Improve configuration backup workflows
* Generate structured network reports
* Provide secure credential handling
* Maintain application responsiveness during network operations
* Provide a standalone Windows application
* Explore the integration of AI into network administration

---

# 🌐 Supported Network Platforms

ShikaNet is designed for multi-vendor network environments.

### Cisco

* Cisco IOS
* Cisco IOS-XE
* Cisco NX-OS

### Other Vendors

* Juniper
* Arista

Additional vendor support can be added as the project evolves.

---

# ✨ Core Features

## ⚡ Network Automation

ShikaNet provides automated interaction with network devices through SSH.

Capabilities include:

* SSH connectivity
* Device connectivity testing
* Command execution
* Batch command execution
* Configuration retrieval
* Network device administration
* Automation workflows

---

## 🖥️ Graphical User Interface

The application uses **Tkinter and ttkbootstrap** to provide a desktop-based interface.

Features include:

* Modern desktop interface
* Application branding
* Structured navigation
* Device management
* Automation console
* Reporting interface
* User-friendly workflow

---

## 🔐 Credential & Application Security

ShikaNet includes security mechanisms for application and device credential management.

Features include:

* Application authentication
* Password hashing
* Credential encryption
* Secure credential storage
* Separation of application credentials and network-device credentials

> **Security Note:** Never commit real network credentials, API keys, passwords, or other secrets to the repository.

---

# 📊 Reporting & Logging

ShikaNet can generate structured information from network automation tasks.

Supported functionality includes:

* Device reports
* CSV exports
* Session logs
* Automation reports
* Configuration backup records

These reports can be used for documentation, troubleshooting, and operational record keeping.

---

# 📧 Email Reporting

ShikaNet includes SMTP-based email functionality for distributing automation results.

Possible outputs include:

* Network reports
* Session logs
* Configuration backups
* Automation results

---

# 💾 Configuration Backup

The platform can retrieve and save device configurations.

Backup functionality includes:

* Running configuration retrieval
* Configuration storage
* Backup documentation
* Report generation
* Export functionality

This provides a foundation for future configuration versioning and comparison features.

---

# 🤖 AI-Assisted Network Administration

ShikaNet also explores the use of AI within network administration workflows.

AI-assisted functionality is intended to help with areas such as:

* Troubleshooting
* Interpreting network information
* Automation assistance
* Configuration analysis
* Network administration workflows

AI functionality is an evolving part of the project and will continue to be expanded as the platform develops.

---

# 🧵 Background Processing

Network operations can take time depending on device response and network conditions.

ShikaNet uses **Python multithreading** to prevent long-running operations from unnecessarily freezing the graphical interface.

This allows the application to remain responsive while network tasks are executing.

---

# 🪟 Standalone Windows Application

ShikaNet can be packaged as a standalone Windows executable.

### Standalone deployment

```text
ShikaNet.exe
```

The standalone application is designed so that users can launch ShikaNet without manually installing Python or configuring the development environment.

---

# 🛠️ Technologies Used

## Programming

* Python 3.11

## Network Automation

* Netmiko
* SSH

## GUI

* Tkinter
* ttkbootstrap

## Security

* Cryptography
* hashlib
* Base64

## Data Processing

* JSON
* CSV

## Email

* SMTP
* email.mime

## Python Modules

* threading
* datetime
* subprocess
* shutil
* difflib
* os

---

# 💻 Development Environment

ShikaNet was developed and maintained using:

* Visual Studio Code
* Python 3.11
* Git
* GitHub
* Windows

---

# 📥 Installation

## Option 1 — Standalone Application

The recommended method for normal users is to download the latest Windows executable from the repository's **Releases** section.

Run:

```text
ShikaNet.exe
```

No Python installation is required for the standalone version.

---

## Option 2 — Run From Source

Clone the repository:

```bash
git clone https://github.com/Thafundraiser007/ShikaNet-Python-Network-Automation-Platform.git
```

Enter the project directory:

```bash
cd ShikaNet-Python-Network-Automation-Platform
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python ShikaNet.py
```
# 📁 Project Structure

The current repository is organized around the ShikaNet v9 application and its supporting documentation and resources.

```text
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

### 📄 Main Application

**`ShikaNet v9/ShikaNet V9.py`**

The primary Python application containing the ShikaNet v9 desktop network automation platform.

### 📦 Requirements

**`ShikaNet v9/Requirments for python.txt`**

Contains the Python packages required to run the application from source.

### 📧 Email Reports

**`ShikaNet v9/Reports received via Email option in ShikaNet/`**

Contains supporting material demonstrating the email reporting functionality within ShikaNet.

### 📸 Screenshots

**`ShikaNet v9/screenshots/`**

Contains screenshots and visual documentation of the application interface and functionality.

---

# 🔑 Default Application Login

If the application is configured with the default development credentials:

**Username**

```text
admin
```

**Password**

```text
admin
```

> **Important:** These credentials are for the ShikaNet application login only. They are not the credentials used to access routers, switches, firewalls, or other network devices.

For production deployment, the default credentials should be changed.

---

# 🏗️ Application Architecture

The project is structured around several functional areas:

```text
                    ┌──────────────────────┐
                    │      ShikaNet GUI    │
                    │   Tkinter / ttkboot. │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       Device Management   Automation       Reporting
              │                │                │
              └────────────────┼────────────────┘
                               │
                               ▼
                         Network Layer
                            Netmiko
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
            Cisco           Juniper          Arista
```

The architecture continues to evolve as new automation and administration capabilities are introduced.

---

# 📸 Screenshots

## Application Interface

![ShikaNet Interface](https://github.com/user-attachments/assets/00458cd0-e0f9-4b25-8a61-d0d0cba9a7fc)

Additional screenshots will be added as the application interface and functionality continue to develop.

Planned screenshots:

* Login screen
* Main dashboard
* Device manager
* Automation console
* Network reports
* Configuration backup
* Email reporting
* Monitoring functionality

---

# 🧪 Testing

ShikaNet is developed and tested against lab-based network environments.

Testing focuses on:

* SSH connectivity
* Device authentication
* Command execution
* Multi-device automation
* Configuration retrieval
* Report generation
* Configuration backups
* GUI responsiveness
* Error handling

Network automation testing is performed using supported network platforms and laboratory environments.

---

# 🚀 Project Evolution

ShikaNet did not begin as a full network administration platform.

The project evolved through multiple development stages.

## Version 1 — Cisco Automation

The original project focused on basic Cisco automation using Python and Netmiko.

Original repository:

`Cisco-Network-Automation-with-Python-Netmiko-Cisco-DevNet-`

Initial functionality included:

* Cisco SSH connectivity
* Basic command execution
* Simple Tkinter interface
* Basic network automation

---

## Version 2+ — ShikaNet

The project was progressively expanded into a more complete network automation platform.

Major improvements included:

* GUI redesign
* ttkbootstrap integration
* Multi-vendor support
* Cisco IOS support
* Cisco IOS-XE support
* Cisco NX-OS support
* Juniper support
* Arista support
* Application authentication
* Credential encryption
* Password hashing
* Automated email reporting
* CSV exporting
* Configuration backup
* Improved logging
* Improved exception handling
* AI-assisted functionality
* Background multithreading
* Application branding
* Standalone Windows executable
* Improved file management
* Expanded project architecture

The project has grown from a basic Cisco automation script into a multi-vendor network automation and administration platform containing **4,000+ lines of Python code**.

---

# 🗺️ Future Roadmap

Planned improvements include:

* [ ] SSH Terminal
* [ ] Network Topology Mapping
* [ ] REST API Integration
* [ ] Configuration Comparison
* [ ] Scheduled Automation Tasks
* [ ] Inventory Management
* [ ] Real-Time Alerts
* [ ] Performance Analytics
* [ ] Plugin Architecture
* [ ] Multi-User Authentication
* [ ] Cloud Integration
* [ ] Expanded AI Network Troubleshooting
* [ ] Additional Vendor Support

---

# 🤝 Contributing

Contributions, suggestions, bug reports, and feature requests are welcome.

If you discover an issue or have an idea for improving ShikaNet:

1. Open an **Issue**
2. Describe the problem or proposed feature
3. Create a branch for your changes
4. Submit a **Pull Request**

Example workflow:

```text
Issue
  ↓
Feature Branch
  ↓
Development
  ↓
Testing
  ↓
Pull Request
  ↓
Review
  ↓
Merge
```

---

# 🤖 AI-Assisted Development

AI tools were used during development as productivity and learning assistants.

### ChatGPT — OpenAI

Used for:

* Feature brainstorming
* Python development assistance
* Debugging
* Code review
* Networking guidance
* Automation ideas
* Documentation
* README development
* Release notes
* Software engineering guidance

### Claude — Anthropic

Used for:

* Python integration ideas
* Feature implementation assistance
* GUI development
* Code organization
* Logic refinement

### Replit AI

Used for:

* GUI design ideas
* User interface improvements
* Layout suggestions
* User experience recommendations

### Transparency Statement

ShikaNet was designed, developed, tested, integrated, debugged, and maintained by the project author.

AI tools were used as development assistants for brainstorming, debugging, documentation, implementation suggestions, and learning. The project author remains responsible for integrating, testing, and maintaining the resulting software.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

ShikaNet makes use of and was developed with the help of technologies and communities including:

* Python
* Netmiko
* Tkinter
* ttkbootstrap
* Cryptography
* GitHub
* Cisco DevNet
* OpenAI
* Anthropic
* Replit

These projects and communities provide valuable tools and resources for learning, experimentation, and software development.

---

# 👨‍💻 Author

## Jamill Naipao

**Aspiring Network Engineer | Python Developer | Network Automation Enthusiast**

Building practical networking and infrastructure projects focused on automation, administration, and enterprise network technologies.

---

# ⭐ Support ShikaNet

If you find ShikaNet useful or interesting:

⭐ **Star the repository**

🍴 **Fork the project**

🐛 **Report bugs**

💡 **Suggest features**

🤝 **Contribute improvements**

Your feedback helps guide the continued development of ShikaNet.
