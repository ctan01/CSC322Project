from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


# ProfilePage
class Ui_profilePage(object):
    def setupUi(self, profilePage):
        profilePage.setObjectName("ProfilePage")
        profilePage.resize(402, 650)
        self.centralwidget = QtWidgets.QWidget(profilePage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Name = QtWidgets.QLabel(self.centralwidget)
        self.label_Name.setGeometry(QtCore.QRect(10, 80, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Name.setFont(font)
        self.label_Name.setObjectName("label_Name")
        self.label_Email = QtWidgets.QLabel(self.centralwidget)
        self.label_Email.setGeometry(QtCore.QRect(10, 130, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Email.setFont(font)
        self.label_Email.setObjectName("label_Email")
        self.label_Projects = QtWidgets.QLabel(self.centralwidget)
        self.label_Projects.setGeometry(QtCore.QRect(10, 370, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Projects.setFont(font)
        self.label_Projects.setObjectName("label_Projects")
        self.label_Score = QtWidgets.QLabel(self.centralwidget)
        self.label_Score.setGeometry(QtCore.QRect(10, 530, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Score.setFont(font)
        self.label_Score.setObjectName("label_Score")
        self.textBrowse_Name = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowse_Name.setGeometry(QtCore.QRect(70, 70, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowse_Name.setFont(font)
        self.textBrowse_Name.setObjectName("textBrowse_Name")
        self.textBrowser_Email = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Email.setGeometry(QtCore.QRect(70, 120, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowser_Email.setFont(font)
        self.textBrowser_Email.setObjectName("textBrowser_Email")
        self.textBrowser_Score = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Score.setGeometry(QtCore.QRect(70, 520, 41, 31))
        self.textBrowser_Score.setObjectName("textBrowser_Score")
        self.label_Inerest = QtWidgets.QLabel(self.centralwidget)
        self.label_Inerest.setGeometry(QtCore.QRect(10, 170, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Inerest.setFont(font)
        self.label_Inerest.setObjectName("label_Inerest")
        self.label_SkillSets = QtWidgets.QLabel(self.centralwidget)
        self.label_SkillSets.setGeometry(QtCore.QRect(10, 270, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_SkillSets.setFont(font)
        self.label_SkillSets.setObjectName("label_SkillSets")
        self.textBrowser_Projects = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Projects.setGeometry(QtCore.QRect(70, 370, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowser_Projects.setFont(font)
        self.textBrowser_Projects.setObjectName("textBrowser_Projects")
        self.textBrowser_SkillSets = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_SkillSets.setGeometry(QtCore.QRect(70, 270, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowser_SkillSets.setFont(font)
        self.textBrowser_SkillSets.setObjectName("textBrowser_SkillSets")
        self.textBrowser_Inerest = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Inerest.setGeometry(QtCore.QRect(70, 170, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowser_Inerest.setFont(font)
        self.textBrowser_Inerest.setObjectName("textBrowser_Inerest")
        self.pushButton_Edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Edit.setGeometry(QtCore.QRect(280, 570, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_Edit.setFont(font)
        self.pushButton_Edit.setObjectName("pushButton_Edit")
        self.label_UserID = QtWidgets.QLabel(self.centralwidget)
        self.label_UserID.setGeometry(QtCore.QRect(10, 30, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_UserID.setFont(font)
        self.label_UserID.setObjectName("label_UserID")
        self.textBrowse_UserID = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowse_UserID.setGeometry(QtCore.QRect(70, 20, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowse_UserID.setFont(font)
        self.textBrowse_UserID.setObjectName("textBrowse_UserID")
        self.label_Status = QtWidgets.QLabel(self.centralwidget)
        self.label_Status.setGeometry(QtCore.QRect(10, 470, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Status.setFont(font)
        self.label_Status.setObjectName("label_Status")
        self.textBrowser_Status = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Status.setGeometry(QtCore.QRect(70, 460, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowser_Status.setFont(font)
        self.textBrowser_Status.setObjectName("textBrowser_Status")
        profilePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(profilePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName("menubar")
        profilePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(profilePage)
        self.statusbar.setObjectName("statusbar")
        profilePage.setStatusBar(self.statusbar)

        self.retranslateUi(profilePage)
        QtCore.QMetaObject.connectSlotsByName(profilePage)

    def retranslateUi(self, ProfilePage):
        _translate = QtCore.QCoreApplication.translate
        ProfilePage.setWindowTitle(_translate("ProfilePage", "MainWindow"))
        self.label_Name.setText(_translate("ProfilePage", "Name:"))
        self.label_Email.setText(_translate("ProfilePage", "Email:"))
        self.label_Projects.setText(_translate("ProfilePage", "Projects:"))
        self.label_Score.setText(_translate("ProfilePage", "Score:"))
        self.textBrowse_Name.setHtml(_translate("ProfilePage",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.textBrowser_Email.setHtml(_translate("ProfilePage",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.textBrowser_Score.setHtml(_translate("ProfilePage",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.label_Inerest.setText(_translate("ProfilePage", "Interest:"))
        self.label_SkillSets.setText(_translate("ProfilePage", "Skill sets:"))
        self.textBrowser_Projects.setHtml(_translate("ProfilePage",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.textBrowser_SkillSets.setHtml(_translate("ProfilePage",
                                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.textBrowser_Inerest.setHtml(_translate("ProfilePage",
                                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.pushButton_Edit.setText(_translate("ProfilePage", "Edit"))
        self.label_UserID.setText(_translate("ProfilePage", "User ID:"))
        self.textBrowse_UserID.setHtml(_translate("ProfilePage",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.label_Status.setText(_translate("ProfilePage", "Status: "))
        self.textBrowser_Status.setHtml(_translate("ProfilePage",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ProfilePage = QtWidgets.QMainWindow()
    ui = Ui_profilePage()
    ui.setupUi(ProfilePage)
    ProfilePage.show()
    sys.exit(app.exec_())
