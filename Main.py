from crawley.config import Config
from crawley.Crawler import Crawler
from crawley.CrawlerExecutor import start_crawling
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        datefmt='%m-%d %H:%M',
                        filename=Config.LOG_PATH,
                        filemode='w')
    crawler = Crawler(Config.URL)
    start_crawling(crawler)

