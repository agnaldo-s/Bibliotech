import os
from PySide6.QtWidgets import QMainWindow, QTableWidget, QMessageBox, QLineEdit, QTextEdit, QComboBox, \
    QTableWidgetItem, QHeaderView, QFileDialog
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIntValidator, QPixmap, QImage
from projetoBiblioTech.view.mainWindow import Ui_MainWindow
from projetoBiblioTech.infra.entities.livro import Livro
from projetoBiblioTech.infra.repository.copias_repository import Copias_repository
from projetoBiblioTech.infra.repository.livro_repository import Livro_repository
import shutil


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tela_inicial()
        self.tbl_livros.horizontalHeader()
        self.tbl_livros.setSelectionBehavior(QTableWidget.SelectRows)
        self.tbl_livros.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tbl_livros.verticalHeader().setVisible(False)
        self.btn_adicionar_livro.clicked.connect(self.tela_cadastro_livro)
        self.btn_pesquisar_livro.clicked.connect(self.pesquisar_livro)
        self.txt_input_nome_livro.textChanged.connect(self.pesquisar_nome_livro)
        self.copias_repository = Copias_repository()
        self.btn_voltar.clicked.connect(self.tela_inicial)
        self.btn_voltat_cad.clicked.connect(self.tela_inicial)
        self.tbl_livros.cellDoubleClicked.connect(self.carregar_livro_selecionado)
        self.txt_isbn_cad.textChanged.connect(self.mascara_isbn)
        self.txt_anoPublicacao_cad_2.setValidator(QIntValidator())
        self.txt_numExemplares_cad.setValidator(QIntValidator())
        self.txt_isbn_cad.setValidator(QIntValidator())

        self.txt_id.setReadOnly(True)
        self.btn_deletar.clicked.connect(self.remover_livro)

        self.btn_atualizar.clicked.connect(self.carregar_livros_atualizar)
        self.txt_id_cad.setReadOnly(True)

        self.btn_salvar_cad.clicked.connect(self.cadastrar_livro)
        self.caminho_imagem = ''
        self.btn_addImagem_cad.clicked.connect(self.carregar_imagem)

        self.txt_id_cad.setReadOnly(True)
        self.txt_id.setReadOnly(True)

        self.btn_limpar_cad.clicked.connect(self.limpar_campos)

    ##FUNÇÕES:
    def ajusteTabela(self):
        self.tbl_livros.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tbl_livros.resizeColumnsToContents()

        for row in range(self.tbl_livros.rowCount()):
            height = self.tbl_livros.rowHeight(row)
            self.tbl_livros.setRowHeight(row, height + 5)

    def validarCamposPreenchidos(self):
        titulo = self.txt_titulo_cad.text()
        autora = self.txt_autora_cad.text()
        editora = self.txt_editora_cad.text()
        ano_publicacao = self.txt_anoPublicacao_cad_2.text()

        isbn13 = self.txt_isbn_cad.text().replace('-', '')

        qlines = [titulo, autora, editora, ano_publicacao, isbn13]
        for s in qlines:
            if s == '':
                qlines.remove(s)

        if len(qlines) < 5:
            msg = QMessageBox()
            msg.setWindowTitle('Erro')
            msg.setText('Todos os Campos devem estar Preenchidos')
            msg.exec()

        elif self.validar_digitos(ano_publicacao) == True and len(ano_publicacao) != 4:
            msg = QMessageBox()
            msg.setWindowTitle('Erro')
            msg.setText('Campo Ano Inválido')
            msg.exec()

        elif self.validar_digitos(isbn13) == True and len(isbn13) != 13:
            msg = QMessageBox()
            msg.setWindowTitle('Erro')
            msg.setText('Campo ISBN deve conter 13 dígitos')
            msg.exec()

        else:
            livroValidado = Livro()
            livroValidado.titulo = titulo
            livroValidado.autor = autora
            livroValidado.editora = editora
            livroValidado.ano_publicacao = ano_publicacao
            livroValidado.isbn13 = isbn13

            return livroValidado

    def validar_digitos(self, valor):
        if valor.isdigit():
            return True
        else:
            return False

    def cadastrar_livro(self):
        self.txt_id.setReadOnly
        db = Livro_repository()
        livro = self.validarCamposPreenchidos()

        livro_existente = db.select(self.txt_id_cad.text())
        if str(livro_existente) != 'None':
            self.atualizar_livro()
        else:
            copia = self.txt_numExemplares_cad.text()
            if self.validar_digitos(copia) == False or len(copia) > 3:
                msg = QMessageBox()
                msg.setWindowTitle('Erro')
                msg.setText('Campo N° de Exemplares Inválido')
                msg.exec()
            else:
                teste = str(self.caminho_imagem)
                caminho = self.salvar_imagemBd(self.caminho_imagem) if self.caminho_imagem != '' else self.caminho_imagem
                print(str(caminho))
                livro.imagem = str(caminho)
                print(livro.imagem)
                retorno = db.insert(livro, copia)

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

    def atualizar_livro(self):
        db = Livro_repository()
        livroValido = self.validarCamposPreenchidos()
        qtdCopias = self.txt_numExemplares_cad.text()

        if self.validar_digitos(qtdCopias) == False or len(qtdCopias) > 3:
            msg = QMessageBox()
            msg.setWindowTitle('Erro')
            msg.setText('Campo N° de Exemplares Inválido')
            msg.exec()
        else:
            livroValido.id = self.txt_id_cad.text()
            retorno = db.update(livroValido, qtdCopias)
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

    def limpar_campos(self):
        for widget in self.widget_CadastroLivro.children():
            if isinstance(widget, QTextEdit):
                widget.clear()
            elif isinstance(widget, QLineEdit):
                widget.clear()
            elif isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)
        self.frame_imagemLivro.clear()
        self.btn_limpar_cad.setVisible(True)
        self.btn_salvar_cad.setText('Salvar')
        self.btn_addImagem_cad.setVisible(True)
        self.txt_id_cad.setReadOnly(True)

    def pesquisar_nome_livro(self):
        livro = self.txt_input_nome_livro.text()
        if livro == '':
            self.popula_tabela_livros()
        else:
            db = Livro_repository()
            retorno = db.findByPalavraNoTitulo(livro)
            self.preencher_tabela(retorno)

    def pesquisar_livro(self):
        variavel = self.txt_input_nome_livro.text()
        if variavel != '':
            db = Livro_repository()
            retorno = db.findByTitulo(self.txt_input_nome_livro.text())

            if retorno is not None:
                self.tbl_livros.setRowCount(0)
                resultado = retorno
                self.tbl_livros.setRowCount(len(resultado))

                if resultado:
                    self.preencher_tabela(resultado)
                    QMessageBox.information(self, "Resultados", f"Foram encontrados {str(len(resultado))} resultados.")
                else:
                    QMessageBox.warning(self, "Sem resultados", "Nenhum resultado encontrado.")
                    self.popula_tabela_livros()

    def tela_cadastro_livro(self):
        self.qst_telas.setCurrentWidget(self.page_cadastroLivro)
        self.lbl_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Cadastro</span></p></body></html>", None))
        self.limpar_campos()

    def tela_visualizar_livro(self):
        self.qst_telas.setCurrentWidget(self.pag_editar_livro)

    def tela_inicial(self):
        self.qst_telas.setCurrentWidget(self.pag_procurar_livro)
        self.popula_tabela_livros()

    def remover_livro(self):
        db = Livro_repository()
        msg = QMessageBox()
        msg.setWindowTitle('Remover livro')
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
                nv_msg.setText('Livro removido com sucesso!')
                nv_msg.exec()

            else:
                nv_msg = QMessageBox()
                nv_msg.setWindowTitle('Remover livro')
                nv_msg.setText('Erro ao Remover!')
                nv_msg.exec()

        self.limpar_campos()
        self.tela_inicial()

    def popula_tabela_livros(self):
        self.tbl_livros.setRowCount(0)
        conn = Copias_repository()
        lista_join = conn.joinCopias_Livros()
        self.tbl_livros.setRowCount(len(lista_join))
        self.preencher_tabela(lista_join)
    def carregar_livro_selecionado(self, row):
        self.tela_visualizar_livro()

        self.txt_id.setText(self.tbl_livros.item(row, 0).text())
        self.txt_titulo.setText(self.tbl_livros.item(row, 1).text())
        self.txt_autora.setText(self.tbl_livros.item(row, 2).text())
        self.txt_editora.setText(self.tbl_livros.item(row, 3).text())
        self.txt_isbn.setText(str(self.tbl_livros.item(row, 4).text()))
        self.txt_anoPublicacao.setText(str(self.tbl_livros.item(row, 5).text()))
        self.txt_numExemplares_2.setText(str(self.tbl_livros.item(row, 6).text()))

        self.txt_id.setReadOnly
        db = Livro_repository()
        idLivro = self.tbl_livros.item(row, 0).text()
        livro_imagem = db.select_imagem(idLivro)
        print('path: ', livro_imagem)

        # pixmap = QPixmap(livro_imagem)
        # self.lbl_imagem_livro_editar.setPixmap(QPixmap(livro_imagem))

    def preencher_tabela(self, resultado):
        self.tbl_livros.setRowCount(0)
        self.tbl_livros.setRowCount(len(resultado))
        linha = 0
        for Object in resultado:
            valores = [Object.Livro.id, Object.Livro.titulo, Object.Livro.autor, Object.Livro.editora,
                       Object.Livro.isbn13,
                       Object.Livro.ano_publicacao, Object.Livro.imagem, Object.Copias.qtd_copias]
            for valor in valores:
                if valor is Object.Livro.imagem:
                    continue
                else:
                    print(valor)
                    item = QTableWidgetItem(str(valor))
                    if valor is Object.Copias.qtd_copias:
                        self.tbl_livros.setItem(linha, (valores.index(valor) - 1), item)
                        self.tbl_livros.item(linha, valores.index(valor))
                    else:
                        self.tbl_livros.setItem(linha, valores.index(valor), item)
                        self.tbl_livros.item(linha, valores.index(valor))
            linha += 1
        self.ajusteTabela()

    def carregar_livros_atualizar(self):
        self.tela_cadastro_livro()
        self.lbl_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Atualizar</span></p></body></html>", None))

        self.txt_id_cad.setText(self.txt_id.text())
        self.txt_titulo_cad.setText(self.txt_titulo.text())
        self.txt_autora_cad.setText(self.txt_autora.text())
        self.txt_editora_cad.setText(self.txt_editora.text())
        self.txt_isbn_cad.setText(self.txt_isbn.text())
        self.txt_anoPublicacao_cad_2.setText(self.txt_anoPublicacao.text())
        self.txt_numExemplares_cad.setText(self.txt_numExemplares_2.text())


    def mascara_isbn(self):
        teste = self.txt_isbn_cad.text()
        if self.txt_isbn_cad.text() == '----':
            self.txt_isbn_cad.setInputMask('')
        elif len(self.txt_isbn_cad.text()) == 1:
            self.txt_isbn_cad.setInputMask('000-00-000-0000-0')

    def carregar_imagem(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Imagens (*.png *.jpg *.jpeg)")
        file_dialog.exec()

        if file_dialog.result() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            print(file_path)
            pixmap = QPixmap(file_path)
            self.frame_imagemLivro.setPixmap(pixmap)

        self.caminho_imagem = file_path

    def salvar_imagemBd(self, file_path):
        caminho_original = file_path

        # Remove o nome do arquivo do caminho para obter o diretório
        diretorio, nome_arquivo = os.path.split(file_path)

        # Define o caminho completo do diretório de destino
        novo_diretorio = os.path.join(diretorio, 'capaLivro')
        os.makedirs(novo_diretorio, exist_ok=True)  # Cria a pasta caso não exista

        nome_arquivo_unico = self.txt_titulo_cad.text() + '_imagem'

        # Define o caminho completo do arquivo no diretório de destino
        diretorio_completo = os.path.join(novo_diretorio, nome_arquivo_unico)

        # Move a imagem para o diretório de destino
        shutil.move(caminho_original, diretorio_completo)

        return diretorio_completo
