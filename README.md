# ATM Simulator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Application-6c63ff?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  A Python-based command-line ATM simulator supporting PIN authentication, balance inquiry, cash withdrawal, and money transfer with transaction logging.
</p>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Workflow](#project-workflow)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Author](#author)

---

## Overview

ATM Simulator mimics core ATM functionality through a clean command-line interface. It supports multiple user accounts, PIN-based authentication with a 3-attempt lockout, and logs every transaction automatically to a reference log file using Python's built-in logging module.

---

## Features

| Feature | Description |
|:---|:---|
| PIN Authentication | 3-attempt lockout system with input validation |
| Check Balance | Displays account holder name and available balance |
| Cash Withdrawal | Validates amount against balance before processing |
| Money Transfer | 10-digit account number validation with balance check |
| Transaction Logging | All transactions logged to `reference.log` with timestamp |
| Multi-user Support | 7 pre-loaded user accounts with individual balances |
| Cross-platform | Screen clear works on both Windows and Linux/Mac |

---

## Project Workflow

| Step | Description |
|:---:|:---|
| 1 | Launch app — screen clears, current date and time displayed |
| 2 | User enters PIN — validated against `USERS` dictionary |
| 3 | On success — transaction menu displayed with 4 options |
| 4 | Check Balance — prints account holder name and balance |
| 5 | Withdraw Cash — validates amount, deducts from balance |
| 6 | Transfer Money — validates 10-digit account number and amount |
| 7 | Every transaction logged to `reference.log` automatically |
| 8 | Exit — farewell message displayed |
| 9 | 3 failed PIN attempts — account locked |

---

## Tech Stack

| Tool | Purpose |
|:---|:---|
| Python | Core language |
| `os` | Cross-platform screen clearing |
| `time` | Processing delay simulation |
| `logging` | Automatic transaction log to `reference.log` |
| `datetime` | Live date and time display |

---

## How to Run

**1. Clone the repository**
~~~bash
git clone https://github.com/Rabia605/atm-simulator-python.git
cd atm-simulator-python
~~~

**2. Run the simulator**
~~~bash
python atm_simulator.py
~~~

**3. Enter a valid PIN to log in**

| Account Holder | PIN |
|:---|:---:|
| Rabia Noreen | 1234 |
| Raffay | 1122 |
| Sara | 1133 |
| Ahmed | 1803 |
| Hassan | 1672 |
| Ayesha | 1110 |
| Umer | 1111 |

**4. Choose a transaction from the menu**

~~~
1. Check Balance
2. Withdraw Cash
3. Transfer Money
4. Exit
~~~

---

## Project Structure

~~~
atm-simulator-python/
│
├── atm_simulator.py
└── README.md
~~~

---

## Author

**Rabia Noreen**
*Software Engineer | Building with Python*

---

<p align="center">If this project inspired you, hit that ⭐ button!</p>