# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BackgroundSignalOGsDKE.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_BackgroundWindow(object):
    def setupUi(self, BackgroundWindow):
        if not BackgroundWindow.objectName():
            BackgroundWindow.setObjectName(u"BackgroundWindow")
        BackgroundWindow.resize(800, 500)
        BackgroundWindow.setMinimumSize(QSize(800, 500))
        BackgroundWindow.setMaximumSize(QSize(16777215, 16777215))
        BackgroundWindow.setStyleSheet(u"/*	Propriedades globais, que se aplicam em toda interface*/\n"
"*{\n"
"	font-family:\"Segoe UI\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"#container_app{\n"
"	background-color: rgb(40, 44, 52);\n"
"	border-radius: 4px;\n"
"}\n"
"/*	Propriedades que se aplicam ao conteudo do cabe\u00e7alho da interface*/\n"
"#header_content{\n"
"	background-color:#21252B;\n"
"	border-bottom: 1px solid rgba(0,0,0,0.2);\n"
"	color: grey;\n"
"}\n"
"#header_content QPushButton{\n"
"	background-color: transparent;\n"
"	\n"
"}\n"
"\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito de hover quando o mouse \u00e9 passado por eles*/\n"
"#header_content QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"/*	Propriedades que se aplicam aos bot\u00f5es , que aplicam um efeito dque muda a cor dos bot\u00f5es quando eles s\u00e3o pressionados */\n"
"#header_content.QPushButton:pressed {	\n"
"	background-color: #169EF2 ;\n"
"	color: #495D7DE3;\n"
"}\n"
"/*	Pr"
                        "opriedades que se aplicam ao widget do conte\u00fado principal da janela*/\n"
"#Graph_content{\n"
"	background-color:rgb(40, 44, 52);\n"
"}\n"
"")
        self.centralwidget = QWidget(BackgroundWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container_app = QWidget(self.centralwidget)
        self.container_app.setObjectName(u"container_app")
        self.verticalLayout_2 = QVBoxLayout(self.container_app)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_content = QWidget(self.container_app)
        self.header_content.setObjectName(u"header_content")
        self.header_content.setMinimumSize(QSize(0, 30))
        self.header_content.setMaximumSize(QSize(16777214, 30))
        self.header_content.setStyleSheet(u"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.header_content)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.frame = QFrame(self.header_content)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(25, 25))
        self.frame.setStyleSheet(u"background-image: url(:/images/images/logo_25x25.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.label = QLabel(self.header_content)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_redm_janela = QFrame(self.header_content)
        self.frame_redm_janela.setObjectName(u"frame_redm_janela")
        self.frame_redm_janela.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 0px\n"
"}")
        self.frame_redm_janela.setFrameShape(QFrame.StyledPanel)
        self.frame_redm_janela.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_redm_janela)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_MinimizeApp = QPushButton(self.frame_redm_janela)
        self.btn_MinimizeApp.setObjectName(u"btn_MinimizeApp")
        self.btn_MinimizeApp.setMinimumSize(QSize(25, 25))
        self.btn_MinimizeApp.setMaximumSize(QSize(25, 25))
        self.btn_MinimizeApp.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_MinimizeApp.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_MinimizeApp)

        self.btn_RestaureSizeApp = QPushButton(self.frame_redm_janela)
        self.btn_RestaureSizeApp.setObjectName(u"btn_RestaureSizeApp")
        self.btn_RestaureSizeApp.setMinimumSize(QSize(25, 25))
        self.btn_RestaureSizeApp.setMaximumSize(QSize(25, 25))
        self.btn_RestaureSizeApp.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_RestaureSizeApp.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.btn_RestaureSizeApp)

        self.btn_CloseApp = QPushButton(self.frame_redm_janela)
        self.btn_CloseApp.setObjectName(u"btn_CloseApp")
        self.btn_CloseApp.setMinimumSize(QSize(25, 25))
        self.btn_CloseApp.setMaximumSize(QSize(25, 25))
        self.btn_CloseApp.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: red;\n"
"	border-top-right-radius: 2px;\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_CloseApp.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.btn_CloseApp)


        self.horizontalLayout.addWidget(self.frame_redm_janela)


        self.verticalLayout_2.addWidget(self.header_content)

        self.body_content = QWidget(self.container_app)
        self.body_content.setObjectName(u"body_content")
        self.body_content.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.body_content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Graph_content = QWidget(self.body_content)
        self.Graph_content.setObjectName(u"Graph_content")
        self.Graph_content.setStyleSheet(u"border-bottom-right-radius: 4px;")
        self.verticalLayout_6 = QVBoxLayout(self.Graph_content)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.graphic_area = QWidget(self.Graph_content)
        self.graphic_area.setObjectName(u"graphic_area")
        self.verticalLayout_7 = QVBoxLayout(self.graphic_area)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_6.addWidget(self.graphic_area)

        self.grid_resize = QFrame(self.Graph_content)
        self.grid_resize.setObjectName(u"grid_resize")
        self.grid_resize.setMinimumSize(QSize(20, 20))
        self.grid_resize.setMaximumSize(QSize(20, 20))
        self.grid_resize.setStyleSheet(u"background-image: url(:/icones/icons/cil-size-grip.png);\n"
"background-repeat: none;")
        self.grid_resize.setFrameShape(QFrame.StyledPanel)
        self.grid_resize.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.grid_resize, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.Graph_content)


        self.verticalLayout_2.addWidget(self.body_content)


        self.verticalLayout.addWidget(self.container_app)

        BackgroundWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BackgroundWindow)

        QMetaObject.connectSlotsByName(BackgroundWindow)
    # setupUi

    def retranslateUi(self, BackgroundWindow):
        BackgroundWindow.setWindowTitle(QCoreApplication.translate("BackgroundWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("BackgroundWindow", u" Background/Signal", None))
#if QT_CONFIG(tooltip)
        self.btn_MinimizeApp.setToolTip(QCoreApplication.translate("BackgroundWindow", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_MinimizeApp.setText("")
#if QT_CONFIG(tooltip)
        self.btn_RestaureSizeApp.setToolTip(QCoreApplication.translate("BackgroundWindow", u"Maximizar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RestaureSizeApp.setText("")
#if QT_CONFIG(tooltip)
        self.btn_CloseApp.setToolTip(QCoreApplication.translate("BackgroundWindow", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.btn_CloseApp.setText("")
    # retranslateUi

