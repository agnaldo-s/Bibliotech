# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 870)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_20 = QHBoxLayout(self.widget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_13 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_13)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"   border-radius: 25%;\n"
"	border: 2px solid #000000\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_15)

        self.img_cabecalho = QLabel(self.frame)
        self.img_cabecalho.setObjectName(u"img_cabecalho")
        self.img_cabecalho.setMinimumSize(QSize(100, 100))
        self.img_cabecalho.setMaximumSize(QSize(100, 100))
        self.img_cabecalho.setStyleSheet(u"border: none;")
        self.img_cabecalho.setPixmap(QPixmap(u"../../icones/logo.png"))
        self.img_cabecalho.setScaledContents(True)

        self.horizontalLayout.addWidget(self.img_cabecalho)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_16)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.txt_cabecalho = QLabel(self.frame)
        self.txt_cabecalho.setObjectName(u"txt_cabecalho")
        self.txt_cabecalho.setStyleSheet(u"border: none;")

        self.verticalLayout_9.addWidget(self.txt_cabecalho)


        self.horizontalLayout_20.addWidget(self.frame)

        self.horizontalSpacer_14 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_14)


        self.verticalLayout_2.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    background-color: #F8F8F8;\n"
"    color: #333333;\n"
"    border: 2px solid #CCCCCC;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #EDEDED;\n"
"    border-color: #AAAAAA;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #DDDDDD;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #CCCCCC;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    background-color: #F8F8F8;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #AAAAAA;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #555555;\n"
"}\n"
"QLabel{\n"
"    border-radius: 10px;\n"
"}")
        self.pag_procurar_livro = QWidget()
        self.pag_procurar_livro.setObjectName(u"pag_procurar_livro")
        self.verticalLayout_3 = QVBoxLayout(self.pag_procurar_livro)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_input_nome_livro = QLineEdit(self.pag_procurar_livro)
        self.lbl_input_nome_livro.setObjectName(u"lbl_input_nome_livro")

        self.horizontalLayout_8.addWidget(self.lbl_input_nome_livro)

        self.btn_pesquisar_livro = QPushButton(self.pag_procurar_livro)
        self.btn_pesquisar_livro.setObjectName(u"btn_pesquisar_livro")
        self.btn_pesquisar_livro.setMinimumSize(QSize(25, 25))
        self.btn_pesquisar_livro.setMaximumSize(QSize(25, 25))
        self.btn_pesquisar_livro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar_livro.setMouseTracking(True)
        self.btn_pesquisar_livro.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: none;\n"
"    color: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F8F8F8;\n"
"    color: #333333;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../icones/pesquisar-livro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar_livro.setIcon(icon)
        self.btn_pesquisar_livro.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.btn_pesquisar_livro)

        self.btn_adicionar_livro = QPushButton(self.pag_procurar_livro)
        self.btn_adicionar_livro.setObjectName(u"btn_adicionar_livro")
        self.btn_adicionar_livro.setMinimumSize(QSize(25, 25))
        self.btn_adicionar_livro.setMaximumSize(QSize(25, 25))
        self.btn_adicionar_livro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adicionar_livro.setMouseTracking(True)
        self.btn_adicionar_livro.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: none;\n"
