# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'catalog2.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QScrollArea, QSizePolicy,
    QWidget)

class Ui_Catalog2(object):
    def setupUi(self, Catalog2):
        if not Catalog2.objectName():
            Catalog2.setObjectName(u"Catalog2")
        Catalog2.resize(800, 800)
        self.groupBox = QGroupBox(Catalog2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(-10, 20, 891, 80))
        self.scrollArea = QScrollArea(Catalog2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 120, 800, 591))
        self.scrollArea.setMinimumSize(QSize(800, 400))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 798, 589))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Catalog2)

        QMetaObject.connectSlotsByName(Catalog2)
    # setupUi

    def retranslateUi(self, Catalog2):
        Catalog2.setWindowTitle(QCoreApplication.translate("Catalog2", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Catalog2", u"GroupBox", None))
    # retranslateUi

