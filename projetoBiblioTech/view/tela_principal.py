from PySide6.QtWidgets import QMainWindow, QHeaderView
from PySide6.QtGui import QPixmap, QPicture

from os import path


from projetoBiblioTech.view.mainWindow import Ui_MainWindow

pasta_base = path.abspath(path.join(path.dirname(__file__), '..'))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.qst_telas.setCurrentWidget(self.pag_procurar_livro)
        self.tbl_livros.horizontalHeader()
        self.tbl_livros.itemChanged.connect(self.ajusteTabela)


    def ajusteTabela(self):
        self.tbl_livros.resizeColumnsToContents()
        self.tbl_livros.resizeRowsToContents()
        for row in range(self.tbl_livros.rowCount()):
            height = self.tbl_livros.rowHeight(row)
            self.tbl_livros.setRowHeight(row, height + 7)
