from sqlalchemy import Column, String, Integer
from projetoBiblioTech.infra.configs.base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
