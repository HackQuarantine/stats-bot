import sys
import logging
import datetime

LOG_PATH = "logs"

def init():
    global logger
    logging.addLevelName(logging.WARNING, 'WARN')
    logging.addLevelName(logging.CRITICAL, 'FATAL')
    logger = logging.getLogger('conflux-bot')
    logger.setLevel(logging.DEBUG)

    console_format = logging.Formatter('%(levelname)5s %(module)8s: %(message)s')
    file_format = logging.Formatter('%(levelname)5s %(module)8s: %(message)s')

    file_handler = logging.FileHandler(filename=f'{LOG_PATH}/{datetime.datetime.utcnow()}.log', encoding='utf-8', mode='w')
    file_handler.setFormatter(file_format)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_format)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
