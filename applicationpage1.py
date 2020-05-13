# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'applicationpage1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    username = None

    def openPrevPage(self):
        from systemmanagement1 import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openInboxPage(self):
        from InboxPage import Ui_InboxPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InboxPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openGroupPage(self):
        from GroupPage import Ui_GroupPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GroupPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomePageSU(self):
        from HomePageSU import Ui_HomePageSU
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomePageSU()
        self.ui.setupUi(self.window)
        self.window.show()

    def pressApprove(self):
        from initialRepScore1 import Ui_reputationScore
        Ui_MainWindow.username = str(self.comboBox.currentText())
        df = pd.read_csv('UserData.csv')
        username = Ui_MainWindow.username
        rownum = df[df['Username'] == username].index[0]
        df.loc[0, 'temp'] = rownum
        df.to_csv('UserData.csv', index=False)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_reputationScore()
        self.ui.setupUi(self.window)
        self.window.show()

    def pressDecline(self):
        df = pd.read_csv('UserData.csv')
        Ui_MainWindow.username = str(self.comboBox.currentText())
        username = Ui_MainWindow.username
        rownum = df[df['Username'] == username].index[0]
        df = df.drop(rownum)
        df.to_csv('UserData.csv', index=False)
        msg = QMessageBox()
        msg.setWindowTitle("Change setting")
        msg.setText("DECLINED!")
        x = msg.exec_()

    def setupUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        df = pd.read_csv('UserData.csv')
        count = df.shape[0]
        #count = (df['Status'] == 'visitor').sum()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 100, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(1)
        self.label_2.setMidLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 420, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 420, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(580, 70, 221, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 60, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 200, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 320, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 150, 321, 41))
        self.comboBox.setObjectName("comboBox")
        i = 0
        while count != 0:
            if df.at[i, 'Status'] == 'visitor':
                self.comboBox.addItem(df.at[i, 'Username'])
                count -= 1
                i += 1
            else:
                count -= 1
                i += 1

        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_2.clicked.connect(self.pressApprove)

        self.pushButton_2.clicked.connect(MainWindow.close)

        self.pushButton_3.clicked.connect(self.pressDecline)
        self.pushButton_3.clicked.connect(self.openPrevPage)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.pushButton_4.clicked.connect(self.openHomePageSU)
        self.pushButton_4.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.openInboxPage)
        self.pushButton_6.clicked.connect(self.openGroupPage)
        self.pushButton.clicked.connect(self.openPrevPage)
        self.pushButton.clicked.connect(MainWindow.close)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "<<"))
        self.label.setText(_translate("MainWindow", "                           Team-Up"))
        self.label_2.setText(_translate("MainWindow", "applicant list"))
        self.pushButton_2.setText(_translate("MainWindow", "approve"))
        self.pushButton_3.setText(_translate("MainWindow", "decline"))
        self.pushButton_4.setText(_translate("MainWindow", "home page"))  # connect the button to home page 2
        self.pushButton_5.setText(_translate("MainWindow", "inbox page"))
        self.pushButton_6.setText(_translate("MainWindow", "group page"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
