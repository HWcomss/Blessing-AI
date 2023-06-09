# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainoxsSeu.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QListView, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea, QScrollBar,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
# import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
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
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
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
"	background-color: rgb(18"
                        "9, 147, 249);\n"
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
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
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
"	background-color: rgb("
                        "189, 147, 249);\n"
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
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/book-icon.png);\n"
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
"	border-top"
                        ": 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
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
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: "
                        "solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
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
"	color: rgb(255"
                        ", 255, 255);\n"
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
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
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
"	background-color:"
                        " rgb(33, 37, 43);\n"
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
"	background-color: rgb(33, 37, 43);\n"
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
"	selection-background-color"
                        ": rgb(255, 121, 198);\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
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
"QS"
                        "crollBar::sub-line:horizontal {\n"
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
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
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
"     subc"
                        "ontrol-origin: margin;\n"
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
"	backgr"
                        "ound-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
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
"	subcont"
                        "rol-position: top right;\n"
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
"QComboBox QAbstractItemView {\n"
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
"    hei"
                        "ght: 10px;\n"
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
"QCommandLink"
                        "Button {	\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
        self.appMargins.setContentsMargins(10, 10, 10, 10)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

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
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_character = QPushButton(self.topMenu)
        self.btn_character.setObjectName(u"btn_character")
        sizePolicy1.setHeightForWidth(self.btn_character.sizePolicy().hasHeightForWidth())
        self.btn_character.setSizePolicy(sizePolicy1)
        self.btn_character.setMinimumSize(QSize(0, 45))
        self.btn_character.setFont(font)
        self.btn_character.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_character.setLayoutDirection(Qt.LeftToRight)
        self.btn_character.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-mood-very-good.png);")

        self.verticalLayout_8.addWidget(self.btn_character)

        self.btn_audio_setting = QPushButton(self.topMenu)
        self.btn_audio_setting.setObjectName(u"btn_audio_setting")
        sizePolicy1.setHeightForWidth(self.btn_audio_setting.sizePolicy().hasHeightForWidth())
        self.btn_audio_setting.setSizePolicy(sizePolicy1)
        self.btn_audio_setting.setMinimumSize(QSize(0, 45))
        self.btn_audio_setting.setFont(font)
        self.btn_audio_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_audio_setting.setLayoutDirection(Qt.LeftToRight)
        self.btn_audio_setting.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-volume-high.png);")

        self.verticalLayout_8.addWidget(self.btn_audio_setting)

        self.btn_prompt_setting = QPushButton(self.topMenu)
        self.btn_prompt_setting.setObjectName(u"btn_prompt_setting")
        sizePolicy1.setHeightForWidth(self.btn_prompt_setting.sizePolicy().hasHeightForWidth())
        self.btn_prompt_setting.setSizePolicy(sizePolicy1)
        self.btn_prompt_setting.setMinimumSize(QSize(0, 45))
        self.btn_prompt_setting.setFont(font)
        self.btn_prompt_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_prompt_setting.setLayoutDirection(Qt.LeftToRight)
        self.btn_prompt_setting.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-paragraph.png);")

        self.verticalLayout_8.addWidget(self.btn_prompt_setting)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy1.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy1)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/book-icon.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textBrowser = QTextBrowser(self.extraCenter)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(222, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        self.textBrowser.setFont(font3)
        self.textBrowser.setStyleSheet(u"background: transparent;")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textBrowser)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


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
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.Home_Page = QWidget()
        self.Home_Page.setObjectName(u"Home_Page")
        self.Home_Page.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.Home_Page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self._home_top_verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_24.addItem(self._home_top_verticalSpacer)

        self.a_verticalLayout_top = QVBoxLayout()
        self.a_verticalLayout_top.setObjectName(u"a_verticalLayout_top")
        self.a_verticalLayout_top.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout_chat_log = QHBoxLayout()
        self.horizontalLayout_chat_log.setSpacing(6)
        self.horizontalLayout_chat_log.setObjectName(u"horizontalLayout_chat_log")
        self.horizontalLayout_chat_log.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_chat_log.setContentsMargins(10, 0, 10, 0)
        self.label_chat_log = QLabel(self.Home_Page)
        self.label_chat_log.setObjectName(u"label_chat_log")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_chat_log.sizePolicy().hasHeightForWidth())
        self.label_chat_log.setSizePolicy(sizePolicy4)
        self.label_chat_log.setMaximumSize(QSize(80, 30))
        self.label_chat_log.setLayoutDirection(Qt.LeftToRight)
        self.label_chat_log.setStyleSheet(u"")
        self.label_chat_log.setMargin(0)

        self.horizontalLayout_chat_log.addWidget(self.label_chat_log)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_chat_log.addItem(self.horizontalSpacer)

        self.label_token_count = QLabel(self.Home_Page)
        self.label_token_count.setObjectName(u"label_token_count")
        sizePolicy4.setHeightForWidth(self.label_token_count.sizePolicy().hasHeightForWidth())
        self.label_token_count.setSizePolicy(sizePolicy4)
        self.label_token_count.setMaximumSize(QSize(200, 30))
        self.label_token_count.setLayoutDirection(Qt.RightToLeft)
        self.label_token_count.setAutoFillBackground(False)
        self.label_token_count.setStyleSheet(u"")
        self.label_token_count.setAlignment(Qt.AlignCenter)
        self.label_token_count.setMargin(0)

        self.horizontalLayout_chat_log.addWidget(self.label_token_count)

        self.lineEdit_token_count = QLineEdit(self.Home_Page)
        self.lineEdit_token_count.setObjectName(u"lineEdit_token_count")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lineEdit_token_count.sizePolicy().hasHeightForWidth())
        self.lineEdit_token_count.setSizePolicy(sizePolicy5)
        self.lineEdit_token_count.setMaximumSize(QSize(70, 30))
        self.lineEdit_token_count.setLayoutDirection(Qt.RightToLeft)
        self.lineEdit_token_count.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(49, 49, 72);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}")
        self.lineEdit_token_count.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_chat_log.addWidget(self.lineEdit_token_count)


        self.a_verticalLayout_top.addLayout(self.horizontalLayout_chat_log)

        self.chat = QWidget(self.Home_Page)
        self.chat.setObjectName(u"chat")
        self.chat.setStyleSheet(u"#chat {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}")
        self.verticalLayout_25 = QVBoxLayout(self.chat)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.chat_layout = QVBoxLayout()
        self.chat_layout.setSpacing(0)
        self.chat_layout.setObjectName(u"chat_layout")
        self.chat_widget_placeholder_2 = QLabel(self.chat)
        self.chat_widget_placeholder_2.setObjectName(u"chat_widget_placeholder_2")
        self.chat_widget_placeholder_2.setMinimumSize(QSize(0, 200))
        self.chat_widget_placeholder_2.setPixmap(QPixmap(u":/user_profile/images/user_profile/me.png"))
        self.chat_widget_placeholder_2.setAlignment(Qt.AlignCenter)

        self.chat_layout.addWidget(self.chat_widget_placeholder_2)


        self.verticalLayout_25.addLayout(self.chat_layout)


        self.a_verticalLayout_top.addWidget(self.chat)


        self.verticalLayout_24.addLayout(self.a_verticalLayout_top)

        self.b_gridLayout_mid = QGridLayout()
        self.b_gridLayout_mid.setObjectName(u"b_gridLayout_mid")
        self.b_gridLayout_mid.setContentsMargins(6, -1, 6, -1)
        self.textEdit_user_message = QTextEdit(self.Home_Page)
        self.textEdit_user_message.setObjectName(u"textEdit_user_message")
        self.textEdit_user_message.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.textEdit_user_message.sizePolicy().hasHeightForWidth())
        self.textEdit_user_message.setSizePolicy(sizePolicy1)
        self.textEdit_user_message.setMinimumSize(QSize(0, 0))
        self.textEdit_user_message.setMaximumSize(QSize(16777215, 30))
        self.textEdit_user_message.setStyleSheet(u"QTextEdit {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(66, 70, 86);\n"
"}")
        self.textEdit_user_message.setReadOnly(True)

        self.b_gridLayout_mid.addWidget(self.textEdit_user_message, 0, 1, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, -1, -1, -1)
        self.label_last_user_message = QLabel(self.Home_Page)
        self.label_last_user_message.setObjectName(u"label_last_user_message")
        self.label_last_user_message.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.label_last_user_message.sizePolicy().hasHeightForWidth())
        self.label_last_user_message.setSizePolicy(sizePolicy4)
        self.label_last_user_message.setMaximumSize(QSize(200, 30))
        self.label_last_user_message.setStyleSheet(u"")
        self.label_last_user_message.setMargin(0)

        self.verticalLayout_23.addWidget(self.label_last_user_message)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_23.addItem(self.verticalSpacer_2)


        self.b_gridLayout_mid.addLayout(self.verticalLayout_23, 0, 0, 1, 1)

        self.textEdit_bot_reply = QTextEdit(self.Home_Page)
        self.textEdit_bot_reply.setObjectName(u"textEdit_bot_reply")
        self.textEdit_bot_reply.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.textEdit_bot_reply.sizePolicy().hasHeightForWidth())
        self.textEdit_bot_reply.setSizePolicy(sizePolicy1)
        self.textEdit_bot_reply.setMinimumSize(QSize(0, 0))
        self.textEdit_bot_reply.setMaximumSize(QSize(16777215, 30))
        self.textEdit_bot_reply.setBaseSize(QSize(0, 0))
        self.textEdit_bot_reply.setStyleSheet(u"QTextEdit {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(66, 70, 86);\n"
"}")
        self.textEdit_bot_reply.setReadOnly(True)

        self.b_gridLayout_mid.addWidget(self.textEdit_bot_reply, 1, 1, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, -1, -1, -1)
        self.label_last_bot_reply = QLabel(self.Home_Page)
        self.label_last_bot_reply.setObjectName(u"label_last_bot_reply")
        self.label_last_bot_reply.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.label_last_bot_reply.sizePolicy().hasHeightForWidth())
        self.label_last_bot_reply.setSizePolicy(sizePolicy4)
        self.label_last_bot_reply.setMaximumSize(QSize(200, 30))
        self.label_last_bot_reply.setStyleSheet(u"")
        self.label_last_bot_reply.setMargin(0)

        self.verticalLayout_21.addWidget(self.label_last_bot_reply)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_21.addItem(self.verticalSpacer_3)


        self.b_gridLayout_mid.addLayout(self.verticalLayout_21, 1, 0, 1, 1)


        self.verticalLayout_24.addLayout(self.b_gridLayout_mid)

        self.c_verticalLayout_lower = QVBoxLayout()
        self.c_verticalLayout_lower.setObjectName(u"c_verticalLayout_lower")
        self.c_verticalLayout_lower.setContentsMargins(6, -1, 6, -1)
        self.label = QLabel(self.Home_Page)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setAlignment(Qt.AlignCenter)

        self.c_verticalLayout_lower.addWidget(self.label)

        self.listView_message_queue = QListView(self.Home_Page)
        self.listView_message_queue.setObjectName(u"listView_message_queue")
        self.listView_message_queue.setMinimumSize(QSize(0, 50))
        self.listView_message_queue.setMaximumSize(QSize(16777215, 200))
        self.listView_message_queue.setStyleSheet(u"QListView {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}\n"
"QListView:hover {\n"
"	border: 2px solid rgb(66, 70, 86);\n"
"}\n"
"QListView:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.c_verticalLayout_lower.addWidget(self.listView_message_queue)

        self.horizontalLayout_command_button = QHBoxLayout()
        self.horizontalLayout_command_button.setSpacing(70)
        self.horizontalLayout_command_button.setObjectName(u"horizontalLayout_command_button")
        self.horizontalLayout_command_button.setContentsMargins(170, 0, 170, 0)
        self.pushButton_mute_tts = QPushButton(self.Home_Page)
        self.pushButton_mute_tts.setObjectName(u"pushButton_mute_tts")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_mute_tts.sizePolicy().hasHeightForWidth())
        self.pushButton_mute_tts.setSizePolicy(sizePolicy6)
        self.pushButton_mute_tts.setMinimumSize(QSize(0, 50))
        self.pushButton_mute_tts.setMaximumSize(QSize(300, 80))
        self.pushButton_mute_tts.setStyleSheet(u"QPushButton{\n"
"	font: 14pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(131, 56, 236);\n"
"	border-radius: 5px;\n"
"}")

        self.horizontalLayout_command_button.addWidget(self.pushButton_mute_tts)

        self.pushButton_mute_mic = QPushButton(self.Home_Page)
        self.pushButton_mute_mic.setObjectName(u"pushButton_mute_mic")
        sizePolicy6.setHeightForWidth(self.pushButton_mute_mic.sizePolicy().hasHeightForWidth())
        self.pushButton_mute_mic.setSizePolicy(sizePolicy6)
        self.pushButton_mute_mic.setMinimumSize(QSize(0, 50))
        self.pushButton_mute_mic.setMaximumSize(QSize(300, 80))
        self.pushButton_mute_mic.setStyleSheet(u"QPushButton{\n"
"	font: 14pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(131, 56, 236);\n"
"	border-radius: 5px;\n"
"}")

        self.horizontalLayout_command_button.addWidget(self.pushButton_mute_mic)

        self.pushButton_pause_reply = QPushButton(self.Home_Page)
        self.pushButton_pause_reply.setObjectName(u"pushButton_pause_reply")
        self.pushButton_pause_reply.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.pushButton_pause_reply.sizePolicy().hasHeightForWidth())
        self.pushButton_pause_reply.setSizePolicy(sizePolicy6)
        self.pushButton_pause_reply.setMinimumSize(QSize(0, 50))
        self.pushButton_pause_reply.setMaximumSize(QSize(300, 80))
        self.pushButton_pause_reply.setStyleSheet(u"QPushButton{\n"
"	font: 14pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(251, 86, 7);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(251, 149, 7);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(197, 66, 5);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-media-skip-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_pause_reply.setIcon(icon4)

        self.horizontalLayout_command_button.addWidget(self.pushButton_pause_reply)

        self.pushButton_stop_reply = QPushButton(self.Home_Page)
        self.pushButton_stop_reply.setObjectName(u"pushButton_stop_reply")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_stop_reply.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_reply.setSizePolicy(sizePolicy7)
        self.pushButton_stop_reply.setMinimumSize(QSize(0, 50))
        self.pushButton_stop_reply.setMaximumSize(QSize(300, 80))
        self.pushButton_stop_reply.setStyleSheet(u"QPushButton{\n"
"	font: 14pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(255, 0, 110);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 0, 166);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(200, 0, 87);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_stop_reply.setIcon(icon5)

        self.horizontalLayout_command_button.addWidget(self.pushButton_stop_reply)


        self.c_verticalLayout_lower.addLayout(self.horizontalLayout_command_button)


        self.verticalLayout_24.addLayout(self.c_verticalLayout_lower)

        self.stackedWidget.addWidget(self.Home_Page)
        self.Character_page = QWidget()
        self.Character_page.setObjectName(u"Character_page")
        self.verticalLayout_20 = QVBoxLayout(self.Character_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self._char_top_verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_20.addItem(self._char_top_verticalSpacer)

        self.horizontalLayout_char_info_top = QHBoxLayout()
        self.horizontalLayout_char_info_top.setObjectName(u"horizontalLayout_char_info_top")
        self.verticalLayout_char_info_1 = QVBoxLayout()
        self.verticalLayout_char_info_1.setObjectName(u"verticalLayout_char_info_1")
        self.label_your_name = QLabel(self.Character_page)
        self.label_your_name.setObjectName(u"label_your_name")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_your_name.sizePolicy().hasHeightForWidth())
        self.label_your_name.setSizePolicy(sizePolicy8)
        self.label_your_name.setMinimumSize(QSize(80, 30))
        self.label_your_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_char_info_1.addWidget(self.label_your_name)

        self.textEdit_yourname = QTextEdit(self.Character_page)
        self.textEdit_yourname.setObjectName(u"textEdit_yourname")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.textEdit_yourname.sizePolicy().hasHeightForWidth())
        self.textEdit_yourname.setSizePolicy(sizePolicy9)
        self.textEdit_yourname.setMinimumSize(QSize(0, 0))
        self.textEdit_yourname.setMaximumSize(QSize(16777215, 40))
        self.textEdit_yourname.setStyleSheet(u"QTextEdit {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(66, 70, 86);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}")

        self.verticalLayout_char_info_1.addWidget(self.textEdit_yourname)

        self.label_greeting = QLabel(self.Character_page)
        self.label_greeting.setObjectName(u"label_greeting")
        sizePolicy8.setHeightForWidth(self.label_greeting.sizePolicy().hasHeightForWidth())
        self.label_greeting.setSizePolicy(sizePolicy8)
        self.label_greeting.setMinimumSize(QSize(80, 30))
        self.label_greeting.setAlignment(Qt.AlignCenter)

        self.verticalLayout_char_info_1.addWidget(self.label_greeting)

        self.textEdit_greeting = QTextEdit(self.Character_page)
        self.textEdit_greeting.setObjectName(u"textEdit_greeting")
        sizePolicy9.setHeightForWidth(self.textEdit_greeting.sizePolicy().hasHeightForWidth())
        self.textEdit_greeting.setSizePolicy(sizePolicy9)
        self.textEdit_greeting.setMinimumSize(QSize(0, 0))
        self.textEdit_greeting.setMaximumSize(QSize(16777215, 100))
        self.textEdit_greeting.setStyleSheet(u"QTextEdit {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(66, 70, 86);\n"
"}")
        self.textEdit_greeting.setReadOnly(True)

        self.verticalLayout_char_info_1.addWidget(self.textEdit_greeting)


        self.horizontalLayout_char_info_top.addLayout(self.verticalLayout_char_info_1)

        self.verticalLayout_char_profile = QVBoxLayout()
        self.verticalLayout_char_profile.setObjectName(u"verticalLayout_char_profile")
        self.label_char_img = QLabel(self.Character_page)
        self.label_char_img.setObjectName(u"label_char_img")
        sizePolicy8.setHeightForWidth(self.label_char_img.sizePolicy().hasHeightForWidth())
        self.label_char_img.setSizePolicy(sizePolicy8)
        self.label_char_img.setMinimumSize(QSize(200, 200))
        self.label_char_img.setLayoutDirection(Qt.LeftToRight)
        self.label_char_img.setFrameShape(QFrame.Box)
        self.label_char_img.setFrameShadow(QFrame.Raised)
        self.label_char_img.setLineWidth(2)
        self.label_char_img.setMidLineWidth(1)
        self.label_char_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout_char_profile.addWidget(self.label_char_img, 0, Qt.AlignHCenter)

        self.label_char_name = QLabel(self.Character_page)
        self.label_char_name.setObjectName(u"label_char_name")
        sizePolicy8.setHeightForWidth(self.label_char_name.sizePolicy().hasHeightForWidth())
        self.label_char_name.setSizePolicy(sizePolicy8)
        self.label_char_name.setMinimumSize(QSize(150, 30))
        self.label_char_name.setMaximumSize(QSize(16777215, 16777215))
        self.label_char_name.setLayoutDirection(Qt.LeftToRight)
        self.label_char_name.setFrameShape(QFrame.Box)
        self.label_char_name.setFrameShadow(QFrame.Raised)
        self.label_char_name.setLineWidth(2)
        self.label_char_name.setMidLineWidth(1)
        self.label_char_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_char_profile.addWidget(self.label_char_name, 0, Qt.AlignHCenter)


        self.horizontalLayout_char_info_top.addLayout(self.verticalLayout_char_profile)


        self.verticalLayout_20.addLayout(self.horizontalLayout_char_info_top)

        self.verticalLayout_char_info_2 = QVBoxLayout()
        self.verticalLayout_char_info_2.setObjectName(u"verticalLayout_char_info_2")
        self.label_context = QLabel(self.Character_page)
        self.label_context.setObjectName(u"label_context")
        sizePolicy8.setHeightForWidth(self.label_context.sizePolicy().hasHeightForWidth())
        self.label_context.setSizePolicy(sizePolicy8)
        self.label_context.setMinimumSize(QSize(80, 30))
        self.label_context.setAlignment(Qt.AlignCenter)

        self.verticalLayout_char_info_2.addWidget(self.label_context)

        self.textEdit_context = QTextEdit(self.Character_page)
        self.textEdit_context.setObjectName(u"textEdit_context")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.textEdit_context.sizePolicy().hasHeightForWidth())
        self.textEdit_context.setSizePolicy(sizePolicy10)
        self.textEdit_context.setMinimumSize(QSize(0, 0))
        self.textEdit_context.setMaximumSize(QSize(16777215, 600))
        self.textEdit_context.setStyleSheet(u"QTextEdit {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(66, 70, 86);\n"
"}")
        self.textEdit_context.setReadOnly(True)

        self.verticalLayout_char_info_2.addWidget(self.textEdit_context)

        self.verticalLayout_char_info_2.setStretch(1, 2)

        self.verticalLayout_20.addLayout(self.verticalLayout_char_info_2)

        self.stackedWidget.addWidget(self.Character_page)
        self.Audio_Page = QWidget()
        self.Audio_Page.setObjectName(u"Audio_Page")
        self.Audio_Page.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(66, 70, 86);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}\n"
