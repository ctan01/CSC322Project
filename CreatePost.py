from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pandas as pd


class Ui_CreatePost(object):
    def publishPost(self):
        df = pd.read_csv('Posts.csv')
        
        # part that will check which groupID currentGroup has value 1

        # PostID, GroupID, PostContents, Comment0, Comment1, Comment2,Comment3
        new_row = {'PostID': len(df.index),
            'GroupID' : 'UNK',
            'PostContents': self.lineEdit_Postcontents.text(),
            'Comment0': None,
            'Comment1': None,
            'Comment2': None,
            'Comment3': None
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
