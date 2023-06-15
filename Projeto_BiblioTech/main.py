import sys
from PySide6.QtWidgets import QApplication

from View.Tela_principal import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()