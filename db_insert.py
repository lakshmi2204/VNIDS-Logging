import sqlite3
from datetime import datetime

def insert_log(ip, attack_type, severity):
    
    # Connect to database
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    # Get current timestamp
    timestamp = datetime.now()

    # Insert log
    cursor.execute("""
        INSERT INTO attack_log 
        (timestamp, ip, attack_type, severity)
        VALUES (?, ?, ?, ?)
    """, (timestamp, ip, attack_type, severity))

    # Save changes
    conn.commit()

    # Close connection
    conn.close()

    print("Log inserted successfully!")