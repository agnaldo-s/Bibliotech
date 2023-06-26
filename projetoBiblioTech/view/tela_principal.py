from PySide6.QtWidgets import QMainWindow, QTableWidget, QMessageBox, QLineEdit, QTextEdit, QComboBox, QTableWidgetItem, \
    QPushButton

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
        self.tela_inicial()
        self.tbl_livros.horizontalHeader()
        self.tbl_livros.setSelectionBehavior(QTableWidget.SelectRows)
        self.tbl_livros.setEditTriggers(QTableWidget.NoEditTriggers)
        self.btn_adicionar_livro.clicked.connect(self.tela_cadastro_livro)
        self.btn_pesquisar_livro.clicked.connect(self.pesquisar_livro_Ana)
        self.copias_repository = Copias_repository()

        self.btn_voltar.clicked.connect(self.tela_inicial)
        self.btn_voltat_cad.clicked.connect(self.tela_inicial)

        self.btn_pesquisar_livro.clicked.connect(self.pesquisar_livro)
        self.tbl_livros.cellDoubleClicked.connect(self.carregar_livro_selecionado)

        # Tela de visualizar informações livro
        self.txt_id.setReadOnly(True)
        self.btn_deletar.clicked.connect(self.remover_livro)

        self.btn_atualizar.clicked.connect(self.carregar_livros_atualizar)
        self.btn_salvar_cad.clicked.connect(self.validarCamposPreenchidos)

        self.txt_id_cad.setReadOnly(True)
        self.txt_id.setReadOnly(True)

        self.btn_limpar_cad.clicked.connect(self.limpar_campos)


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
        self.txt_id.setReadOnly
        db = Livro_repository()
        copia = self.lbn_numExemplares_cad.text()

        select_id = self.txt_id_cad.text()
        if db.select(select_id) != 'None':
            qtdCopias = self.txt_numExemplares_cad.text()
            retorno = db.update(livro, qtdCopias)
            print(retorno)
            if retorno == 'ok':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Livro Atualizado')
                msg.setText('Livro atualizado com sucesso')
                msg.exec()
                self.limpar_campos()
                self.tela_inicial()
                self.popula_tabela_livros()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao atualizar')
                msg.setText(f'Erro ao atualizar o livro, verifique os dados')
                msg.exec()

        else:
            retorno = db.insert(livro, copia)
            print(retorno)

            if retorno == 'ok':
                msg = QMessageBox()
                msg.setWindowTitle('Cadastro')
                msg.setText('Livro Cadastrado com sucesso')
                msg.exec()
                self.limpar_campos()
                self.tela_inicial()
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

    def pesquisar_livro_Ana(self):
        variavel = self.txt_input_nome_livro.text()
        print(variavel)
        if variavel != '':

            db = Livro_repository()
            retorno = db.findByTitulo(self.txt_input_nome_livro.text())

            if retorno is not None:
                self.tbl_livros.setRowCount(0)
                resultado = retorno
                print(retorno)
                self.tbl_livros.setRowCount(len(resultado))

                linha = 0
                for livro in resultado:
                    valores = [livro.id, livro.titulo, livro.titulo, livro.editora, livro.isbn13, livro.ano_publicacao]
                    for valor in valores:
                        item = QTableWidgetItem(str(valor))
                        self.tbl_livros.setItem(linha, valores.index(valor), item)
                        self.tbl_livros.item(linha, valores.index(valor))
                    linha += 1

    def tela_cadastro_livro(self):
        self.qst_telas.setCurrentWidget(self.page_cadastroLivro)

    def tela_visualizar_livro(self):
        self.qst_telas.setCurrentWidget(self.pag_editar_livro)

    def tela_inicial(self):
        self.qst_telas.setCurrentWidget(self.pag_procurar_livro)
        self.popula_tabela_livros()
      
    def pesquisar_livro(self):
        pesquisa = self.txt_input_nome_livro.text()
        resultado = self.copias_repository.select(pesquisa)

        if resultado:
            QMessageBox.information(self, "Resultados", f"Foram encontrados {resultado} resultados.")
            for rt in resultado:
                print(resultado)
        else:
            QMessageBox.warning(self, "Sem resultados", "Nenhum resultado encontrado.")

    def remover_livro(self):

        db = Livro_repository()
        msg = QMessageBox()
        msg.setWindowTitle('Remover livro')
        msg.setText('Este livro será removida')
        msg.setInformativeText(f'Você deseja remover o livro de id {self.txt_id.text()}?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.button(QMessageBox.Yes).setText('Sim')
        msg.button(QMessageBox.No).setText('Não')

        resposta = msg.exec()

        if resposta == QMessageBox.Yes:
            retorno = db.delete(self.txt_id.text())

            if retorno == 'ok':
                nv_msg = QMessageBox()
                nv_msg.setWindowTitle('Remover livro')
                nv_msg.setText('Livro removido com sucesso')
                nv_msg.exec()
            else:
                nv_msg = QMessageBox()
                nv_msg.setWindowTitle('Remover livro')
                nv_msg.setText('Erro ao Remover')
                nv_msg.exec()
            self.txt_id.setReadOnly(False)
            self.popula_tabela_livros()


    def popula_tabela_livros(self):
        self.tbl_livros.setRowCount(0)
        conn = Copias_repository()
        lista_livros = conn.joinCopias_Livros()
        print(lista_livros)
        self.tbl_livros.setRowCount(len(lista_livros))

        print(conn.joinCopias_Livros())

        linha = 0
        for object in lista_livros:
            valores = [object.Livro.id, object.Livro.titulo, object.Livro.autor, object.Livro.editora, object.Livro.isbn13,
                       object.Livro.ano_publicacao, object.Copias.qtd_copias]
            for valor in valores:
                item = QTableWidgetItem(str(valor))
                self.tbl_livros.setItem(linha, valores.index(valor), item)
                self.tbl_livros.item(linha, valores.index(valor))
            linha += 1

        self.ajusteTabela()
    def carregar_livro_selecionado(self, row, collum):
        self.tela_visualizar_livro()

        self.txt_id.setText(self.tbl_livros.item(row, 0).text())
        self.txt_titulo.setText(self.tbl_livros.item(row, 1).text())
        self.txt_autora.setText(self.tbl_livros.item(row, 2).text())
        self.txt_editora.setText(self.tbl_livros.item(row, 3).text())
        self.txt_isbn.setText(self.tbl_livros.item(row, 4).text())
        self.txt_anoPublicacao.setText(self.tbl_livros.item(row, 5).text())
        self.txt_numExemplares_2.setText(str(self.tbl_livros.item(row, 6).text()))

        self.txt_id.setReadOnly

    def remover_livro(self):
        msg = QMessageBox()
        msg.setWindowTitle('Remover Livro')
        msg.setText('Esse Livro será Removido')
        msg.setInformativeText(f'Você deseja remover o livro de isbn: {self.txt_isbn.text()} ?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.button(QMessageBox.Yes).setText('Sim')
        msg.button(QMessageBox.No).setText('Não')
        resposta = msg.exec()
        self.limpar_campos()

        if resposta == QMessageBox.Yes:
            db = Livro_repository()
            retorno = db.delete(self.txt_isbn.text())

            if retorno == 'ok':
                new_msg = QMessageBox()
                new_msg.setWindowTitle('Remover Livro')
                new_msg.setText('Livro removido com sucesso!')
                new_msg.exec()
                self.limpar_campos()
            else:
                new_msg = QMessageBox()
                new_msg.setWindowTitle('Remover Livro')
                new_msg.setText('Erro ao remover livro!')
                new_msg.exec()
        self.tela_inicial()
        self.popula_tabela_livros()

    def carregar_livros_atualizar(self):
        db = Livro_repository()
        self.tela_cadastro_livro()

        self.txt_id_cad.setText(self.txt_id.text())
        self.txt_titulo_cad.setText(self.txt_titulo.text())
        self.txt_autora_cad.setText(self.txt_autora.text())
        self.txt_editora_cad.setText(self.txt_editora.text())
        self.txt_isbn_cad.setText(self.txt_isbn.text())
        self.txt_anoPublicacao_cad_2.setText(self.txt_anoPublicacao.text())
        self.lbn_numExemplares_cad.setText(self.txt_numExemplares_2.text())

