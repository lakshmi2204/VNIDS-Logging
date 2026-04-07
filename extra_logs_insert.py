import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect("logs.db")
cursor = conn.cursor()

# Current time
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Insert multiple logs
logs = [
    (timestamp, "192.168.1.101", "Port Scan", "HIGH"),
    (timestamp, "192.168.1.150", "Brute Force", "CRITICAL"),
    (timestamp, "192.168.1.175", "SQL Injection", "MEDIUM")
]

cursor.executemany("""
INSERT INTO attack_log (timestamp, ip, attack_type, severity)
VALUES (?, ?, ?, ?)
""", logs)

# Save changes
conn.commit()

print("Multiple logs inserted successfully!")

# Close connection
conn.close()