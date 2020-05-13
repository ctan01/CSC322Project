from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_InboxPage(object):
        def openGroupsPage(self):
                from UsersGroups import Ui_UsersGroupsPage
                self.window = QtWidgets.QMainWindow() # USERID PARAMETERS
                self.ui = Ui_UsersGroupsPage()
                self.ui.setupUi(self.window)
                self.window.show()

        def openProfilePage(self):              # USERID PARAMETERS
                from ProfilePage import Ui_profilePage
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_profilePage()
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


        def setupUi(self, InboxPage):
                InboxPage.setObjectName("InboxPage")
                InboxPage.resize(1052, 846)
                self.InboxDashboard = QtWidgets.QWidget(InboxPage)
                self.InboxDashboard.setObjectName("InboxDashboard")
                self.NavigationSideBar = QtWidgets.QGroupBox(self.InboxDashboard)
                self.NavigationSideBar.setGeometry(QtCore.QRect(590, 0, 451, 61))
                self.NavigationSideBar.setObjectName("NavigationSideBar")

                self.HomeButton = QtWidgets.QPushButton(self.NavigationSideBar)         # LINKED
                self.HomeButton.setGeometry(QtCore.QRect(120, 20, 101, 28))
                self.HomeButton.setObjectName("HomeButton")
                self.HomeButton.clicked.connect(self.openHomePage)
                self.HomeButton.clicked.connect(InboxPage.close)

                
                self.ProfileButton = QtWidgets.QPushButton(self.NavigationSideBar)      # LINKED
                self.ProfileButton.setGeometry(QtCore.QRect(10, 20, 101, 28))
                self.ProfileButton.setObjectName("ProfileButton")
                self.ProfileButton.setObjectName("ProfileButton")
                self.ProfileButton.clicked.connect(self.openProfilePage)

                self.LogOUt = QtWidgets.QPushButton(self.NavigationSideBar)             # LINKED
                self.LogOUt.setGeometry(QtCore.QRect(340, 20, 101, 28))
                self.LogOUt.setObjectName("LogOUt")
                self.LogOUt.setObjectName("LogOUt")
                self.LogOUt.clicked.connect(InboxPage.close)

                self.GroupsButton = QtWidgets.QPushButton(self.NavigationSideBar)        #LINKED
                self.GroupsButton.setGeometry(QtCore.QRect(230, 20, 101, 28))
                self.GroupsButton.setObjectName("GroupsButton")
                self.GroupsButton.clicked.connect(self.openGroupsPage)

                # FILLING INBOX INFO

                inboxContents = [" "," "," "," "," "]

                InboxType = [0,0,0,0,0]

                df = pd.read_csv('InboxMessages.csv')
                #MessageID, UserID, Type, TypeID, GroupID, SubjectUserID
                dfcheck = pd.read_csv('UserData.csv')
                currentUserRow = dfcheck[dfcheck['CurrentUser'] == 1]
                currentUserID = currentUserRow['UserID'].iloc[0]
                count = 0
                for index, row in df.iterrows():
                        if row['UserID'] == currentUserID:
                                inboxContents[count] = row['GroupName']
                                InboxType[count] = row['Type']
                                count = count + 1

                # CLEAR EMPTY BOXES 
                # MOVE TO BOTTOM
                checkempty = [0,0,0,0,0]
                if inboxContents[0] == " ":
                        checkempty[0] = 1
                if inboxContents[1] == " ":
                        checkempty[1] = 1
                if inboxContents[2] == " ":
                        checkempty[2] = 1
                if inboxContents[3] == " ":
                        checkempty[3] = 1
                if inboxContents[4] == " ":
                        checkempty[4] = 1

                # MESSAGE BOXES


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

                if checkempty[0] == 0:
                        self.InvitationMessage = QtWidgets.QWidget(self.InboxDashboard)
                        self.InvitationMessage.setGeometry(QtCore.QRect(20, 80, 1011, 101))
                        self.InvitationMessage.setObjectName("InvitationMessage")
                        self.textBrowser = QtWidgets.QTextBrowser(self.InvitationMessage)
                        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 991, 51))
                        self.textBrowser.setObjectName("textBrowser")
                        self.pushButton = QtWidgets.QPushButton(self.InvitationMessage)
                        self.pushButton.setGeometry(QtCore.QRect(10, 70, 93, 28))
                        self.pushButton.setObjectName("pushButton")
                        self.Decline2 = QtWidgets.QPushButton(self.InvitationMessage)
                        self.Decline2.setGeometry(QtCore.QRect(110, 70, 93, 28))
                        self.Decline2.setObjectName("Decline2")

                if checkempty[1] == 0:
                        self.InvitationMessage_2 = QtWidgets.QWidget(self.InboxDashboard)
                        self.InvitationMessage_2.setGeometry(QtCore.QRect(20, 190, 1011, 101))
                        self.InvitationMessage_2.setObjectName("InvitationMessage_2")
                        self.textBrowser_2 = QtWidgets.QTextBrowser(self.InvitationMessage_2)
                        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 991, 51))
                        self.textBrowser_2.setObjectName("textBrowser_2")
                        self.Accept3 = QtWidgets.QPushButton(self.InvitationMessage_2)
                        self.Accept3.setGeometry(QtCore.QRect(10, 70, 93, 28))
                        self.Accept3.setObjectName("Accept3")
                        self.Decline3 = QtWidgets.QPushButton(self.InvitationMessage_2)
                        self.Decline3.setGeometry(QtCore.QRect(110, 70, 93, 28))
                        self.Decline3.setObjectName("Decline3")

                if checkempty[2] == 0:
                        self.InvitationMessage3 = QtWidgets.QWidget(self.InboxDashboard)
                        self.InvitationMessage3.setGeometry(QtCore.QRect(20, 300, 1011, 101))
                        self.InvitationMessage3.setObjectName("InvitationMessage3")
                        self.textBrowser3 = QtWidgets.QTextBrowser(self.InvitationMessage3)
                        self.textBrowser3.setGeometry(QtCore.QRect(10, 10, 991, 51))
                        self.textBrowser3.setObjectName("textBrowser3")
                        self.pushButton43 = QtWidgets.QPushButton(self.InvitationMessage3)
                        self.pushButton43.setGeometry(QtCore.QRect(10, 70, 93, 28))
                        self.pushButton43.setObjectName("pushButton43")
                        self.Decline43 = QtWidgets.QPushButton(self.InvitationMessage3)
                        self.Decline43.setGeometry(QtCore.QRect(110, 70, 93, 28))
                        self.Decline43.setObjectName("Decline43")

                if checkempty[3] == 0:
                        self.InvitationMessage4 = QtWidgets.QWidget(self.InboxDashboard)
                        self.InvitationMessage4.setGeometry(QtCore.QRect(20, 410, 1011, 101))
                        self.InvitationMessage4.setObjectName("InvitationMessage4")
                        self.textBrowser4 = QtWidgets.QTextBrowser(self.InvitationMessage4)
                        self.textBrowser4.setGeometry(QtCore.QRect(10, 10, 991, 51))
                        self.textBrowser4.setObjectName("textBrowser4")
                        self.pushButton4 = QtWidgets.QPushButton(self.InvitationMessage4)
                        self.pushButton4.setGeometry(QtCore.QRect(10, 70, 93, 28))
                        self.pushButton4.setObjectName("pushButton4")
                        self.Decline4 = QtWidgets.QPushButton(self.InvitationMessage4)
                        self.Decline4.setGeometry(QtCore.QRect(110, 70, 93, 28))
                        self.Decline4.setObjectName("Decline4")

                if checkempty[4] == 0:
                        self.InvitationMessage5 = QtWidgets.QWidget(self.InboxDashboard)
                        self.InvitationMessage5.setGeometry(QtCore.QRect(20, 520, 1011, 101))
                        self.InvitationMessage5.setObjectName("InvitationMessage5")
                        self.textBrowser5 = QtWidgets.QTextBrowser(self.InvitationMessage5)
                        self.textBrowser5.setGeometry(QtCore.QRect(10, 10, 991, 51))
                        self.textBrowser5.setObjectName("textBrowser5")
                        self.pushButton5 = QtWidgets.QPushButton(self.InvitationMessage5)
                        self.pushButton5.setGeometry(QtCore.QRect(10, 70, 93, 28))
                        self.pushButton5.setObjectName("pushButton5")
                        self.Decline5 = QtWidgets.QPushButton(self.InvitationMessage5)
                        self.Decline5.setGeometry(QtCore.QRect(110, 70, 93, 28))
                        self.Decline5.setObjectName("Decline5")



                self.AcceptALL = QtWidgets.QPushButton(self.InboxDashboard)
                self.AcceptALL.setGeometry(QtCore.QRect(740, 740, 141, 28))
                self.AcceptALL.setObjectName("AcceptALL")

                self.DeclineALL = QtWidgets.QPushButton(self.InboxDashboard)
                self.DeclineALL.setGeometry(QtCore.QRect(890, 740, 141, 28))
                self.DeclineALL.setObjectName("DeclineALL")
                InboxPage.setCentralWidget(self.InboxDashboard)
                self.menubar = QtWidgets.QMenuBar(InboxPage)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 26))
                self.menubar.setObjectName("menubar")
                InboxPage.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(InboxPage)
                self.statusbar.setObjectName("statusbar")
                InboxPage.setStatusBar(self.statusbar)

                self.retranslateUi(InboxPage)
                QtCore.QMetaObject.connectSlotsByName(InboxPage)

        def retranslateUi(self, InboxPage):
                _translate = QtCore.QCoreApplication.translate
                InboxPage.setWindowTitle(_translate("InboxPage", "InboxPage"))
                self.NavigationSideBar.setTitle(_translate("InboxPage", "Navigation"))
                self.HomeButton.setText(_translate("InboxPage", "Home"))
                self.ProfileButton.setText(_translate("InboxPage", "Profile"))
                self.LogOUt.setText(_translate("InboxPage", "LogOut"))
                self.GroupsButton.setText(_translate("InboxPage", "Groups"))
                self.groupBox_2.setTitle(_translate("InboxPage", "Search"))
                self.HomeButton_2.setText(_translate("InboxPage", "Search"))

                # FILLING INBOX INFO

                inboxContents = [" "," "," "," "," "]

                InboxType = [0,0,0,0,0]

                df = pd.read_csv('InboxMessages.csv')
                #MessageID, UserID, Type, TypeID, GroupID, SubjectUserID
                dfcheck = pd.read_csv('UserData.csv')
                currentUserRow = dfcheck[dfcheck['CurrentUser'] == 1]
                currentUserID = currentUserRow['UserID'].iloc[0]
                count = 0
                for index, row in df.iterrows():
                        if row['UserID'] == currentUserID:
                                inboxContents[count] = row['GroupName']
                                InboxType[count] = row['Type']
                                count = count + 1

                # CLEAR EMPTY BOXES 
                # MOVE TO BOTTOM
                checkempty = [0,0,0,0,0]
                if inboxContents[0] == " ":
                        checkempty[0] = 1
                if inboxContents[1] == " ":
                        checkempty[1] = 1
                if inboxContents[2] == " ":
                        checkempty[2] = 1
                if inboxContents[3] == " ":
                        checkempty[3] = 1
                if inboxContents[4] == " ":
                        checkempty[4] = 1


                if checkempty[0] == 0:
                        self.textBrowser.setHtml(_translate("InboxPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Invitation to Join " + inboxContents[0] + " </span></p>\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
                        self.pushButton.setText(_translate("InboxPage", "Accept"))
                        self.Decline2.setText(_translate("InboxPage", "Decline"))
                
                if checkempty[1] == 0:
                        self.textBrowser_2.setHtml(_translate("InboxPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Invitation to Join " + inboxContents[1] + "</span></p></body></html>"))
                        self.Accept3.setText(_translate("InboxPage", "Accept"))
                        self.Decline3.setText(_translate("InboxPage", "Decline"))

                if checkempty[2] == 0:
                        self.textBrowser3.setHtml(_translate("InboxPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Invitation to Join " + inboxContents[2] + "</span></p></body></html>"))
                        self.pushButton43.setText(_translate("InboxPage", "Accept"))
                        self.Decline43.setText(_translate("InboxPage", "Decline"))

                if checkempty[3] == 0:
                        self.textBrowser4.setHtml(_translate("InboxPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Invitation to Join " + inboxContents[3] + "</span></p></body></html>"))
                        self.pushButton4.setText(_translate("InboxPage", "Accept"))
                        self.Decline4.setText(_translate("InboxPage", "Decline"))

                if checkempty[4] == 0:
                        self.textBrowser5.setHtml(_translate("InboxPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Invitation to Join " + inboxContents[4] + "</span></p></body></html>")) 
                        self.pushButton5.setText(_translate("InboxPage", "Accept"))
                        self.Decline5.setText(_translate("InboxPage", "Decline"))

                self.AcceptALL.setText(_translate("InboxPage", "Accept All Invitations"))
                self.DeclineALL.setText(_translate("InboxPage", "Decline All Invitations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InboxPage = QtWidgets.QMainWindow()
    ui = Ui_InboxPage()
    ui.setupUi(InboxPage)
    InboxPage.show()
    sys.exit(app.exec_())