"    color: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F8F8F8;\n"
"    color: #333333;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../icones/adicionar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_adicionar_livro.setIcon(icon1)
        self.btn_adicionar_livro.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.btn_adicionar_livro)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tbl_livros = QTableWidget(self.pag_procurar_livro)
        if (self.tbl_livros.columnCount() < 6):
            self.tbl_livros.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_livros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_livros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_livros.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_livros.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_livros.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_livros.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tbl_livros.rowCount() < 1):
            self.tbl_livros.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_livros.setVerticalHeaderItem(0, __qtablewidgetitem6)
        self.tbl_livros.setObjectName(u"tbl_livros")
        self.tbl_livros.setStyleSheet(u"QTableView {\n"
"    background-color: #FFFFFF;\n"
"    alternate-background-color: #F8F8F8;\n"
"    border: 1px solid #CCCCCC;\n"
"    gridline-color: #DDDDDD;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"    border-bottom: 1px solid #DDDDDD;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #EDEDED;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F8F8F8;\n"
"    color: #333333;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"    background-color: #EDEDED;\n"
"    color: #333333;\n"
"}")

        self.verticalLayout_3.addWidget(self.tbl_livros)

        self.stackedWidget.addWidget(self.pag_procurar_livro)
        self.pag_editar_livro = QWidget()
        self.pag_editar_livro.setObjectName(u"pag_editar_livro")
        self.verticalLayout_8 = QVBoxLayout(self.pag_editar_livro)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.imagemLivro = QFrame(self.pag_editar_livro)
        self.imagemLivro.setObjectName(u"imagemLivro")
        self.imagemLivro.setStyleSheet(u"border: none;\n"
"")
        self.imagemLivro.setFrameShape(QFrame.StyledPanel)
        self.imagemLivro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.imagemLivro)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_11 = QSpacerItem(386, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)

        self.lbl_imagem_livro_editar = QLabel(self.imagemLivro)
        self.lbl_imagem_livro_editar.setObjectName(u"lbl_imagem_livro_editar")
        self.lbl_imagem_livro_editar.setMinimumSize(QSize(100, 150))
        self.lbl_imagem_livro_editar.setMaximumSize(QSize(100, 150))
        self.lbl_imagem_livro_editar.setStyleSheet(u"border: 1px solid #000000;")
        self.lbl_imagem_livro_editar.setPixmap(QPixmap(u"../../icones/sem_foto.png"))
        self.lbl_imagem_livro_editar.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.lbl_imagem_livro_editar)

        self.horizontalSpacer_12 = QSpacerItem(386, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_12)


        self.verticalLayout_8.addWidget(self.imagemLivro)

        self.widget_2 = QWidget(self.pag_editar_livro)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.txt_id = QLabel(self.widget_2)
        self.txt_id.setObjectName(u"txt_id")

        self.horizontalLayout_6.addWidget(self.txt_id)

        self.lbl_id = QLineEdit(self.widget_2)
        self.lbl_id.setObjectName(u"lbl_id")

        self.horizontalLayout_6.addWidget(self.lbl_id)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txt_titulo = QLabel(self.widget_2)
        self.txt_titulo.setObjectName(u"txt_titulo")

        self.horizontalLayout_7.addWidget(self.txt_titulo)

        self.lbl_titulo = QLineEdit(self.widget_2)
        self.lbl_titulo.setObjectName(u"lbl_titulo")

        self.horizontalLayout_7.addWidget(self.lbl_titulo)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txt_autora = QLabel(self.widget_2)
        self.txt_autora.setObjectName(u"txt_autora")

        self.horizontalLayout_4.addWidget(self.txt_autora)

        self.lbl_autora = QLineEdit(self.widget_2)
        self.lbl_autora.setObjectName(u"lbl_autora")

        self.horizontalLayout_4.addWidget(self.lbl_autora)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_editora = QLabel(self.widget_2)
        self.txt_editora.setObjectName(u"txt_editora")

        self.horizontalLayout_3.addWidget(self.txt_editora)

        self.lbl_editora = QLineEdit(self.widget_2)
        self.lbl_editora.setObjectName(u"lbl_editora")

        self.horizontalLayout_3.addWidget(self.lbl_editora)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_isbn = QLabel(self.widget_2)
        self.txt_isbn.setObjectName(u"txt_isbn")

        self.horizontalLayout_5.addWidget(self.txt_isbn)

        self.lbl_isbn = QLineEdit(self.widget_2)
        self.lbl_isbn.setObjectName(u"lbl_isbn")

        self.horizontalLayout_5.addWidget(self.lbl_isbn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_anoPublicacao = QLabel(self.widget_2)
        self.txt_anoPublicacao.setObjectName(u"txt_anoPublicacao")

        self.horizontalLayout_2.addWidget(self.txt_anoPublicacao)

        self.lbl_anoPublicacao = QLineEdit(self.widget_2)
        self.lbl_anoPublicacao.setObjectName(u"lbl_anoPublicacao")

        self.horizontalLayout_2.addWidget(self.lbl_anoPublicacao)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.txt_numExemplares = QLabel(self.widget_2)
        self.txt_numExemplares.setObjectName(u"txt_numExemplares")

        self.horizontalLayout_17.addWidget(self.txt_numExemplares)

        self.lbl_numExemplares = QLineEdit(self.widget_2)
        self.lbl_numExemplares.setObjectName(u"lbl_numExemplares")

        self.horizontalLayout_17.addWidget(self.lbl_numExemplares)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_17)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_10)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_editar = QPushButton(self.pag_editar_livro)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setMinimumSize(QSize(300, 0))
        self.btn_editar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_editar)

        self.btn_deletar = QPushButton(self.pag_editar_livro)
        self.btn_deletar.setObjectName(u"btn_deletar")
        self.btn_deletar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_deletar)

        self.btn_atualizar = QPushButton(self.pag_editar_livro)
        self.btn_atualizar.setObjectName(u"btn_atualizar")
        self.btn_atualizar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.btn_atualizar)


        self.horizontalLayout_18.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.stackedWidget.addWidget(self.pag_editar_livro)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_10 = QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.page_3)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.txt_cadastro = QLabel(self.widget_3)
        self.txt_cadastro.setObjectName(u"txt_cadastro")

        self.verticalLayout_4.addWidget(self.txt_cadastro)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.txt_id_cad = QLabel(self.widget_3)
        self.txt_id_cad.setObjectName(u"txt_id_cad")

        self.horizontalLayout_15.addWidget(self.txt_id_cad)

        self.lbl_id_cad = QLineEdit(self.widget_3)
        self.lbl_id_cad.setObjectName(u"lbl_id_cad")

        self.horizontalLayout_15.addWidget(self.lbl_id_cad)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.txt_titulo_cad = QLabel(self.widget_3)
        self.txt_titulo_cad.setObjectName(u"txt_titulo_cad")

        self.horizontalLayout_10.addWidget(self.txt_titulo_cad)

        self.lbl_titulo_cad = QLineEdit(self.widget_3)
        self.lbl_titulo_cad.setObjectName(u"lbl_titulo_cad")

        self.horizontalLayout_10.addWidget(self.lbl_titulo_cad)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.txt_autora_cad = QLabel(self.widget_3)
        self.txt_autora_cad.setObjectName(u"txt_autora_cad")

        self.horizontalLayout_11.addWidget(self.txt_autora_cad)

        self.lbl_autora_cad = QLineEdit(self.widget_3)
        self.lbl_autora_cad.setObjectName(u"lbl_autora_cad")

        self.horizontalLayout_11.addWidget(self.lbl_autora_cad)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.txt_editora_cad = QLabel(self.widget_3)
        self.txt_editora_cad.setObjectName(u"txt_editora_cad")

        self.horizontalLayout_12.addWidget(self.txt_editora_cad)

        self.lbl_editora_cad = QLineEdit(self.widget_3)
        self.lbl_editora_cad.setObjectName(u"lbl_editora_cad")

        self.horizontalLayout_12.addWidget(self.lbl_editora_cad)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.txt_isbn_cad = QLabel(self.widget_3)
        self.txt_isbn_cad.setObjectName(u"txt_isbn_cad")

        self.horizontalLayout_13.addWidget(self.txt_isbn_cad)

        self.lbl_isbn_cad = QLineEdit(self.widget_3)
        self.lbl_isbn_cad.setObjectName(u"lbl_isbn_cad")

        self.horizontalLayout_13.addWidget(self.lbl_isbn_cad)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.txt_anoPublicacao_cad = QLabel(self.widget_3)
        self.txt_anoPublicacao_cad.setObjectName(u"txt_anoPublicacao_cad")

        self.horizontalLayout_14.addWidget(self.txt_anoPublicacao_cad)

        self.lbl_anoPublicacao_cad = QLineEdit(self.widget_3)
        self.lbl_anoPublicacao_cad.setObjectName(u"lbl_anoPublicacao_cad")

        self.horizontalLayout_14.addWidget(self.lbl_anoPublicacao_cad)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.txt_numExemplares_cad = QLabel(self.widget_3)
        self.txt_numExemplares_cad.setObjectName(u"txt_numExemplares_cad")

        self.horizontalLayout_9.addWidget(self.txt_numExemplares_cad)

        self.lbn_numExemplares_cad = QLineEdit(self.widget_3)
        self.lbn_numExemplares_cad.setObjectName(u"lbn_numExemplares_cad")

        self.horizontalLayout_9.addWidget(self.lbn_numExemplares_cad)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_7)

        self.frame_imagemLivro = QLabel(self.widget_4)
        self.frame_imagemLivro.setObjectName(u"frame_imagemLivro")
        self.frame_imagemLivro.setMinimumSize(QSize(100, 150))
        self.frame_imagemLivro.setMaximumSize(QSize(100, 150))
        self.frame_imagemLivro.setAutoFillBackground(False)
        self.frame_imagemLivro.setStyleSheet(u"border: 1px solid #000000;")
        self.frame_imagemLivro.setPixmap(QPixmap(u"../../icones/sem_foto.png"))
        self.frame_imagemLivro.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.frame_imagemLivro)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_17)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_addImagem_cad = QPushButton(self.widget_4)
        self.btn_addImagem_cad.setObjectName(u"btn_addImagem_cad")
        self.btn_addImagem_cad.setMinimumSize(QSize(300, 0))
        self.btn_addImagem_cad.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_addImagem_cad)

        self.btn_salvar_cad = QPushButton(self.widget_4)
        self.btn_salvar_cad.setObjectName(u"btn_salvar_cad")
        self.btn_salvar_cad.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_salvar_cad)


        self.horizontalLayout_21.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_18)


        self.verticalLayout_6.addLayout(self.horizontalLayout_21)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_cabecalho.setText("")
        self.txt_cabecalho.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">BiblioTecH</span></p></body></html>", None))
        self.lbl_input_nome_livro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira o nome do livro", None))
        self.btn_pesquisar_livro.setText("")
        self.btn_adicionar_livro.setText("")
        ___qtablewidgetitem = self.tbl_livros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tbl_livros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem2 = self.tbl_livros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem3 = self.tbl_livros.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Editora", None));
        ___qtablewidgetitem4 = self.tbl_livros.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem5 = self.tbl_livros.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ano de Publica\u00e7\u00e3o", None));
        ___qtablewidgetitem6 = self.tbl_livros.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.lbl_imagem_livro_editar.setText("")
        self.txt_id.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.lbl_id.setInputMask("")
        self.lbl_id.setText("")
        self.txt_titulo.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.lbl_titulo.setInputMask("")
        self.lbl_titulo.setText("")
        self.txt_autora.setText(QCoreApplication.translate("MainWindow", u"Autor (a)", None))
        self.lbl_autora.setText("")
        self.txt_editora.setText(QCoreApplication.translate("MainWindow", u"Editora:", None))
        self.lbl_editora.setText("")
        self.txt_isbn.setText(QCoreApplication.translate("MainWindow", u"ISBN:", None))
        self.lbl_isbn.setInputMask(QCoreApplication.translate("MainWindow", u"0-000-00000-0", None))
        self.lbl_isbn.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.lbl_isbn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I", None))
        self.txt_anoPublicacao.setText(QCoreApplication.translate("MainWindow", u"Ano de Publica\u00e7\u00e3o:", None))
        self.lbl_anoPublicacao.setInputMask(QCoreApplication.translate("MainWindow", u"0000", None))
        self.lbl_anoPublicacao.setText("")
        self.txt_numExemplares.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Exemplares:", None))
        self.lbl_numExemplares.setText("")
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_deletar.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.btn_atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.txt_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Cadastro</span></p></body></html>", None))
        self.txt_id_cad.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.lbl_id_cad.setText("")
        self.txt_titulo_cad.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.lbl_titulo_cad.setText("")
        self.txt_autora_cad.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.lbl_autora_cad.setText("")
        self.txt_editora_cad.setText(QCoreApplication.translate("MainWindow", u"Editora:", None))
        self.lbl_editora_cad.setText("")
        self.txt_isbn_cad.setText(QCoreApplication.translate("MainWindow", u"ISBN:", None))
        self.lbl_isbn_cad.setText("")
        self.txt_anoPublicacao_cad.setText(QCoreApplication.translate("MainWindow", u"Ano de Publica\u00e7\u00e3o:", None))
        self.lbl_anoPublicacao_cad.setText("")
        self.txt_numExemplares_cad.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Exemplares:", None))
        self.lbn_numExemplares_cad.setText("")
        self.frame_imagemLivro.setText("")
        self.btn_addImagem_cad.setText(QCoreApplication.translate("MainWindow", u"Adicionar Imagem", None))
        self.btn_salvar_cad.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

