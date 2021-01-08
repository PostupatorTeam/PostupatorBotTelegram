import logging
from config import config
from config.init.initialize_database import create_database, create_tables
from src.main.middle_module import middle_module
from src.main.telegram_module.telegram_module import start


if __name__ == '__main__':
    logging.basicConfig(filename=config.logs_path, format='%(levelname)s - %(message)s')
    create_database()
    create_tables()
    middle_module.notify()
    start()
