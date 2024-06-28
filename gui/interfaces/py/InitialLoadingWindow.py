# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InitialLoadingWindowYyGnwe.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(700, 400)
        SplashScreen.setMinimumSize(QSize(700, 400))
        SplashScreen.setMaximumSize(QSize(700, 400))
        SplashScreen.setStyleSheet(u"*{\n"
"	font-family: \"Bahnschrift\";\n"
"	background-repeat: none;\n"
"	background-position: center;\n"
"}\n"
"#splash{\n"
"	background-color:rgb(40, 44, 52);\n"
"	border-radius: 10px;\n"
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
"	\n"
"\n"
"\n"
"}")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splash = QFrame(self.centralwidget)
        self.splash.setObjectName(u"splash")
        self.splash.setFrameShape(QFrame.StyledPanel)
        self.splash.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.splash)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.frame_3 = QFrame(self.splash)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 150))
        self.frame.setMaximumSize(QSize(150, 150))
        self.frame.setStyleSheet(u"background-image: url(:/images/images/logo_200x200.png);\n"
"background-image: url(:/images/images/logo_200x200.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"color: grey;\n"
"font-size: 12pt;")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(500, 20))
        self.progressBar.setMaximumSize(QSize(500, 20))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.verticalLayout_3.addWidget(self.progressBar, 0, Qt.AlignHCenter)

        self.label_tips = QLabel(self.frame_3)
        self.label_tips.setObjectName(u"label_tips")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tips.sizePolicy().hasHeightForWidth())
        self.label_tips.setSizePolicy(sizePolicy)
        self.label_tips.setMinimumSize(QSize(500, 60))
        self.label_tips.setMaximumSize(QSize(500, 60))
        self.label_tips.setStyleSheet(u"color: grey;\n"
"font-size: 10pt;")
        self.label_tips.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_tips, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: grey;\n"
"")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.splash)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"Loading...", None))
        self.label_tips.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SplashScreen", u"v0.01", None))
    # retranslateUi

