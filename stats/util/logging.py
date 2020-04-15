import sys
import logging
import datetime

LOG_PATH = "logs"

def init():
    global logger
    logging.addLevelName(logging.WARNING, 'WARN')
    logging.addLevelName(logging.CRITICAL, 'FATAL')
    logger = logging.getLogger('stats-bot')
    logger.setLevel(logging.DEBUG)

    console_format = logging.Formatter('%(levelname)5s %(module)8s: %(message)s')

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_format)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(console_handler)
