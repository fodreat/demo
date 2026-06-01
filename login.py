# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(292, 300)
        self.Login_line = QLineEdit(Form)
        self.Login_line.setObjectName(u"Login_line")
        self.Login_line.setGeometry(QRect(70, 100, 113, 22))
        self.Password_line = QLineEdit(Form)
        self.Password_line.setObjectName(u"Password_line")
        self.Password_line.setGeometry(QRect(70, 140, 113, 22))
        self.Password_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.Guest_button = QPushButton(Form)
        self.Guest_button.setObjectName(u"Guest_button")
        self.Guest_button.setGeometry(QRect(200, 10, 75, 24))
        self.Entry_button = QPushButton(Form)
        self.Entry_button.setObjectName(u"Entry_button")
        self.Entry_button.setGeometry(QRect(80, 170, 101, 24))
        self.Registry_button = QPushButton(Form)
        self.Registry_button.setObjectName(u"Registry_button")
        self.Registry_button.setGeometry(QRect(80, 220, 101, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Login_line.setText("")
        self.Password_line.setText("")
        self.Guest_button.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0441\u0442\u044c", None))
        self.Entry_button.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438 ", None))
        self.Registry_button.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

