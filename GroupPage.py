# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GroupPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(986, 758)
        self.Dashboard = QtWidgets.QScrollArea(Dialog)
        self.Dashboard.setGeometry(QtCore.QRect(230, 70, 501, 671))
        self.Dashboard.setWidgetResizable(True)
        self.Dashboard.setObjectName("Dashboard")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 499, 669))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.MeetUpPoll = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.MeetUpPoll.setGeometry(QtCore.QRect(10, 200, 481, 91))
        self.MeetUpPoll.setObjectName("MeetUpPoll")
        self.Choice1 = QtWidgets.QCheckBox(self.MeetUpPoll)
        self.Choice1.setGeometry(QtCore.QRect(10, 20, 101, 20))
        self.Choice1.setObjectName("Choice1")
        self.SubmitVote = QtWidgets.QPushButton(self.MeetUpPoll)
        self.SubmitVote.setGeometry(QtCore.QRect(380, 60, 93, 28))
        self.SubmitVote.setObjectName("SubmitVote")
        self.Choice2 = QtWidgets.QCheckBox(self.MeetUpPoll)
        self.Choice2.setGeometry(QtCore.QRect(10, 50, 101, 20))
        self.Choice2.setObjectName("Choice2")
        self.Choice3 = QtWidgets.QCheckBox(self.MeetUpPoll)
        self.Choice3.setGeometry(QtCore.QRect(130, 20, 101, 20))
        self.Choice3.setObjectName("Choice3")
        self.Choice4 = QtWidgets.QCheckBox(self.MeetUpPoll)
        self.Choice4.setGeometry(QtCore.QRect(130, 50, 101, 20))
        self.Choice4.setObjectName("Choice4")
        self.Choice5 = QtWidgets.QCheckBox(self.MeetUpPoll)
        self.Choice5.setGeometry(QtCore.QRect(250, 20, 101, 20))
        self.Choice5.setObjectName("Choice5")
        self.GroupPost = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.GroupPost.setGeometry(QtCore.QRect(10, 10, 481, 181))
        self.GroupPost.setObjectName("GroupPost")
        self.PostText = QtWidgets.QTextBrowser(self.GroupPost)
        self.PostText.setGeometry(QtCore.QRect(10, 20, 461, 111))
        self.PostText.setObjectName("PostText")
        self.Comment = QtWidgets.QTextBrowser(self.GroupPost)
        self.Comment.setGeometry(QtCore.QRect(10, 140, 461, 31))
        self.Comment.setObjectName("Comment")
        self.VoteWarning = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.VoteWarning.setGeometry(QtCore.QRect(10, 300, 481, 91))
        self.VoteWarning.setObjectName("VoteWarning")
        self.YesBox = QtWidgets.QCheckBox(self.VoteWarning)
        self.YesBox.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.YesBox.setObjectName("YesBox")
        self.NoBox = QtWidgets.QCheckBox(self.VoteWarning)
        self.NoBox.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.NoBox.setObjectName("NoBox")
        self.SubmitVote_2 = QtWidgets.QPushButton(self.VoteWarning)
        self.SubmitVote_2.setGeometry(QtCore.QRect(380, 60, 93, 28))
        self.SubmitVote_2.setObjectName("SubmitVote_2")
        self.Dashboard.setWidget(self.scrollAreaWidgetContents)
        self.GroupPageTitle = QtWidgets.QLabel(Dialog)
        self.GroupPageTitle.setGeometry(QtCore.QRect(30, 30, 121, 16))
        self.GroupPageTitle.setObjectName("GroupPageTitle")
        self.NavigationSideBar = QtWidgets.QGroupBox(Dialog)
        self.NavigationSideBar.setGeometry(QtCore.QRect(30, 70, 181, 261))
        self.NavigationSideBar.setObjectName("NavigationSideBar")
        self.HomeButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.HomeButton.setGeometry(QtCore.QRect(0, 20, 181, 28))
        self.HomeButton.setObjectName("HomeButton")
        self.InboxButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.InboxButton.setGeometry(QtCore.QRect(0, 50, 181, 28))
        self.InboxButton.setObjectName("InboxButton")
        self.ProfileButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.ProfileButton.setGeometry(QtCore.QRect(0, 80, 181, 28))
        self.ProfileButton.setObjectName("ProfileButton")
        self.GroupCommands = QtWidgets.QGroupBox(Dialog)
        self.GroupCommands.setGeometry(QtCore.QRect(750, 70, 201, 271))
        self.GroupCommands.setObjectName("GroupCommands")
        self.Leave_Group = QtWidgets.QPushButton(self.GroupCommands)
        self.Leave_Group.setGeometry(QtCore.QRect(0, 240, 201, 28))
        self.Leave_Group.setObjectName("Leave_Group")
        self.Create_Post = QtWidgets.QPushButton(self.GroupCommands)
        self.Create_Post.setGeometry(QtCore.QRect(0, 20, 201, 28))
        self.Create_Post.setObjectName("Create_Post")
        self.Create_Poll = QtWidgets.QPushButton(self.GroupCommands)
        self.Create_Poll.setGeometry(QtCore.QRect(0, 50, 201, 28))
        self.Create_Poll.setObjectName("Create_Poll")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.MeetUpPoll.setTitle(_translate("Dialog", "Poll"))
        self.Choice1.setText(_translate("Dialog", "Tuesday 2pm"))
        self.SubmitVote.setText(_translate("Dialog", "Submit"))
        self.Choice2.setText(_translate("Dialog", "Tuesday 7pm"))
        self.Choice3.setText(_translate("Dialog", "Thursday 1pm"))
        self.Choice4.setText(_translate("Dialog", "Saturday 3pm"))
        self.Choice5.setText(_translate("Dialog", "Sunday 2pm"))
        self.GroupPost.setTitle(_translate("Dialog", "Post"))
        self.PostText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">This is a group post</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.Comment.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">this is a comment</span></p></body></html>"))
        self.VoteWarning.setTitle(_translate("Dialog", "Vote to Send Warning/Compliment to [USER NAME]"))
        self.YesBox.setText(_translate("Dialog", "Yes"))
        self.NoBox.setText(_translate("Dialog", "No"))
        self.SubmitVote_2.setText(_translate("Dialog", "Submit"))
        self.GroupPageTitle.setText(_translate("Dialog", "Community Garden"))
        self.NavigationSideBar.setTitle(_translate("Dialog", "Navigation"))
        self.HomeButton.setText(_translate("Dialog", "Home"))
        self.InboxButton.setText(_translate("Dialog", "Inbox"))
        self.ProfileButton.setText(_translate("Dialog", "Profile"))
        self.GroupCommands.setTitle(_translate("Dialog", "GroupBox"))
        self.Leave_Group.setText(_translate("Dialog", "Leave Group"))
        self.Create_Post.setText(_translate("Dialog", "Create Post"))
        self.Create_Poll.setText(_translate("Dialog", "Create Poll"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
