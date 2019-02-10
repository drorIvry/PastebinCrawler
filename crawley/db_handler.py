from tinydb import TinyDB, Query
from crawley.config import Config
from crawley.paste import Paste
import logging

logger = logging.getLogger(__name__)


class DBHandler:
    """
    this class holds a singleton instance of the DB connection.
    (throughout the entire run of the we'll hold a single DB connection.)
    """
    db_instance = None

    def __new__(cls, *args, **kwargs):
        if not DBHandler.db_instance:
            DBHandler.db_instance = TinyDB(Config.DB_PATH)

        return DBHandler

    @staticmethod
    def insert(data: Paste):
        """
        this methods will insert a new record to the DB,
        it will verify that an existing record of the same data doesn't exists,
        insert the new data and log the event accordingly.
        :param data: the PasteScheme dto insert.
        """
        if not isinstance(data, Paste):
            logger.error('invalid param: ', data)
            raise TypeError('invalid parameter at insert.')

        # create new DB connection if needed
        if not DBHandler.db_instance:
            DBHandler.db_instance = TinyDB(Config.DB_PATH)

        normalized_data = data.get_db_record()

        query = Query()
        search = DBHandler.db_instance.search(
            query.date == normalized_data['date']
            and query.content == normalized_data['content'])

        if not search:
            logger.info('inserting a new record.')
            DBHandler.db_instance.insert(normalized_data)
        else:
            logger.warning('found duplicate!'
                           ' at date: {}'.format(normalized_data['date']))
