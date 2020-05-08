# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 211, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.textEdit.setObjectName("textEdit")
        self.HomeButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.HomeButton_2.setGeometry(QtCore.QRect(140, 20, 61, 31))
        self.HomeButton_2.setObjectName("HomeButton_2")
        self.NavigationSideBar = QtWidgets.QGroupBox(self.centralwidget)
        self.NavigationSideBar.setGeometry(QtCore.QRect(600, 0, 451, 61))
        self.NavigationSideBar.setObjectName("NavigationSideBar")
        self.InboxButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.InboxButton.setGeometry(QtCore.QRect(120, 20, 101, 28))
        self.InboxButton.setObjectName("InboxButton")
        self.ProfileButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.ProfileButton.setGeometry(QtCore.QRect(10, 20, 101, 28))
        self.ProfileButton.setObjectName("ProfileButton")
        self.LogOUt = QtWidgets.QPushButton(self.NavigationSideBar)
        self.LogOUt.setGeometry(QtCore.QRect(340, 20, 101, 28))
        self.LogOUt.setObjectName("LogOUt")
        self.GroupsButton = QtWidgets.QPushButton(self.NavigationSideBar)
        self.GroupsButton.setGeometry(QtCore.QRect(230, 20, 101, 28))
        self.GroupsButton.setObjectName("GroupsButton")
        self.Matches = QtWidgets.QGroupBox(self.centralwidget)
        self.Matches.setGeometry(QtCore.QRect(200, 70, 601, 471))
        self.Matches.setObjectName("Matches")
        self.Match1 = QtWidgets.QWidget(self.Matches)
        self.Match1.setGeometry(QtCore.QRect(10, 20, 581, 121))
        self.Match1.setObjectName("Match1")
        self.textBrowser = QtWidgets.QTextBrowser(self.Match1)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 561, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.Match1)
        self.pushButton.setGeometry(QtCore.QRect(370, 80, 201, 28))
        self.pushButton.setObjectName("pushButton")
        self.Match2 = QtWidgets.QWidget(self.Matches)
        self.Match2.setGeometry(QtCore.QRect(10, 150, 581, 121))
        self.Match2.setObjectName("Match2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Match2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 561, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.Match2)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 80, 201, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Match3 = QtWidgets.QWidget(self.Matches)
        self.Match3.setGeometry(QtCore.QRect(10, 280, 581, 121))
        self.Match3.setObjectName("Match3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.Match3)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 561, 61))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.Match3)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 80, 201, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.SearchMessage = QtWidgets.QTextBrowser(self.Matches)
        self.SearchMessage.setGeometry(QtCore.QRect(10, 410, 581, 51))
        self.SearchMessage.setObjectName("SearchMessage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 26))
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
        self.groupBox_2.setTitle(_translate("MainWindow", "Search"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Garden</span></p></body></html>"))
        self.HomeButton_2.setText(_translate("MainWindow", "Search"))
        self.NavigationSideBar.setTitle(_translate("MainWindow", "Navigation"))
        self.InboxButton.setText(_translate("MainWindow", "Inbox"))
        self.ProfileButton.setText(_translate("MainWindow", "Profile"))
        self.LogOUt.setText(_translate("MainWindow", "LogOut"))
        self.GroupsButton.setText(_translate("MainWindow", "Groups"))
        self.Matches.setTitle(_translate("MainWindow", "Top Three Matches"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Community Garden</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Description</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "View Group Page [Non-Members]"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Michelle Garden</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Interests and Skills</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "View Profile"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Park Garden</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Description</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "View Group Page [Non-Members]"))
        self.SearchMessage.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Did Not Find What You\'re Looking For? Try Another Search.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
