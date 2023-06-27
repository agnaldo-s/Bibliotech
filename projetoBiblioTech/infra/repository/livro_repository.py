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
            join = db.session.query(Livro).join(Copias, Copias.id_livro == Livro.id).all()
            db.session.commit()
            return join

    def findByTitulo(self, titulo):
        with DBConnectionHandler() as db:
            data = db.session.query(Livro, Copias).join(Copias, Livro.id == Copias.id_livro).filter(
                Livro.titulo.ilike(titulo)).all()
            return data

    def findByPalavraNoTitulo(self, palavra):
        with DBConnectionHandler() as db:
            subquery = db.session.query(Livro.id).filter(Livro.titulo.ilike(f"%{palavra}%")).subquery()
            data = db.session.query(Livro, Copias).join(Copias, Copias.id_livro == Livro.id).filter(
                Livro.id.in_(subquery)).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Livro).filter(Livro.id == id).first()

            return data

    def select_imagem(self, id):
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).filter(Livro.id == id).first()
            if livro:
                imagem = livro.imagem
                return imagem
            else:
                return None

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

                db2.insert(copia)
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e


    def delete(self, id):
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).get(id)
            db.session.delete(livro)
            db.session.commit()
            return 'ok'

    def update(self, livro: Livro, qtdCopias):
        with DBConnectionHandler() as db:
            db2 = Copias_repository()
            copia = db2.select(livro.id)
            copia.qtd_copias = qtdCopias
            db2.update(copia)

            db.session.query(Livro).filter(Livro.id == livro.id).update(
                {'titulo': livro.titulo, 'autor': livro.autor, 'editora':
                    livro.editora, 'ano_publicacao': livro.ano_publicacao, 'isbn13': livro.isbn13, 'imagem': livro.imagem})
            db.session.commit()
        return 'ok'
