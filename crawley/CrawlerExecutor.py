import threading
from crawley.Crawler import Crawler
from crawley.config import Config
import logging

logger = logging.getLogger(__name__)


def start_crawling(crawler_instance: Crawler):
    """
    This method schedules the crawler to crawl.
    :param crawler_instance: the crawler as configured.
    """
    print('start crawling!')
    logger.info('started a new crawl!')
    crawler_instance.crawl()
    threading.Timer(Config.CRAWL_TIMEOUT, start_crawling,
                    [crawler_instance]).start()
