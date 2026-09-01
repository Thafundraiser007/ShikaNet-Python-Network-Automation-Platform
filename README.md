# 🚀 ShikaNet — Python Network Automation Platform

> **A Multi-Vendor Network Automation & Administration Platform built with Python**

![ShikaNet Application Interface](ShikaNet%20v9/screenshots/Screenshot%202026-06-29%20012901.png)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-success)
![GUI](https://img.shields.io/badge/GUI-ttkbootstrap-orange)
![Automation](https://img.shields.io/badge/Automation-Netmiko-red)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

A Python-based desktop platform for automating repetitive network administration tasks across multiple vendors, built around a graphical interface, credential management, automated reporting, configuration backup, and AI-assisted network administration.

The project demonstrates an end-to-end network automation tool build — from a single-vendor Cisco automation script through to a multi-vendor desktop application containing **4,000+ lines of Python code**.

---

# 📖 Project Overview

**ShikaNet** simplifies repetitive network administration work by providing engineers with a single desktop application for connecting to, automating, backing up, and reporting on network infrastructure across multiple vendors.

Instead of repeatedly performing the same CLI operations device by device, ShikaNet provides a centralized graphical interface for common network administration workflows.

### Intended Users

* Network Engineers
* Network Administrators
* NOC Engineers
* IT Support Engineers
* System Administrators
* Networking Students
* Cybersecurity Students
* Python Developers learning network automation

### Project Objectives

* Automate repetitive network administration tasks
* Support multiple network vendors through one interface
* Provide a user-friendly graphical interface
* Improve configuration backup workflows
* Generate structured reports
* Provide encrypted credential handling
* Keep the GUI responsive during long-running network operations
* Provide standalone Windows deployment
* Explore practical AI integration within network administration

---

# 🛠️ Environment & Technology Stack

| Component               | Details                                     |
| ----------------------- | ------------------------------------------- |
| Language                | Python 3.11                                 |
| GUI Framework           | Tkinter + ttkbootstrap                      |
| Network Automation      | Netmiko / SSH                               |
| Security                | Cryptography, hashlib, Base64               |
| Data Handling           | JSON, CSV                                   |
| Email                   | SMTP, `email.mime`                          |
| Concurrency             | Python `threading`                          |
| Packaging               | PyInstaller                                 |
| Development Environment | VS Code, Git, GitHub, Windows               |
| Supported Vendors       | Cisco IOS / IOS-XE / NX-OS, Juniper, Arista |

---

# 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │     ShikaNet GUI     │
                    │ Tkinter / ttkbootstrap│
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
                       Network Automation
                            Netmiko
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
            Cisco           Juniper          Arista
```

The architecture continues to evolve as new automation, administration, reporting, and AI capabilities are introduced.

---

# ⚡ Core Features

## 1. Network Automation Engine

ShikaNet handles network-device interaction over SSH using **Netmiko**.

Capabilities include:

* SSH connectivity
* Device reachability testing
* Single-device command execution
* Batch command execution
* Configuration retrieval
* Multi-device automation
* Reusable automation workflows

---

## 2. Graphical User Interface

The application uses **Tkinter and ttkbootstrap** to provide a desktop-based network administration interface.

Features include:

* Modern desktop interface
* Application branding
* Structured navigation
* Device management
* Automation console
* Reporting interface
* User-friendly workflows

The GUI is designed to allow administrators to perform routine automation tasks without manually interacting with the CLI for every operation.

---

## 3. Credential & Application Security

ShikaNet separates application-level authentication from network-device credentials.

Security functionality includes:

* Application login authentication
* Password hashing
* Encrypted credential storage
* Separation of application credentials and network-device credentials

> **Security Note:** Never commit real passwords, network credentials, API keys, or other secrets to the repository.

---

## 4. Reporting & Logging

Automation runs produce structured information for documentation and troubleshooting.

Supported functionality includes:

* Device reports
* CSV exports
* Session logs
* Automation results
* Configuration-backup records

---

## 5. Email Reporting

ShikaNet can distribute automation results through SMTP email.

Possible outputs include:

* Network reports
* Session logs
* Configuration backups
* Automation results

This allows results to be shared without manually collecting them from the application after every automation task.

---

## 6. Configuration Backup

ShikaNet can retrieve and store device running configurations.

Backup functionality provides:

* Running configuration retrieval
* Configuration storage
* Backup documentation
* Export functionality

This also provides a foundation for future configuration versioning and comparison.

---

## 7. AI-Assisted Network Administration

ShikaNet includes an AI assistant tab using the **Anthropic API** to explore AI-assisted network administration.

The AI functionality can assist with areas such as:

* Troubleshooting
* Interpreting network information
* Configuration analysis
* Network administration assistance
* Automation workflows

AI functionality is an evolving part of the platform and will continue to expand as development progresses.

---

## 8. Background Processing

Network operations can take time depending on device response and network conditions.

ShikaNet uses Python's `threading` module to execute network operations in the background.

This prevents long-running automation tasks from freezing the graphical interface and allows the application to remain responsive during network operations.

---

## 9. Standalone Windows Packaging

ShikaNet is packaged using **PyInstaller** into a standalone Windows executable.

```text
ShikaNet.exe
```

The standalone version allows users to run the application without manually installing Python or configuring the development environment.

---

# 📥 Installation

## Option 1 — Standalone Application

The recommended method for most users is to download the latest Windows executable from the repository's **Releases** section.

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

Navigate to the ShikaNet v9 application directory:

```bash
cd "ShikaNet v9"
```

Install the required Python packages:

```bash
pip install -r "Requirments for python.txt"
```

Run the application:

```bash
python "ShikaNet V9.py"
```

---

# 🔑 Default Application Login

If running with the default development credentials:

```text
Username: admin
Password: admin
```

> **Important:** These credentials are used only for the ShikaNet application login. They are not the credentials used to access routers, switches, firewalls, or other network devices.

> Change the default credentials before using the application in any production environment.

---

# 🧠 Design Decisions & Challenges

Several practical networking and software-development problems influenced the design of ShikaNet.

## GUI Freezing During Network Operations

SSH operations across multiple network devices can take significantly longer than a normal graphical-interface action.

Running those operations directly on the GUI's main thread could cause the application to freeze.

### Solution

Network operations were moved to background threads using Python's `threading` module.

This allows automation tasks to continue running while the interface remains responsive.

---

## Credential Exposure Risk

Storing plaintext network credentials alongside automation scripts creates a significant security risk.

### Solution

ShikaNet separates application authentication from network-device credentials and incorporates:

* Password hashing
* Credential encryption
* Separate credential handling
* Improved credential management

---

## Multi-Vendor Command Differences

Different network vendors use different command structures and CLI syntax.

Cisco IOS, IOS-XE, NX-OS, Juniper, and Arista cannot always be automated using identical commands.

### Solution

ShikaNet uses **Netmiko's vendor-aware connection architecture** as the network automation layer.

This provides a common automation framework while allowing device-specific connection handling.

---

## Making Automation Results Accessible

Automation output that only exists inside the application session can easily be lost.

### Solution

ShikaNet provides:

* CSV exports
* Structured reports
* Session logging
* Configuration backups
* SMTP email reporting

This allows automation results to be retained, reviewed, and shared.

---

# 📚 What This Project Demonstrates

This project demonstrates practical experience with:

* Python desktop application development
* Tkinter and ttkbootstrap
* Network automation with Netmiko
* SSH-based device management
* Multi-vendor network automation
* Cisco IOS / IOS-XE / NX-OS
* Juniper
* Arista
* Credential encryption
* Password hashing
* Multithreaded GUI design
* Structured reporting
* CSV export
* SMTP email integration
* Configuration backup workflows
* AI API integration
* PyInstaller application packaging
* Git and GitHub development workflows
* Iterative software architecture development

---

# 🧪 Testing

ShikaNet is developed and tested using laboratory-based network environments.

Testing focuses on:

* SSH connectivity
* Device authentication
* Command execution
* Multi-device automation
* Configuration retrieval
* Configuration backup
* Report generation
* Email reporting
* GUI responsiveness
* Error handling

Testing is performed against supported network platforms and controlled laboratory environments.

---

# 📈 Project Evolution

ShikaNet did not begin as a complete network administration platform.

The project evolved through several development stages.

## Version 1 — Cisco Network Automation

The original project:

```text
Cisco-Network-Automation-with-Python-Netmiko-Cisco-DevNet-
```

focused primarily on Cisco network automation.

Initial functionality included:

* Cisco SSH connectivity
* Basic command execution
* Tkinter GUI
* Basic automation workflows

---

## Version 2+ — ShikaNet

The project was progressively expanded into a multi-vendor network automation platform.

Major additions included:

* Redesigned GUI
* ttkbootstrap interface
* Multi-vendor support
* Cisco IOS
* Cisco IOS-XE
* Cisco NX-OS
* Juniper
* Arista
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
* Standalone Windows packaging
* Improved file management
* Expanded project architecture

The project has grown from a basic Cisco automation script into a multi-vendor network automation and administration platform containing **4,000+ lines of Python code**.

---

# 🧪 Testing & Development Environment

The application is developed and tested using controlled network laboratory environments.

Testing focuses on:

```text
Network Device
      │
      │ SSH
      ▼
   Netmiko
      │
      ▼
  ShikaNet
      │
      ├── Automation
      ├── Configuration Backup
      ├── Reporting
      └── Email Delivery
```

Testing includes network connectivity, authentication, command execution, configuration retrieval, backup workflows, reporting, error handling, and GUI responsiveness.

---

# 🗺️ Future Roadmap

Planned future development includes:

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

The recommended development workflow is:

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

### Contribution Process

1. Open an **Issue** describing the problem or proposed feature.
2. Create a feature or documentation branch.
3. Implement and test your changes.
4. Submit a **Pull Request**.
5. Review the changes.
6. Merge the Pull Request once approved.

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
* Layout suggestions
* User interface improvements
* User experience recommendations

### Transparency Statement

ShikaNet was designed, developed, tested, integrated, debugged, and maintained by the project author.

AI tools were used as development assistants for brainstorming, debugging, documentation, implementation suggestions, and learning.

The project author remains responsible for integrating, testing, and maintaining the resulting software.

---

# 📁 Repository Structure

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
        │
        ├── Screenshot 2026-06-29 012839.png
        ├── Screenshot 2026-06-29 012901.png
        ├── Screenshot 2026-06-29 012928.png
        ├── Screenshot 2026-06-29 012955.png
        ├── Screenshot 2026-06-29 013126.png
        ├── Screenshot 2026-06-29 013217.png
        ├── Screenshot 2026-06-29 013303.png
        └── Screenshot 2026-06-29 013357.png
```

### Main Application

**`ShikaNet v9/ShikaNet V9.py`**

The primary Python application containing the ShikaNet v9 desktop network automation platform.

### Requirements

**`ShikaNet v9/Requirments for python.txt`**

Contains the Python packages required to run ShikaNet from source.

### Email Reports

**`ShikaNet v9/Reports received via Email option in ShikaNet/`**

Contains supporting material demonstrating the email reporting functionality.

### Screenshots

**`ShikaNet v9/screenshots/`**

Contains screenshots and visual documentation of the ShikaNet application.

---

# 📸 Screenshots

The repository contains multiple screenshots documenting the ShikaNet interface and its functionality.

## Application Interface

![ShikaNet Application Interface](ShikaNet%20v9/screenshots/Screenshot%202026-06-29%20012901.png)

## Application View

![ShikaNet Application View](ShikaNet%20v9/screenshots/Screenshot%202026-06-29%20012839.png)

## Network Automation

![ShikaNet Network Automation](ShikaNet%20v9/screenshots/Screenshot%202026-06-29%20012928.png)

## Device Management

![ShikaNet Device Management](ShikaNet%20v9/screenshots/Screenshot%202026-06-29%20012955.png)

## Configuration & Automation

![ShikaNet Configuration](ShikaNet%20v9/screenshots/Screenshot%202026-06-29%20013126.png)

## Reporting

![ShikaNet Reporting](ShikaNet%20v9/screenshots/Screenshot%202026-06-29%20013217.png)

## Additional Application View

![ShikaNet Application View](ShikaNet%20v9/screenshots/Screenshot%202026-06-29%20013303.png)

## Additional Interface

![ShikaNet Interface](ShikaNet%20v9/screenshots/Screenshot%202026-06-29%20013357.png)

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

ShikaNet was developed using and with the support of technologies and communities including:

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

These technologies and communities provide valuable resources for learning, experimentation, network automation, and software development.

---

# 👨‍💻 Author

**Jamill Naipao**

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
