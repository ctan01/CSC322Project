from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_MemberPoll(object):
    def setupUi(self, CreateMemberPoll):
        CreateMemberPoll.setObjectName("CreateMemberPoll")
        CreateMemberPoll.resize(386, 300)
        self.centralwidget = QtWidgets.QWidget(CreateMemberPoll)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateMemberPoll)
        self.buttonBox.setGeometry(QtCore.QRect(90, 220, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(CreateMemberPoll)
        self.comboBox.setGeometry(QtCore.QRect(60, 60, 271, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.textBrowser = QtWidgets.QTextBrowser(CreateMemberPoll)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 351, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox_2 = QtWidgets.QComboBox(CreateMemberPoll)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 150, 271, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.textBrowser_2 = QtWidgets.QTextBrowser(CreateMemberPoll)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 100, 351, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(CreateMemberPoll)
        QtCore.QMetaObject.connectSlotsByName(CreateMemberPoll)

    def retranslateUi(self, CreateMemberPoll):
        _translate = QtCore.QCoreApplication.translate
        CreateMemberPoll.setWindowTitle(_translate("CreateMemberPoll", "CreateMemberPoll"))
        self.textBrowser.setHtml(_translate("CreateMemberPoll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
       
        self.comboBox.setItemText(0, _translate("CreateMemberPoll", userZero)) 
        self.comboBox.setItemText(1, _translate("CreateMemberPoll", userOne))       
        self.comboBox.setItemText(2, _translate("CreateMemberPoll", userTwo))       
        self.comboBox.setItemText(3, _translate("CreateMemberPoll", userThree))       
        self.comboBox.setItemText(4, _translate("CreateMemberPoll", userFour))       
        self.comboBox.setItemText(5, _translate("CreateMemberPoll", userFive))       
        self.comboBox.setItemText(6, _translate("CreateMemberPoll", userSix))       
        self.comboBox.setItemText(7, _translate("CreateMemberPoll", userSeven))       

        self.comboBox_2.setItemText(0, _translate("CreateMemberPoll", "Vote to Send Warning to Member"))
        self.comboBox_2.setItemText(1, _translate("CreateMemberPoll", "Vote to Kick Member Out"))
        self.comboBox_2.setItemText(2, _translate("CreateMemberPoll", "Vote to Send Compliment to Member"))
        self.textBrowser_2.setHtml(_translate("CreateMemberPoll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Select Polling Action</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateMemberPoll = QtWidgets.QMainWindow()
    ui = Ui_MemberPoll()
    ui.setupUi(CreateMemberPoll)
    CreateMemberPoll.show()
    sys.exit(app.exec_())
