from crawley.db_handler import DBHandler
from tinydb import TinyDB, Query
from crawley.config import Config
from crawley.paste import Paste
import arrow


def test_db_insert():
    paste = Paste('test', 'test', 'test', arrow.now())
    db_handler = DBHandler()
    db_handler.insert(paste)
    db = TinyDB(Config.DB_PATH)
    query = Query()
    search = db.search(
      query.title == paste.get_db_record()['title'])
    assert search


def test_db_double_insert():
    paste = Paste('test', 'test', 'test', arrow.now())
    db_handler = DBHandler()
    db_handler.insert(paste)
    db_handler.insert(paste)
    db = TinyDB(Config.DB_PATH)
    query = Query()
    search = db.search(
      query.title == paste.get_db_record()['title'])
    assert len(search) == 1