"\n"
"QSlider::groove {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 40px;\n"
"    width: 10px;\n"
"    margin: -20px 0;\n"
"    border-radius: 20px;\n"
"    padding: -20px 0px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(155, 180, 255);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 255, 195);\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.Audio_Page)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self._audio_top_verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_30.addItem(self._audio_top_verticalSpacer)

        self.scrollArea_2 = QScrollArea(self.Audio_Page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1152, 811))
        self.verticalLayout_31 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_27.addWidget(self.label_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.comboBox_mic_device = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_mic_device.addItem("")
        self.comboBox_mic_device.addItem("")
        self.comboBox_mic_device.addItem("")
        self.comboBox_mic_device.setObjectName(u"comboBox_mic_device")
        sizePolicy1.setHeightForWidth(self.comboBox_mic_device.sizePolicy().hasHeightForWidth())
        self.comboBox_mic_device.setSizePolicy(sizePolicy1)
        self.comboBox_mic_device.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_19.addWidget(self.comboBox_mic_device)

        self.pushButton_mic_default = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_mic_default.setObjectName(u"pushButton_mic_default")
        sizePolicy4.setHeightForWidth(self.pushButton_mic_default.sizePolicy().hasHeightForWidth())
        self.pushButton_mic_default.setSizePolicy(sizePolicy4)
        self.pushButton_mic_default.setMinimumSize(QSize(130, 30))
        self.pushButton_mic_default.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(122, 137, 168);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 184, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(75, 84, 103);\n"
"}")

        self.horizontalLayout_19.addWidget(self.pushButton_mic_default)


        self.verticalLayout_27.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_20.addWidget(self.label_19)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_12 = QSpacerItem(40, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)


        self.verticalLayout_27.addLayout(self.horizontalLayout_20)

        self.horizontalSlider_mic_threshold = QSlider(self.scrollAreaWidgetContents_2)
        self.horizontalSlider_mic_threshold.setObjectName(u"horizontalSlider_mic_threshold")
        self.horizontalSlider_mic_threshold.setStyleSheet(u"QSlider::groove {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 40px;\n"
"    width: 10px;\n"
"    margin: -20px 0;\n"
"    border-radius: 20px;\n"
"    padding: -20px 0px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(155, 180, 255);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 255, 195);\n"
"}")
        self.horizontalSlider_mic_threshold.setMaximum(100)
        self.horizontalSlider_mic_threshold.setOrientation(Qt.Horizontal)

        self.verticalLayout_27.addWidget(self.horizontalSlider_mic_threshold)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_21)

        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_13)

        self.lineEdit_phrase_timeout = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_phrase_timeout.setObjectName(u"lineEdit_phrase_timeout")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.lineEdit_phrase_timeout.sizePolicy().hasHeightForWidth())
        self.lineEdit_phrase_timeout.setSizePolicy(sizePolicy11)
        self.lineEdit_phrase_timeout.setMinimumSize(QSize(60, 0))
        self.lineEdit_phrase_timeout.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_phrase_timeout.setAcceptDrops(True)
        self.lineEdit_phrase_timeout.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_phrase_timeout)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_23)

        self.horizontalSpacer_14 = QSpacerItem(40, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_14)


        self.verticalLayout_27.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_spk_device = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_27.addItem(self.verticalSpacer_spk_device)

        self.bottom_verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.bottom_verticalSpacer_7)


        self.verticalLayout_29.addLayout(self.verticalLayout_27)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_29.addWidget(self.label_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.comboBox_spk_device = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_spk_device.addItem("")
        self.comboBox_spk_device.addItem("")
        self.comboBox_spk_device.addItem("")
        self.comboBox_spk_device.setObjectName(u"comboBox_spk_device")
        sizePolicy1.setHeightForWidth(self.comboBox_spk_device.sizePolicy().hasHeightForWidth())
        self.comboBox_spk_device.setSizePolicy(sizePolicy1)
        self.comboBox_spk_device.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_8.addWidget(self.comboBox_spk_device)

        self.pushButton_spk_default = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_spk_default.setObjectName(u"pushButton_spk_default")
        sizePolicy4.setHeightForWidth(self.pushButton_spk_default.sizePolicy().hasHeightForWidth())
        self.pushButton_spk_default.setSizePolicy(sizePolicy4)
        self.pushButton_spk_default.setMinimumSize(QSize(130, 30))
        self.pushButton_spk_default.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(122, 137, 168);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 184, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(75, 84, 103);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_spk_default)


        self.verticalLayout_29.addLayout(self.horizontalLayout_8)


        self.verticalLayout_22.addLayout(self.verticalLayout_29)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_22.addWidget(self.label_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.comboBox_tts_charcter = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_tts_charcter.addItem("")
        self.comboBox_tts_charcter.addItem("")
        self.comboBox_tts_charcter.addItem("")
        self.comboBox_tts_charcter.setObjectName(u"comboBox_tts_charcter")
        sizePolicy1.setHeightForWidth(self.comboBox_tts_charcter.sizePolicy().hasHeightForWidth())
        self.comboBox_tts_charcter.setSizePolicy(sizePolicy1)
        self.comboBox_tts_charcter.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_10.addWidget(self.comboBox_tts_charcter)


        self.verticalLayout_22.addLayout(self.horizontalLayout_10)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_22.addWidget(self.label_8)

        self.comboBox_tts_language = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_tts_language.addItem("")
        self.comboBox_tts_language.addItem("")
        self.comboBox_tts_language.addItem("")
        self.comboBox_tts_language.setObjectName(u"comboBox_tts_language")
        sizePolicy1.setHeightForWidth(self.comboBox_tts_language.sizePolicy().hasHeightForWidth())
        self.comboBox_tts_language.setSizePolicy(sizePolicy1)
        self.comboBox_tts_language.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_22.addWidget(self.comboBox_tts_language)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_22.addWidget(self.label_9)

        self.comboBox_tts_voice_id = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_tts_voice_id.addItem("")
        self.comboBox_tts_voice_id.setObjectName(u"comboBox_tts_voice_id")
        sizePolicy1.setHeightForWidth(self.comboBox_tts_voice_id.sizePolicy().hasHeightForWidth())
        self.comboBox_tts_voice_id.setSizePolicy(sizePolicy1)
        self.comboBox_tts_voice_id.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_22.addWidget(self.comboBox_tts_voice_id)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_13.addWidget(self.label_10)

        self.lineEdit_voice_volume = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_voice_volume.setObjectName(u"lineEdit_voice_volume")
        sizePolicy11.setHeightForWidth(self.lineEdit_voice_volume.sizePolicy().hasHeightForWidth())
        self.lineEdit_voice_volume.setSizePolicy(sizePolicy11)
        self.lineEdit_voice_volume.setMinimumSize(QSize(60, 0))
        self.lineEdit_voice_volume.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_voice_volume.setAcceptDrops(True)
        self.lineEdit_voice_volume.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.lineEdit_voice_volume)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.pushButton_tts_volume_default = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_tts_volume_default.setObjectName(u"pushButton_tts_volume_default")
        sizePolicy4.setHeightForWidth(self.pushButton_tts_volume_default.sizePolicy().hasHeightForWidth())
        self.pushButton_tts_volume_default.setSizePolicy(sizePolicy4)
        self.pushButton_tts_volume_default.setMinimumSize(QSize(130, 30))
        self.pushButton_tts_volume_default.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(122, 137, 168);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 184, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(75, 84, 103);\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_tts_volume_default)


        self.verticalLayout_28.addLayout(self.horizontalLayout_13)

        self.horizontalSlider_tts_speed = QSlider(self.scrollAreaWidgetContents_2)
        self.horizontalSlider_tts_speed.setObjectName(u"horizontalSlider_tts_speed")
        self.horizontalSlider_tts_speed.setStyleSheet(u"")
        self.horizontalSlider_tts_speed.setMaximum(200)
        self.horizontalSlider_tts_speed.setSingleStep(0)
        self.horizontalSlider_tts_speed.setValue(100)
        self.horizontalSlider_tts_speed.setOrientation(Qt.Horizontal)

        self.verticalLayout_28.addWidget(self.horizontalSlider_tts_speed)


        self.verticalLayout_22.addLayout(self.verticalLayout_28)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.lineEdit_voice_speed = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_voice_speed.setObjectName(u"lineEdit_voice_speed")
        sizePolicy11.setHeightForWidth(self.lineEdit_voice_speed.sizePolicy().hasHeightForWidth())
        self.lineEdit_voice_speed.setSizePolicy(sizePolicy11)
        self.lineEdit_voice_speed.setMinimumSize(QSize(60, 0))
        self.lineEdit_voice_speed.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_voice_speed.setAcceptDrops(True)
        self.lineEdit_voice_speed.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.lineEdit_voice_speed)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)

        self.pushButton_spk_default_3 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_spk_default_3.setObjectName(u"pushButton_spk_default_3")
        sizePolicy4.setHeightForWidth(self.pushButton_spk_default_3.sizePolicy().hasHeightForWidth())
        self.pushButton_spk_default_3.setSizePolicy(sizePolicy4)
        self.pushButton_spk_default_3.setMinimumSize(QSize(130, 30))
        self.pushButton_spk_default_3.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(122, 137, 168);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 184, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(75, 84, 103);\n"
