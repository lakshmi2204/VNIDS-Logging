import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect("logs.db")

cursor = conn.cursor()

# Convert datetime to string (fix warning)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Sample logs
sample_logs = [
    (current_time, "192.168.1.10", "Port Scan", "Medium"),
    (current_time, "192.168.1.15", "SYN Flood", "High"),
    (current_time, "192.168.1.22", "Brute Force", "Critical"),
    (current_time, "192.168.1.8", "Port Scan", "Low")
]

# Insert logs
cursor.executemany("""
INSERT INTO attack_log 
(timestamp, ip, attack_type, severity)
VALUES (?, ?, ?, ?)
""", sample_logs)

# Save changes
conn.commit()

# Close database
conn.close()

print("Sample logs inserted successfully!")