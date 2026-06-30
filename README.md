# Port Scanner

## Overview

The Port Scanner is a Python application that scans a target IP address or hostname for open TCP ports.

It helps identify active network services and demonstrates basic network reconnaissance techniques commonly used in cybersecurity.

---

## Features

- Scan a target IP address or hostname
- Scan a custom range of TCP ports
- Detect open ports
- Display scan results in the terminal
- Generate a scan report automatically
- Handle invalid hostnames gracefully

---

## Technologies Used

- Python 3
- Socket module
- Datetime module
- Visual Studio Code

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jameelrobinson93-blip/port-scanner.git
```

Navigate to the project:

```bash
cd port-scanner
```

Run the scanner:

```bash
python scanner.py
```

---

## Example Output

```
==================================================
PORT SCANNER
==================================================

Target: 127.0.0.1

Scanning...

Port 135 is OPEN

==================================================
Scan Complete
==================================================

Open Ports Found: 1

Report saved to reports/scan_report.txt
```

---

## Project Structure

```
port-scanner/
│
├── scanner.py
├── sample_targets.txt
├── requirements.txt
├── README.md
├── reports/
│   └── scan_report.txt
└── screenshots/
```

---

## Future Improvements

- Banner grabbing
- Service detection
- UDP port scanning
- Multi-threaded scanning
- Export reports as CSV
- Export reports as JSON
- GUI version

---

## Author

**Jameel Robinson**

Cybersecurity Portfolio Project