"}")

        self.horizontalLayout_14.addWidget(self.pushButton_spk_default_3)


        self.verticalLayout_32.addLayout(self.horizontalLayout_14)

        self.horizontalSlider_tts_speed_2 = QSlider(self.scrollAreaWidgetContents_2)
        self.horizontalSlider_tts_speed_2.setObjectName(u"horizontalSlider_tts_speed_2")
        self.horizontalSlider_tts_speed_2.setStyleSheet(u"")
        self.horizontalSlider_tts_speed_2.setMaximum(200)
        self.horizontalSlider_tts_speed_2.setValue(100)
        self.horizontalSlider_tts_speed_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_32.addWidget(self.horizontalSlider_tts_speed_2)


        self.verticalLayout_22.addLayout(self.verticalLayout_32)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_15.addWidget(self.label_12)

        self.lineEdit_intonation_scale = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_intonation_scale.setObjectName(u"lineEdit_intonation_scale")
        sizePolicy11.setHeightForWidth(self.lineEdit_intonation_scale.sizePolicy().hasHeightForWidth())
        self.lineEdit_intonation_scale.setSizePolicy(sizePolicy11)
        self.lineEdit_intonation_scale.setMinimumSize(QSize(60, 0))
        self.lineEdit_intonation_scale.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_intonation_scale.setAcceptDrops(True)
        self.lineEdit_intonation_scale.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lineEdit_intonation_scale)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)

        self.pushButton_spk_default_4 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_spk_default_4.setObjectName(u"pushButton_spk_default_4")
        sizePolicy4.setHeightForWidth(self.pushButton_spk_default_4.sizePolicy().hasHeightForWidth())
        self.pushButton_spk_default_4.setSizePolicy(sizePolicy4)
        self.pushButton_spk_default_4.setMinimumSize(QSize(130, 30))
        self.pushButton_spk_default_4.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(122, 137, 168);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 184, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(75, 84, 103);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_spk_default_4)


        self.verticalLayout_33.addLayout(self.horizontalLayout_15)

        self.horizontalSlider_tts_intonation_scale = QSlider(self.scrollAreaWidgetContents_2)
        self.horizontalSlider_tts_intonation_scale.setObjectName(u"horizontalSlider_tts_intonation_scale")
        self.horizontalSlider_tts_intonation_scale.setStyleSheet(u"")
        self.horizontalSlider_tts_intonation_scale.setMaximum(200)
        self.horizontalSlider_tts_intonation_scale.setValue(100)
        self.horizontalSlider_tts_intonation_scale.setOrientation(Qt.Horizontal)

        self.verticalLayout_33.addWidget(self.horizontalSlider_tts_intonation_scale)


        self.verticalLayout_22.addLayout(self.verticalLayout_33)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_17.addWidget(self.label_14)

        self.lineEdit_pre_phoneme_length = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_pre_phoneme_length.setObjectName(u"lineEdit_pre_phoneme_length")
        sizePolicy11.setHeightForWidth(self.lineEdit_pre_phoneme_length.sizePolicy().hasHeightForWidth())
        self.lineEdit_pre_phoneme_length.setSizePolicy(sizePolicy11)
        self.lineEdit_pre_phoneme_length.setMinimumSize(QSize(60, 0))
        self.lineEdit_pre_phoneme_length.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_pre_phoneme_length.setAcceptDrops(True)
        self.lineEdit_pre_phoneme_length.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.lineEdit_pre_phoneme_length)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_7)

        self.pushButton_spk_default_6 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_spk_default_6.setObjectName(u"pushButton_spk_default_6")
        sizePolicy4.setHeightForWidth(self.pushButton_spk_default_6.sizePolicy().hasHeightForWidth())
        self.pushButton_spk_default_6.setSizePolicy(sizePolicy4)
        self.pushButton_spk_default_6.setMinimumSize(QSize(130, 30))
        self.pushButton_spk_default_6.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(122, 137, 168);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 184, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(75, 84, 103);\n"
