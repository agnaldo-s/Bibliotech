from PySide6.QtWidgets import QMainWindow, QLineEdit, QMessageBox, QTextEdit, QComboBox
from os import path

from projetoBiblioTech.infra.configs.connection import DBConnectionHandler
from projetoBiblioTech.infra.entities.livro import Livro
from projetoBiblioTech.view.mainWindow import Ui_MainWindow

pasta_base = path.abspath(path.join(path.dirname(__file__), '..'))
from projetoBiblioTech.infra.repository.livro_repository import Livro_repository


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        conn = DBConnectionHandler()

        db_livro = Livro_repository
        #
        # self.lbl_input_nome_livro = QLineEdit(self.pag_editar_livro)
        # if len(self.lbl_input_nome_livro.text()) <= 2:
        #     titulo = self.lbl_input_nome_livro.text()
        #     print(titulo)
        #     db_livro.findByTitulo(titulo)

        def cadastrar_livro(self):
            db = Livro_repository()

            livro = Livro(
                titulo=self.lbl_titulo_cad.text(),
                editora=self.lbl_editora_cad.text(),
                ano_publicacao=self.lbl_anoPublicacao_cad.text(),
                isbn13=self.lbl_isbn_cad.text()
            )

            if self.btn_salvar_cad.text() == 'Salvar':
                retorno = db.insert(livro)
                print(retorno)

                if retorno == 'ok':
                    msg = QMessageBox()
                    msg.setWindowTitle('Cadastro')
                    msg.setText('Livro Cadastrado com sucesso')
                    msg.exec()
                    self.limpar_campos() ### confirmar limparCampos
                elif 'UNIQUE constraint failed:' in retorno.args[0]:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowTitle('Livro já cadastrado')
                    msg.setText(f'O Livro {self.lbl_titulo_cad.text()} já está cadastrado')
                    msg.exec()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowTitle('Erro ao cadastrar')
                    msg.setText(f'Erro ao cadastrar o livro, verifique os dados')
                    msg.exec()

            elif self.btn_salvar.text() == 'Atualizar':

                cliente.cpf = self.txt_cpf.text()
                db.update(cliente)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Cadastro Atualizado ')
                msg.setText('Cadastro atualizado com sucesso')
                msg.exec()
                self.limpar_campos()

            self.popula_tabela_clientes()

        def limpar_campos(self):

            ##entender essa joça aqui
            for widget in self.container.children():
                if isinstance(widget, QTextEdit):
                    widget.clear()
                elif isinstance(widget, QLineEdit):
                    widget.clear()
                elif isinstance(widget, QComboBox):
                    widget.setCurrentIndex(0)
            self.btn_remover.setVisible(False)
            self.btn_salvar.setText('Salvar')
            self.txt_cpf.setReadOnly(False)






