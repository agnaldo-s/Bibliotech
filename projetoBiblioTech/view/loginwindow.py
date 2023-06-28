from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from projetoBiblioTech.infra.repository.usuario_repository import UsuarioRepository
from projetoBiblioTech.view.cadastrowindow import CadastroWindow


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Definir a interface da tela de login
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        self.lbl_username = QLabel("Usuário:", self)
        self.txt_username = QLineEdit(self)

        self.lbl_password = QLabel("Senha:", self)
        self.txt_password = QLineEdit(self)
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Login", self)
        self.btn_login.clicked.connect(self.login)

        self.btn_cadastro = QPushButton("Cadastrar", self)
        self.btn_cadastro.clicked.connect(self.cadastrar)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_username)
        layout.addWidget(self.txt_username)
        layout.addWidget(self.lbl_password)
        layout.addWidget(self.txt_password)
        layout.addWidget(self.btn_login)
        layout.addWidget(self.btn_cadastro)

        self.setLayout(layout)

    def login(self):
        username = self.txt_username.text()
        password = self.txt_password.text()

        # Verificar a autenticação do usuário no banco de dados
        usuario_repository = UsuarioRepository()
        usuario = usuario_repository.find_by_username(username)
        if usuario and usuario.password == password:
            self.accept()  # Login bem-sucedido, aceita o diálogo
        else:
            QMessageBox.warning(self, "Login", "Usuário ou senha inválidos.")

    def cadastrar(self):
        cadastro_window = CadastroWindow()
        if cadastro_window.exec_() == QDialog.Accepted:
            QMessageBox.information(self, "Cadastro", "Cadastro realizado com sucesso.")
