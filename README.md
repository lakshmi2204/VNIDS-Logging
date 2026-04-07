# VNIDS Logging System (Member 3)

This repository contains the logging module for the VNIDS (Virtual Network Intrusion Detection System) project.

## 🔹 Module Role
Member 3 — Logging System + Database

Responsible for:

- Storing attack logs
- Managing SQLite database
- Creating backup systems
- Providing log viewer functionality

---

## 📅 Progress (Day 1–14)

Completed:

- SQLite database setup
- attack_log table creation
- Log insertion scripts
- Port Scan logging
- SYN Flood logging
- Brute Force logging
- SQL Injection logging
- Log viewer script
- Database backup system
- GitHub integration

---

## 🛠 Technologies Used

- Python
- SQLite
- Git
- GitHub

---

## 📂 Key Files

- logs.db — main database
- logs_backup.db — backup database
- backup_db.py — backup script
- log_viewer.py — view logs
- portscan_log.py — port scan logging
- syn_log_insert.py — SYN flood logging
- extra_logs_insert.py — multiple attack logs

---

## 🎯 Project Goal

Build a SOC-style logging system capable of:

- Storing IDS alerts
- Managing attack records
- Supporting dashboard visualization
- Maintaining reliable backups