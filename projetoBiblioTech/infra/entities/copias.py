from projetoBiblioTech.infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Copias(Base):
    __tablename__ = 'copias'

    id = Column(Integer, autoincrement=True, primary_key=True)
    qtd_copias = Column(Integer)
    id_livro = Column(Integer, ForeignKey('livros.id'))
