import sys
from PySide6.QtWidgets import (QApplication,QWidget,QMainWindow)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt,Signal
from card import Ui_tovar_card
from database import connect_bd,has_password
import os


class product_card(QWidget):
    clicked=Signal(int)

    def __init__(self,product):
        super().__init__()
        self.ui = Ui_tovar_card()
        self.ui.setupUi(self)
        self.product_id=product[0]

        self.setMinimumHeight(140)
        self.setMinimumWidth(400)

        self.setStyleSheet("""
                    QWidget {
                        background-color: white;
                        border: 2px solid #22C55E;
                        border-radius: 8px;
                    }
                """)

        self.ui.name_label.setText(f"{product[1]}")
        self.ui.article_label.setText(f"{product[2]}")
        self.ui.price_label.setText(f"{product[3]}")
        self.ui.size_label.setText(f"{product[4]}")
        self.ui.brand_label.setText(f"{product[5]}")
        #image=product[6]

        """if image:
            patch=os.path.join('images',image)
            if os.path.exists(patch):
                self.ui.image_label.setPixmap(QPixmap(patch))
            else:
                self.ui.image_label.setText("Нет фото")"""

    def mousePressEvent(self, event):
        if event.buttons()==Qt.MouseButton:
            self.clicked.emit(self.product_id)
        super().mousePressEvent(event)