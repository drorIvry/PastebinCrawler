class Config:
    DB_PATH = 'data/db.json'
    URL = 'https://pastebin.com/'
    CRAWL_TIMEOUT = 2
    LOG_PATH = 'log/dev.log'
    DEFAULT_VALUE = 'N/A'
    UNKNOWN_VALUES = ['unknown', 'guest',
                      'anonymous', 'a guest',
                      '', 'untitled']
