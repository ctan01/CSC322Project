# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initialRepScore1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reputationScore(object):
    def setupUi(self, reputationScore):
        reputationScore.setObjectName("reputationScore")
        reputationScore.resize(449, 217)
        self.centralwidget = QtWidgets.QWidget(reputationScore)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 451, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(180, 90, 73, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 25, 291, 41))
        self.label.setObjectName("label")
        reputationScore.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(reputationScore)
        self.statusbar.setObjectName("statusbar")
        reputationScore.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(reputationScore.close)
        self.retranslateUi(reputationScore)
        QtCore.QMetaObject.connectSlotsByName(reputationScore)

    def retranslateUi(self, reputationScore):
        _translate = QtCore.QCoreApplication.translate
        reputationScore.setWindowTitle(_translate("reputationScore", "MainWindow"))
        self.pushButton.setText(_translate("reputationScore", "cancel"))
        self.pushButton_2.setText(_translate("reputationScore", "confirm"))
        self.comboBox.setItemText(0, _translate("reputationScore", "0"))
        self.comboBox.setItemText(1, _translate("reputationScore", "1"))
        self.comboBox.setItemText(2, _translate("reputationScore", "2"))
        self.comboBox.setItemText(3, _translate("reputationScore", "3"))
        self.comboBox.setItemText(4, _translate("reputationScore", "4"))
        self.comboBox.setItemText(5, _translate("reputationScore", "5"))
        self.comboBox.setItemText(6, _translate("reputationScore", "6"))
        self.comboBox.setItemText(7, _translate("reputationScore", "7"))
        self.comboBox.setItemText(8, _translate("reputationScore", "8"))
        self.comboBox.setItemText(9, _translate("reputationScore", "9"))
        self.comboBox.setItemText(10, _translate("reputationScore", "10"))
        self.comboBox.setItemText(11, _translate("reputationScore", "11"))
        self.comboBox.setItemText(12, _translate("reputationScore", "12"))
        self.comboBox.setItemText(13, _translate("reputationScore", "13"))
        self.comboBox.setItemText(14, _translate("reputationScore", "14"))
        self.comboBox.setItemText(15, _translate("reputationScore", "15"))
        self.comboBox.setItemText(16, _translate("reputationScore", "16"))
        self.comboBox.setItemText(17, _translate("reputationScore", "17"))
        self.comboBox.setItemText(18, _translate("reputationScore", "18"))
        self.comboBox.setItemText(19, _translate("reputationScore", "19"))
        self.comboBox.setItemText(20, _translate("reputationScore", "20"))
        self.label.setText(_translate("reputationScore", "Enter the initial reputation score for the new user"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reputationScore = QtWidgets.QMainWindow()
    ui = Ui_reputationScore()
    ui.setupUi(reputationScore)
    reputationScore.show()
    sys.exit(app.exec_())
