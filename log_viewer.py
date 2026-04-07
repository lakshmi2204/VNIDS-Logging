import sqlite3

def view_logs():
    # Connect to database
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()

    # Fetch all logs
    cursor.execute("SELECT * FROM attack_log")

    logs = cursor.fetchall()

    # Display logs
    print("\n===== STORED LOGS =====\n")

    count = 0

    if logs:
        for log in logs:
            count += 1
            print(
                f"ID: {log[0]} | "
                f"Time: {log[1]} | "
                f"IP: {log[2]} | "
                f"Attack: {log[3]} | "
                f"Severity: {log[4]}"
            )

        print(f"\nTotal Logs: {count}")

    else:
        print("No logs found.")
    # Close connection
    conn.close()


# Run function
view_logs()