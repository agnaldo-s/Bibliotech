import sys
from PySide6.QtWidgets import QApplication

from View.Tela_principal import MainWindow
from View.mainWindow import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

from View.mainWindow import Ui_MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
