import arrow
import logging
from dateutil.parser import parse
from crawley.PasteScheme import PasteScheme
from crawley.config import Config
from bs4 import BeautifulSoup
logger = logging.getLogger(__name__)


class PasteHandler:
    """
    This utility class is responsible for
    extracting a PasteScheme from a BeautifulSoup object.
    """
    @staticmethod
    def extract_data_scheme(paste_soup: BeautifulSoup):
        header_soup = paste_soup.find('div', {'class': 'paste_box_info'})
        title = header_soup.find('h1').text
        author = header_soup.find('img').next_sibling.string.strip()
        content = paste_soup.find('textarea').text

        raw_date = header_soup.find('span')['title']
        date = parse(raw_date, tzinfos={"CDT": "UTC-5"})
        arrow_date = arrow.get(date)

        author = PasteHandler.normalize(author)
        title = PasteHandler.normalize(title)
        paste = PasteScheme(author, content, title, arrow_date)
        logger.debug('extracted a new paste.', paste.get_db_entry())
        return paste

    @staticmethod
    def normalize(data: str):
        return Config.DEFAULT_VALUE \
          if data.lower() in Config.UNKNOWN_VALUES else data
