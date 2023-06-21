from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap, QPicture

from os import path


from projetoBiblioTech.view.mainWindow import Ui_MainWindow

pasta_base = path.abspath(path.join(path.dirname(__file__), '..'))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

