import sqlite3
from datetime import datetime


def insert_bulk_logs():

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    print("\nInserting bulk logs...")

    for i in range(100):

        cursor.execute("""
            INSERT INTO attack_log
            (timestamp, ip, attack_type, severity)
            VALUES (?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            f"192.168.1.{i}",
            "Port Scan",
            "MEDIUM"
        ))

    conn.commit()
    conn.close()

    print("Bulk logs inserted successfully!")


if __name__ == "__main__":
    insert_bulk_logs()