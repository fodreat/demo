# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_tovar_card(object):
    def setupUi(self, tovar_card):
        if not tovar_card.objectName():
            tovar_card.setObjectName(u"tovar_card")
        tovar_card.resize(381, 124)
        self.image_label = QLabel(tovar_card)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(10, 40, 61, 16))
        self.image_label.setScaledContents(False)
        self.name_label = QLabel(tovar_card)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(250, 10, 61, 16))
        self.article_label = QLabel(tovar_card)
        self.article_label.setObjectName(u"article_label")
        self.article_label.setGeometry(QRect(250, 30, 49, 16))
        self.price_label = QLabel(tovar_card)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setGeometry(QRect(250, 50, 49, 16))
        self.size_label = QLabel(tovar_card)
        self.size_label.setObjectName(u"size_label")
        self.size_label.setGeometry(QRect(250, 70, 49, 16))
        self.brand_label = QLabel(tovar_card)
        self.brand_label.setObjectName(u"brand_label")
        self.brand_label.setGeometry(QRect(250, 90, 49, 16))
        self.image_label.raise_()
        self.brand_label.raise_()
        self.name_label.raise_()
        self.article_label.raise_()
        self.size_label.raise_()
        self.price_label.raise_()

        self.retranslateUi(tovar_card)

        QMetaObject.connectSlotsByName(tovar_card)
    # setupUi

    def retranslateUi(self, tovar_card):
        tovar_card.setWindowTitle(QCoreApplication.translate("tovar_card", u"Form", None))
        self.image_label.setText(QCoreApplication.translate("tovar_card", u"\u041d\u0435\u0442 \u0444\u043e\u0442\u043e", None))
        self.name_label.setText(QCoreApplication.translate("tovar_card", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.article_label.setText(QCoreApplication.translate("tovar_card", u"\u0430\u0440\u0442\u0438\u043a\u043b", None))
        self.price_label.setText(QCoreApplication.translate("tovar_card", u"\u0446\u0435\u043d\u0430", None))
        self.size_label.setText(QCoreApplication.translate("tovar_card", u"\u0440\u0430\u0437\u043c\u0435\u0440", None))
        self.brand_label.setText(QCoreApplication.translate("tovar_card", u"\u0411\u0440\u0435\u043d\u0434", None))
    # retranslateUi

