import sys
from view.tela_principal import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)

window = MainWindow()
window.show()
window.showMaximized()

app.exec()
