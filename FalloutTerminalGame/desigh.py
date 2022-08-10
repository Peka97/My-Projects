from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QLabel, QPushButton, QTextEdit, QWidget)
import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"Qlabel {\n"
                                         "	color: white;\n"
                                         "	font-family: Undertale Battle Font;\n"
                                         "	font-size: 10pt;\n"
                                         "	font-color: white;\n"
                                         "	background-color: white;\n"
                                         "	\n"
                                         "}")
        self.back = QLabel(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(0, 0, 800, 600))
        self.back.setPixmap(QPixmap(u":/newPrefix/Theme Window.jpg"))
        self.text_code = QLabel(self.centralwidget)
        self.text_code.setObjectName(u"text_code")
        self.text_code.setGeometry(QRect(30, 50, 600, 461))
        font = QFont()
        font.setFamilies([u"Undertale Battle Font"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.text_code.setFont(font)
        self.text_code.setStyleSheet(u"font: 0 bold 11pt \"Undertale Battle Font\";\n"
                                     "color: #5FCF80;")
        self.text_attempts = QLabel(self.centralwidget)
        self.text_attempts.setObjectName(u"text_attempts")
        self.text_attempts.setGeometry(QRect(30, 80, 800, 51))
        self.text_attempts.setFont(font)
        self.text_attempts.setStyleSheet(u"font: 0 bold 12pt \"Undertale Battle Font\";\n"
                                         "color: #5FCF80;")
        self.text_word = QTextEdit(self.centralwidget)
        self.text_word.setObjectName(u"text_word")
        self.text_word.setGeometry(QRect(30, 130, 565, 41))
        font1 = QFont()
        font1.setFamilies([u"Undertale Battle Font"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.text_word.setFont(font1)
        self.text_word.setStyleSheet(u"background-color: #5FCF80;")
        self.btn_enter = QPushButton(self.centralwidget)
        self.btn_enter.setObjectName(u"btn_enter")
        self.btn_enter.setGeometry(QRect(590, 130, 91, 41))
        self.btn_enter.setStyleSheet(u"font: 0 bold 12pt \"Undertale Battle Font\";\n"
                                     "color: #5FCF80;\n"
                                     "background-color:rgba(255, 255, 255, 0)\n"
                                     "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fallout Terminal Game", None))
        self.back.setText("")
        self.text_code.setText(
            QCoreApplication.translate("MainWindow", u"", None))
        self.text_attempts.setText(
            QCoreApplication.translate("MainWindow", u"", None))
        self.btn_enter.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
    # retranslateUi
