import sys
from PySide6.QtWidgets import QApplication

from view.tela_principal import MainWindow
from view.mainWindow import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

from view.mainWindow import Ui_MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
