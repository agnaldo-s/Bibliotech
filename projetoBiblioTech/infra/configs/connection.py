from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from projetoBiblioTech.infra.configs.base import Base


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

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        print('Gerando conexão')
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando conexão')
        self.session.close()
