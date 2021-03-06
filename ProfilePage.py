from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_profilePage(object):

    def setupUi(self, ProfilePage):
        df = pd.read_csv('UserData.csv')
        count = df.shape[0]
        ProfilePage.setObjectName("ProfilePage")
        ProfilePage.resize(398, 531)
        self.centralwidget = QtWidgets.QWidget(ProfilePage)
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
        self.label_Projects.setGeometry(QtCore.QRect(10, 280, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Projects.setFont(font)
        self.label_Projects.setObjectName("label_Projects")
        self.label_Score = QtWidgets.QLabel(self.centralwidget)
        self.label_Score.setGeometry(QtCore.QRect(10, 390, 54, 12))
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
        self.textBrowser_Score.setGeometry(QtCore.QRect(70, 380, 41, 31))
        self.textBrowser_Score.setObjectName("textBrowser_Score")
        self.label_Inerest = QtWidgets.QLabel(self.centralwidget)
        self.label_Inerest.setGeometry(QtCore.QRect(10, 180, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Inerest.setFont(font)
        self.label_Inerest.setObjectName("label_Inerest")
        self.label_SkillSets = QtWidgets.QLabel(self.centralwidget)
        self.label_SkillSets.setGeometry(QtCore.QRect(10, 230, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_SkillSets.setFont(font)
        self.label_SkillSets.setObjectName("label_SkillSets")
        self.pushButton_Edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Edit.setGeometry(QtCore.QRect(280, 430, 81, 31))
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
        self.label_Status.setGeometry(QtCore.QRect(10, 330, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_Status.setFont(font)
        self.label_Status.setObjectName("label_Status")
        self.textBrowser_Status = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Status.setGeometry(QtCore.QRect(70, 320, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.textBrowser_Status.setFont(font)
        self.textBrowser_Status.setObjectName("textBrowser_Status")
        self.comboBox_Interest = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Interest.setGeometry(QtCore.QRect(70, 170, 291, 31))
        self.comboBox_Interest.setObjectName("comboBox_Interest")
        self.comboBox_SkillSets = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_SkillSets.setGeometry(QtCore.QRect(70, 220, 291, 31))
        self.comboBox_SkillSets.setObjectName("comboBox_SkillSets")
        self.comboBox_Projects = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Projects.setGeometry(QtCore.QRect(70, 270, 291, 31))
        self.comboBox_Projects.setObjectName("comboBox_Projects")
        ProfilePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProfilePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 21))
        self.menubar.setObjectName("menubar")
        ProfilePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProfilePage)
        self.statusbar.setObjectName("statusbar")
        ProfilePage.setStatusBar(self.statusbar)

        self.retranslateUi(ProfilePage)
        QtCore.QMetaObject.connectSlotsByName(ProfilePage)

        while count != -1:
            self.comboBox_Interest.addItem("")
            count -= 1

        count = df.shape[0]

        while count != -1:
            self.comboBox_SkillSets.addItem("")
            count -= 1

        count = df.shape[0]

        while count != -1:
            self.comboBox_Projects.addItem("")
            count -= 1

        count = df.shape[0]

        self.retranslateUi(ProfilePage)
        QtCore.QMetaObject.connectSlotsByName(ProfilePage)

    def retranslateUi(self, ProfilePage):
        df = pd.read_csv('UserData.csv')

        for index, row in df.iterrows():
            if row['CurrentUser'] == 1:
                current_user_index = index
                print(current_user_index)

        combo_count = df.shape[0]
        i = 0

        current_user_id = current_user_index + 1
        _translate = QtCore.QCoreApplication.translate
        ProfilePage.setWindowTitle(_translate("ProfilePage", "MainWindow"))
        self.label_Name.setText(_translate("ProfilePage", "Name:"))
        self.label_Email.setText(_translate("ProfilePage", "Email:"))
        self.label_Projects.setText(_translate("ProfilePage", "Projects:"))
        self.label_Score.setText(_translate("ProfilePage", "Score:"))
        self.textBrowse_Name.setHtml(_translate("ProfilePage", df.loc[current_user_index, 'First_Name'] + " " + df.loc[
            current_user_index, 'Last_Name']))
        self.textBrowser_Email.setHtml(_translate("ProfilePage", df.loc[current_user_index, 'Email']))
        self.textBrowser_Score.setHtml(_translate("ProfilePage", str(df.loc[current_user_index, 'Reputation_Score'])))
        print(df.loc[current_user_index, 'Reputation_Score'])
        self.label_Inerest.setText(_translate("ProfilePage", "Interest:"))
        self.label_SkillSets.setText(_translate("ProfilePage", "Skill sets:"))
        self.pushButton_Edit.setText(_translate("ProfilePage", "Edit"))
        self.label_UserID.setText(_translate("ProfilePage", "User ID:"))
        self.textBrowse_UserID.setHtml(_translate("ProfilePage", str(df.loc[current_user_index, 'UserID'])))
        self.label_Status.setText(_translate("ProfilePage", "Status: "))
        self.textBrowser_Status.setHtml(_translate("ProfilePage", df.loc[current_user_index, 'Status']))

        """interests = []

        if df.iloc[current_user_index, 'Interests0'] == 'Education':
            interests.append(df.iloc[current_user_index, 'Interests1'])
        if df.iloc[current_user_index, 'Interests0'] == 'Reading':
            interests.append(df.iloc[current_user_index, 'Interests2'])
        if df.iloc[current_user_index, 'Interests0'] == 'Coding':
            interests.append(df.iloc[current_user_index, 'Interests3'])
        if df.iloc[current_user_index, 'Interests0'] == 'Environment':
            interests.append(df.iloc[current_user_index, 'Interests4'])
        if df.iloc[current_user_index, 'Interests0'] == 'Sports':
            interests.append(df.iloc[current_user_index, 'Interests5'])
        if df.iloc[current_user_index, 'Interests0'] == 'Design':
            interests.append(df.iloc[current_user_index, 'Interests6'])
        if df.iloc[current_user_index, 'Interests0'] == 'Finance':
            interests.append(df.iloc[current_user_index, 'Interests7'])
        if df.iloc[current_user_index, 'Interests0'] == 'Technology':
            interests.append(df.iloc[current_user_index, 'Interests8'])
        if df.iloc[current_user_index, 'Interests0'] == 'Kids':
            interests.append(df.iloc[current_user_index, 'Interests9'])
        if df.iloc[current_user_index, 'Interests0'] == 'Family Activities':
            interests.append(df.iloc[current_user_index, 'Interests10'])
        if df.iloc[current_user_index, 'Interests0'] == 'Public Welfare':
            interests.append(df.iloc[current_user_index, 'Interests11'])

        print(interests)
"""
        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_Interest.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0

        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_SkillSets.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0

        while combo_count != 0:
            if i == 0:
                i += 1
                combo_count -= 1
            else:
                self.comboBox_Projects.setItemText(i, _translate("MainWindow", df.at[i, 'Username']))
                i += 1
                combo_count -= 1

        combo_count = df.shape[0]
        i = 0


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ProfilePage = QtWidgets.QMainWindow()
    ui = Ui_profilePage()
    ui.setupUi(ProfilePage)
    ProfilePage.show()
    sys.exit(app.exec_())
