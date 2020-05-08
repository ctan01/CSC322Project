
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreatePost(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 281)
        self.Publish = QtWidgets.QDialogButtonBox(Dialog)
        self.Publish.setGeometry(QtCore.QRect(190, 240, 201, 32))
        self.Publish.setOrientation(QtCore.Qt.Horizontal)
        self.Publish.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Publish.setObjectName("Publish")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        self.Publish.accepted.connect(Dialog.accept)
        self.Publish.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Write Post Here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_CreatePost()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
