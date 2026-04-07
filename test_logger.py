from logger import log_attack

# Test log entries

log_attack("192.168.1.10", "Port Scan", "HIGH")

log_attack("192.168.1.25", "SYN Flood", "CRITICAL")

log_attack("192.168.1.50", "Brute Force", "MEDIUM")