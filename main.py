import logging
from config import config
from telegram_module.bot_handler import start


# logging.basicConfig(filename=config.logs_path, format='%(levelname)s - %(message)s')

def main():
    start()


if __name__ == '__main__':
    main()
