from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd


class Ui_CreatePost(object):
    def refreshGroupPage(self):
        from GroupPage import Ui_GroupPage
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GroupPage()
        self.ui.setupUi(self.window)
        self.window.show()

    
    def publishPost(self):
        df = pd.read_csv('Posts.csv')
        dfgroup = pd.read_csv('GroupData.csv')
        dfuser = pd.read_csv('UserData.csv')
        currentGroupRow = dfgroup[dfgroup['currentGroup'] ==  1]
        currentGroupID = currentGroupRow['GroupID'].iloc[0]
        print(currentGroupID)
        checkTaboo = False
        # TABOO CHECK
        fullpost = self.lineEdit_Postcontents.text()
        print(fullpost)
        postarray = fullpost.split()
        print(postarray[0])
        count = -1
        newpost = ""
        for x in postarray:
            count = count + 1
            if postarray[count] == "hate":
                postarray[count] = "****"
                checkTaboo = True

            elif postarray[count] == "bad":
                postarray[count] = "***"
                checkTaboo = True

            elif postarray[count] == "darn":
                postarray[count] = "****"
                checkTaboo = True
            newpost = newpost + " " + str(postarray[count])

        stat = dfuser[(dfuser['CurrentUser']) == 1].index[0]
        if checkTaboo == True:
            dfuser.loc[stat, 'Reputation_Score'] = dfuser.loc[stat, 'Reputation_Score'] - 1

        if int(dfuser.at[stat, 'Reputation_Score']) < 30:
            dfuser.loc[stat, 'Status'] = 'OU'

        dfuser.to_csv('UserData.csv', index=False)

        # PostID, GroupID, PostContents, Comment0, Comment1, Comment2,Comment3
        new_row = {'PostID': (len(df.index)+1),
            'GroupID' : currentGroupID,
            'PostContents': newpost,
            'Comment0': " ",
            'Comment1': " ",
            'Comment2': " ",
            'Comment3': " "
            }
        df = df.append(new_row, ignore_index=True)
        df.to_csv('Posts.csv', index= False)

        msg = QMessageBox()
        msg.setWindowTitle("Publish Post")
        msg.setText("Post has been published!")
        x = msg.exec_()

    def setupUi(self, CreatePost):
        CreatePost.setObjectName("CreatePost")
        CreatePost.resize(320, 100)
        self.centralwidget = QtWidgets.QWidget(CreatePost)
        self.centralwidget.setObjectName("centralwidget")
        

        self.lineEdit_Postcontents = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Postcontents.setGeometry(QtCore.QRect(10,10,300,30))
        self.lineEdit_Postcontents.setObjectName("lineEdit_Postcontents")

        self.PublishPostButton = QtWidgets.QPushButton(self.centralwidget)
        self.PublishPostButton.setGeometry(QtCore.QRect(60, 50, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.PublishPostButton.setFont(font)
        self.PublishPostButton.setObjectName("Publish")
        self.PublishPostButton.clicked.connect(self.publishPost) # BEGIN TO PUBLISH POST
        self.PublishPostButton.clicked.connect(CreatePost.close)
        self.PublishPostButton.clicked.connect(self.refreshGroupPage)

        CreatePost.setCentralWidget(self.centralwidget) 

        self.retranslateUi(CreatePost)
        QtCore.QMetaObject.connectSlotsByName(CreatePost)

    def retranslateUi(self, CreatePost):
        _translate = QtCore.QCoreApplication.translate
        CreatePost.setWindowTitle(_translate("CreatePost", "CreatePost"))
        self.PublishPostButton.setText(_translate("CreatePost", "Publish"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreatePost = QtWidgets.QMainWindow()
    ui = Ui_CreatePost()
    ui.setupUi(CreatePost)
    CreatePost.show()
    sys.exit(app.exec_())