"}")

        self.horizontalLayout_17.addWidget(self.pushButton_spk_default_6)


        self.verticalLayout_35.addLayout(self.horizontalLayout_17)

        self.horizontalSlider_pre_phoneme_length = QSlider(self.scrollAreaWidgetContents_2)
        self.horizontalSlider_pre_phoneme_length.setObjectName(u"horizontalSlider_pre_phoneme_length")
        self.horizontalSlider_pre_phoneme_length.setStyleSheet(u"")
        self.horizontalSlider_pre_phoneme_length.setMaximum(200)
        self.horizontalSlider_pre_phoneme_length.setValue(100)
        self.horizontalSlider_pre_phoneme_length.setOrientation(Qt.Horizontal)

        self.verticalLayout_35.addWidget(self.horizontalSlider_pre_phoneme_length)


        self.verticalLayout_22.addLayout(self.verticalLayout_35)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.lineEdit_post_phoneme_length = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_post_phoneme_length.setObjectName(u"lineEdit_post_phoneme_length")
        sizePolicy11.setHeightForWidth(self.lineEdit_post_phoneme_length.sizePolicy().hasHeightForWidth())
        self.lineEdit_post_phoneme_length.setSizePolicy(sizePolicy11)
        self.lineEdit_post_phoneme_length.setMinimumSize(QSize(60, 0))
        self.lineEdit_post_phoneme_length.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_post_phoneme_length.setAcceptDrops(True)
        self.lineEdit_post_phoneme_length.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lineEdit_post_phoneme_length)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)

        self.pushButton_spk_default_5 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_spk_default_5.setObjectName(u"pushButton_spk_default_5")
        sizePolicy4.setHeightForWidth(self.pushButton_spk_default_5.sizePolicy().hasHeightForWidth())
        self.pushButton_spk_default_5.setSizePolicy(sizePolicy4)
        self.pushButton_spk_default_5.setMinimumSize(QSize(130, 30))
        self.pushButton_spk_default_5.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(122, 137, 168);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 184, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(75, 84, 103);\n"
