import sqlite3
from datetime import datetime


def insert_portscan_log(ip, severity):
    
    # Connect to database
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    # Current time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insert log
    cursor.execute("""
        INSERT INTO attack_log 
        (timestamp, ip, attack_type, severity)
        VALUES (?, ?, ?, ?)
    """, (timestamp, ip, "Port Scan", severity))

    # Save and close
    conn.commit()
    conn.close()

    print("Port Scan log inserted!")


# Test run
insert_portscan_log("192.168.1.101", "LOW")
insert_portscan_log("192.168.1.102", "MEDIUM")
insert_portscan_log("192.168.1.103", "CRITICAL")