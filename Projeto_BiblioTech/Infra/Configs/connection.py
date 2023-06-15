from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from Infra.Configs.Base import Base


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = 'mysql+pymysql://root:253028@localhost/biblioteca' ## Escolher
        # banco de dados que será utilizado
        self.__engine = self.__create_data_baseEngine()
        self.session = None
        self.__create_database()
        self.__create_table()