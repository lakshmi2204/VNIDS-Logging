import sqlite3


def search_by_ip(ip):

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM attack_log
        WHERE ip = ?
    """, (ip,))

    rows = cursor.fetchall()

    print("\n=== Logs From IP ===")

    for row in rows:
        print(row)

    conn.close()


def search_by_attack(attack_type):

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM attack_log
        WHERE attack_type = ?
    """, (attack_type,))

    rows = cursor.fetchall()

    print("\n=== Logs By Attack ===")

    for row in rows:
        print(row)

    conn.close()


def search_by_severity(severity):

    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM attack_log
        WHERE severity = ?
    """, (severity,))

    rows = cursor.fetchall()

    print("\n=== Logs By Severity ===")

    for row in rows:
        print(row)

    conn.close()



# Test Queries
if __name__ == "__main__":

    search_by_ip("192.168.1.101")

    search_by_attack("Brute Force")

    search_by_severity("CRITICAL")