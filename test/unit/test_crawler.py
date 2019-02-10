import httpretty
from crawley.crawler import Crawler
from crawley.db_handler import DBHandler
from test.resources import crawler_resources
from tinydb import TinyDB, Query
from crawley.config import Config


@httpretty.activate
def test_crawler_fetch():
    httpretty.register_uri(httpretty.GET, "http://google.com/",
                           body="this is google!")
    crawler = Crawler('http://google.com', DBHandler())
    data = crawler.fetch_page('http://google.com')
    assert data.text == "this is google!"


@httpretty.activate
def test_crawl_to_paste():
    httpretty.register_uri(httpretty.GET, "http://google.com/",
                           body=crawler_resources.PASTE_RESPONSE)
    db = TinyDB(Config.DB_PATH)
    crawler = Crawler('http://aaa.com', DBHandler())
    crawler._crawl_to_paste('http://google.com')
    query = Query()
    search = db.search(
      query.title == 'makotn')
    assert search
