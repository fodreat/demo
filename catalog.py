# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'catalog.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QScrollArea,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Catalog(object):
    def setupUi(self, Catalog):
        if not Catalog.objectName():
            Catalog.setObjectName(u"Catalog")
        Catalog.resize(900, 700)
        self.centralwidget = QWidget(Catalog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 70, 800, 591))
        self.scrollArea.setMinimumSize(QSize(800, 400))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 798, 589))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        Catalog.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Catalog)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        Catalog.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Catalog)
        self.statusbar.setObjectName(u"statusbar")
        Catalog.setStatusBar(self.statusbar)

        self.retranslateUi(Catalog)

        QMetaObject.connectSlotsByName(Catalog)
    # setupUi

    def retranslateUi(self, Catalog):
        Catalog.setWindowTitle(QCoreApplication.translate("Catalog", u"MainWindow", None))
    # retranslateUi

