from Infra.Configs.Base import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Copias(Base):
    __tablename__ = 'copias'

    id = Column(Integer, autoincrement=True, primary_key=True)
    id_livro = Column(Integer, ForeignKey('livro.id'))
    qtd_copias = Column(Integer(100))
