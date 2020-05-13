from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MeetUpPoll(object):
    def submit(self):
        pass

    def setupUi(self, CreateMeetUpPoll):
        CreateMeetUpPoll.setObjectName("CreateMeetUpPoll")
        CreateMeetUpPoll.resize(389, 343)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateMeetUpPoll)
        self.buttonBox.setGeometry(QtCore.QRect(90, 310, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.dateTimeEdit_1 = QtWidgets.QDateTimeEdit(CreateMeetUpPoll)
        self.dateTimeEdit_1.setGeometry(QtCore.QRect(100, 50, 194, 22))
        self.dateTimeEdit_1.setObjectName("dateTimeEdit_1")
        self.textBrowser = QtWidgets.QTextBrowser(CreateMeetUpPoll)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 361, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(CreateMeetUpPoll)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(100, 90, 194, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(CreateMeetUpPoll)
        self.dateTimeEdit_3.setGeometry(QtCore.QRect(100, 130, 194, 22))
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.dateTimeEdit_4 = QtWidgets.QDateTimeEdit(CreateMeetUpPoll)
        self.dateTimeEdit_4.setGeometry(QtCore.QRect(100, 170, 194, 22))
        self.dateTimeEdit_4.setObjectName("dateTimeEdit_4")
        self.dateTimeEdit_5 = QtWidgets.QDateTimeEdit(CreateMeetUpPoll)
        self.dateTimeEdit_5.setGeometry(QtCore.QRect(100, 210, 194, 22))
        self.dateTimeEdit_5.setObjectName("dateTimeEdit_5")
        self.dateTimeEdit_6 = QtWidgets.QDateTimeEdit(CreateMeetUpPoll)
        self.dateTimeEdit_6.setGeometry(QtCore.QRect(100, 250, 194, 22))
        self.dateTimeEdit_6.setObjectName("dateTimeEdit_6")

        self.retranslateUi(CreateMeetUpPoll)
        QtCore.QMetaObject.connectSlotsByName(CreateMeetUpPoll)

    def retranslateUi(self, CreateMeetUpPoll):
        _translate = QtCore.QCoreApplication.translate
        CreateMeetUpPoll.setWindowTitle(_translate("CreateMeetUpPoll", "CreateMeetUpPoll"))
        self.textBrowser.setHtml(_translate("CreateMeetUpPoll", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Select Up to 6 Meeting Times:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateMeetUpPoll = QtWidgets.QMainWindow()
    ui = Ui_MeetUpPoll()
    ui.setupUi(CreateMeetUpPoll)
    CreateMeetUpPoll.show()
    sys.exit(app.exec_())
