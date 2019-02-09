from crawley.config import Config
from crawley.Crawler import Crawler
from crawley.CrawlerExecutor import start_crawling
import logging

if __name__ == '__main__':
    logging.basicConfig(level=Config.LOG_LEVEL,
                        datefmt=Config.LOG_DATE_FORMAT,
                        filename=Config.LOG_PATH,
                        filemode='w')
    crawler = Crawler(Config.URL)
    start_crawling(crawler)

