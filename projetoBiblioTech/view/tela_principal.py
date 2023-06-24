from PySide6.QtWidgets import QMainWindow, QTableWidget, QMessageBox, QLineEdit, QTextEdit, QComboBox

from projetoBiblioTech.infra.entities.copias import Copias
from projetoBiblioTech.view.mainWindow import Ui_MainWindow
from os import path
from projetoBiblioTech.infra.configs.connection import DBConnectionHandler
from projetoBiblioTech.infra.entities.livro import Livro
from projetoBiblioTech.infra.repository.copias_repository import Copias_repository
from projetoBiblioTech.infra.repository.livro_repository import Livro_repository


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.qst_telas.setCurrentWidget(self.pag_procurar_livro)
        self.tbl_livros.horizontalHeader()
        self.tbl_livros.itemChanged.connect(self.ajusteTabela)
        self.tbl_livros.setSelectionBehavior(QTableWidget.SelectRows)
        self.tbl_livros.setEditTriggers(QTableWidget.NoEditTriggers)
        self.btn_adicionar_livro.clicked.connect(self.tela_cadastro_livro)

        #Tela cadastro:

        self.txt_id_cad.setReadOnly(True)
        self.btn_salvar_cad.clicked.connect(self.validarCamposPreenchidos)


        self.btn_limpar_cad.clicked.connect(self.limpar_campos)


        #Tela de visualizar informações livro
        self.txt_id.setReadOnly(True)

    ##FUNÇÕES:
    def ajusteTabela(self):
        self.tbl_livros.resizeColumnsToContents()
        self.tbl_livros.resizeRowsToContents()

        for row in range(self.tbl_livros.rowCount()):
            height = self.tbl_livros.rowHeight(row)
            self.tbl_livros.setRowHeight(row, height + 5)

    def validarCamposPreenchidos(self):
        titulo = self.txt_titulo_cad.text()
        autora = self.txt_autora_cad.text()
        editora = self.txt_editora_cad.text()
        ano_publicacao = self.txt_anoPublicacao_cad_2.text()
        isbn13 = self.txt_isbn_cad.text()

        qlines = [titulo, autora, editora, ano_publicacao, isbn13]
        for s in qlines:
            if s == '':
                qlines.remove(s)

        if len(qlines) < 5:
            msg = QMessageBox()
            msg.setWindowTitle('Erro')
            msg.setText('Todos os Campos devem estar Preenchidos')
            msg.exec()
        else:
            livro = Livro()
            livro.titulo = titulo
            livro.autor = autora
            livro.editora = editora
            livro.ano_publicacao = ano_publicacao
            livro.isbn13 = isbn13
            self.cadastrar_livro(livro)

    def cadastrar_livro(self, livro:Livro):
        db = Livro_repository()
        db2 = Copias_repository()

        retorno = db.insert(livro)

        print(retorno)

        if retorno == 'ok':
            numExemplares = int(self.lbn_numExemplares_cad.text())
            print(numExemplares)

            for i in range(numExemplares):
                copia = Copias()
                print(copia)
                copia.id_livro = livro.id
                db2.insert(copia)

            msg = QMessageBox()
            msg.setWindowTitle('Cadastro')
            msg.setText('Livro Cadastrado com sucesso')
            msg.exec()
            self.limpar_campos()  ### confirmar limparCampos
            self.qst_telas.setCurrentWidget(self.pag_procurar_livro)
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
        for widget in self.widget_CadastroLivro.children():
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

    def tela_cadastro_livro(self):
        self.qst_telas.setCurrentWidget(self.page_cadastroLivro)


