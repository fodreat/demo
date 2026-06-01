# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        Menu.resize(400, 300)
        self.order_Button = QPushButton(Menu)
        self.order_Button.setObjectName(u"order_Button")
        self.order_Button.setGeometry(QRect(260, 120, 91, 41))
        self.katalog_Button = QPushButton(Menu)
        self.katalog_Button.setObjectName(u"katalog_Button")
        self.katalog_Button.setGeometry(QRect(60, 120, 91, 41))
        self.name_label = QLabel(Menu)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(320, 20, 49, 16))
        self.exit_Button = QPushButton(Menu)
        self.exit_Button.setObjectName(u"exit_Button")
        self.exit_Button.setGeometry(QRect(320, 270, 75, 24))

        self.retranslateUi(Menu)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"Form", None))
        self.order_Button.setText(QCoreApplication.translate("Menu", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
        self.katalog_Button.setText(QCoreApplication.translate("Menu", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.name_label.setText(QCoreApplication.translate("Menu", u"\u0413\u043e\u0441\u0442\u044c", None))
        self.exit_Button.setText(QCoreApplication.translate("Menu", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

