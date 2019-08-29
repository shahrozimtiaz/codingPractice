from PyQt5.Qt import *
import sys
import MySqlConnector

cursor = MySqlConnector.connect('root','Jokerface07!')

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        screen = app.primaryScreen().size()
        self.title = 'Restaurant Application'
        width = screen.width()
        height = screen.height()
        self.left = 0
        self.top = 0
        self.width = width
        self.height = height
        self.table_widget = MyTableWidget()
        self.setCentralWidget(self.table_widget.tabs)
        self.initUI()

        self.show()

    def initUI(self):
        # window
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # statusbar
        self.statusBar().showMessage('Welcome to el restaurante')

class MyTableWidget(QWidget):
    validUser = True

    def __init__(self):
        super().__init__()

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.login = QWidget()
        self.menu = QWidget()
        self.checkOut = QWidget()
        self.tabs.resize(500, 200)

        # Add tabs
        self.tabs.addTab(self.login, "Login")
        self.tabs.addTab(self.menu, "Menu")
        self.tabs.addTab(self.checkOut, "Check out")

        #intialze tabs
        self.login_startup()
        self.menu_startup()
        self.checkout_startup()

    def login_startup(self):
        self.login.layout = QFormLayout(self)

        self.login.userBox = QLineEdit()
        self.login.userBox.returnPressed.connect(self.on_click_login)
        self.login.layout.addRow(QLabel("Username:"), self.login.userBox)
        self.login.passBox = QLineEdit()
        self.login.passBox.setEchoMode(QLineEdit.Password)
        self.login.passBox.returnPressed.connect(self.on_click_login)
        self.login.layout.addRow(QLabel("Password:"), self.login.passBox)
        self.login.loginButton = QPushButton('Login', self)
        self.login.loginButton.clicked.connect(self.on_click_login)
        self.login.layout.addRow(QLabel(""), self.login.loginButton)
        self.login.setLayout(self.login.layout)

        # login text
        self.login.loginPrompt = QLabel("Please provide a valid login")
        self.login.loginPrompt.setFixedSize(315, 30)
        self.login.loginPromptFont = QFont("Times", 27, QFont.Bold)
        self.login.loginPrompt.setFont(self.login.loginPromptFont)
        self.login.layout.addWidget(self.login.loginPrompt)


    def menu_startup(self):
        self.menu.layout = QGridLayout()
        self.menuInvalidUserLogin = QLabel("Please login in to view")
        self.menu.layout.addWidget(self.menuInvalidUserLogin)


        self.menu.pizza10 = QToolButton()
        self.menu.pizza10.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.menu.pizza10.setAutoFillBackground(True)
        # self.menu.pizza10.set
        # mppix = QPixmap('macCheese.jpg')
        # icon = mppix.scaled(QSize(125,65),Qt.KeepAspectRatio)
        # self.menu.pizza10.setIconSize(self.menu.pizza10.size())
        # self.menu.pizza10.setText('10" pizza $10.99')
        # self.menu.pizza10.setBackgroundRole(QPalette.Button)
        # iBackButton->setBackgroundRole(QPalette::Button);
        self.menu.pizza10.setIcon(QIcon('macCheese.jpg'))
        self.menu.pizza12 = QPushButton('12" pizza $12.99')
        self.menu.pizza14 = QPushButton('14" pizza $14.99')
        self.menu.macNCheese = QPushButton("Mac n' Cheese $4.99")
        self.menu.greatWhite = QPushButton('Great White $7.99')
        self.menu.steak = QPushButton('Steak $14.99')
        self.menu.yeetBuster = QPushButton('YeetBuster $29.99')
        self.menu.calzone = QPushButton('Calzone $8.99')
        self.menu.salmon = QPushButton('Salmon $19.99')

        self.menu.items = [self.menu.pizza10,self.menu.pizza12,self.menu.pizza14,self.menu.macNCheese,self.menu.greatWhite,
                           self.menu.steak,self.menu.yeetBuster,self.menu.calzone,self.menu.salmon]
        for item in self.menu.items:
            item.setFixedSize(155, 95)

        self.menu.layout.addWidget(self.menu.pizza10, 0, 0)
        self.menu.layout.addWidget(self.menu.pizza12, 0, 1)
        self.menu.layout.addWidget(self.menu.pizza14, 0, 2)
        self.menu.layout.addWidget(self.menu.macNCheese, 1, 0)
        self.menu.layout.addWidget(self.menu.greatWhite, 1, 1)
        self.menu.layout.addWidget(self.menu.steak, 1, 2)
        self.menu.layout.addWidget(self.menu.yeetBuster, 2, 0)
        self.menu.layout.addWidget(self.menu.calzone, 2, 1)
        self.menu.layout.addWidget(self.menu.salmon, 2, 2)


        self.menu_update()
        self.menu.setLayout(self.menu.layout)
    def checkout_startup(self):
        self.checkOut.layout = QFormLayout(self)
        self.checkOut.layout.addRow(QLabel("Username:"), QLineEdit())
        self.checkOut.layout.addRow(QLabel("Password:"), QLineEdit())
        self.checkOut.setLayout(self.checkOut.layout)

    def menu_update(self):
        if (self.validUser):
            self.menuInvalidUserLogin.hide()
            for item in self.menu.items:
                item.show()
        else:
            for i in reversed(range(self.menu.layout.count())):
                widgetToRemove = self.menu.layout.itemAt(i).widget()
                # self.menu.layout.removeWidget(widgetToRemove)
                widgetToRemove.hide()
            self.menuInvalidUserLogin.show()

    def on_click_login(self):
        userTextboxValue = self.login.userBox.text()
        passTextboxValue = self.login.passBox.text()
        self.login.userBox.clear()
        self.login.passBox.clear()
        self.login.userBox.setFocus()
        cursor.execute("Select password from python.menuUsers where username = '" + userTextboxValue + "'")
        row = cursor.fetchone()
        if(row != None):
            if (passTextboxValue == row[0]):
                self.validUser=True
                self.login.loginPrompt.setText("Shore Shack \u2122")
                QMessageBox.question(self, 'Response', "Login successful: Welcome", QMessageBox.Ok,QMessageBox.Ok)
            else:
                self.validUser=False
                self.login.loginPrompt.setText("Please provide a valid login")
                QMessageBox.question(self, 'Response', "Login unsuccessful: EXPLAIN YOURSELF", QMessageBox.Ok,QMessageBox.Ok)
        else:
            self.validUser = False
            self.login.loginPrompt.setText("Please provide a valid login")
            QMessageBox.question(self, 'Response', "Login unsuccessful: EXPLAIN YOURSELF", QMessageBox.Ok,QMessageBox.Ok)
        self.menu_update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())