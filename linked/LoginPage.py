from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginPage(object):
    def openHomePage2(self):
        from HomePage2 import Ui_HomePage2
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomePage2()
        self.ui.setupUi(self.window)

        self.window.show()

    def setupUi(self, loginPage):
        loginPage.setObjectName("LoginPage")
        loginPage.resize(446, 193)
        self.centralwidget = QtWidgets.QWidget(loginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(20, 30, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(20, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.textEdit_username = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_username.setGeometry(QtCore.QRect(90, 20, 301, 31))
        self.textEdit_username.setObjectName("textEdit_username")
        self.textEdit_password = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_password.setGeometry(QtCore.QRect(90, 60, 301, 31))
        self.textEdit_password.setObjectName("textEdit_password")
        self.pushButton_login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_login.setGeometry(QtCore.QRect(100, 110, 101, 41))
        self.pushButton_login.setObjectName("pushButton_login")

        self.pushButton_login.clicked.connect(self.openHomePage2) # connect the button to home page 2
        self.pushButton_login.clicked.connect(loginPage.close)
        self.pushButton_forgotPassowrd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_forgotPassowrd.setGeometry(QtCore.QRect(220, 110, 121, 41))
        self.pushButton_forgotPassowrd.setObjectName("pushButton_forgotPassowrd")
        loginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 21))
        self.menubar.setObjectName("menubar")
        loginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginPage)
        self.statusbar.setObjectName("statusbar")
        loginPage.setStatusBar(self.statusbar)

        self.retranslateUi(loginPage)
        QtCore.QMetaObject.connectSlotsByName(loginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "MainWindow"))
        self.label_username.setText(_translate("LoginPage", "Username"))
        self.label_password.setText(_translate("LoginPage", "Password"))
        self.pushButton_login.setText(_translate("LoginPage", "Log in"))
        self.pushButton_forgotPassowrd.setText(_translate("LoginPage", "Forgot Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_loginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
