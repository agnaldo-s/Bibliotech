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
        MainWindow.resize(944, 816)
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

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(100, 100))
        self.label_19.setMaximumSize(QSize(100, 100))
        self.label_19.setStyleSheet(u"border: none;")
        self.label_19.setPixmap(QPixmap(u"icones/logo.png"))
        self.label_19.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_19)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_16)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border: none;")

        self.verticalLayout_9.addWidget(self.label_2)


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
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_8.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(25, 25))
        self.pushButton.setMaximumSize(QSize(25, 25))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u"icones/pesquisar-livro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(25, 25))
        self.pushButton_2.setMaximumSize(QSize(25, 25))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(u"icones/adicionar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButton_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableWidget = QTableWidget(self.page)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableView {\n"
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

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.imagemLivro = QFrame(self.page_2)
        self.imagemLivro.setObjectName(u"imagemLivro")
        self.imagemLivro.setStyleSheet(u"border: none;\n"
"")
        self.imagemLivro.setFrameShape(QFrame.StyledPanel)
        self.imagemLivro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.imagemLivro)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_11 = QSpacerItem(386, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_11)

        self.label_18 = QLabel(self.imagemLivro)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(100, 150))
        self.label_18.setMaximumSize(QSize(100, 150))
        self.label_18.setStyleSheet(u"border: 1px solid #000000;")
        self.label_18.setPixmap(QPixmap(u"icones/sem_foto.png"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.label_18)

        self.horizontalSpacer_12 = QSpacerItem(386, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_12)


        self.verticalLayout_8.addWidget(self.imagemLivro)

        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_6 = QLineEdit(self.widget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_4.addWidget(self.lineEdit_6)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lineEdit_7 = QLineEdit(self.widget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_3.addWidget(self.lineEdit_7)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(self.widget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_5.addWidget(self.lineEdit_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.widget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.widget_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.lineEdit_15 = QLineEdit(self.widget_2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.horizontalLayout_17.addWidget(self.lineEdit_15)

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
        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(300, 0))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.page_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.pushButton_6)


        self.horizontalLayout_18.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_10 = QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.page_3)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_4.addWidget(self.label_15)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_15.addWidget(self.label_8)

        self.lineEdit_8 = QLineEdit(self.widget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_15.addWidget(self.lineEdit_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lineEdit_9 = QLineEdit(self.widget_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_10.addWidget(self.lineEdit_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.lineEdit_10 = QLineEdit(self.widget_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_11.addWidget(self.lineEdit_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.lineEdit_11 = QLineEdit(self.widget_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_12.addWidget(self.lineEdit_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.lineEdit_13 = QLineEdit(self.widget_3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_13.addWidget(self.lineEdit_13)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.lineEdit_12 = QLineEdit(self.widget_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_14.addWidget(self.lineEdit_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.lineEdit_14 = QLineEdit(self.widget_3)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_9.addWidget(self.lineEdit_14)


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

        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(100, 150))
        self.label_16.setMaximumSize(QSize(100, 150))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setStyleSheet(u"border: 1px solid #000000;")
        self.label_16.setPixmap(QPixmap(u"icones/sem_foto.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_16)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_17)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_7 = QPushButton(self.widget_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(300, 0))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.widget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.pushButton_8)


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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_19.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">BiblioTecH</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira o nome do livro", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Editora", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ano de Publica\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_18.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.lineEdit_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.lineEdit_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Editora:", None))
        self.lineEdit_7.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ISBN:", None))
        self.lineEdit_5.setInputMask(QCoreApplication.translate("MainWindow", u"0-000-00000-0", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"I", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ano de Publica\u00e7\u00e3o:", None))
        self.lineEdit_4.setInputMask(QCoreApplication.translate("MainWindow", u"0000", None))
        self.lineEdit_4.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Exemplares:", None))
        self.lineEdit_15.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Cadastro</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.lineEdit_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.lineEdit_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.lineEdit_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Editora:", None))
        self.lineEdit_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ISBN:", None))
        self.lineEdit_13.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ano de Publica\u00e7\u00e3o:", None))
        self.lineEdit_12.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Exemplares:", None))
        self.lineEdit_14.setText("")
        self.label_16.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Adicionar Imagem", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
    # retranslateUi

