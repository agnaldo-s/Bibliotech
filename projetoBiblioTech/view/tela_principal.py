from PySide6.QtWidgets import QMainWindow, QLineEdit, QMessageBox, QTextEdit, QComboBox
from os import path

from projetoBiblioTech.infra.configs.connection import DBConnectionHandler
from projetoBiblioTech.infra.entities.livro import Livro
from projetoBiblioTech.infra.repository.copias_repository import Copias_repository
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
        #
        # self.horizontalLayout_8.addWidget(self.btn_pesquisar_livro)
        #
        # self.btn_pesquisar_livro.clicked.connect(self.)

        ##FUNÇÕES:
    def cadastrar_livro(self):
        db = Livro_repository()

        livro = Livro(
            titulo=self.lbl_titulo_cad.text(),
            editora=self.lbl_editora_cad.text(),
            ano_publicacao=self.lbl_anoPublicacao_cad.text(),
            isbn13=self.lbl_isbn_cad.text()
        )

        retorno = db.insert(livro)
        print(retorno)

        if retorno == 'ok':
            msg = QMessageBox()
            msg.setWindowTitle('Cadastro')
            msg.setText('Livro Cadastrado com sucesso')
            msg.exec()
            self.limpar_campos()  ### confirmar limparCampos
            ##Inserir método para retornar a página inicial
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

    def limpar_campos(self):
        for widget in self.widget_3.children():
            if isinstance(widget, QTextEdit):
                widget.clear()
            elif isinstance(widget, QLineEdit):
                widget.clear()
            elif isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)
        self.btn_limpar_cad.setVisible(True)
        self.btn_salvar_cad.setText('Salvar')
        self.btn_addImagem_cad.setVisible(True)
        self.txt_id_cad.setReadOnly(True)

    def consultar_livro(self):
        if self.txt_cpf.text().replace('.', '').replace('-', '') != '':

            db = Livro_repository()
            db2 = Copias_repository()
            retorno = db.select(self.txt_input_nome_livro.text().lower())

            if retorno is not None:
                self.self.stackedWidget.setCurrentIndex(1)

                self.txt_id.setText(retorno[0])
                self.txt_titulo.setText(retorno[1])
                self.txt_autora.setText(retorno[2])
                self.txt_editora.setText(retorno[3])
                self.txt_isbn.setText(retorno[5])
                self.txt_anoPublicacao.setText(retorno[6])

                id_chaveEstrangeira = retorno[0]
                qtd = db2.select(id_chaveEstrangeira)  ##Confirmar se volta como valor
                print(qtd)
                self.txt_numExemplares.setText(len(qtd))

            else:
                msg = QMessageBox()
                msg.setWindowTitle('Resultado da Busca')
                msg.setText(f'O Livro {self.txt_input_nome_livro.text()} não está cadastrado\n Clique em Adicionar')
                msg.exec()
