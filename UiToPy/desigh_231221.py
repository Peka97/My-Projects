# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desigh.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resurses_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(330, 128)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.act_open = QAction(MainWindow)
        self.act_open.setObjectName(u"act_open")
        self.act_save = QAction(MainWindow)
        self.act_save.setObjectName(u"act_save")
        self.act_exit = QAction(MainWindow)
        self.act_exit.setObjectName(u"act_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn = QPushButton(self.centralwidget)
        self.btn.setObjectName(u"btn")

        self.verticalLayout_2.addWidget(self.btn)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 330, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.act_open)
        self.menu.addAction(self.act_save)
        self.menu.addSeparator()
        self.menu.addAction(self.act_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.act_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.act_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.act_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c .ui \u0432 .py", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u043e\u0439 \u0444\u0430\u0439\u043b \u0432 \u043c\u0435\u043d\u044e \u0432\u044b\u0448\u0435 \u0438 \u043d\u0430\u0436\u043c\u0438 \u043a\u043d\u043e\u043f\u043a\u0443", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

