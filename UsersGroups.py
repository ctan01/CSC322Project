from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UsersGroupsPage(object):
    def openInboxPage(self):                # USERID PARAMETERS
        from InboxPage import Ui_InboxPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InboxPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openProfilePage(self):              # USERID PARAMETERS
        from ProfilePage import Ui_profilePage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profilePage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCreatePostPage(self):           # GROUPID PARAMETERS    
        from CreatePost import Ui_CreatePost
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreatePost()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCreateMeetUpPoll(self):         # POP UP WINDOW 
        from CreateMeetUpPoll import Ui_MeetUpPoll
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MeetUpPoll()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSearchWindow(self):             # Might have to carry other parameters, such as input of search
        from SearchPage import Ui_SearchPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SearchPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openUsersGroups(self):              # USER ID PARAMETERS
        from UsersGroups import Ui_UsersGroupsPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UsersGroupsPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHomePage(self):
        from HomePage2 import Ui_HomePage2
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HomePage2()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, UsersGroups):
        UsersGroups.setObjectName("UsersGroups")
        UsersGroups.resize(1233, 788)
        self.centralwidget = QtWidgets.QWidget(UsersGroups)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(210, 70, 791, 651))
        self.groupBox.setObjectName("groupBox")

        self.Match1 = QtWidgets.QWidget(self.groupBox)
        self.Match1.setGeometry(QtCore.QRect(10, 20, 771, 121))
        self.Match1.setObjectName("Match1")
        self.textBrowser = QtWidgets.QTextBrowser(self.Match1)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 751, 61))
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton = QtWidgets.QPushButton(self.Match1)
        self.pushButton.setGeometry(QtCore.QRect(560, 80, 201, 28))
        self.pushButton.setObjectName("pushButton")

        self.Match1_2 = QtWidgets.QWidget(self.groupBox)
        self.Match1_2.setGeometry(QtCore.QRect(10, 150, 771, 121))
        self.Match1_2.setObjectName("Match1_2")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Match1_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 751, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.Match1_2)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 80, 201, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.Match1_3 = QtWidgets.QWidget(self.groupBox)
        self.Match1_3.setGeometry(QtCore.QRect(10, 280, 771, 121))
        self.Match1_3.setObjectName("Match1_3")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.Match1_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 751, 61))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.pushButton_3 = QtWidgets.QPushButton(self.Match1_3)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 80, 201, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 211, 61))
        self.groupBox_2.setObjectName("groupBox_2")

        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.textEdit.setObjectName("textEdit")

        self.HomeButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.HomeButton_2.setGeometry(QtCore.QRect(140, 20, 61, 31))
        self.HomeButton_2.setObjectName("HomeButton_2")

        self.NavigationSideBar = QtWidgets.QGroupBox(self.centralwidget)
        self.NavigationSideBar.setGeometry(QtCore.QRect(770, 0, 451, 61))
        self.NavigationSideBar.setObjectName("NavigationSideBar")

        self.HomeButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.HomeButton.setGeometry(QtCore.QRect(120, 20, 101, 28))
        self.HomeButton.setObjectName("HomeButton")
        self.HomeButton.clicked.connect(self.openHomePage)
        self.HomeButton.clicked.connect(UsersGroups.close)

        self.ProfileButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.ProfileButton.setGeometry(QtCore.QRect(10, 20, 101, 28))
        self.ProfileButton.setObjectName("ProfileButton")
        self.ProfileButton.clicked.connect(self.openProfilePage)
        self.ProfileButton.clicked.connect(UsersGroups.close)

        self.LogOUt = QtWidgets.QPushButton(self.NavigationSideBar)
        self.LogOUt.setGeometry(QtCore.QRect(340, 20, 101, 28))
        self.LogOUt.setObjectName("LogOUt")
        self.LogOUt.clicked.connect(UsersGroups.close)

        self.InboxButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.InboxButton.setGeometry(QtCore.QRect(230, 20, 101, 28))
        self.InboxButton.setObjectName("InboxButton")
        self.InboxButton.clicked.connect(self.openInboxPage)
        self.InboxButton.clicked.connect(UsersGroups.close)

        UsersGroups.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UsersGroups)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1233, 26))
        self.menubar.setObjectName("menubar")
        UsersGroups.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UsersGroups)
        self.statusbar.setObjectName("statusbar")
        UsersGroups.setStatusBar(self.statusbar)

        self.retranslateUi(UsersGroups)
        QtCore.QMetaObject.connectSlotsByName(UsersGroups)

    def retranslateUi(self, UsersGroups):
        _translate = QtCore.QCoreApplication.translate
        UsersGroups.setWindowTitle(_translate("UsersGroups", "UsersGroups"))
        self.groupBox.setTitle(_translate("UsersGroups", "List of Groups"))
        self.textBrowser.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Community Garden</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Description</span></p></body></html>"))
        self.pushButton.setText(_translate("UsersGroups", "Go to Group Page"))
        self.textBrowser_2.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Roadside Litter Pick Up</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Description</span></p></body></html>"))
        self.pushButton_2.setText(_translate("UsersGroups", "Go to Group Page"))
        self.textBrowser_3.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Beach Clean Up</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Description</span></p></body></html>"))
        self.pushButton_3.setText(_translate("UsersGroups", "Go to Group Page"))
        self.groupBox_2.setTitle(_translate("UsersGroups", "Search"))
        self.textEdit.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Garden</span></p></body></html>"))
        self.HomeButton_2.setText(_translate("UsersGroups", "Search"))
        self.NavigationSideBar.setTitle(_translate("UsersGroups", "Navigation"))
        self.HomeButton.setText(_translate("UsersGroups", "Home"))
        self.ProfileButton.setText(_translate("UsersGroups", "Profile"))
        self.LogOUt.setText(_translate("UsersGroups", "LogOut"))
        self.InboxButton.setText(_translate("UsersGroups", "Inbox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UsersGroups = QtWidgets.QMainWindow()
    ui = Ui_UsersGroupsPage()
    ui.setupUi(UsersGroups)
    UsersGroups.show()
    sys.exit(app.exec_())
