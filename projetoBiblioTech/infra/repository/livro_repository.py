from projetoBiblioTech.infra.configs.connection import DBConnectionHandler
from projetoBiblioTech.infra.entities.copias import Copias
from projetoBiblioTech.infra.entities.livro import Livro
from projetoBiblioTech.infra.repository.copias_repository import Copias_repository


class Livro_repository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Livro).all()
            return data

    def joinLivro_Copias(self):
        with DBConnectionHandler() as db:
            join = db.session.query(Livro).join(Copias, Livro.id == Copias.id_livro).all()
            return join

    def findByTitulo(self, titulo):
        with DBConnectionHandler() as db:
            data = db.session.query(Livro).join(Copias, Livro.id == Copias.id_livro).filter(Livro.titulo == titulo
                                                                                            ).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Livro).filter(Livro.id == id).first()
            return data

    def insert(self, livro: Livro, copias: int):
        with DBConnectionHandler() as db:
            try:
                db2 = Copias_repository()
                copia = Copias()
                copia.qtd_copias = copias
                db.session.add(livro)
                db.session.commit()
                last_id = db.session.query(Livro.id).order_by(Livro.id.desc()).limit(1).scalar()
                copia.id_livro = last_id
                print(copia.id_livro, copia.qtd_copias)

                db2.insert(copia)

                print("Último ID inserido:", last_id)
                print('commitou')
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

        print(last_id)

    def delete(self, isbn):
        with DBConnectionHandler() as db:
            db.session.query(Livro).filter(Livro.isbn13 == id).delete()
            db.session.commit()
            return 'ok'

    def update(self, livro: Livro):
        with DBConnectionHandler() as db:
            db.session.query(Livro).filter(Livro.id == livro.id).update({'titulo': livro.titulo, 'autor': livro.autor, 'editora':
                livro.editora, 'ano_publicacao': livro.ano_publicacao, 'isbn13': livro.isbn13, 'isbn10': livro.isbn10})
            db.session.commit()
