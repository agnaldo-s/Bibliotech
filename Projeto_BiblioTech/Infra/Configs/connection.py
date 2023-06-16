from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Infra.Configs.Base import Base


class DBConnectionHandler:
    def __init__(self):
        self.database_name = 'biblioTech'
        self.__connection_string = f'sqlite:///{self.database_name}?mode=memory&cache=shared'
        self.__engine = self.__create_database_engine()
        self.session = self.__create_session()
        self.__create_tables()
        self.session.close()

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def __create_session(self):
        Session = sessionmaker(bind=self.__engine)
        session = Session()
        return session

    def __create_tables(self):
        Base.metadata.create_all(bind=self.__engine)
        print("Tabelas criadas com sucesso")