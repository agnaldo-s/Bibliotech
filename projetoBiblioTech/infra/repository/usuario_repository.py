from projetoBiblioTech.infra.configs.connection import DBConnectionHandler
from projetoBiblioTech.infra.entities.usuario import Usuario

class UsuarioRepository:
    def find_by_username(self, username):
        with DBConnectionHandler() as db:
            user = db.session.query(Usuario).filter(Usuario.username == username).first()
            return user

    def insert(self, usuario):
        with DBConnectionHandler() as db:
            db.session.add(usuario)
            db.session.commit()
