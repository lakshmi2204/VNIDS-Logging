import sqlite3
from datetime import datetime

def log_brute_force(ip):

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    attack_type = "Brute Force"
    severity = "CRITICAL"

    cursor.execute("""
        INSERT INTO attack_log 
        (timestamp, ip, attack_type, severity)
        VALUES (?, ?, ?, ?)
    """, (timestamp, ip, attack_type, severity))

    conn.commit()
    conn.close()

    print(f"[LOGGED] Brute Force from {ip} (CRITICAL)")


# Test run
if __name__ == "__main__":
    log_brute_force("192.168.1.101")