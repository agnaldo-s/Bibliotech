from Infra.Configs.connection import  DBConnectionHandler
from Infra.Entities.Livro import Livro


class Livro_repository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Livro).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Livro).filter(Livro.id == id).first()
            return data

    def insert(self, livro: Livro):
        with DBConnectionHandler() as db:
            try:
                db.session.add(livro)
                db.session.commit()
                print('commitou')
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(Livro).filter(Livro.id == id).delete()
            db.session.commit()

    def update(self, livro: Livro):
        with DBConnectionHandler() as db:
            db.session.query(Livro).filter(Livro.id == livro.id).update({'titulo': livro.titulo, 'editora':
                livro.editora, 'ano_publicacao': livro.ano_publicacao,'isbn13': livro.isbn13, 'isbn10': livro.isbn10})
            db.session.commit()
