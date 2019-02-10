import httpretty
from crawley.crawler import Crawler


@httpretty.activate
def test_crawler_fetch():
    httpretty.register_uri(httpretty.GET, "http://google.com/",
                        body="this is google!")
    crawler = Crawler('http://google.com')
    data = crawler.fetch_page()
    assert data.text == "this is google!"


def test_crawl_to_paste():
    httpretty.register_uri(httpretty.GET, "http://google.com/",
                         body="this is google!")
    crawler = Crawler('http://google.com')
    data = crawler.fetch_page()
