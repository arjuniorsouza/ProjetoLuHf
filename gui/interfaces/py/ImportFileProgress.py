# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImportFileProgressOrdITB.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_ImportFilesWindow(object):
    def setupUi(self, ImportFilesWindow):
        if not ImportFilesWindow.objectName():
            ImportFilesWindow.setObjectName(u"ImportFilesWindow")
        ImportFilesWindow.resize(590, 200)
        ImportFilesWindow.setMinimumSize(QSize(590, 200))
        ImportFilesWindow.setMaximumSize(QSize(590, 200))
        ImportFilesWindow.setStyleSheet(u"*{\n"
"	font-family: \"Bahnschrift\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"\n"
"\n"
"#header_content{\n"
"	background-color: rgb(11, 13, 15);\n"
"}	\n"
"\n"
"#body_content{\n"
"	background-color:rgb(40, 44, 52);\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ProgressBar */\n"
"\n"
"QProgressBar {\n"
"	color: black;\n"
"	text-align: center;\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 white , stop:0.5 #B2D0F3 , stop:1 #6E84FB, stop: 2 #4E60FF);\n"
"}")
        self.verticalLayout = QVBoxLayout(ImportFilesWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.container_app = QFrame(ImportFilesWindow)
        self.container_app.setObjectName(u"container_app")
        self.container_app.setMinimumSize(QSize(580, 170))
        self.container_app.setMaximumSize(QSize(580, 170))
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
        font.setFamilies([u"Bahnschrift"])
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
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: grey;")

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_6.addWidget(self.header_content)

        self.body_content = QFrame(self.container_app)
        self.body_content.setObjectName(u"body_content")
        self.body_content.setStyleSheet(u"")
        self.body_content.setFrameShape(QFrame.StyledPanel)
        self.body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.body_content)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setStyleSheet(u"color: grey;\n"
"font-size: 14pt;")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.progressBar = QProgressBar(self.body_content)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(500, 20))
        self.progressBar.setMaximumSize(QSize(500, 20))
        self.progressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.progressBar, 0, Qt.AlignHCenter)

        self.label_num_files = QLabel(self.body_content)
        self.label_num_files.setObjectName(u"label_num_files")
        self.label_num_files.setMinimumSize(QSize(0, 20))
        self.label_num_files.setMaximumSize(QSize(16777215, 20))
        self.label_num_files.setStyleSheet(u"color: grey;\n"
"font-size: 10pt;")
        self.label_num_files.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_num_files, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.body_content)


        self.verticalLayout.addWidget(self.container_app)


        self.retranslateUi(ImportFilesWindow)

        QMetaObject.connectSlotsByName(ImportFilesWindow)
    # setupUi

    def retranslateUi(self, ImportFilesWindow):
        ImportFilesWindow.setWindowTitle(QCoreApplication.translate("ImportFilesWindow", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ImportFilesWindow", u"LuHf", None))
        self.label_2.setText(QCoreApplication.translate("ImportFilesWindow", u"Importing files...", None))
        self.label_num_files.setText("")
    # retranslateUi

