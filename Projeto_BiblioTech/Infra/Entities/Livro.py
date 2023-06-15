from Infra.Configs.Base import Base
from sqlalchemy import Column, String, Integer

class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(20), nullable=False)
