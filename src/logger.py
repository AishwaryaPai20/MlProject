import logging
import os
from datetime import datetime

def configure_logging():
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    logs_path = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_path, exist_ok=True)

    LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

# Adding Logs
# if __name__ == "__main__":
#     configure_logging()

#     print("This is a logger module")
#     logging.info("This is a logger module")
