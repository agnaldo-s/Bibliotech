from projetoBiblioTech.infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, autoincrement=True, primary_key=True, )
    titulo = Column(String(20), nullable=False)
    autor = Column(String(20), nullable=False)
    editora = Column(String(20), nullable=False)
    ano_publicacao = Column(String(4), nullable=False)
    isbn13 = Column(String(13), nullable=True)
    copias = relationship("Copias", cascade="all, delete")
