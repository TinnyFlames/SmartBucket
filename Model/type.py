import pymysql
import config
import secure


class Search:

    def __init__(self, search_type=config.SEARCH_TYPE):
        if search_type == 'db':
            self.__host = secure.DB_HOST
            self.__psd = secure.DB_PSD
            self.__user = secure.DB_USER
            self.__db = secure.DB_NAME  # database name
            self.key_word = None
        else:
            pass

    """ 
    Try to build connection between client and db
    """

    def _get_con(self) -> pymysql:
        # create connection to the database
        con = pymysql.Connect(
            host=self.__host,
            user=self.__user,
            password=self.__psd,
            db=self.__db
        )
        return con

    """
    execute sql command in database and get result in tuple
    """

    def _get_result(self, con: pymysql) ->tuple:
        # search result in database
        try:
            with con.cursor() as cursor:
                sql = "SELECT `type`,`path` FROM `garbage_info` WHERE name = %s"
                cursor.execute(sql, (self.key_word,))
                result = cursor.fetchone()
        finally:
            con.close()
        return result

    """
    main function which search info in the database 
    with @key_word: str and return search result 
    in @tuple(type_info: str, path: str)
    or @None if not found
    """

    def search(self, key_word: str) ->tuple or None:
        self.key_word = key_word
        if key_word is None:
            return None
        con = self._get_con()
        result = self._get_result(con)
        return result
