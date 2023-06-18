from projetoBiblioTech.infra.configs.connection import DBConnectionHandler
from projetoBiblioTech.infra.entities.copias import Copias


class Copias_repository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Copias).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Copias).filter(Copias.id == id).first()
            return data

    def insert(self, copias: Copias):
        with DBConnectionHandler() as db:
            try:
                db.session.add(copias)
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

    def update(self, copias: Copias):
        with DBConnectionHandler() as db:
            db.session.query(Copias).filter(Copias.id == copias.id).update({'qtd_copias':
                copias.qtd_copias})
            db.session.commit()
