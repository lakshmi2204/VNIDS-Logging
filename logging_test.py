import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Test logs
logging.info("System started")
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("System under attack!")

print("Logs written successfully!")