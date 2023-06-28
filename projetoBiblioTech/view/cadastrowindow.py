from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from projetoBiblioTech.infra.entities.usuario import Usuario
from projetoBiblioTech.infra.repository.usuario_repository import UsuarioRepository


class CadastroWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Definir a interface da tela de cadastro
        self.setWindowTitle("Cadastro")
        self.setGeometry(100, 100, 300, 200)

        self.lbl_username = QLabel("Usuário:", self)
        self.txt_username = QLineEdit(self)

        self.lbl_password = QLabel("Senha:", self)
        self.txt_password = QLineEdit(self)
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.btn_cadastrar = QPushButton("Cadastrar", self)
        self.btn_cadastrar.clicked.connect(self.cadastrar)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_username)
        layout.addWidget(self.txt_username)
        layout.addWidget(self.lbl_password)
        layout.addWidget(self.txt_password)
        layout.addWidget(self.btn_cadastrar)

        self.setLayout(layout)

    def cadastrar(self):
        username = self.txt_username.text()
        password = self.txt_password.text()

        # Verificar se o usuário já existe no banco de dados
        usuario_repository = UsuarioRepository()
        if usuario_repository.find_by_username(username):
            QMessageBox.warning(self, "Cadastro", "Usuário já existente.")
            return

        # Cadastrar o novo usuário no banco de dados
        usuario = Usuario(username=username, password=password)
        usuario_repository.insert(usuario)

        self.accept()  # Cadastro bem-sucedido, aceita o diálogo
