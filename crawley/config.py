import logging


class Config:
    DB_PATH = 'data/db.json'
    URL = 'https://pastebin.com/'

    # 10 minutes
    CRAWL_TIMEOUT = 10 * 60
    LOG_PATH = 'log/dev.log'
    LOG_LEVEL = logging.DEBUG
    LOG_DATE_FORMAT = '%m-%d %H:%M'
    DEFAULT_VALUE = 'N/A'
    UNKNOWN_VALUES = ['unknown', 'guest',
                      'anonymous', 'a guest',
                      '', 'untitled']
