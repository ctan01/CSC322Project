from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd

class Ui_CreateGroupPage(object):
    def createGroup(self):
        msg = QMessageBox()
        df = pd.read_csv('GroupData.csv')
        groupID = (len(df.index) + 1)
        print(groupID)
        df.loc[groupID + 1, 'GroupID'] = groupID
        df.loc[groupID + 1, 'GroupName'] = self.lineEdit_GroupName.text()
        df.loc[groupID + 1, 'Description'] = self.lineEdit_GroupDescription.text()
        df.loc[groupID + 1, 'Member0'] = self.comboBox_InviteMember1.currentText()
        df.loc[groupID + 1, 'Member1'] = self.comboBox_InviteMember2.currentText()
        df.loc[groupID + 1, 'Member2'] = self.comboBox_InviteMember3.currentText()
        df.loc[groupID + 1, 'Member3'] = self.comboBox_InviteMember4.currentText()
        df.loc[groupID + 1, 'Member4'] = self.comboBox_InviteMember5.currentText()
        df.loc[groupID + 1, 'Member5'] = self.comboBox_InviteMember6.currentText()
        df.loc[groupID + 1, 'Member6'] = self.comboBox_InviteMember7.currentText()
        df.loc[groupID + 1, 'Member7'] = self.comboBox_InviteMember8.currentText()
        df.loc[groupID + 1, 'CurrentGroup'] = 0
        """print(self.lineEdit_GroupDescription.text())
        print(self.comboBox_InviteMember1.currentText())
        new_row = {'GroupID': (len(df.index) + 1),
                   'GroupName': self.lineEdit_GroupName.text(),
                   'Description': self.lineEdit_GroupDescription.text(),
                   'Member0': self.comboBox_InviteMember1.currentText(),
                   'Member1': self.comboBox_InviteMember2.currenttext(),
                   'Member2': self.comboBox_InviteMember3.currenttext(),
                   'Member3': self.comboBox_InviteMember4.currenttext(),
                   'Member4': self.comboBox_InviteMember5.currenttext(),
                   'Member5': self.comboBox_InviteMember6.currenttext(),
                   'Member6': self.comboBox_InviteMember7.currenttext(),
                   'Member7': self.comboBox_InviteMember8.currenttext(),
                   'currentGroup': 0
                   }
        df = df.append(new_row, ignore_index=True)"""
        # df.loc[1, 'GroupName'] = 3
        df.to_csv('GroupData.csv', index=False)

        msg.setText('Group created and Invitation sent')
        msg.exec_()

    def setupUi(self, CreateGroupPage):
        df = pd.read_csv('UserData.csv')
        count = df.shape[0]
        CreateGroupPage.resize(441, 776)
        self.centralwidget = QtWidgets.QWidget(CreateGroupPage)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Confirm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Confirm.setGeometry(QtCore.QRect(300, 660, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_Confirm.setFont(font)
        self.pushButton_Confirm.setObjectName("pushButton_Confirm")

        self.pushButton_Confirm.clicked.connect(self.createGroup) # button click with save data into csv

        self.label_GroupName = QtWidgets.QLabel(self.centralwidget)
        self.label_GroupName.setGeometry(QtCore.QRect(40, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_GroupName.setFont(font)
        self.label_GroupName.setObjectName("label_GroupName")
        self.label_GroupDescription = QtWidgets.QLabel(self.centralwidget)
        self.label_GroupDescription.setGeometry(QtCore.QRect(10, 80, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_GroupDescription.setFont(font)
        self.label_GroupDescription.setObjectName("label_GroupDescription")
        self.label_InviteMember1 = QtWidgets.QLabel(self.centralwidget)
        self.label_InviteMember1.setGeometry(QtCore.QRect(20, 320, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_InviteMember1.setFont(font)
        self.label_InviteMember1.setObjectName("label_InviteMember1")
        self.lineEdit_GroupName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_GroupName.setGeometry(QtCore.QRect(140, 30, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_GroupName.setFont(font)
        self.lineEdit_GroupName.setObjectName("lineEdit_GroupName")
        self.lineEdit_GroupDescription = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_GroupDescription.setGeometry(QtCore.QRect(140, 80, 281, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_GroupDescription.setFont(font)
        self.lineEdit_GroupDescription.setObjectName("lineEdit_GroupDescription")
        self.comboBox_InviteMember1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_InviteMember1.setGeometry(QtCore.QRect(140, 320, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_InviteMember1.setFont(font)
        self.comboBox_InviteMember1.setObjectName("comboBox_InviteMember1")
        self.comboBox_InviteMember2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_InviteMember2.setGeometry(QtCore.QRect(140, 360, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_InviteMember2.setFont(font)
        self.comboBox_InviteMember2.setObjectName("comboBox_InviteMember2")
        self.label_InviteMember2 = QtWidgets.QLabel(self.centralwidget)
        self.label_InviteMember2.setGeometry(QtCore.QRect(20, 360, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_InviteMember2.setFont(font)
        self.label_InviteMember2.setObjectName("label_InviteMember2")
        self.comboBox_InviteMember3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_InviteMember3.setGeometry(QtCore.QRect(140, 400, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_InviteMember3.setFont(font)
        self.comboBox_InviteMember3.setObjectName("comboBox_InviteMember3")
        self.label_InviteMember3 = QtWidgets.QLabel(self.centralwidget)
        self.label_InviteMember3.setGeometry(QtCore.QRect(20, 400, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_InviteMember3.setFont(font)
        self.label_InviteMember3.setObjectName("label_InviteMember3")
        self.comboBox_InviteMember4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_InviteMember4.setGeometry(QtCore.QRect(140, 440, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_InviteMember4.setFont(font)
        self.comboBox_InviteMember4.setObjectName("comboBox_InviteMember4")
        self.label_InviteMember4 = QtWidgets.QLabel(self.centralwidget)
        self.label_InviteMember4.setGeometry(QtCore.QRect(20, 440, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_InviteMember4.setFont(font)
        self.label_InviteMember4.setObjectName("label_InviteMember4")
        self.comboBox_InviteMember5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_InviteMember5.setGeometry(QtCore.QRect(140, 480, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_InviteMember5.setFont(font)
        self.comboBox_InviteMember5.setObjectName("comboBox_InviteMember5")
        self.label_InviteMember5 = QtWidgets.QLabel(self.centralwidget)
        self.label_InviteMember5.setGeometry(QtCore.QRect(20, 480, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_InviteMember5.setFont(font)
        self.label_InviteMember5.setObjectName("label_InviteMember5")
        self.comboBox_InviteMember6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_InviteMember6.setGeometry(QtCore.QRect(140, 520, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_InviteMember6.setFont(font)
        self.comboBox_InviteMember6.setObjectName("comboBox_InviteMember6")
        self.label_InviteMember6 = QtWidgets.QLabel(self.centralwidget)
        self.label_InviteMember6.setGeometry(QtCore.QRect(20, 520, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_InviteMember6.setFont(font)
        self.label_InviteMember6.setObjectName("label_InviteMember6")
        self.comboBox_InviteMember7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_InviteMember7.setGeometry(QtCore.QRect(140, 560, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_InviteMember7.setFont(font)
        self.comboBox_InviteMember7.setObjectName("comboBox_InviteMember7")
        self.label_InviteMember7 = QtWidgets.QLabel(self.centralwidget)
        self.label_InviteMember7.setGeometry(QtCore.QRect(20, 560, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_InviteMember7.setFont(font)
        self.label_InviteMember7.setObjectName("label_InviteMember7")
        self.comboBox_InviteMember8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_InviteMember8.setGeometry(QtCore.QRect(140, 600, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox_InviteMember8.setFont(font)
        self.comboBox_InviteMember8.setObjectName("comboBox_InviteMember8")
        self.label_InviteMember8 = QtWidgets.QLabel(self.centralwidget)
        self.label_InviteMember8.setGeometry(QtCore.QRect(20, 600, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_InviteMember8.setFont(font)
        self.label_InviteMember8.setObjectName("label_InviteMember8")
        CreateGroupPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateGroupPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menubar.setObjectName("menubar")
        CreateGroupPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateGroupPage)
        self.statusbar.setObjectName("statusbar")
        CreateGroupPage.setStatusBar(self.statusbar)

        while count != -1:
            self.comboBox_InviteMember1.addItem("")
            count -= 1

        count = df.shape[0]

        while count != -1:
            self.comboBox_InviteMember2.addItem("")
            count -= 1

        count = df.shape[0]

        while count != -1:
            self.comboBox_InviteMember3.addItem("")
            count -= 1

        count = df.shape[0]

        while count != -1:
            self.comboBox_InviteMember4.addItem("")
            count -= 1

        count = df.shape[0]

        while count != -1:
            self.comboBox_InviteMember5.addItem("")
            count -= 1

        count = df.shape[0]

        while count != -1:
            self.comboBox_InviteMember6.addItem("")
            count -= 1

        count = df.shape[0]

        while count != -1:
            self.comboBox_InviteMember7.addItem("")
            count -= 1

        count = df.shape[0]

        while count != -1:
            self.comboBox_InviteMember8.addItem("")
            count -= 1

        self.retranslateUi(CreateGroupPage)
        QtCore.QMetaObject.connectSlotsByName(CreateGroupPage)

    def retranslateUi(self, CreateGroupPage):
        df = pd.read_csv('UserData.csv')
        combo_count = df.shape[0]
        i = 0
        _translate = QtCore.QCoreApplication.translate
        CreateGroupPage.setWindowTitle(_translate("CreateGroupPage", "MainWindow"))
        self.pushButton_Confirm.setText(_translate("CreateGroupPage", "Confirm"))
        self.label_GroupName.setText(_translate("CreateGroupPage", "Group Name:"))
        self.label_GroupDescription.setText(_translate("CreateGroupPage", "Group Description:"))
        self.label_InviteMember1.setText(_translate("CreateGroupPage", "Invite Member 1:"))
        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_InviteMember1.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0

        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_InviteMember2.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0

        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_InviteMember3.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0

        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_InviteMember4.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0

        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_InviteMember5.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0

        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_InviteMember6.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0

        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_InviteMember7.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0

        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_InviteMember8.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        self.label_InviteMember2.setText(_translate("CreateGroupPage", "Invite Member 2:"))
        self.label_InviteMember3.setText(_translate("CreateGroupPage", "Invite Member 3:"))
        self.label_InviteMember4.setText(_translate("CreateGroupPage", "Invite Member 4:"))
        self.label_InviteMember5.setText(_translate("CreateGroupPage", "Invite Member 5:"))
        self.label_InviteMember6.setText(_translate("CreateGroupPage", "Invite Member 6:"))
        self.label_InviteMember7.setText(_translate("CreateGroupPage", "Invite Member 7:"))
        self.label_InviteMember8.setText(_translate("CreateGroupPage", "Invite Member 8:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateGroupPage = QtWidgets.QMainWindow()
    ui = Ui_CreateGroupPage()
    ui.setupUi(CreateGroupPage)
    CreateGroupPage.show()
    sys.exit(app.exec_())
