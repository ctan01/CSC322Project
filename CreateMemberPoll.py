from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5.QtWidgets import QMessageBox


class Ui_MemberPoll(object):

    def submitMemberPoll(self):
        df = pd.read_csv('MemberPoll.csv')
        # MemberPollID,GroupID,AffectedMemberID,Type,Yes,No,Total
        affectedMemberName = self.comboBox.currentText()
        typepoll = self.comboBox_2.currentText()
        dfnamecheck = pd.read_csv('UserData.csv')
        fullname = affectedMemberName.split();
        firstname = fullname[0]
        for index, row in dfnamecheck.iterrows():
            if row['First_Name'] == firstname:
                affectedMemberID = row['UserID']
        
        dfgroup = pd.read_csv('GroupData.csv')
        currentGroupRow = dfgroup[dfgroup['currentGroup'] ==  1]
        currentGroupID = currentGroupRow['GroupID'][0]


        new_row = {'MemberPollID': (len(df.index)+1),
            'GroupID' : currentGroupID, # UNKOWN FOR NOW (LINK WITH GROUP ID VALUE == 1)
            'AffectedMemberID' : affectedMemberID, # MATCH WITH FIRST NAME
            'Type' : typepoll,
            'Yes' : 1,
            'No' : 0,
            'Total' : 0
        }
        df = df.append(new_row, ignore_index=True)
        df.to_csv('MemberPoll.csv', index = False)

        msg = QMessageBox()
        msg.setWindowTitle("Publish Poll")
        msg.setText("Poll has been published! Wait for at least 60% of Members to Respond before Results!")
        x = msg.exec_()


    def setupUi(self, MemberPoll):
        MemberPoll.setObjectName("MemberPoll")
        MemberPoll.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MemberPoll)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(MemberPoll)
        self.comboBox.setGeometry(QtCore.QRect(60, 180, 271, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.textBrowser = QtWidgets.QTextBrowser(MemberPoll)
        self.textBrowser.setGeometry(QtCore.QRect(20, 50, 351, 28))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox_2 = QtWidgets.QComboBox(MemberPoll)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 85, 271, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.textBrowser_2 = QtWidgets.QTextBrowser(MemberPoll)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 145, 351, 28))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.PublishPostButton = QtWidgets.QPushButton(self.centralwidget)
        self.PublishPostButton.setGeometry(QtCore.QRect(10, 0, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.PublishPostButton.setFont(font)
        self.PublishPostButton.setObjectName("Publish")
        self.PublishPostButton.clicked.connect(self.submitMemberPoll) # BEGIN TO PUBLISH POST
        self.PublishPostButton.clicked.connect(MemberPoll.close)

        self.retranslateUi(MemberPoll)
        QtCore.QMetaObject.connectSlotsByName(MemberPoll)

    def retranslateUi(self, MemberPoll):
        _translate = QtCore.QCoreApplication.translate
        MemberPoll.setWindowTitle(_translate("MemberPoll", "MemberPoll"))
        self.textBrowser.setHtml(_translate("MemberPoll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Select Member In Drop Down Menu</span></p></body></html>"))
       
        userZero = " "
        userOne = " "
        userTwo = " "
        userThree = " "
        userFour = " "
        userFive = " "
        userSix = " "
        userSeven = " "
        df = pd.read_csv('GroupData.csv')
        for index, row in df.iterrows():
            if row['GroupID'] == 1:
                userZero = userZero + row['Member0']
                userOne = userOne + row['Member1']
                userTwo = userTwo + row['Member2']
                userThree = userThree + row['Member3']
                userFour = userFour + row['Member4']
                userFive = userFive + row['Member5']
                userSix = userSix + row['Member6']
                userSeven = userSeven + row['Member7']
       
        self.comboBox.setItemText(0, _translate("MemberPoll", userZero)) 
        self.comboBox.setItemText(1, _translate("MemberPoll", userOne))       
        self.comboBox.setItemText(2, _translate("MemberPoll", userTwo))       
        self.comboBox.setItemText(3, _translate("MemberPoll", userThree))       
        self.comboBox.setItemText(4, _translate("MemberPoll", userFour))       
        self.comboBox.setItemText(5, _translate("MemberPoll", userFive))       
        self.comboBox.setItemText(6, _translate("MemberPoll", userSix))       
        self.comboBox.setItemText(7, _translate("MemberPoll", userSeven))       

        self.comboBox_2.setItemText(0, _translate("MemberPoll", "Vote to Send Warning to Member"))
        self.comboBox_2.setItemText(1, _translate("MemberPoll", "Vote to Kick Member Out"))
        self.comboBox_2.setItemText(2, _translate("MemberPoll", "Vote to Send Compliment to Member"))
        self.PublishPostButton.setText(_translate("CreatePost", "Publish"))
        self.textBrowser_2.setHtml(_translate("MemberPoll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Select Polling Action</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MemberPoll = QtWidgets.QMainWindow()
    ui = Ui_MemberPoll()
    ui.setupUi(MemberPoll)
    MemberPoll.show()
    sys.exit(app.exec_())
