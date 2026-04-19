import sqlite3


def get_attack_counts():

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT attack_type, COUNT(*)
        FROM attack_log
        GROUP BY attack_type
    """)

    results = cursor.fetchall()

    print("\n=== Attack Counts ===")

    for attack, count in results:
        print(f"{attack} : {count}")

    conn.close()


def get_severity_counts():

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT severity, COUNT(*)
        FROM attack_log
        GROUP BY severity
    """)

    results = cursor.fetchall()

    print("\n=== Severity Counts ===")

    for severity, count in results:
        print(f"{severity} : {count}")

    conn.close()


# Test Run
if __name__ == "__main__":

    get_attack_counts()
    get_severity_counts()