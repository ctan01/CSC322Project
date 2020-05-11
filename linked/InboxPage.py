# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InboxPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ProfilePage import Ui_profilePage


class Ui_InboxPage(object):
    def logout(self):
        from HomePage import Ui_HomePage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomePage()
        self.ui.setupUi(self.window)
        self.window.show()


    def openGroupPage(self):
        from GroupPage import Ui_GroupPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GroupPage()
        self.ui.setupUi(self.window)
        self.window.show()


    def openProfileWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profilePage()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 846)
        self.InboxDashboard = QtWidgets.QWidget(MainWindow)
        self.InboxDashboard.setObjectName("InboxDashboard")
        self.NavigationSideBar = QtWidgets.QGroupBox(self.InboxDashboard)
        self.NavigationSideBar.setGeometry(QtCore.QRect(590, 0, 451, 61))
        self.NavigationSideBar.setObjectName("NavigationSideBar")
        self.HomeButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.HomeButton.setGeometry(QtCore.QRect(120, 20, 101, 28))
        self.HomeButton.setObjectName("HomeButton")
        self.ProfileButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.ProfileButton.setGeometry(QtCore.QRect(10, 20, 101, 28))
        self.ProfileButton.setObjectName("ProfileButton")

        self.ProfileButton.clicked.connect(self.openProfileWindow)


        self.LogOUt = QtWidgets.QPushButton(self.NavigationSideBar)
        self.LogOUt.setGeometry(QtCore.QRect(340, 20, 101, 28))
        self.LogOUt.setObjectName("LogOUt")
        self.LogOUt.clicked.connect(self.logout)
        self.pushButton_LogOUt.clicked.connect(self.logout)
        self.pushButton_LogOUt.clicked.connect(MainWindow.close)

        self.GroupsButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.GroupsButton.setGeometry(QtCore.QRect(230, 20, 101, 28))
        self.GroupsButton.setObjectName("GroupsButton")
        self.GroupsButton.clicked.connect(self.openGroupPage)
        self.GroupsButton.clicked.connect(MainWindow.close)
        self.groupBox_2 = QtWidgets.QGroupBox(self.InboxDashboard)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 211, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.textEdit.setObjectName("textEdit")
        self.HomeButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.HomeButton_2.setGeometry(QtCore.QRect(140, 20, 61, 31))
        self.HomeButton_2.setObjectName("HomeButton_2")
        self.listWidget = QtWidgets.QListWidget(self.InboxDashboard)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 1031, 711))
        self.listWidget.setObjectName("listWidget")
        self.InvitationMessage = QtWidgets.QWidget(self.InboxDashboard)
        self.InvitationMessage.setGeometry(QtCore.QRect(20, 80, 1011, 101))
        self.InvitationMessage.setObjectName("InvitationMessage")
        self.textBrowser = QtWidgets.QTextBrowser(self.InvitationMessage)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 991, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.InvitationMessage)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.InvitationMessage)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 70, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.InvitationMessage_2 = QtWidgets.QWidget(self.InboxDashboard)
        self.InvitationMessage_2.setGeometry(QtCore.QRect(20, 190, 1011, 101))
        self.InvitationMessage_2.setObjectName("InvitationMessage_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.InvitationMessage_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 991, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.InvitationMessage_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 70, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.InvitationMessage_2)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 70, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.NotificationWidget = QtWidgets.QWidget(self.InboxDashboard)
        self.NotificationWidget.setGeometry(QtCore.QRect(20, 300, 1011, 101))
        self.NotificationWidget.setObjectName("NotificationWidget")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.NotificationWidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 991, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.NotificationWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 70, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.PlainNotification = QtWidgets.QWidget(self.InboxDashboard)
        self.PlainNotification.setGeometry(QtCore.QRect(20, 410, 1011, 81))
        self.PlainNotification.setObjectName("PlainNotification")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.PlainNotification)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 10, 991, 61))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.InboxDashboard)
        self.pushButton_6.setGeometry(QtCore.QRect(740, 740, 141, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.InboxDashboard)
        self.pushButton_7.setGeometry(QtCore.QRect(890, 740, 141, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.InboxDashboard)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NavigationSideBar.setTitle(_translate("MainWindow", "Navigation"))
        self.HomeButton.setText(_translate("MainWindow", "Home"))
        self.ProfileButton.setText(_translate("MainWindow", "Profile"))
        self.LogOUt.setText(_translate("MainWindow", "LogOut"))
        self.GroupsButton.setText(_translate("MainWindow", "Groups"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Search"))
        self.HomeButton_2.setText(_translate("MainWindow", "Search"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Invitation to Join Beach Clean Up</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Accept"))
        self.pushButton_2.setText(_translate("MainWindow", "Decline"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Invitation to Join Animal Shelter Volunteer Group</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Accept"))
        self.pushButton_4.setText(_translate("MainWindow", "Decline"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Community Garden Set Up a Meeting Time Poll</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Go to Page"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">You\'ve Been Issued a Warning by the Members of Community Garden</span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Accept All Invitations"))
        self.pushButton_7.setText(_translate("MainWindow", "Decline All Invitations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InboxPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
