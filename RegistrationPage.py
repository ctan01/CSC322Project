from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd


class Ui_registrationPage(object):
    def submit(self):
        # record data in to db
        # global skill1, skill2, skill3, skill4, skill5, skill6, skill7, skill8, skill9,
        # skill10, skill11, interest1, interest2, interest3, interest4, interest5, interest6, interest8, interest7,
        # interest9, interest10, interest11
        df = pd.read_csv('UserData.csv')
        if self.checkBox_interest1.isChecked():
            interest1 = self.checkBox_interest1.text()
        else:
            interest1 = None

        if self.checkBox_interest2.isChecked():
            interest2 = self.checkBox_interest2.text()
        else:
            interest2 = None

        if self.checkBox_interest3.isChecked():
            interest3 = self.checkBox_interest3.text()
        else:
            interest3 = None

        if self.checkBox_interest4.isChecked():
            interest4 = self.checkBox_interest4.text()
        else:
            interest4 = None

        if self.checkBox_interest5.isChecked():
            interest5 = self.checkBox_interest5.text()
        else:
            interest5 = None

        if self.checkBox_interest6.isChecked():
            interest6 = self.checkBox_interest6.text()
        else:
            interest6 = None

        if self.checkBox_interest7.isChecked():
            interest7 = self.checkBox_interest7.text()
        else:
            interest7 = None

        if self.checkBox_interest8.isChecked():
            interest8 = self.checkBox_interest8.text()
        else:
            interest8 = None

        if self.checkBox_interest9.isChecked():
            interest9 = self.checkBox_interest9.text()
        else:
            interest9 = None

        if self.checkBox_interest10.isChecked():
            interest10 = self.checkBox_interest10.text()
        else:
            interest10 = None

        if self.checkBox_interest11.isChecked():
            interest11 = self.checkBox_interest11.text()
        else:
            interest11 = None

        if self.checkBox_skill1.isChecked():
            skill1 = self.checkBox_skill1.text()
        else:
            skill1 = None

        if self.checkBox_skill2.isChecked():
            skill2 = self.checkBox_skill2.text()
        else:
            skill2 = None

        if self.checkBox_skill3.isChecked():
            skill3 = self.checkBox_skill3.text()
        else:
            skill3 = None

        if self.checkBox_skill4.isChecked():
            skill4 = self.checkBox_skill4.text()
        else:
            skill4 = None

        if self.checkBox_skill5.isChecked():
            skill5 = self.checkBox_skill5.text()
        else:
            skill5 = None

        if self.checkBox_skill6.isChecked():
            skill6 = self.checkBox_skill6.text()
        else:
            skill6 = None

        if self.checkBox_skill7.isChecked():
            skill7 = self.checkBox_skill7.text()
        else:
            skill7 = None

        if self.checkBox_skill8.isChecked():
            skill8 = self.checkBox_skill8.text()
        else:
            skill8 = None

        if self.checkBox_skill9.isChecked():
            skill9 = self.checkBox_skill9.text()
        else:
            skill9 = None

        if self.checkBox_skill10.isChecked():
            skill10 = self.checkBox_skill10.text()
        else:
            skill10 = None

        if self.checkBox_skill11.isChecked():
            skill11 = self.checkBox_skill11.text()
        else:
            skill11 = None


        new_row = {'UserID': len(df.index),
                   'First_Name': self.lineEdit_firstName.text(),
                   'Last_Name': self.lineEdit_lastName.text(),
                   'Email': self.lineEdit_email.text(),
                   'Reference1': self.lineEdit_reference1.text(),
                   'Reference2': self.lineEdit_reference2.text(),
                   'Username': self.lineEdit_username.text(),
                   'Password': self.lineEdit_password.text(),
                   'Skills1': skill1,
                   'Skills2': skill2,
                   'Skills3': skill3,
                   'Skills4': skill4,
                   'Skills5': skill5,
                   'Skills6': skill6,
                   'Skills7': skill7,
                   'Skills8': skill8,
                   'Skills9': skill9,
                   'Skills10': skill10,
                   'Skills11': skill11,
                   'Interests1': interest1,
                   'Interests2': interest2,
                   'Interests3': interest3,
                   'Interests4': interest4,
                   'Interests5': interest5,
                   'Interests6': interest6,
                   'Interests7': interest7,
                   'Interests8': interest8,
                   'Interests9': interest9,
                   'Interests10': interest10,
                   'Interests11': interest11
                   }
        df = df.append(new_row, ignore_index=True)
        df.to_csv('UserData.csv', index=False)

        # pop up window
        msg = QMessageBox()
        msg.setWindowTitle("Registration Status")
        msg.setText("Registration form submitted!")
        x = msg.exec_()

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
        self.label_references = QtWidgets.QLabel(self.centralwidget)
        self.label_references.setGeometry(QtCore.QRect(20, 190, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_references.setFont(font)
        self.label_references.setObjectName("label_references")
        self.label_interests = QtWidgets.QLabel(self.centralwidget)
        self.label_interests.setGeometry(QtCore.QRect(20, 270, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_interests.setFont(font)
        self.label_interests.setObjectName("label_interests")
        self.label_skills = QtWidgets.QLabel(self.centralwidget)
        self.label_skills.setGeometry(QtCore.QRect(20, 400, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_skills.setFont(font)
        self.label_skills.setObjectName("label_skills")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(20, 540, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(20, 590, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.pushButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(170, 650, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setObjectName("pushButton_submit")

        self.pushButton_submit.clicked.connect(self.submit)  # connect button to pop up window function

        self.checkBox_interest2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest2.setGeometry(QtCore.QRect(170, 300, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest2.setFont(font)
        self.checkBox_interest2.setObjectName("checkBox_interest2")
        self.checkBox_interest1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest1.setGeometry(QtCore.QRect(80, 300, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest1.setFont(font)
        self.checkBox_interest1.setObjectName("checkBox_interest1")
        self.checkBox_skill1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill1.setGeometry(QtCore.QRect(80, 430, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill1.setFont(font)
        self.checkBox_skill1.setObjectName("checkBox_skill1")
        self.checkBox_interest3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest3.setGeometry(QtCore.QRect(260, 300, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest3.setFont(font)
        self.checkBox_interest3.setObjectName("checkBox_interest3")
        self.checkBox_interest4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest4.setGeometry(QtCore.QRect(350, 300, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest4.setFont(font)
        self.checkBox_interest4.setObjectName("checkBox_interest4")
        self.checkBox_interest5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest5.setGeometry(QtCore.QRect(80, 330, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest5.setFont(font)
        self.checkBox_interest5.setObjectName("checkBox_interest5")
        self.checkBox_interest6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest6.setGeometry(QtCore.QRect(170, 330, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest6.setFont(font)
        self.checkBox_interest6.setObjectName("checkBox_interest6")
        self.checkBox_interest7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest7.setGeometry(QtCore.QRect(260, 330, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest7.setFont(font)
        self.checkBox_interest7.setObjectName("checkBox_interest7")
        self.checkBox_interest8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest8.setGeometry(QtCore.QRect(350, 330, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest8.setFont(font)
        self.checkBox_interest8.setObjectName("checkBox_interest8")
        self.checkBox_skill2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill2.setGeometry(QtCore.QRect(170, 430, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill2.setFont(font)
        self.checkBox_skill2.setObjectName("checkBox_skill2")
        self.checkBox_skill5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill5.setGeometry(QtCore.QRect(80, 460, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill5.setFont(font)
        self.checkBox_skill5.setObjectName("checkBox_skill5")
        self.checkBox_skill3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill3.setGeometry(QtCore.QRect(260, 430, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill3.setFont(font)
        self.checkBox_skill3.setObjectName("checkBox_skill3")
        self.checkBox_skill6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill6.setGeometry(QtCore.QRect(190, 460, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill6.setFont(font)
        self.checkBox_skill6.setObjectName("checkBox_skill6")
        self.checkBox_skill4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill4.setGeometry(QtCore.QRect(350, 430, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill4.setFont(font)
        self.checkBox_skill4.setObjectName("checkBox_skill4")
        self.checkBox_skill7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill7.setGeometry(QtCore.QRect(310, 460, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill7.setFont(font)
        self.checkBox_skill7.setObjectName("checkBox_skill7")
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
        self.lineEdit_reference1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_reference1.setGeometry(QtCore.QRect(100, 190, 291, 21))
        self.lineEdit_reference1.setObjectName("lineEdit_reference1")
        self.lineEdit_reference2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_reference2.setGeometry(QtCore.QRect(100, 230, 291, 21))
        self.lineEdit_reference2.setObjectName("lineEdit_reference2")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(100, 540, 291, 21))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(100, 590, 291, 21))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.checkBox_skill8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill8.setGeometry(QtCore.QRect(80, 490, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill8.setFont(font)
        self.checkBox_skill8.setObjectName("checkBox_skill8")
        self.checkBox_skill9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill9.setGeometry(QtCore.QRect(170, 490, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill9.setFont(font)
        self.checkBox_skill9.setObjectName("checkBox_skill9")
        self.checkBox_skill11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill11.setGeometry(QtCore.QRect(350, 490, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill11.setFont(font)
        self.checkBox_skill11.setObjectName("checkBox_skill11")
        self.checkBox_skill10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_skill10.setGeometry(QtCore.QRect(260, 490, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_skill10.setFont(font)
        self.checkBox_skill10.setObjectName("checkBox_skill10")
        self.checkBox_interest9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest9.setGeometry(QtCore.QRect(80, 360, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest9.setFont(font)
        self.checkBox_interest9.setObjectName("checkBox_interest9")
        self.checkBox_interest11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest11.setGeometry(QtCore.QRect(300, 360, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest11.setFont(font)
        self.checkBox_interest11.setObjectName("checkBox_interest11")
        self.checkBox_interest10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_interest10.setGeometry(QtCore.QRect(170, 360, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.checkBox_interest10.setFont(font)
        self.checkBox_interest10.setObjectName("checkBox_interest10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 270, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 400, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        registrationPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(registrationPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
        self.menubar.setObjectName("menubar")
        registrationPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(registrationPage)
        self.statusbar.setObjectName("statusbar")
        registrationPage.setStatusBar(self.statusbar)

        self.retranslateUi(registrationPage)
        QtCore.QMetaObject.connectSlotsByName(registrationPage)

    def retranslateUi(self, registrationPage):
        _translate = QtCore.QCoreApplication.translate
        registrationPage.setWindowTitle(_translate("registrationPage", "MainWindow"))
        self.label_lastname.setText(_translate("registrationPage", "Last name:"))
        self.label_email.setText(_translate("registrationPage", "Email:"))
        self.label_references.setText(_translate("registrationPage", "References:"))
        self.label_interests.setText(_translate("registrationPage", "Interests:"))
        self.label_skills.setText(_translate("registrationPage", "Skill sets:"))
        self.label_username.setText(_translate("registrationPage", "Username:"))
        self.label_password.setText(_translate("registrationPage", "Password:"))
        self.pushButton_submit.setText(_translate("registrationPage", "Submit"))
        self.checkBox_interest2.setText(_translate("registrationPage", "Reading"))
        self.checkBox_interest1.setText(_translate("registrationPage", "Education"))
        self.checkBox_skill1.setText(_translate("registrationPage", "Organizing"))
        self.checkBox_interest3.setText(_translate("registrationPage", "Coding"))
        self.checkBox_interest4.setText(_translate("registrationPage", "Environment"))
        self.checkBox_interest5.setText(_translate("registrationPage", "Sports"))
        self.checkBox_interest6.setText(_translate("registrationPage", "Design"))
        self.checkBox_interest7.setText(_translate("registrationPage", "Finance"))
        self.checkBox_interest8.setText(_translate("registrationPage", "Technology"))
        self.checkBox_skill2.setText(_translate("registrationPage", "Gardening"))
        self.checkBox_skill5.setText(_translate("registrationPage", "Teaching"))
        self.checkBox_skill3.setText(_translate("registrationPage", "Cooking"))
        self.checkBox_skill6.setText(_translate("registrationPage", "Graphic Design"))
        self.checkBox_skill4.setText(_translate("registrationPage", "Excel"))
        self.checkBox_skill7.setText(_translate("registrationPage", "Accounting"))
        self.label_firstname.setText(_translate("registrationPage", "First name:"))
        self.checkBox_skill8.setText(_translate("registrationPage", "Python"))
        self.checkBox_skill9.setText(_translate("registrationPage", "Sewing"))
        self.checkBox_skill11.setText(_translate("registrationPage", "NetWorking"))
        self.checkBox_skill10.setText(_translate("registrationPage", "Carpentry"))
        self.checkBox_interest9.setText(_translate("registrationPage", "Kids"))
        self.checkBox_interest11.setText(_translate("registrationPage", "Public Welfare"))
        self.checkBox_interest10.setText(_translate("registrationPage", "Family Activities"))
        self.label.setText(_translate("registrationPage", "Please choose at most 5 interests"))
        self.label_2.setText(_translate("registrationPage", "Please choose at most 5 skill sets"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    registrationPage = QtWidgets.QMainWindow()
    ui = Ui_registrationPage()
    ui.setupUi(registrationPage)
    registrationPage.show()
    sys.exit(app.exec_())
