from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd


class Ui_MainWindow(object):
    def submit(self):
        df = pd.read_csv('UserData.csv')
        index = df.at[1, 'temp']
        # record data in to db
        df = pd.read_csv('UserData.csv')
        if self.lineEdit_lastName.text() != "":
            df.loc[int(index), 'Last_Name'] = self.lineEdit_lastName.text()
        if self.lineEdit_firstName.text() != "":
            df.loc[int(index), 'First_Name'] = self.lineEdit_firstName.text()
        if self.lineEdit_email.text() != "":
            df.loc[int(index), 'Email'] = self.lineEdit_email.text()
        if self.lineEdit_status.text() != "":
            df.loc[int(index), 'Status'] = self.lineEdit_status.text()
        if self.lineEdit_reputation.text() != "":
            df.loc[int(index), 'Reputation_Score'] = self.lineEdit_reputation.text()
        df.to_csv('UserData.csv', index=False)

        # pop up window
        msg = QMessageBox()
        msg.setWindowTitle("Change setting")
        msg.setText("change has been submitted!")
        x = msg.exec_()

    def openPrevPage(self):
        from systemmanagement1 import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, registrationPage):
        registrationPage.setObjectName("registrationPage")
        registrationPage.resize(465, 799)
        self.centralwidget = QtWidgets.QWidget(registrationPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_lastname = QtWidgets.QLabel(self.centralwidget)
        self.label_lastname.setGeometry(QtCore.QRect(20, 90, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_lastname.setFont(font)
        self.label_lastname.setObjectName("label_lastname")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(20, 140, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")

        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(20, 190, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_username")
        self.label_reputation = QtWidgets.QLabel(self.centralwidget)
        self.label_reputation.setGeometry(QtCore.QRect(0, 240, 100, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_reputation.setFont(font)
        self.label_reputation.setObjectName("label_password")
        self.pushButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(170, 650, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setObjectName("pushButton_submit")

        self.pushButton_submit.clicked.connect(self.submit)  # connect button to pop up window function
        self.pushButton_submit.clicked.connect(registrationPage.close)
        self.label_firstname = QtWidgets.QLabel(self.centralwidget)
        self.label_firstname.setGeometry(QtCore.QRect(20, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_firstname.setFont(font)
        self.label_firstname.setObjectName("label_firstname")
        self.lineEdit_firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_firstName.setGeometry(QtCore.QRect(100, 40, 291, 21))
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.lineEdit_lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lastName.setGeometry(QtCore.QRect(100, 90, 291, 21))
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(100, 140, 291, 21))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_status = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_status.setGeometry(QtCore.QRect(100, 190, 291, 21))
        self.lineEdit_status.setObjectName("lineEdit_username")
        self.lineEdit_reputation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_reputation.setGeometry(QtCore.QRect(100, 240, 291, 21))
        self.lineEdit_reputation.setObjectName("lineEdit_password")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 270, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")

        registrationPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(registrationPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
        self.menubar.setObjectName("menubar")
        registrationPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(registrationPage)
        self.statusbar.setObjectName("statusbar")
        registrationPage.setStatusBar(self.statusbar)
        self.pushButton_submit.clicked.connect(self.openPrevPage)
        self.pushButton_submit.clicked.connect(registrationPage.close)
        self.retranslateUi(registrationPage)
        QtCore.QMetaObject.connectSlotsByName(registrationPage)

    def retranslateUi(self, registrationPage):
        _translate = QtCore.QCoreApplication.translate
        registrationPage.setWindowTitle(_translate("registrationPage", "MainWindow"))
        self.label_lastname.setText(_translate("registrationPage", "Last name:"))
        self.label_email.setText(_translate("registrationPage", "Email:"))
        self.label_status.setText(_translate("registrationPage", "Status:"))
        self.label_reputation.setText(_translate("registrationPage", "ReputationScore:"))
        self.pushButton_submit.setText(_translate("registrationPage", "Submit"))
        self.label_firstname.setText(_translate("registrationPage", "First name:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    registrationPage = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(registrationPage)
    registrationPage.show()
    sys.exit(app.exec_())
