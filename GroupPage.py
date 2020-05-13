from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

#class Post:
#    def __init__(self):
#        self.text = ""
    

#class MeetupPost(Post):
#    def __init__(self):
#        self.time = 0

#    def draw(self):
#        pass


class Ui_GroupPage(object):
    def refreshGroupPage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GroupPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def submitComment(self):
        pass
    
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

    def openCreatePostPage(self):           # POP UP COMPLETE !! :)  
        from CreatePost import Ui_CreatePost
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreatePost()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCreateMeetUpPoll(self):         # POP UP WINDOW     
        from CreateMeetUpPoll import Ui_MeetUpPoll
        self.window= QtWidgets.QMainWindow()
        self.ui = Ui_MeetUpPoll()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCreateMemberPoll(self):         # POP UP WINDOW
        from CreateMemberPoll import Ui_MemberPoll
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MemberPoll()
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

    def setupUi(self, GroupPage):
        df = pd.read_csv('UserData.csv')

        GroupPage.setObjectName("GroupPage")
        GroupPage.resize(1234, 846)
        self.centralwidget = QtWidgets.QWidget(GroupPage)
        self.centralwidget.setObjectName("centralwidget")
        self.NavigationSideBar = QtWidgets.QGroupBox(self.centralwidget)
        self.NavigationSideBar.setGeometry(QtCore.QRect(760, 0, 451, 61))
        self.NavigationSideBar.setObjectName("NavigationSideBar")
        
        self.InboxButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.InboxButton.setGeometry(QtCore.QRect(120, 20, 101, 28))
        self.InboxButton.setObjectName("InboxButton")   
        self.InboxButton.clicked.connect(self.openInboxPage)                # LINKED
        self.InboxButton.clicked.connect(GroupPage.close)


        self.ProfileButton = QtWidgets.QPushButton(self.NavigationSideBar)  # LINKED
        self.ProfileButton.setGeometry(QtCore.QRect(10, 20, 101, 28))
        self.ProfileButton.setObjectName("ProfileButton")
        self.ProfileButton.clicked.connect(self.openProfilePage)
        

        self.LogOUt = QtWidgets.QPushButton(self.NavigationSideBar)         # LINKED
        self.LogOUt.setGeometry(QtCore.QRect(340, 20, 101, 28))
        self.LogOUt.setObjectName("LogOUt")
        self.LogOUt.clicked.connect(GroupPage.close)


        self.HomeButton = QtWidgets.QPushButton(self.NavigationSideBar)     # LINKED
        self.HomeButton.setGeometry(QtCore.QRect(230, 20, 101, 28))
        self.HomeButton.setObjectName("HomeButton")
        self.HomeButton.clicked.connect(self.openHomePage)
        self.HomeButton.clicked.connect(GroupPage.close)

        self.Dashboard = QtWidgets.QScrollArea(self.centralwidget)
        self.Dashboard.setGeometry(QtCore.QRect(230, 80, 751, 661))
        self.Dashboard.setWidgetResizable(True)
        self.Dashboard.setObjectName("Dashboard")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 749, 659))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #self.MeetUpPoll = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)        # MEET UP POLL CLOSES AFTER 75% of users respond
        #self.MeetUpPoll.setGeometry(QtCore.QRect(10, 240, 701, 91))
        #self.MeetUpPoll.setObjectName("MeetUpPoll")

        #self.Choice1 = QtWidgets.QCheckBox(self.MeetUpPoll)
        #self.Choice1.setGeometry(QtCore.QRect(10, 20, 101, 20))
        #self.Choice1.setObjectName("Choice1")

        #self.SubmitVote = QtWidgets.QPushButton(self.MeetUpPoll)        # READ INPUT INTO FILE  VOTE CLOSES AFTER 75% OF USERS RESPOND
        #self.SubmitVote.setGeometry(QtCore.QRect(590, 60, 93, 28))
        #self.SubmitVote.setObjectName("SubmitVote")


        #self.Choice2 = QtWidgets.QCheckBox(self.MeetUpPoll)
        #self.Choice2.setGeometry(QtCore.QRect(10, 50, 101, 20))
        #self.Choice2.setObjectName("Choice2")
        #self.Choice3 = QtWidgets.QCheckBox(self.MeetUpPoll)
        #self.Choice3.setGeometry(QtCore.QRect(160, 20, 131, 20))
        #self.Choice3.setObjectName("Choice3")
        #self.Choice4 = QtWidgets.QCheckBox(self.MeetUpPoll)
        #self.Choice4.setGeometry(QtCore.QRect(160, 50, 131, 20))
        #self.Choice4.setObjectName("Choice4")
        #self.Choice5 = QtWidgets.QCheckBox(self.MeetUpPoll)
        #self.Choice5.setGeometry(QtCore.QRect(320, 20, 101, 20))
        #self.Choice5.setObjectName("Choice5")

        # GROUP POSTS

        self.GroupPost = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.GroupPost.setGeometry(QtCore.QRect(10, 10, 701, 175))
        self.GroupPost.setObjectName("GroupPost")                        

        self.PostText = QtWidgets.QTextBrowser(self.GroupPost)
        self.PostText.setGeometry(QtCore.QRect(10, 20, 681, 80))
        self.PostText.setObjectName("PostText")

        self.textEdit = QtWidgets.QTextEdit(self.GroupPost)           # ADD COMMENT BOX
        self.textEdit.setGeometry(QtCore.QRect(10, 105, 681, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.GroupPost)         # READ COMMMENT INPUT
        self.pushButton.setGeometry(QtCore.QRect(590, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")

        # GROUP POST TWO
        self.GroupPost2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.GroupPost2.setGeometry(QtCore.QRect(10, 200, 701, 175))
        self.GroupPost2.setObjectName("GroupPost2")                        

        self.PostText2 = QtWidgets.QTextBrowser(self.GroupPost2)
        self.PostText2.setGeometry(QtCore.QRect(10, 20, 681, 80))
        self.PostText2.setObjectName("PostText2")

        self.textEdit2 = QtWidgets.QTextEdit(self.GroupPost2)           # ADD COMMENT BOX
        self.textEdit2.setGeometry(QtCore.QRect(10, 105, 681, 31))
        self.textEdit2.setObjectName("textEdit2")
        self.pushButton2 = QtWidgets.QPushButton(self.GroupPost2)         # READ COMMMENT INPUT
        self.pushButton2.setGeometry(QtCore.QRect(590, 140, 93, 28))
        self.pushButton2.setObjectName("pushButton2")

        # GROUP POST THREE
        self.GroupPost3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.GroupPost3.setGeometry(QtCore.QRect(10, 390, 701, 175))
        self.GroupPost3.setObjectName("GroupPost3")                        

        self.PostText3 = QtWidgets.QTextBrowser(self.GroupPost3)
        self.PostText3.setGeometry(QtCore.QRect(10, 20, 681, 80))
        self.PostText3.setObjectName("PostText3")

        self.textEdit3 = QtWidgets.QTextEdit(self.GroupPost3)           # ADD COMMENT BOX
        self.textEdit3.setGeometry(QtCore.QRect(10, 105, 681, 31))
        self.textEdit3.setObjectName("textEdit3")
        self.pushButton3 = QtWidgets.QPushButton(self.GroupPost3)         # READ COMMMENT INPUT
        self.pushButton3.setGeometry(QtCore.QRect(590, 140, 93, 28))
        self.pushButton3.setObjectName("pushButton3")

        # GROUP POST FOUR
        self.GroupPost4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.GroupPost4.setGeometry(QtCore.QRect(10, 570, 701, 175))
        self.GroupPost4.setObjectName("GroupPost4")                        

        self.PostText4 = QtWidgets.QTextBrowser(self.GroupPost4)
        self.PostText4.setGeometry(QtCore.QRect(10, 20, 681, 80))
        self.PostText4.setObjectName("PostText4")

        self.textEdit4 = QtWidgets.QTextEdit(self.GroupPost4)           # ADD COMMENT BOX
        self.textEdit4.setGeometry(QtCore.QRect(10, 105, 681, 31))
        self.textEdit4.setObjectName("textEdit4")
        self.pushButton4 = QtWidgets.QPushButton(self.GroupPost4)         # READ COMMMENT INPUT
        self.pushButton4.setGeometry(QtCore.QRect(590, 140, 93, 28))
        self.pushButton4.setObjectName("pushButton4")



        #posts = list()

        
        #for p in posts:
        #    p.draw()

        #self.VoteWarning = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)   # VOTE CLOSES AFTER 75% of USERS RESPOND
        #self.VoteWarning.setGeometry(QtCore.QRect(10, 340, 701, 91))
        #self.VoteWarning.setObjectName("VoteWarning")

        #self.YesBox = QtWidgets.QCheckBox(self.VoteWarning)
        #self.YesBox.setGeometry(QtCore.QRect(10, 30, 81, 20))
        #self.YesBox.setObjectName("YesBox")
        #self.NoBox = QtWidgets.QCheckBox(self.VoteWarning)
        #self.NoBox.setGeometry(QtCore.QRect(10, 60, 81, 20))
        #self.NoBox.setObjectName("NoBox")

        #self.SubmitVote_2 = QtWidgets.QPushButton(self.VoteWarning)         # TAKE INPUT
        #self.SubmitVote_2.setGeometry(QtCore.QRect(590, 60, 93, 28))
        #self.SubmitVote_2.setObjectName("SubmitVote_2")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(730, 0, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.Dashboard.setWidget(self.scrollAreaWidgetContents)

        self.GroupCommands = QtWidgets.QGroupBox(self.centralwidget)
        self.GroupCommands.setGeometry(QtCore.QRect(990, 70, 221, 271))
        self.GroupCommands.setObjectName("GroupCommands")

        self.Leave_Group_2 = QtWidgets.QPushButton(self.GroupCommands)
        self.Leave_Group_2.setGeometry(QtCore.QRect(0, 240, 221, 28))
        self.Leave_Group_2.setObjectName("Leave_Group_2")
        # open leave group confirmation

        self.CreatePost = QtWidgets.QPushButton(self.GroupCommands)     # POP UP
        self.CreatePost.setGeometry(QtCore.QRect(0, 20, 221, 28))
        self.CreatePost.setObjectName("CreatePost")
        self.CreatePost.clicked.connect(self.openCreatePostPage)

        self.CreateMeetUpPoll = QtWidgets.QPushButton(self.GroupCommands) # POP UP
        self.CreateMeetUpPoll.setGeometry(QtCore.QRect(0, 50, 221, 28))
        self.CreateMeetUpPoll.setObjectName("CreateMeetUpPoll")
        self.CreateMeetUpPoll.clicked.connect(self.openCreateMeetUpPoll)

        self.CreateMemberPoll = QtWidgets.QPushButton(self.GroupCommands)   # POP UP
        self.CreateMemberPoll.setGeometry(QtCore.QRect(0, 80, 221, 28))
        self.CreateMemberPoll.setObjectName("CreateMemberPoll")
        self.CreateMemberPoll.clicked.connect(self.openCreateMemberPoll)

        self.GroupInfo = QtWidgets.QPushButton(self.GroupCommands)
        self.GroupInfo.setGeometry(QtCore.QRect(0, 110, 221, 28))
        self.GroupInfo.setObjectName("GroupInfo")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 211, 271))
        self.groupBox.setObjectName("groupBox")

        self.GroupNotificationsList = QtWidgets.QListView(self.groupBox)
        self.GroupNotificationsList.setGeometry(QtCore.QRect(10, 20, 191, 241))
        self.GroupNotificationsList.setObjectName("GroupNotificationsList")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 211, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.textEdit.setObjectName("textEdit")

        self.HomeButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.HomeButton_2.setGeometry(QtCore.QRect(140, 20, 61, 31))
        self.HomeButton_2.setObjectName("HomeButton_2")

        GroupPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GroupPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1234, 26))
        self.menubar.setObjectName("menubar")
        GroupPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GroupPage)
        self.statusbar.setObjectName("statusbar")
        GroupPage.setStatusBar(self.statusbar)

        self.retranslateUi(GroupPage)
        QtCore.QMetaObject.connectSlotsByName(GroupPage)

    def retranslateUi(self, GroupPage):
        _translate = QtCore.QCoreApplication.translate
        GroupPage.setWindowTitle(_translate("GroupPage", "GroupPage"))
        self.NavigationSideBar.setTitle(_translate("GroupPage", "Navigation"))
        self.InboxButton.setText(_translate("GroupPage", "Inbox"))
        self.ProfileButton.setText(_translate("GroupPage", "Profile"))
        self.LogOUt.setText(_translate("GroupPage", "LogOut"))
        self.HomeButton.setText(_translate("GroupPage", "Home"))
        #self.MeetUpPoll.setTitle(_translate("GroupPage", "Poll"))
        #self.Choice1.setText(_translate("GroupPage", "Tuesday 2pm"))
        #self.SubmitVote.setText(_translate("GroupPage", "Submit"))
        #self.Choice2.setText(_translate("GroupPage", "Tuesday 7pm"))
        #self.Choice3.setText(_translate("GroupPage", "Thursday 1pm"))
        #self.Choice4.setText(_translate("GroupPage", "Saturday 3pm"))
        #self.Choice5.setText(_translate("GroupPage", "Sunday 2pm"))

        # HERE, POST CONTENTS WILL BE THE POSTCONTENTS OF POSTS.CSV FILE FOR POSTS WITH GROUPID == GROUP WITH CURRENTGROUP = 1
        postcontents = "POST: "
        # Comments
        commentHeader = "COMMENTS: "
        comment0 = " "
        comment1 = " "
        comment2 = " "
        comment3 = " "

        df = pd.read_csv('Posts.csv')
        dfcheck = pd.read_csv('GroupData.csv')
        currentGroupRow = dfcheck[dfcheck['currentGroup'] == 1]
        currentGroupID = currentGroupRow['GroupID'].iloc[0]
        print(currentGroupID)
        for index, row in df.iterrows():
            if row['GroupID'] == currentGroupID:
                postcontents = postcontents + row['PostContents']
                comment0 = comment0 + row['Comment0']
                comment1 = comment1 + row['Comment1']
                comment2 = comment2 + row['Comment2']
                comment3 = comment3 + row['Comment3']

        self.GroupPost.setTitle(_translate("GroupPage", "Post"))
        self.PostText.setHtml(_translate("GroupPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">" + postcontents + "<br></br><br></br>" + comment0 + "<br></br>" + comment1 + "<br></br>" + comment2 + "<br></br>" + comment3 +"</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        
        self.pushButton.setText(_translate("GroupPage", "Comment"))

        #self.VoteWarning.setTitle(_translate("GroupPage", "Vote to Send Warning/Compliment to [USER NAME]"))
        #self.YesBox.setText(_translate("GroupPage", "Yes"))
        #self.NoBox.setText(_translate("GroupPage", "No"))
        #self.SubmitVote_2.setText(_translate("GroupPage", "Submit"))
        self.GroupCommands.setTitle(_translate("GroupPage", "GroupBox"))
        self.Leave_Group_2.setText(_translate("GroupPage", "Leave Group"))
        self.CreatePost.setText(_translate("GroupPage", "Create Post"))
        self.CreateMeetUpPoll.setText(_translate("GroupPage", "Create Meet Up Poll"))
        self.CreateMemberPoll.setText(_translate("GroupPage", "Create Member Poll"))
        self.GroupInfo.setText(_translate("GroupPage", "Group Info"))
        self.groupBox.setTitle(_translate("GroupPage", "Community Garden Notifications:"))
        self.groupBox_2.setTitle(_translate("GroupPage", "Search"))
        self.HomeButton_2.setText(_translate("GroupPage", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GroupPage = QtWidgets.QMainWindow()
    ui = Ui_GroupPage()
    ui.setupUi(GroupPage)
    GroupPage.show()
    sys.exit(app.exec_())
