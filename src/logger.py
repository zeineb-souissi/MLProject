import logging
import os
from datetime import datetime

# Create a log file with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the "logs" directory if it doesn't exist
os.makedirs(os.path.dirname(log_path), exist_ok=True)

# Set up the logging configuration
LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s [%(lineno)d] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