"}")

        self.horizontalLayout_16.addWidget(self.pushButton_spk_default_5)


        self.verticalLayout_34.addLayout(self.horizontalLayout_16)

        self.horizontalSlider_post_phoneme_length = QSlider(self.scrollAreaWidgetContents_2)
        self.horizontalSlider_post_phoneme_length.setObjectName(u"horizontalSlider_post_phoneme_length")
        self.horizontalSlider_post_phoneme_length.setStyleSheet(u"")
        self.horizontalSlider_post_phoneme_length.setMaximum(200)
        self.horizontalSlider_post_phoneme_length.setValue(100)
        self.horizontalSlider_post_phoneme_length.setOrientation(Qt.Horizontal)

        self.verticalLayout_34.addWidget(self.horizontalSlider_post_phoneme_length)


        self.verticalLayout_22.addLayout(self.verticalLayout_34)

        self.audio_bottom_verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.audio_bottom_verticalSpacer)


        self.verticalLayout_31.addLayout(self.verticalLayout_22)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_30.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.Audio_Page)
        self.Prompt_Page = QWidget()
        self.Prompt_Page.setObjectName(u"Prompt_Page")
        self.Prompt_Page.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(48, 50, 62);\n"
"	border-radius: 10px;\n"
"	color: #FFF;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-color:rgb(34,36,44)\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(66, 70, 86);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(43, 45, 56);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 40px;\n"
"    width: 10px;\n"
"    margin: -20px 0;\n"
"    border-radius: 20px;\n"
"    padding: -20px 0px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(155, 180, 255);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 255, 195);\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.Prompt_Page)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(6, 0, 6, -1)
        self._prompt_top_verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_26.addItem(self._prompt_top_verticalSpacer)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_5 = QLabel(self.Prompt_Page)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_22.addWidget(self.label_5)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_15)

        self.textBrowser_google_colab_link = QTextBrowser(self.Prompt_Page)
        self.textBrowser_google_colab_link.setObjectName(u"textBrowser_google_colab_link")
        sizePolicy11.setHeightForWidth(self.textBrowser_google_colab_link.sizePolicy().hasHeightForWidth())
        self.textBrowser_google_colab_link.setSizePolicy(sizePolicy11)
        self.textBrowser_google_colab_link.setMinimumSize(QSize(0, 0))
        self.textBrowser_google_colab_link.setMaximumSize(QSize(200, 20))
        self.textBrowser_google_colab_link.setFocusPolicy(Qt.NoFocus)
        self.textBrowser_google_colab_link.setAcceptDrops(True)
        self.textBrowser_google_colab_link.setInputMethodHints(Qt.ImhNone)
        self.textBrowser_google_colab_link.setFrameShape(QFrame.NoFrame)
        self.textBrowser_google_colab_link.setFrameShadow(QFrame.Plain)
        self.textBrowser_google_colab_link.setLineWidth(1)
        self.textBrowser_google_colab_link.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_google_colab_link.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_google_colab_link.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.textBrowser_google_colab_link.setAutoFormatting(QTextEdit.AutoNone)
        self.textBrowser_google_colab_link.setLineWrapMode(QTextEdit.NoWrap)
        self.textBrowser_google_colab_link.setAcceptRichText(True)

        self.horizontalLayout_22.addWidget(self.textBrowser_google_colab_link)


        self.verticalLayout_42.addLayout(self.horizontalLayout_22)


        self.verticalLayout_40.addLayout(self.verticalLayout_42)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_api_url = QLineEdit(self.Prompt_Page)
        self.lineEdit_api_url.setObjectName(u"lineEdit_api_url")
        sizePolicy11.setHeightForWidth(self.lineEdit_api_url.sizePolicy().hasHeightForWidth())
        self.lineEdit_api_url.setSizePolicy(sizePolicy11)
        self.lineEdit_api_url.setMinimumSize(QSize(0, 30))
        self.lineEdit_api_url.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_api_url.setEchoMode(QLineEdit.Normal)
        self.lineEdit_api_url.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lineEdit_api_url)

        self.pushButton_view_original_url = QPushButton(self.Prompt_Page)
        self.pushButton_view_original_url.setObjectName(u"pushButton_view_original_url")
        sizePolicy4.setHeightForWidth(self.pushButton_view_original_url.sizePolicy().hasHeightForWidth())
        self.pushButton_view_original_url.setSizePolicy(sizePolicy4)
        self.pushButton_view_original_url.setMinimumSize(QSize(130, 30))
        self.pushButton_view_original_url.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(255, 43, 43);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 114, 114);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(159, 27, 27);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_view_original_url)


        self.verticalLayout_40.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_30 = QLabel(self.Prompt_Page)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_23.addWidget(self.label_30)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_16)

        self.label_25 = QLabel(self.Prompt_Page)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_23.addWidget(self.label_25)


        self.verticalLayout_40.addLayout(self.horizontalLayout_23)


        self.verticalLayout_26.addLayout(self.verticalLayout_40)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_26.addItem(self.verticalSpacer)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_3 = QLabel(self.Prompt_Page)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_24.addWidget(self.label_3)

        self.lineEdit_max_prompt_token = QLineEdit(self.Prompt_Page)
        self.lineEdit_max_prompt_token.setObjectName(u"lineEdit_max_prompt_token")
        self.lineEdit_max_prompt_token.setMinimumSize(QSize(60, 0))
        self.lineEdit_max_prompt_token.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_max_prompt_token.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.lineEdit_max_prompt_token)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_17)

        self.pushButton_max_prompt_token_default = QPushButton(self.Prompt_Page)
        self.pushButton_max_prompt_token_default.setObjectName(u"pushButton_max_prompt_token_default")
        sizePolicy4.setHeightForWidth(self.pushButton_max_prompt_token_default.sizePolicy().hasHeightForWidth())
        self.pushButton_max_prompt_token_default.setSizePolicy(sizePolicy4)
        self.pushButton_max_prompt_token_default.setMinimumSize(QSize(130, 30))
        self.pushButton_max_prompt_token_default.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(122, 137, 168);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 184, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(75, 84, 103);\n"
