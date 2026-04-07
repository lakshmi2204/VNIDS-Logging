import logging

# Configure logging
logging.basicConfig(
    filename="attack.log",   # Log file name
    level=logging.INFO,      # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create logger object
logger = logging.getLogger()


# Function to log attack events
def log_attack(ip, attack_type, severity):

    message = f"IP: {ip} | Attack: {attack_type} | Severity: {severity}"

    logger.info(message)

    print("Log recorded:", message)