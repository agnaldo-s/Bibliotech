import sys

from projetoBiblioTech.view.loginwindow import LoginWindow
from view.tela_principal import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    if login_window.exec_() == LoginWindow.Accepted:
        # Se o login for bem-sucedido, abra a janela principal
        main_window = MainWindow()
        main_window.showMaximized()

    sys.exit(app.exec())
