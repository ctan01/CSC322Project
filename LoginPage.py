# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(432, 200)
        self.centralwidget = QtWidgets.QWidget(Login)
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
        self.pushButton_forgotPassowrd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_forgotPassowrd.setGeometry(QtCore.QRect(220, 110, 121, 41))
        self.pushButton_forgotPassowrd.setObjectName("pushButton_forgotPassowrd")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        self.menuback = QtWidgets.QMenu(self.menubar)
        self.menuback.setObjectName("menuback")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuback.menuAction())

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label_username.setText(_translate("Login", "Username"))
        self.label_password.setText(_translate("Login", "Password"))
        self.pushButton_login.setText(_translate("Login", "Log in"))
        self.pushButton_forgotPassowrd.setText(_translate("Login", "Forgot Password"))
        self.menuback.setTitle(_translate("Login", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
