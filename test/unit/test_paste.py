from crawley.paste import Paste
from test.resources import paste_resource
import arrow


def test_default_paste():
    paste = Paste()
    assert paste.get_db_record() == paste_resource.DEFAULT_PASTE


def test_init_paste():
    paste = Paste('test', 'test', 'test', arrow.now().for_json())
    assert paste.get_db_record() == paste_resource.INIT_PASTE
