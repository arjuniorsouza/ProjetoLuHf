# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewProjectriOYiT.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from gui.resources import *

class Ui_NewProjectWindow(object):
    def setupUi(self, NewProjectWindow):
        if not NewProjectWindow.objectName():
            NewProjectWindow.setObjectName(u"NewProjectWindow")
        NewProjectWindow.resize(500, 250)
        NewProjectWindow.setMinimumSize(QSize(500, 250))
        NewProjectWindow.setMaximumSize(QSize(500, 250))
        NewProjectWindow.setStyleSheet(u"*{\n"
"	font-family:\"Segoe UI\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"	color: rgb(221, 221, 221);\n"
"}\n"
"\n"
"#container_app{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#header_content{\n"
"	background-color: rgb(11, 13, 15);\n"
"	\n"
"}\n"
"#header_content QPushButton{\n"
"	background-color: transparent;\n"
"	border-radius: 5px;\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#header_content QPushButton:hover{\n"
"	background-color: red;\n"
"}\n"
"#body_content{\n"
"	background-color:rgb(26, 29, 34);\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(11, 13, 15);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 5px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color:  #55afcf;\n"
"}\n"
"#label_LocalProject{\n"
"	background-color: rgb(11, 13, 15);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 5px;\n"
""
                        "	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")
        self.centralwidget = QWidget(NewProjectWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.container_app = QFrame(self.centralwidget)
        self.container_app.setObjectName(u"container_app")
        self.container_app.setFrameShape(QFrame.StyledPanel)
        self.container_app.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.container_app)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_content = QFrame(self.container_app)
        self.header_content.setObjectName(u"header_content")
        self.header_content.setMinimumSize(QSize(0, 30))
        self.header_content.setMaximumSize(QSize(16777215, 30))
        self.header_content.setStyleSheet(u"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;")
        self.header_content.setFrameShape(QFrame.StyledPanel)
        self.header_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.header_content)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(30, 30))
        self.frame_3.setMaximumSize(QSize(30, 30))
        self.frame_3.setStyleSheet(u"background-image: url(:/images/images/logo_25x25.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.header_content)
        self.frame_2.setObjectName(u"frame_2")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: 10pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header_content)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(25, 25))
        self.frame.setMaximumSize(QSize(25, 25))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_Close = QPushButton(self.frame)
        self.btn_Close.setObjectName(u"btn_Close")
        self.btn_Close.setMinimumSize(QSize(25, 25))
        self.btn_Close.setMaximumSize(QSize(25, 25))
        self.btn_Close.setStyleSheet(u"background-image: url(:/icones/icons/icon_close.png);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Close.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_Close)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.header_content)

        self.body_content = QFrame(self.container_app)
        self.body_content.setObjectName(u"body_content")
        self.body_content.setStyleSheet(u"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;")
        self.body_content.setFrameShape(QFrame.StyledPanel)
        self.body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_nome = QFrame(self.body_content)
        self.frame_nome.setObjectName(u"frame_nome")
        self.frame_nome.setMinimumSize(QSize(0, 40))
        self.frame_nome.setMaximumSize(QSize(16777215, 40))
        self.frame_nome.setFrameShape(QFrame.StyledPanel)
        self.frame_nome.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_nome)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(self.frame_nome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))
        self.label_2.setMaximumSize(QSize(50, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.lineEdit_NameProject = QLineEdit(self.frame_nome)
        self.lineEdit_NameProject.setObjectName(u"lineEdit_NameProject")

        self.horizontalLayout_2.addWidget(self.lineEdit_NameProject)


        self.verticalLayout_3.addWidget(self.frame_nome)

        self.frame_local_projeto = QFrame(self.body_content)
        self.frame_local_projeto.setObjectName(u"frame_local_projeto")
        self.frame_local_projeto.setMinimumSize(QSize(0, 40))
        self.frame_local_projeto.setMaximumSize(QSize(16777215, 40))
        self.frame_local_projeto.setFrameShape(QFrame.StyledPanel)
        self.frame_local_projeto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_local_projeto)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_local_projeto)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 0))
        self.label_3.setMaximumSize(QSize(60, 16777215))
        self.label_3.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_LocalProject = QLineEdit(self.frame_local_projeto)
        self.lineEdit_LocalProject.setObjectName(u"lineEdit_LocalProject")

        self.horizontalLayout_3.addWidget(self.lineEdit_LocalProject)

        self.btn_LocalSaveProject = QPushButton(self.frame_local_projeto)
        self.btn_LocalSaveProject.setObjectName(u"btn_LocalSaveProject")
        self.btn_LocalSaveProject.setMinimumSize(QSize(80, 20))
        self.btn_LocalSaveProject.setMaximumSize(QSize(90, 20))
        self.btn_LocalSaveProject.setFont(font1)
        self.btn_LocalSaveProject.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: none;\n"
"	border-radius: 3px;\n"
"	background-position: left;\n"
"	font: 10pt \"Segoe UI\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255,255,255,0.1);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: 2828c5;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid, rgba(0,0,0,0.1);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_LocalSaveProject.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btn_LocalSaveProject)


        self.verticalLayout_3.addWidget(self.frame_local_projeto)

        self.frame_5 = QFrame(self.body_content)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_CreateProject = QPushButton(self.frame_5)
        self.btn_CreateProject.setObjectName(u"btn_CreateProject")
        self.btn_CreateProject.setMinimumSize(QSize(100, 30))
        self.btn_CreateProject.setMaximumSize(QSize(100, 30))
        self.btn_CreateProject.setStyleSheet(u"QPushButton{\n"
"border: none; /* Remove as bordas */\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #B3D2F2, stop:1 #4E60FF); /* Gradiente de cor de fundo */\n"
"color: white; /* Cor do texto do bot\u00e3o */\n"
"padding: 5px; /* Espa\u00e7amento interno do bot\u00e3o */\n"
"border-radius: 5px; /* Bordas arredondadas (opcional) */\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #FFBD33, stop:1 #FF5733); /* Gradiente ao passar o mouse */\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: 2828c5;\n"
"	color: rgb(255, 255, 255);\n"
"	border: 1px solid, rgba(0,0,0,0.1);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_CreateProject, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.body_content)


        self.verticalLayout.addWidget(self.container_app)

        NewProjectWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewProjectWindow)

        QMetaObject.connectSlotsByName(NewProjectWindow)
    # setupUi

    def retranslateUi(self, NewProjectWindow):
        NewProjectWindow.setWindowTitle(QCoreApplication.translate("NewProjectWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("NewProjectWindow", u"New project", None))
        self.btn_Close.setText("")
        self.label_2.setText(QCoreApplication.translate("NewProjectWindow", u"Name:", None))
        self.lineEdit_NameProject.setText("")
        self.label_3.setText(QCoreApplication.translate("NewProjectWindow", u"Directory:", None))
        self.btn_LocalSaveProject.setText(QCoreApplication.translate("NewProjectWindow", u"Open", None))
        self.btn_CreateProject.setText(QCoreApplication.translate("NewProjectWindow", u"Create ", None))
    # retranslateUi

