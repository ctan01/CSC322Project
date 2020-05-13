# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'systemmanagement1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_MainWindow(object):
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

    def findUser(self):
        df = pd.read_csv('UserData.csv')
        username = str(self.comboBox.currentText())
        rownum = df[df['Username'] == username].index[0]
        df.loc[0, 'temp'] = username
        df.loc[1, 'temp'] = rownum
        df.to_csv('UserData.csv', index=False)

    def openMemberPage(self):              # USER ID PARAMETERS
        from memberpage1 import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openApplicationPage(self):              # USER ID PARAMETERS
        from applicationpage1 import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomePageSU(self):
        from HomePageSU import Ui_HomePageSU
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomePageSU()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        df = pd.read_csv('UserData.csv')
        count = df.shape[0]

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 50, 551, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(70, 90, 441, 231))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 180, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")


        self.members = QtWidgets.QLabel(self.frame_4)
        self.members.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.members.setFrameShape(QtWidgets.QFrame.Panel)
        self.members.setFrameShadow(QtWidgets.QFrame.Raised)
        self.members.setObjectName("members")
        self.comboBox = QtWidgets.QComboBox(self.frame_4)
        self.comboBox.setGeometry(QtCore.QRect(20, 70, 91, 22))
        self.comboBox.setObjectName("comboBox")

        while count != -1:
            self.comboBox.addItem("")
            count -= 1

        self.pushButton_3.clicked.connect(self.findUser)

        self.frame_4.raise_()
        self.label_2.raise_()
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 49, 141, 461))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(690, 50, 141, 461))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 420, 131, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3.clicked.connect(self.openMemberPage)
        self.pushButton_3.clicked.connect(MainWindow.close)


        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 100, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 150, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 141, 20))
        self.label_5.setObjectName("label_5")

        self.pushButton.raise_()
        self.pushButton.clicked.connect(self.openHomePageSU)
        self.pushButton.clicked.connect(MainWindow.close)

        self.pushButton_2.clicked.connect(self.openApplicationPage)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.pushButton_6.clicked.connect(self.openGroupPage)
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.openInboxPage)
        self.pushButton_5.clicked.connect(MainWindow.close)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        df = pd.read_csv('UserData.csv')
        count = df.shape[0]
        i = 0
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "<<"))
        self.label.setText(_translate("MainWindow", "                                 Team-Up"))
        self.label_2.setText(_translate("MainWindow", "System Management Page(Super User Only)"))
        self.pushButton_3.setText(_translate("MainWindow", "check profile"))
        self.pushButton_2.setText(_translate("MainWindow", "application page >>"))
        self.members.setText(_translate("MainWindow", "MemberList"))
        while count != 0:
            self.comboBox.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
            i += 1
            count -= 1



        self.pushButton_5.setText(_translate("MainWindow", "inbox page"))
        self.pushButton_6.setText(_translate("MainWindow", "group page"))
        self.label_5.setText(_translate("MainWindow", "         Navigation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
