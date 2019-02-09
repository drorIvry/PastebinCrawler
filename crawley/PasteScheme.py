
class PasteScheme:
    """
    This class represents a paste object,
    holding the paste attributes.
    """
    def __init__(self, author='N/A', content='', title='N/A', date=None):
        self._author = author
        self._content = content
        self._title = title
        self._date = date

    def get_db_entry(self):
        return {
             'author': self._author,
             'title': self._title,
             'date': self._date.for_json(),
             'content': self._content
         }
