import arrow

DEFAULT_PASTE = {
    'author': 'N/A',
    'content': '',
    'title': 'N/A',
    'date': None
}

INIT_PASTE = {
    'author': 'test',
    'content': 'test',
    'title': 'test',
    'date': arrow.now().for_json()
}
