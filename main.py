import logging
from config import config

logging.basicConfig(filename=config.logs_path, format='%(levelname)s - %(message)s')
