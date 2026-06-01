import sys
from PySide6.QtWidgets import (QApplication,QWidget,QMainWindow,QVBoxLayout,QMessageBox)
from login import Ui_Form
from menu import Ui_Menu
from database import connect_bd,has_password
from product_card import product_card
from catalog import Ui_Catalog
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Entry_button.clicked.connect(self.log)
        self.ui.Guest_button.clicked.connect(self.guest)

        self.conn=connect_bd()
        self.cur=self.conn.cursor()
    def guest(self):
        self.open_menu("Гость",6)

    def log(self):
        login=self.ui.Login_line.text()
        password=self.ui.Password_line.text()
        password=has_password(password)
        self.cur.execute("SELECT * FROM users")
        users=self.cur.fetchall()
        for i in users:
            if password in i and login in i:
                self.open_menu(login,i[3])
    def open_menu(self,login,role):
        self.menu=Menu(login,role)
        self.menu.show()
        self.hide()
class Menu(QWidget):
    def __init__(self,login,role):
        super().__init__()
        self.ui=Ui_Menu()
        self.ui.setupUi(self)
        self.role=role
        self.login=login
        self.role_reales()
        self.ui.exit_Button.clicked.connect(self.exits)
        self.ui.katalog_Button.clicked.connect(self.open_catalog)
    def role_reales(self):
        if self.role=="Guest" :
            self.ui.order_Button.hide()
        elif self.role==2:
            self.ui.order_Button.hide()

            self.ui.name_label.setText(self.login)
        elif self.role ==3:
            self.ui.name_label.setText(self.login)
        else:
            self.ui.name_label.setText(self.login)

    def exits(self):
        self.login_window = Login()
        self.login_window.show()
        self.hide()

    def open_catalog(self):
        self.katalog = Katalog()
        self.katalog.show()
        self.hide()

class Katalog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Catalog()
        self.ui.setupUi(self)

        self.conn=connect_bd()
        self.cur=self.conn.cursor()

        self.load_products()
    def load_products(self):
        self.cur.execute("Select * from products")
        products=self.cur.fetchall()
        print(f"Найдено товаров: {len(products)}")
        container=QWidget()
        layout=QVBoxLayout(container)
        layout.setSpacing(10)

        for i in products:
            card=product_card(i)
            card.clicked.connect(self.show_detals)
            layout.addWidget(card)
            print(i)
        layout.addStretch()

        self.ui.scrollArea.setWidget(container)
    def show_detals(self,product_id):
        self.cur.execute("SELECT name, brent FROM products WHERE id=?",
            (product_id,))
        p=self.cur.fetchone()
        print(33)
        QMessageBox.information(self,f"dassd")

app=QApplication(sys.argv)
win=Login()
win.show()
sys.exit(app.exec())

