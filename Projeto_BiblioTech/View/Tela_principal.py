from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap
from os import path


from View.mainWindow import Ui_MainWindow

pasta_base = path.abspath(path.join(path.dirname(__file__), '..'))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
