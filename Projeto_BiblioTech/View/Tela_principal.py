import json

import requests
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QComboBox, QWidget, QPushButton, QMessageBox, QSizePolicy, \
    QLabel, QLineEdit, QTableWidget, QAbstractItemView, QTableWidgetItem, QTextEdit, QHeaderView

from Infra.Configs.connection import DBConnectionHandler
from Infra.Entities.Livro import Livro
from Infra.Repository.Livro_repository import Livro_repository


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()