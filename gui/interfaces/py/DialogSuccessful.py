# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogSuccessfulHKyXVG.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from gui.resources import *

class Ui_DialogSucessful(object):
    def setupUi(self, DialogSucessful):
        if not DialogSucessful.objectName():
            DialogSucessful.setObjectName(u"DialogSucessful")
        DialogSucessful.resize(500, 200)
        DialogSucessful.setMinimumSize(QSize(500, 200))
        DialogSucessful.setMaximumSize(QSize(500, 200))
        DialogSucessful.setStyleSheet(u"*{\n"
"	font-family:\"Segoe UI\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"	color: rgb(221, 221, 221);\n"
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
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"#body_content{\n"
"	background-color:rgb(26, 29, 34);\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(DialogSucessful)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.container_app = QFrame(DialogSucessful)
        self.container_app.setObjectName(u"container_app")
        self.container_app.setFrameShape(QFrame.StyledPanel)
        self.container_app.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.container_app)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout.setContentsMargins(0, 0, 4, 0)
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
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.header_content)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(20, 20))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_Close = QPushButton(self.frame)
        self.btn_Close.setObjectName(u"btn_Close")
        self.btn_Close.setMinimumSize(QSize(20, 20))
        self.btn_Close.setMaximumSize(QSize(20, 20))
        self.btn_Close.setStyleSheet(u"background-image: url(:/icons/icons/icon_close.png);")

        self.horizontalLayout_4.addWidget(self.btn_Close)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.header_content)

        self.body_content = QFrame(self.container_app)
        self.body_content.setObjectName(u"body_content")
        self.body_content.setStyleSheet(u"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;")
        self.body_content.setFrameShape(QFrame.StyledPanel)
        self.body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.body_content)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.body_content)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(13)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.frame_image = QFrame(self.frame_6)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setMinimumSize(QSize(40, 40))
        self.frame_image.setMaximumSize(QSize(40, 40))
        self.frame_image.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-image: url(:/images/images/exito40.png);\n"
"background-position: center;")
        self.frame_image.setFrameShape(QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_image)

        self.label_message = QLabel(self.frame_6)
        self.label_message.setObjectName(u"label_message")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_message.sizePolicy().hasHeightForWidth())
        self.label_message.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_message.setFont(font3)
        self.label_message.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_message.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_message.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_message)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.body_content)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 6)
        self.btn_ok = QPushButton(self.frame_5)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(100, 30))
        self.btn_ok.setMaximumSize(QSize(100, 30))
        self.btn_ok.setStyleSheet(u"QPushButton{\n"
"	border: none; /* Remove as bordas */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"                                stop:0 #B3D2F2, stop:1 #4E60FF); /* Gradiente de cor de fundo */\n"
"    color: white; /* Cor do texto do bot\u00e3o */\n"
"    padding: 5px; /* Espa\u00e7amento interno do bot\u00e3o */\n"
"    border-radius: 5px; /* Bordas arredondadas (opcional) */\n"
"	font-weight: bold;\n"
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

        self.verticalLayout_4.addWidget(self.btn_ok, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.body_content)


        self.verticalLayout.addWidget(self.container_app)


        self.retranslateUi(DialogSucessful)

        QMetaObject.connectSlotsByName(DialogSucessful)
    # setupUi

    def retranslateUi(self, DialogSucessful):
        DialogSucessful.setWindowTitle(QCoreApplication.translate("DialogSucessful", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogSucessful", u"LuHf", None))
        self.btn_Close.setText("")
        self.label_2.setText(QCoreApplication.translate("DialogSucessful", u"Successful!", None))
        self.label_message.setText(QCoreApplication.translate("DialogSucessful", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogSucessful", u"Ok", None))
    # retranslateUi

