# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'systemmanagement1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def openInboxPage(self):
        from InboxPage import Ui_InboxPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InboxPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomePage2(self):
        from HomePage2 import Ui_HomePage2
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomePage2()
        self.ui.setupUi(self.window)

        self.window.show()

    def openGroupPage(self):
        from GroupPage import Ui_GroupPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GroupPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openPrevPage(self):
        from HomePageSU import Ui_HomePageSU
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomePageSU()
        self.ui.setupUi(self.window)
        self.window.show()

    def openNextPage(self):
        from applicationpage1 import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
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
        self.spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.spinBox.setGeometry(QtCore.QRect(140, 70, 121, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 121, 21))
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(280, 50, 121, 21))
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setObjectName("label_4")
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_4)
        self.spinBox_2.setGeometry(QtCore.QRect(280, 70, 121, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.members = QtWidgets.QLabel(self.frame_4)
        self.members.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.members.setFrameShape(QtWidgets.QFrame.Panel)
        self.members.setFrameShadow(QtWidgets.QFrame.Raised)
        self.members.setObjectName("members")
        self.comboBox = QtWidgets.QComboBox(self.frame_4)
        self.comboBox.setGeometry(QtCore.QRect(20, 70, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 120, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
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
        self.pushButton_2.setObjectName("application")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 50, 93, 28))
        self.pushButton_4.setObjectName("home")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 100, 93, 28))
        self.pushButton_5.setObjectName("imbox")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 150, 93, 28))
        self.pushButton_6.setObjectName("group")

        self.pushButton.raise_()
        self.pushButton.clicked.connect(self.openPrevPage)
        self.pushButton.clicked.connect(MainWindow.close)

        self.pushButton_2.clicked.connect(self.openNextPage)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_6.clicked.connect(self.openGroupPage)
        self.pushButton_6.clicked.connect(MainWindow.close)
        self.pushButton_5.clicked.connect(self.openInboxPage)
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.pushButton_4.clicked.connect(self.openHomePage2)
        self.pushButton_4.clicked.connect(MainWindow.close)


        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 141, 20))
        self.label_5.setObjectName("label_5")


        self.label.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label.setText(_translate("MainWindow", "                                 Team-Up"))
        self.label_2.setText(_translate("MainWindow", "System Management Page(Super User Only)"))
        self.pushButton_3.setText(_translate("MainWindow", "check profile"))
        self.label_3.setText(_translate("MainWindow", "increase rep score"))
        self.label_4.setText(_translate("MainWindow", "decrease rep score"))
        self.members.setText(_translate("MainWindow", "member list"))
        self.comboBox.setItemText(1, _translate("MainWindow", "member1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "member2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "member3"))
        self.comboBox.setItemText(4, _translate("MainWindow", "member4"))
        self.pushButton.setText(_translate("MainWindow", "<<"))
        self.pushButton_7.setText(_translate("MainWindow", "confirm"))
        self.pushButton_2.setText(_translate("MainWindow", "Application page >>"))
        self.pushButton_4.setText(_translate("MainWindow", "home page"))
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
