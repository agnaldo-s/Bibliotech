from PySide6.QtWidgets import QMainWindow, QTableWidget
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

    def ajusteTabela(self):
        self.tbl_livros.resizeColumnsToContents()
        self.tbl_livros.resizeRowsToContents()

        for row in range(self.tbl_livros.rowCount()):
            height = self.tbl_livros.rowHeight(row)
            self.tbl_livros.setRowHeight(row, height + 5)
