import logging

logger = logging.getLogger('main.py')


def init_logging():
    from logging import config

    from src.logging_config import LOGGING_CONFIG
    from src.settings import BASE_DIR

    logs_dir = BASE_DIR / 'logs'
    logs_dir.mkdir(exist_ok=True)

    config.dictConfig(LOGGING_CONFIG)


def main():
    from time import sleep
    from datetime import datetime

    while True:
        logger.debug('debug message, current time is %s', datetime.now())
        sleep(4)


if __name__ == '__main__':
    init_logging()
    main()
