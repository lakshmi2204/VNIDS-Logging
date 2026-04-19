from log_insert import insert_log

insert_log(
    "192.168.1.200",
    "Port Scan",
    "HIGH"
)

insert_log(
    "192.168.1.150",
    "SYN Flood",
    "CRITICAL"
)

insert_log(
    "192.168.1.101",
    "Brute Force",
    "MEDIUM"
)