from Infra.Configs.Base import Base
from sqlalchemy import Column, String, Integer

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(20), nullable=False)
    editora = Column(String(20), nullable=False)
    ano_publicacao = Column(String(4), nullable=False)
    isbn13 = Column(String(13), nullable=True) ##Vamos adicionar os dois tipos de isbn com uma checkbox posteriormente?
    #Lembrar que essa variável só irá aceitar os dígitos: TRATAR A MÁSCARA
    isbn10 = Column(String(10), nullable=True)

