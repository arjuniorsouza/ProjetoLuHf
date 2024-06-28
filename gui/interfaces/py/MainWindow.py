# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowwBBJYx.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from gui.resources import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 566)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"QFrame{\n"
"	border: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(78,96,255);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#top"
                        "Logo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: grey; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(78,96,255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	ba"
                        "ckground-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(78,96,255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(78,96,255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
""
                        "/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover"
                        " {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-c"
                        "olor: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::it"
                        "em{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 3px;\n"
"	padding-right: 3px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgba(255,255,255,0.1);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	backgro"
                        "und-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////"
                        "////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(78,96,255);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(78,96,255);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: non"
                        "e;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(78,96,255);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgb(78,96,255);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
""
                        "     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 10px;\n"
"	height: 10px;\n"
"	border-radius: 8px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
""
                        "QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(78,96,255);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"Q"
                        "ComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
""
                        "	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* ////////////////////"
                        "/////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/logo_45x45.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-ethernet.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_Home = QPushButton(self.topMenu)
        self.btn_Home.setObjectName(u"btn_Home")
        sizePolicy.setHeightForWidth(self.btn_Home.sizePolicy().hasHeightForWidth())
        self.btn_Home.setSizePolicy(sizePolicy)
        self.btn_Home.setMinimumSize(QSize(0, 45))
        self.btn_Home.setFont(font)
        self.btn_Home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Home.setLayoutDirection(Qt.LeftToRight)
        self.btn_Home.setStyleSheet(u"background-image: url(:/icons/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_Home)

        self.btn_NewProject = QPushButton(self.topMenu)
        self.btn_NewProject.setObjectName(u"btn_NewProject")
        sizePolicy.setHeightForWidth(self.btn_NewProject.sizePolicy().hasHeightForWidth())
        self.btn_NewProject.setSizePolicy(sizePolicy)
        self.btn_NewProject.setMinimumSize(QSize(0, 45))
        self.btn_NewProject.setFont(font)
        self.btn_NewProject.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_NewProject.setLayoutDirection(Qt.LeftToRight)
        self.btn_NewProject.setStyleSheet(u"background-image: url(:/icons/icons/cil-folder.png);")

        self.verticalLayout_8.addWidget(self.btn_NewProject)

        self.btn_OpenProject = QPushButton(self.topMenu)
        self.btn_OpenProject.setObjectName(u"btn_OpenProject")
        sizePolicy.setHeightForWidth(self.btn_OpenProject.sizePolicy().hasHeightForWidth())
        self.btn_OpenProject.setSizePolicy(sizePolicy)
        self.btn_OpenProject.setMinimumSize(QSize(0, 45))
        self.btn_OpenProject.setFont(font)
        self.btn_OpenProject.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_OpenProject.setLayoutDirection(Qt.LeftToRight)
        self.btn_OpenProject.setStyleSheet(u"background-image: url(:/icons/icons/cil-folder-open.png);")

        self.verticalLayout_8.addWidget(self.btn_OpenProject)

        self.btn_ImportFiles = QPushButton(self.topMenu)
        self.btn_ImportFiles.setObjectName(u"btn_ImportFiles")
        sizePolicy.setHeightForWidth(self.btn_ImportFiles.sizePolicy().hasHeightForWidth())
        self.btn_ImportFiles.setSizePolicy(sizePolicy)
        self.btn_ImportFiles.setMinimumSize(QSize(0, 45))
        self.btn_ImportFiles.setFont(font)
        self.btn_ImportFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ImportFiles.setLayoutDirection(Qt.LeftToRight)
        self.btn_ImportFiles.setStyleSheet(u"background-image: url(:/icons/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_ImportFiles)

        self.btn_AddMoreFiles = QPushButton(self.topMenu)
        self.btn_AddMoreFiles.setObjectName(u"btn_AddMoreFiles")
        sizePolicy.setHeightForWidth(self.btn_AddMoreFiles.sizePolicy().hasHeightForWidth())
        self.btn_AddMoreFiles.setSizePolicy(sizePolicy)
        self.btn_AddMoreFiles.setMinimumSize(QSize(0, 45))
        self.btn_AddMoreFiles.setFont(font)
        self.btn_AddMoreFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_AddMoreFiles.setLayoutDirection(Qt.LeftToRight)
        self.btn_AddMoreFiles.setStyleSheet(u"background-image: url(:/icons/icons/cil-file-add.png);")

        self.verticalLayout_8.addWidget(self.btn_AddMoreFiles)

        self.btn_ShowData = QPushButton(self.topMenu)
        self.btn_ShowData.setObjectName(u"btn_ShowData")
        self.btn_ShowData.setMinimumSize(QSize(0, 45))
        self.btn_ShowData.setStyleSheet(u"background-image: url(:/icons/icons/cil-screen-desktop.png);")

        self.verticalLayout_8.addWidget(self.btn_ShowData)

        self.btn_DefBackgroundSignal = QPushButton(self.topMenu)
        self.btn_DefBackgroundSignal.setObjectName(u"btn_DefBackgroundSignal")
        self.btn_DefBackgroundSignal.setMinimumSize(QSize(0, 45))
        self.btn_DefBackgroundSignal.setStyleSheet(u"background-image: url(:/icons/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.btn_DefBackgroundSignal)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_Settings = QPushButton(self.bottomMenu)
        self.btn_Settings.setObjectName(u"btn_Settings")
        sizePolicy.setHeightForWidth(self.btn_Settings.sizePolicy().hasHeightForWidth())
        self.btn_Settings.setSizePolicy(sizePolicy)
        self.btn_Settings.setMinimumSize(QSize(0, 45))
        self.btn_Settings.setFont(font)
        self.btn_Settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_Settings.setStyleSheet(u"background-image: url(:/icons/icons/cil-settings.png);")

        self.verticalLayout_9.addWidget(self.btn_Settings)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleProject = QLabel(self.leftBox)
        self.titleProject.setObjectName(u"titleProject")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleProject.sizePolicy().hasHeightForWidth())
        self.titleProject.setSizePolicy(sizePolicy2)
        self.titleProject.setMaximumSize(QSize(16777215, 45))
        self.titleProject.setFont(font)
        self.titleProject.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleProject)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setMaximumSize(QSize(94, 50))
        self.rightButtons.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-position: center;\n"
"    ")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_MinimizeApp = QPushButton(self.rightButtons)
        self.btn_MinimizeApp.setObjectName(u"btn_MinimizeApp")
        self.btn_MinimizeApp.setMinimumSize(QSize(28, 28))
        self.btn_MinimizeApp.setMaximumSize(QSize(28, 28))
        self.btn_MinimizeApp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_MinimizeApp.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_MinimizeApp.setIcon(icon)
        self.btn_MinimizeApp.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_MinimizeApp)

        self.btn_RestaureSizeApp = QPushButton(self.rightButtons)
        self.btn_RestaureSizeApp.setObjectName(u"btn_RestaureSizeApp")
        self.btn_RestaureSizeApp.setMinimumSize(QSize(28, 28))
        self.btn_RestaureSizeApp.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.btn_RestaureSizeApp.setFont(font3)
        self.btn_RestaureSizeApp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_RestaureSizeApp.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_RestaureSizeApp.setIcon(icon1)
        self.btn_RestaureSizeApp.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_RestaureSizeApp)

        self.btn_CloseApp = QPushButton(self.rightButtons)
        self.btn_CloseApp.setObjectName(u"btn_CloseApp")
        self.btn_CloseApp.setMinimumSize(QSize(28, 28))
        self.btn_CloseApp.setMaximumSize(QSize(28, 28))
        self.btn_CloseApp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_CloseApp.setStyleSheet(u"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(170, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_CloseApp.setIcon(icon2)
        self.btn_CloseApp.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_CloseApp)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.pagesContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: transparent;")
        self.pg_Home = QWidget()
        self.pg_Home.setObjectName(u"pg_Home")
        self.horizontalLayout_6 = QHBoxLayout(self.pg_Home)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget = QWidget(self.pg_Home)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(600, 300))
        self.widget.setMaximumSize(QSize(600, 300))
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 250))
        self.frame.setMaximumSize(QSize(250, 250))
        self.frame.setStyleSheet(u"background-image: url(:/images/images/logo_250x250.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame)

        self.verticalLine = QFrame(self.widget)
        self.verticalLine.setObjectName(u"verticalLine")
        self.verticalLine.setMinimumSize(QSize(1, 250))
        self.verticalLine.setMaximumSize(QSize(1, 250))
        self.verticalLine.setStyleSheet(u"background-color: rgb(134, 134, 134);\n"
"")
        self.verticalLine.setFrameShape(QFrame.StyledPanel)
        self.verticalLine.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.verticalLine)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"    border: none; /* Remove as bordas */\n"
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
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.btn_NewProjectHome = QPushButton(self.frame_3)
        self.btn_NewProjectHome.setObjectName(u"btn_NewProjectHome")
        self.btn_NewProjectHome.setMinimumSize(QSize(200, 30))
        self.btn_NewProjectHome.setMaximumSize(QSize(150, 30))

        self.verticalLayout_15.addWidget(self.btn_NewProjectHome, 0, Qt.AlignHCenter)

        self.btn_OpenProjectHome = QPushButton(self.frame_3)
        self.btn_OpenProjectHome.setObjectName(u"btn_OpenProjectHome")
        self.btn_OpenProjectHome.setMinimumSize(QSize(200, 30))
        self.btn_OpenProjectHome.setMaximumSize(QSize(200, 30))

        self.verticalLayout_15.addWidget(self.btn_OpenProjectHome, 0, Qt.AlignHCenter)

        self.btn_ExportProjectHome = QPushButton(self.frame_3)
        self.btn_ExportProjectHome.setObjectName(u"btn_ExportProjectHome")
        self.btn_ExportProjectHome.setMinimumSize(QSize(200, 30))
        self.btn_ExportProjectHome.setMaximumSize(QSize(200, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        self.btn_ExportProjectHome.setFont(font4)

        self.verticalLayout_15.addWidget(self.btn_ExportProjectHome, 0, Qt.AlignHCenter)

        self.btn_SettingsHome = QPushButton(self.frame_3)
        self.btn_SettingsHome.setObjectName(u"btn_SettingsHome")
        self.btn_SettingsHome.setMinimumSize(QSize(200, 30))
        self.btn_SettingsHome.setMaximumSize(QSize(200, 30))
        self.btn_SettingsHome.setFont(font4)

        self.verticalLayout_15.addWidget(self.btn_SettingsHome, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.frame_3)


        self.horizontalLayout_6.addWidget(self.widget)

        self.stackedWidget.addWidget(self.pg_Home)
        self.pg_SeeData = QWidget()
        self.pg_SeeData.setObjectName(u"pg_SeeData")
        self.verticalLayout_11 = QVBoxLayout(self.pg_SeeData)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 5, 0, 0)
        self.frame_5 = QFrame(self.pg_SeeData)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(150, 20))
        self.frame_5.setMaximumSize(QSize(16777215, 20))
        self.frame_5.setStyleSheet(u"border: none;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 20))
        self.label_5.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_13.addWidget(self.label_5)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(300, 20))
        self.frame_8.setMaximumSize(QSize(300, 20))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setSpacing(11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.radioButtonSeeDataInput = QRadioButton(self.frame_8)
        self.radioButtonSeeDataInput.setObjectName(u"radioButtonSeeDataInput")
        self.radioButtonSeeDataInput.setMinimumSize(QSize(55, 0))
        self.radioButtonSeeDataInput.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_12.addWidget(self.radioButtonSeeDataInput)

        self.radioButton_SeeDataCalculateData = QRadioButton(self.frame_8)
        self.radioButton_SeeDataCalculateData.setObjectName(u"radioButton_SeeDataCalculateData")
        self.radioButton_SeeDataCalculateData.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_12.addWidget(self.radioButton_SeeDataCalculateData)

        self.radioButtonSeeFinalTable = QRadioButton(self.frame_8)
        self.radioButtonSeeFinalTable.setObjectName(u"radioButtonSeeFinalTable")
        self.radioButtonSeeFinalTable.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_12.addWidget(self.radioButtonSeeFinalTable)


        self.horizontalLayout_13.addWidget(self.frame_8)

        self.horizontalSpacer = QSpacerItem(481, 15, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.splitter_4 = QSplitter(self.pg_SeeData)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.splitter_4.setHandleWidth(9)
        self.widget_2 = QWidget(self.splitter_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.splitter_5 = QSplitter(self.widget_2)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.splitter_5.setHandleWidth(9)
        self.frame_6 = QFrame(self.splitter_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(100, 16777215))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 15))
        self.label_3.setStyleSheet(u"background-color: rgb(44, 49, 58);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.label_3)

        self.listWidget_FilesStandard = QListWidget(self.frame_6)
        self.listWidget_FilesStandard.setObjectName(u"listWidget_FilesStandard")
        self.listWidget_FilesStandard.setMaximumSize(QSize(100, 16777215))
        self.listWidget_FilesStandard.setFocusPolicy(Qt.NoFocus)
        self.listWidget_FilesStandard.setStyleSheet(u"QListWidget {\n"
"	background-color: rgb(44, 49, 58);\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	\n"
"}\n"
"QListWidget::item{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-radius: 3px;\n"
"	margin-bottom: 1px; /* Espa\u00e7amento inferior entre os itens */\n"
"}\n"
"QListWidget::item:hover {\n"
"	background:  rgb(33, 37, 43);\n"
"}\n"
"QListWidget::item:selected{\n"
"	background-color: rgb(78,96,255);\n"
"	border-radius: 3px;\n"
"	border: none;\n"
"	color: rgb(221,221,221);\n"
"	font-weight: bold;\n"
"\n"
"}")
        self.listWidget_FilesStandard.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_12.addWidget(self.listWidget_FilesStandard)

        self.splitter_5.addWidget(self.frame_6)
        self.tableWidget_StandardData = QTableWidget(self.splitter_5)
        self.tableWidget_StandardData.setObjectName(u"tableWidget_StandardData")
        self.tableWidget_StandardData.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_StandardData.setStyleSheet(u"QTableWidget {	\n"
"	background-color:  rgb(44, 49, 58);\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid  rgb(40, 44, 52);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: none;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(78,96,255);\n"
"	color: white;\n"
"\n"
"}\n"
" QHeaderView::section{\n"
"	background-color: rgb(44, 49, 58);\n"
"	border: 1px solid  rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid  rgb(44, 49, 58);\n"
"    border-right: 1px solid  rgb(44, 49, 58);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:   rgb(44, 49, 58);\n"
"	color: rgb(255, 255, 204);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid  rgb(44, 49, 58);\n"
"	background-color:   rgb(44, 49, 58);\n"
"	padding: 3px;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"  	border"
                        ": 1px solid rgb(44, 49, 58);\n"
"	background-color: rgb(44, 49, 58);\n"
"	padding-left: 7px;\n"
"	color: white;\n"
"	font-weight:bold;\n"
"\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color:  transparent;\n"
"}")
        self.tableWidget_StandardData.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.splitter_5.addWidget(self.tableWidget_StandardData)

        self.horizontalLayout_10.addWidget(self.splitter_5)

        self.splitter_4.addWidget(self.widget_2)
        self.widget_3 = QWidget(self.splitter_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.splitter_6 = QSplitter(self.widget_3)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.splitter_6.setHandleWidth(9)
        self.frame_7 = QFrame(self.splitter_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(100, 16777215))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 15))
        self.label_4.setStyleSheet(u"background-color: rgb(44, 49, 58);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.label_4)

        self.listWidget_FilesSamples = QListWidget(self.frame_7)
        self.listWidget_FilesSamples.setObjectName(u"listWidget_FilesSamples")
        self.listWidget_FilesSamples.setMaximumSize(QSize(100, 16777215))
        self.listWidget_FilesSamples.setFocusPolicy(Qt.NoFocus)
        self.listWidget_FilesSamples.setStyleSheet(u"QListWidget {\n"
"	background-color: rgb(44, 49, 58);\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	\n"
"}\n"
"QListWidget::item{\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-radius: 3px;\n"
"	margin-bottom: 1px; /* Espa\u00e7amento inferior entre os itens */\n"
"}\n"
"QListWidget::item:hover {\n"
"	background:  rgb(33, 37, 43);\n"
"}\n"
"QListWidget::item:selected{\n"
"	background-color: rgb(78,96,255);\n"
"	border-radius: 3px;\n"
"	border: none;\n"
"	color: rgb(221,221,221);\n"
"	font-weight: bold;\n"
"\n"
"}")
        self.listWidget_FilesSamples.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_13.addWidget(self.listWidget_FilesSamples)

        self.splitter_6.addWidget(self.frame_7)
        self.tableWidgetSampleData = QTableWidget(self.splitter_6)
        self.tableWidgetSampleData.setObjectName(u"tableWidgetSampleData")
        self.tableWidgetSampleData.setFocusPolicy(Qt.NoFocus)
        self.tableWidgetSampleData.setStyleSheet(u"QTableWidget {	\n"
"	background-color:  rgb(44, 49, 58);\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid  rgb(40, 44, 52);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: none;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(78,96,255);\n"
"	color: white;\n"
"\n"
"}\n"
" QHeaderView::section{\n"
"	background-color: rgb(44, 49, 58);\n"
"	border: 1px solid  rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid  rgb(44, 49, 58);\n"
"    border-right: 1px solid  rgb(44, 49, 58);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color:   rgb(44, 49, 58);\n"
"	color: rgb(255, 255, 204);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid  rgb(44, 49, 58);\n"
"	background-color:   rgb(44, 49, 58);\n"
"	padding: 3px;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"  	border"
                        ": 1px solid rgb(44, 49, 58);\n"
"	background-color: rgb(44, 49, 58);\n"
"	padding-left: 7px;\n"
"	color: white;\n"
"	font-weight:bold;\n"
"\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color:  transparent;\n"
"}")
        self.tableWidgetSampleData.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.splitter_6.addWidget(self.tableWidgetSampleData)

        self.horizontalLayout_11.addWidget(self.splitter_6)

        self.splitter_4.addWidget(self.widget_3)

        self.verticalLayout_11.addWidget(self.splitter_4)

        self.stackedWidget.addWidget(self.pg_SeeData)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"background-image: url(:/icons/icons/cil-size-grip.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"LuHf", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Data Reduction", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_NewProject.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.btn_OpenProject.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
        self.btn_ImportFiles.setText(QCoreApplication.translate("MainWindow", u"Import Files", None))
        self.btn_AddMoreFiles.setText(QCoreApplication.translate("MainWindow", u"Add Files", None))
        self.btn_ShowData.setText(QCoreApplication.translate("MainWindow", u"Display Data", None))
        self.btn_DefBackgroundSignal.setText(QCoreApplication.translate("MainWindow", u"Background/Signal", None))
        self.btn_Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.titleProject.setText("")
#if QT_CONFIG(tooltip)
        self.btn_MinimizeApp.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_MinimizeApp.setText("")
#if QT_CONFIG(tooltip)
        self.btn_RestaureSizeApp.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RestaureSizeApp.setText("")
#if QT_CONFIG(tooltip)
        self.btn_CloseApp.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_CloseApp.setText("")
        self.btn_NewProjectHome.setText(QCoreApplication.translate("MainWindow", u"New project", None))
        self.btn_OpenProjectHome.setText(QCoreApplication.translate("MainWindow", u"Open project", None))
        self.btn_ExportProjectHome.setText(QCoreApplication.translate("MainWindow", u"Export project", None))
        self.btn_SettingsHome.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Table:", None))
        self.radioButtonSeeDataInput.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.radioButton_SeeDataCalculateData.setText(QCoreApplication.translate("MainWindow", u"Calculate data", None))
        self.radioButtonSeeFinalTable.setText(QCoreApplication.translate("MainWindow", u"Final table", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">STANDARD</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SAMPLE</p></body></html>", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

