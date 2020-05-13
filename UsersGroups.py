from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


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

        groupContents1 = [" ", " "]
        groupContents2 = [" ", " "]
        groupContents3 = [" ", " "]
        groupContents4 = [" ", " "]
        groupContents5 = [" ", " "]
        
        df = pd.read_csv('GroupData.csv')
        #GroupID,GroupName,Description,Post0,Post1,Post2,Post3,Member0,Member1,Member2,Member3,Member4,Member5,Member6,Member7,currentGroup
        dfcheck = pd.read_csv('UserData.csv')
        currentUserRow = dfcheck[dfcheck['CurrentUser'] == 1]
        currentUserID = currentUserRow['UserID'].iloc[0]
        groupName1 = currentUserRow['Group1'].iloc[0]
        groupName2 = currentUserRow['Group2'].iloc[0]
        groupName3 = currentUserRow['Group3'].iloc[0]
        groupName4 = currentUserRow['Group4'].iloc[0]
        groupName5 = currentUserRow['Group5'].iloc[0]
        for index, row in df.iterrows():
            if row['GroupName']== groupName1:
                groupContents1 = [row['GroupName'], row['Description']]
            if row['GroupName'] == groupName2:
                groupContents2 = [row['GroupName'], row['Description']]
            if row['GroupName'] == groupName3:
                groupContents3 = [row['GroupName'], row['Description']]
            if row['GroupName'] == groupName4:
                groupContents4 = [row['GroupName'], row['Description']]
            if row['GroupName'] == groupName5:
                groupContents5 = [row['GroupName'], row['Description']] 
        backup = "Join More Groups!"
        # CLEAR EMPTY BOXES 
        # MOVE TO BOTTOM
        checkempty = [0,0,0,0,0]
        if groupContents1[1] == " ":
            checkempty[0] = 1
        if groupContents2[1] == " ":
            checkempty[1] = 1
        if groupContents3[1] == " ":
            checkempty[2] = 1
        if groupContents4[1] == " ":
            checkempty[3] = 1
        if groupContents5[1] == " ":
            checkempty[4] = 1

        if checkempty[0] == 0:
            self.Match1 = QtWidgets.QWidget(self.groupBox)
            self.Match1.setGeometry(QtCore.QRect(10, 20, 771, 121))
            self.Match1.setObjectName("Match1")
            self.textBrowser = QtWidgets.QTextBrowser(self.Match1)
            self.textBrowser.setGeometry(QtCore.QRect(10, 10, 751, 61))
            self.textBrowser.setObjectName("textBrowser")

            self.GroupButton1 = QtWidgets.QPushButton(self.Match1)
            self.GroupButton1.setGeometry(QtCore.QRect(560, 80, 201, 28))
            self.GroupButton1.setObjectName("pushButton")

        if checkempty[1] == 0:
            self.Match1_2 = QtWidgets.QWidget(self.groupBox)
            self.Match1_2.setGeometry(QtCore.QRect(10, 150, 771, 121))
            self.Match1_2.setObjectName("Match1_2")

            self.textBrowser_2 = QtWidgets.QTextBrowser(self.Match1_2)
            self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 751, 61))
            self.textBrowser_2.setObjectName("textBrowser_2")

            self.GroupButton2 = QtWidgets.QPushButton(self.Match1_2)
            self.GroupButton2.setGeometry(QtCore.QRect(560, 80, 201, 28))
            self.GroupButton2.setObjectName("GroupButton2")

        if checkempty[2] == 0:
            self.Match1_3 = QtWidgets.QWidget(self.groupBox)
            self.Match1_3.setGeometry(QtCore.QRect(10, 280, 771, 121))
            self.Match1_3.setObjectName("Match1_3")

            self.textBrowser_3 = QtWidgets.QTextBrowser(self.Match1_3)
            self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 751, 61))
            self.textBrowser_3.setObjectName("textBrowser_3")

            self.GroupButton3 = QtWidgets.QPushButton(self.Match1_3)
            self.GroupButton3.setGeometry(QtCore.QRect(560, 80, 201, 28))
            self.GroupButton3.setObjectName("GroupButton3")

        if checkempty[3] == 0:
            self.Match1_4 = QtWidgets.QWidget(self.groupBox)
            self.Match1_4.setGeometry(QtCore.QRect(10, 410, 771, 121))
            self.Match1_4.setObjectName("Match1_4")

            self.textBrowser_4 = QtWidgets.QTextBrowser(self.Match1_4)
            self.textBrowser_4.setGeometry(QtCore.QRect(10, 10, 751, 61))
            self.textBrowser_4.setObjectName("textBrowser_4")

            self.GroupButton4 = QtWidgets.QPushButton(self.Match1_4)
            self.GroupButton4.setGeometry(QtCore.QRect(560, 80, 201, 28))
            self.GroupButton4.setObjectName("GroupButton4")

        if checkempty[4] == 0 :
            self.Match1_5 = QtWidgets.QWidget(self.groupBox)
            self.Match1_5.setGeometry(QtCore.QRect(10, 540, 771, 121))
            self.Match1_5.setObjectName("Match1_5")

            self.textBrowser_5 = QtWidgets.QTextBrowser(self.Match1_5)
            self.textBrowser_5.setGeometry(QtCore.QRect(10, 10, 751, 61))
            self.textBrowser_5.setObjectName("textBrowser_5")

            self.GroupButton5 = QtWidgets.QPushButton(self.Match1_5)
            self.GroupButton5.setGeometry(QtCore.QRect(560, 80, 201, 28))
            self.GroupButton5.setObjectName("GroupButton5")


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 211, 61))
        self.groupBox_2.setObjectName("groupBox_2")

        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.textEdit.setObjectName("textEdit")


        # NAVIGATION SECTION

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

        # MENU BAR
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

        # POPULATING THE GROUP BOXES 
        groupContents1 = [" ", " "]
        groupContents2 = [" ", " "]
        groupContents3 = [" ", " "]
        groupContents4 = [" ", " "]
        groupContents5 = [" ", " "]

        df = pd.read_csv('GroupData.csv')
        #GroupID,GroupName,Description,Post0,Post1,Post2,Post3,Member0,Member1,Member2,Member3,Member4,Member5,Member6,Member7,currentGroup
        dfcheck = pd.read_csv('UserData.csv')
        currentUserRow = dfcheck[dfcheck['CurrentUser'] == 1]
        currentUserID = currentUserRow['UserID'].iloc[0]
        #print(currentUserID)
        groupName1 = currentUserRow['Group1'].iloc[0]
        groupName2 = currentUserRow['Group2'].iloc[0]
        groupName3 = currentUserRow['Group3'].iloc[0]
        groupName4 = currentUserRow['Group4'].iloc[0]
        groupName5 = currentUserRow['Group5'].iloc[0]
        for index, row in df.iterrows():
            if row['GroupName']== groupName1:
                groupContents1 = [row['GroupName'], row['Description']]
            if row['GroupName'] == groupName2:
                groupContents2 = [row['GroupName'], row['Description']]
            if row['GroupName'] == groupName3:
                groupContents3 = [row['GroupName'], row['Description']]
            if row['GroupName'] == groupName4:
                groupContents4 = [row['GroupName'], row['Description']]
            if row['GroupName'] == groupName5:
                groupContents5 = [row['GroupName'], row['Description']]
        backup = "Join More Groups!"
        # CLEAR EMPTY BOXES 
        # MOVE TO BOTTOM
        checkempty = [0,0,0,0,0]
        if groupContents1[1] == " ":
            checkempty[0] = 1
        if groupContents2[1] == " ":
            checkempty[1] = 1
        if groupContents3[1] == " ":
            checkempty[2] = 1
        if groupContents4[1] == " ":
            checkempty[3] = 1
        if groupContents5[1] == " ":
            checkempty[4] = 1
        



        if checkempty[0] == 0:
            self.textBrowser.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents1[0] + "</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents1[1] + "</span></p></body></html>"))
            self.GroupButton1.setText(_translate("UsersGroups", "Go to Group Page"))
        
        if checkempty[1] == 0:
            self.textBrowser_2.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents2[0] + "</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents2[1] + "</span></p></body></html>"))
            self.GroupButton2.setText(_translate("UsersGroups", "Go to Group Page"))

        if checkempty[2] == 0:
            self.textBrowser_3.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents3[0] + "</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents3[1] + "</span></p></body></html>"))
            self.GroupButton3.setText(_translate("UsersGroups", "Go to Group Page"))

        if checkempty[3] == 0:
            self.textBrowser_4.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents4[0] + "</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents4[1] + "</span></p></body></html>"))
            self.GroupButton4.setText(_translate("UsersGroups", "Go to Group Page"))

        if checkempty[4] == 0:
            self.textBrowser_5.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents5[0] + "</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + groupContents5[1] + "</span></p></body></html>"))
            self.GroupButton5.setText(_translate("UsersGroups", "Go to Group Page"))


        self.groupBox_2.setTitle(_translate("UsersGroups", "Search"))        
        self.textEdit.setHtml(_translate("UsersGroups", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Search</span></p></body></html>"))
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
