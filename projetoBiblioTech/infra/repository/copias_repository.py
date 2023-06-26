from projetoBiblioTech.infra.configs.connection import DBConnectionHandler
from projetoBiblioTech.infra.entities.copias import Copias
from projetoBiblioTech.infra.entities.livro import Livro


class Copias_repository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Copias).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Copias).filter(Copias.id == id).first()
            return data

    def joinCopias_Livros(self) -> list:
        with DBConnectionHandler() as db:
            join = db.session.query(Livro, Copias).join(Copias, Livro.id == Copias.id_livro).all()
            return join

    def insert(self, copia: Copias):
        with DBConnectionHandler() as db:
            try:
                db.session.add(copia)
                db.session.commit()
                print('commitou')
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(Copias).filter(Copias.id == id).delete()
            db.session.commit()

    def update(self, idLivro, copias:Copias):
        with DBConnectionHandler() as db:
            db.session.query(Copias).filter(Copias.id_livro == idLivro).update({'qtd_copias':
                Copias.qtd_copias})
            db.session.commit()
