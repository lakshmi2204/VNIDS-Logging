import sqlite3
from datetime import datetime

# Connect to database
conn = sqlite3.connect("logs.db")

cursor = conn.cursor()

# Insert SYN Flood log
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ip = "192.168.1.200"
attack_type = "SYN Flood"
severity = "CRITICAL"

cursor.execute("""
INSERT INTO attack_log
(timestamp, ip, attack_type, severity)

VALUES (?, ?, ?, ?)
""", (timestamp, ip, attack_type, severity))

# Save changes
conn.commit()

print("SYN Flood log inserted!")

# Close connection
conn.close()