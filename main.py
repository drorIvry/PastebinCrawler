from crawley.config import Config
from crawley.crawler import Crawler
from crawley.crawler_executor import start_crawling
from crawley.db_handler import DBHandler
import logging

if __name__ == '__main__':
    logging.basicConfig(level=Config.LOG_LEVEL,
                        datefmt=Config.LOG_DATE_FORMAT,
                        filename=Config.LOG_PATH,
                        filemode='w')

    crawler = Crawler(Config.URL, DBHandler())
    start_crawling(crawler)