"}")

        self.horizontalLayout_24.addWidget(self.pushButton_max_prompt_token_default)


        self.verticalLayout_36.addLayout(self.horizontalLayout_24)

        self.horizontalSlider_max_prompt_token = QSlider(self.Prompt_Page)
        self.horizontalSlider_max_prompt_token.setObjectName(u"horizontalSlider_max_prompt_token")
        self.horizontalSlider_max_prompt_token.setStyleSheet(u"")
        self.horizontalSlider_max_prompt_token.setMaximum(8192)
        self.horizontalSlider_max_prompt_token.setPageStep(256)
        self.horizontalSlider_max_prompt_token.setValue(1024)
        self.horizontalSlider_max_prompt_token.setOrientation(Qt.Horizontal)

        self.verticalLayout_36.addWidget(self.horizontalSlider_max_prompt_token)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_26 = QLabel(self.Prompt_Page)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_25.addWidget(self.label_26)

        self.lineEdit_max_reply_token = QLineEdit(self.Prompt_Page)
        self.lineEdit_max_reply_token.setObjectName(u"lineEdit_max_reply_token")
        self.lineEdit_max_reply_token.setMinimumSize(QSize(60, 0))
        self.lineEdit_max_reply_token.setMaximumSize(QSize(60, 16777215))
        self.lineEdit_max_reply_token.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.lineEdit_max_reply_token)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_18)

        self.pushButton_max_reply_token_default = QPushButton(self.Prompt_Page)
        self.pushButton_max_reply_token_default.setObjectName(u"pushButton_max_reply_token_default")
        sizePolicy4.setHeightForWidth(self.pushButton_max_reply_token_default.sizePolicy().hasHeightForWidth())
        self.pushButton_max_reply_token_default.setSizePolicy(sizePolicy4)
        self.pushButton_max_reply_token_default.setMinimumSize(QSize(130, 30))
        self.pushButton_max_reply_token_default.setStyleSheet(u"QPushButton{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	color: white;\n"
"	background-color: rgb(122, 137, 168);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 184, 225);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(75, 84, 103);\n"
"}")

        self.horizontalLayout_25.addWidget(self.pushButton_max_reply_token_default)


        self.verticalLayout_37.addLayout(self.horizontalLayout_25)

        self.horizontalSlider_max_reply_token = QSlider(self.Prompt_Page)
        self.horizontalSlider_max_reply_token.setObjectName(u"horizontalSlider_max_reply_token")
        self.horizontalSlider_max_reply_token.setStyleSheet(u"")
        self.horizontalSlider_max_reply_token.setMaximum(1000)
        self.horizontalSlider_max_reply_token.setPageStep(100)
        self.horizontalSlider_max_reply_token.setValue(200)
        self.horizontalSlider_max_reply_token.setOrientation(Qt.Horizontal)

        self.verticalLayout_37.addWidget(self.horizontalSlider_max_reply_token)


        self.verticalLayout_36.addLayout(self.verticalLayout_37)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_27 = QLabel(self.Prompt_Page)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_38.addWidget(self.label_27)

        self.comboBox_ai_model_language = QComboBox(self.Prompt_Page)
        self.comboBox_ai_model_language.addItem("")
        self.comboBox_ai_model_language.addItem("")
        self.comboBox_ai_model_language.addItem("")
        self.comboBox_ai_model_language.setObjectName(u"comboBox_ai_model_language")
        sizePolicy1.setHeightForWidth(self.comboBox_ai_model_language.sizePolicy().hasHeightForWidth())
        self.comboBox_ai_model_language.setSizePolicy(sizePolicy1)
        self.comboBox_ai_model_language.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_38.addWidget(self.comboBox_ai_model_language)

        self.label_24 = QLabel(self.Prompt_Page)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_38.addWidget(self.label_24)


        self.verticalLayout_36.addLayout(self.verticalLayout_38)


        self.verticalLayout_26.addLayout(self.verticalLayout_36)

        self._prompt_bottom_verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self._prompt_bottom_verticalSpacer)


        self.verticalLayout_39.addLayout(self.verticalLayout_26)

        self.stackedWidget.addWidget(self.Prompt_Page)
        self.Page_example = QWidget()
        self.Page_example.setObjectName(u"Page_example")
        self.Page_example.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.Page_example)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.Page_example)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.Page_example)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon7)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 352, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy1.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy1)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.Page_example)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy12)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.Page_example)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(7)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 10)
        self.label_2 = QLabel(self.contentSettings)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_41.addWidget(self.label_2)

        self.comboBox_discord_print_language = QComboBox(self.contentSettings)
        self.comboBox_discord_print_language.addItem("")
        self.comboBox_discord_print_language.addItem("")
        self.comboBox_discord_print_language.addItem("")
        self.comboBox_discord_print_language.setObjectName(u"comboBox_discord_print_language")
        self.comboBox_discord_print_language.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_41.addWidget(self.comboBox_discord_print_language)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_41.addItem(self.verticalSpacer_7)

        self.checkBox_discord_bot = QCheckBox(self.contentSettings)
        self.checkBox_discord_bot.setObjectName(u"checkBox_discord_bot")

        self.verticalLayout_41.addWidget(self.checkBox_discord_bot)

        self.lineEdit_discord_bot_id = QLineEdit(self.contentSettings)
        self.lineEdit_discord_bot_id.setObjectName(u"lineEdit_discord_bot_id")
        sizePolicy11.setHeightForWidth(self.lineEdit_discord_bot_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_discord_bot_id.setSizePolicy(sizePolicy11)
        self.lineEdit_discord_bot_id.setMinimumSize(QSize(0, 30))
        self.lineEdit_discord_bot_id.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_discord_bot_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.lineEdit_discord_bot_id)

        self.lineEdit_discord_bot_channel_id = QLineEdit(self.contentSettings)
        self.lineEdit_discord_bot_channel_id.setObjectName(u"lineEdit_discord_bot_channel_id")
        sizePolicy11.setHeightForWidth(self.lineEdit_discord_bot_channel_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_discord_bot_channel_id.setSizePolicy(sizePolicy11)
        self.lineEdit_discord_bot_channel_id.setMinimumSize(QSize(0, 30))
        self.lineEdit_discord_bot_channel_id.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_discord_bot_channel_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.lineEdit_discord_bot_channel_id)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_41.addItem(self.verticalSpacer_5)

        self.checkBox_discord_webhook = QCheckBox(self.contentSettings)
        self.checkBox_discord_webhook.setObjectName(u"checkBox_discord_webhook")

        self.verticalLayout_41.addWidget(self.checkBox_discord_webhook)

        self.lineEdit_discord_webhook_url = QLineEdit(self.contentSettings)
        self.lineEdit_discord_webhook_url.setObjectName(u"lineEdit_discord_webhook_url")
        sizePolicy11.setHeightForWidth(self.lineEdit_discord_webhook_url.sizePolicy().hasHeightForWidth())
        self.lineEdit_discord_webhook_url.setSizePolicy(sizePolicy11)
        self.lineEdit_discord_webhook_url.setMinimumSize(QSize(0, 30))
        self.lineEdit_discord_webhook_url.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_discord_webhook_url.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.lineEdit_discord_webhook_url)

        self.lineEdit_discord_webhook_username = QLineEdit(self.contentSettings)
        self.lineEdit_discord_webhook_username.setObjectName(u"lineEdit_discord_webhook_username")
        sizePolicy11.setHeightForWidth(self.lineEdit_discord_webhook_username.sizePolicy().hasHeightForWidth())
        self.lineEdit_discord_webhook_username.setSizePolicy(sizePolicy11)
        self.lineEdit_discord_webhook_username.setMinimumSize(QSize(0, 30))
        self.lineEdit_discord_webhook_username.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_discord_webhook_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.lineEdit_discord_webhook_username)

        self.label_28 = QLabel(self.contentSettings)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_41.addWidget(self.label_28)

        self.lineEdit_discord_webhook_avatar = QLineEdit(self.contentSettings)
        self.lineEdit_discord_webhook_avatar.setObjectName(u"lineEdit_discord_webhook_avatar")
        sizePolicy11.setHeightForWidth(self.lineEdit_discord_webhook_avatar.sizePolicy().hasHeightForWidth())
        self.lineEdit_discord_webhook_avatar.setSizePolicy(sizePolicy11)
        self.lineEdit_discord_webhook_avatar.setMinimumSize(QSize(0, 30))
        self.lineEdit_discord_webhook_avatar.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_discord_webhook_avatar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.lineEdit_discord_webhook_avatar)

        self.label_29 = QLabel(self.contentSettings)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_41.addWidget(self.label_29)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_6)


        self.verticalLayout_13.addLayout(self.verticalLayout_41)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


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
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_character.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.btn_audio_setting.setText(QCoreApplication.translate("MainWindow", u"Mic Setting", None))
        self.btn_prompt_setting.setText(QCoreApplication.translate("MainWindow", u"TTS Setting", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Visit Github Page", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Blessing AI</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">this python program is made for communicating prompt and result from chatbot interface (e.g oobabooga/text-generation-webui), also able t"
                        "o use TTS, voice recognition or text from User.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/HWcomss/Blessing-AI/blob/main/LICENSE.md\"><span style=\" text-decoration: underline; color:#00aaff;\">MIT License</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: HWcoms</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_chat_log.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Chat Log</span></p></body></html>", None))
        self.label_token_count.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Token Count</span></p></body></html>", None))
        self.lineEdit_token_count.setText(QCoreApplication.translate("MainWindow", u"1203", None))
        self.chat_widget_placeholder_2.setText("")
        self.textEdit_user_message.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hello My name is Coms</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nice to meet you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">how are you today.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\">I'm good</p></body></html>", None))
        self.label_last_user_message.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Last User Message</span></p></body></html>", None))
        self.textEdit_bot_reply.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hello, coms!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nice to meet you too!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I'm good today.</p></body></html>", None))
        self.label_last_bot_reply.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Last Bot Reply</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Message Queue</span></p></body></html>", None))
        self.pushButton_mute_tts.setText(QCoreApplication.translate("MainWindow", u"Toggle Spk", None))
        self.pushButton_mute_mic.setText(QCoreApplication.translate("MainWindow", u"Toggle Mic", None))
        self.pushButton_pause_reply.setText(QCoreApplication.translate("MainWindow", u"  Skip", None))
        self.pushButton_stop_reply.setText(QCoreApplication.translate("MainWindow", u" Generate", None))
        self.label_your_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Your Name</span></p></body></html>", None))
        self.textEdit_yourname.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You</p></body></html>", None))
        self.label_greeting.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Greeting</span></p></body></html>", None))
        self.textEdit_greeting.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hello my name is bot</p></body></html>", None))
        self.label_char_img.setText(QCoreApplication.translate("MainWindow", u"char_img", None))
        self.label_char_name.setText(QCoreApplication.translate("MainWindow", u"char_name", None))
        self.label_context.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Context</span></p></body></html>", None))
        self.textEdit_context.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this is AI language model. chat assistance.</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Mic Device</span></p></body></html>", None))
        self.comboBox_mic_device.setItemText(0, QCoreApplication.translate("MainWindow", u"Mic device 1", None))
        self.comboBox_mic_device.setItemText(1, QCoreApplication.translate("MainWindow", u"Mic 2", None))
        self.comboBox_mic_device.setItemText(2, QCoreApplication.translate("MainWindow", u"Mic 3", None))

        self.pushButton_mic_default.setText(QCoreApplication.translate("MainWindow", u"Set to Default", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Mic Threshold</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Phrase TimeOut</span></p></body></html>", None))
        self.lineEdit_phrase_timeout.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>seconds</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Speaker Device</span></p></body></html>", None))
        self.comboBox_spk_device.setItemText(0, QCoreApplication.translate("MainWindow", u"Spk device 1", None))
        self.comboBox_spk_device.setItemText(1, QCoreApplication.translate("MainWindow", u"Spk 2", None))
        self.comboBox_spk_device.setItemText(2, QCoreApplication.translate("MainWindow", u"Spk 3", None))

        self.pushButton_spk_default.setText(QCoreApplication.translate("MainWindow", u"Set to Default", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">TTS Character</span></p></body></html>", None))
        self.comboBox_tts_charcter.setItemText(0, QCoreApplication.translate("MainWindow", u"Character 1", None))
        self.comboBox_tts_charcter.setItemText(1, QCoreApplication.translate("MainWindow", u"Character 2", None))
        self.comboBox_tts_charcter.setItemText(2, QCoreApplication.translate("MainWindow", u"Character 3", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">TTS Language</span></p></body></html>", None))
        self.comboBox_tts_language.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox_tts_language.setItemText(1, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.comboBox_tts_language.setItemText(2, QCoreApplication.translate("MainWindow", u"Korean", None))

        self.comboBox_tts_language.setCurrentText(QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">TTS Voice ID (Index)</span></p></body></html>", None))
        self.comboBox_tts_voice_id.setItemText(0, QCoreApplication.translate("MainWindow", u"0 - Char_name", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Voice Volume</span></p></body></html>", None))
        self.lineEdit_voice_volume.setText(QCoreApplication.translate("MainWindow", u"100 %", None))
        self.pushButton_tts_volume_default.setText(QCoreApplication.translate("MainWindow", u"Set to Default", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Voice Speed</span></p></body></html>", None))
        self.lineEdit_voice_speed.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.pushButton_spk_default_3.setText(QCoreApplication.translate("MainWindow", u"Set to Default", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Intonation Scale</span></p></body></html>", None))
        self.lineEdit_intonation_scale.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.pushButton_spk_default_4.setText(QCoreApplication.translate("MainWindow", u"Set to Default", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Pre Phoneme Length</span></p></body></html>", None))
        self.lineEdit_pre_phoneme_length.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.pushButton_spk_default_6.setText(QCoreApplication.translate("MainWindow", u"Set to Default", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Post Phoneme Length</span></p></body></html>", None))
        self.lineEdit_post_phoneme_length.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.pushButton_spk_default_5.setText(QCoreApplication.translate("MainWindow", u"Set to Default", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Language Model API Url</span></p></body></html>", None))
        self.textBrowser_google_colab_link.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://colab.research.google.com/drive/1VwEONZNajP4WGwJ8bw55MODHQ_yq1hpJ?usp=sharing\"><span style=\" text-decoration: underline; color:#aaffff;\">Run in Cloud (Google Colab)</span></a></p></body></html>", None))
        self.lineEdit_api_url.setText(QCoreApplication.translate("MainWindow", u"http://localhost:5000", None))
        self.lineEdit_api_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"API Request Url", None))
        self.pushButton_view_original_url.setText(QCoreApplication.translate("MainWindow", u"View URL", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">(Example) With Colab: </span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#aaffff;\">https://blessing-ai-test.trycloudflare.com/api</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt;\">With local: </span><span style=\" font-family:'JetBrains Mono','monospace'; font-size:9.8pt; color:#aaffff;\">http://localhost:5000</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Max Prompt Token</span></p></body></html>", None))
        self.lineEdit_max_prompt_token.setText(QCoreApplication.translate("MainWindow", u"1024", None))
        self.pushButton_max_prompt_token_default.setText(QCoreApplication.translate("MainWindow", u"Set to Default", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Max Reply Token</span></p></body></html>", None))
        self.lineEdit_max_reply_token.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.pushButton_max_reply_token_default.setText(QCoreApplication.translate("MainWindow", u"Set to Default", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">AI Model Language</span></p></body></html>", None))
        self.comboBox_ai_model_language.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox_ai_model_language.setItemText(1, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.comboBox_ai_model_language.setItemText(2, QCoreApplication.translate("MainWindow", u"Korean", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700;\">Recommend to set as 'EN'</span></p></body></html>", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Send Discord Bot Message As</span></p></body></html>", None))
        self.comboBox_discord_print_language.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox_discord_print_language.setItemText(1, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.comboBox_discord_print_language.setItemText(2, QCoreApplication.translate("MainWindow", u"Korean", None))

        self.checkBox_discord_bot.setText(QCoreApplication.translate("MainWindow", u"Discord Bot", None))
        self.lineEdit_discord_bot_id.setText("")
        self.lineEdit_discord_bot_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Discord Bot ID (Token)", None))
        self.lineEdit_discord_bot_channel_id.setText("")
        self.lineEdit_discord_bot_channel_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Discord Channel ID to send msg", None))
        self.checkBox_discord_webhook.setText(QCoreApplication.translate("MainWindow", u"Discord Webhook", None))
        self.lineEdit_discord_webhook_url.setText("")
        self.lineEdit_discord_webhook_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Discord Webhook Url (Token)", None))
        self.lineEdit_discord_webhook_username.setText("")
        self.lineEdit_discord_webhook_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom Bot name", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">\u25b2 Default: keep it blank</span></p></body></html>", None))
        self.lineEdit_discord_webhook_avatar.setText("")
        self.lineEdit_discord_webhook_avatar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Custom Profile Picture", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt;\">\u25b2 Default: keep it blank</span></p></body></html>", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Copyright (c) 2023 HWcoms", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

