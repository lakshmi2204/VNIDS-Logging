import sqlite3

def create_indexes():

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    print("\nCreating database indexes...")

    # Index for attack type
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_attack_type
        ON attack_log (attack_type)
    """)

    # Index for severity
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_severity
        ON attack_log (severity)
    """)

    # Index for IP
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_ip
        ON attack_log (ip)
    """)

    conn.commit()
    conn.close()

    print("Indexes created successfully!")


if __name__ == "__main__":
    create_indexes()