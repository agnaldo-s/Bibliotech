from projetoBiblioTech.infra.configs.connection import DBConnectionHandler
from projetoBiblioTech.infra.entities.copias import Copias
from projetoBiblioTech.infra.entities.livro import Livro


class Copias_repository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Copias).all()
            return data

    def select(self, id_livro):
        with DBConnectionHandler() as db:
            data = db.session.query(Copias).filter(Copias.id_livro == id_livro).first().all
            return data

    def joinCopias_Livros(self) -> list:
        with DBConnectionHandler() as db:
            join = db.session.query(Livro, Copias).join(Copias, Livro.id == Copias.id_livro).order_by(
                Livro.titulo).all()
            return join

    def insert(self, copia: Copias):
        with DBConnectionHandler() as db:
            try:
                db.session.add(copia)
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

    def delete(self, id):
        with DBConnectionHandler() as db:
            db.session.query(Copias).filter(Copias.id == id).delete()
            db.session.commit()

    def update(self, copia:Copias):
        with DBConnectionHandler() as db:
            db.session.query(Copias).filter(Copias.id == copia.id).update({'qtd_copias':
               copia.qtd_copias})
            db.session.commit()
