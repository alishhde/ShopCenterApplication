from PyQt5 import QtCore, QtGui, QtWidgets

class StartPage_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(894, 443)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Dialog.setStyleSheet("background-color: rgb(234, 245, 239);")
        self.entertoyouraccountbutton = QtWidgets.QPushButton(Dialog)
        self.entertoyouraccountbutton.setGeometry(QtCore.QRect(270, 180, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        font.setItalic(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.entertoyouraccountbutton.setFont(font)
        self.entertoyouraccountbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.entertoyouraccountbutton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.entertoyouraccountbutton.setStyleSheet("background-color: rgb(250, 255, 242);\n"
"border-color: rgb(244, 255, 252);")
        self.entertoyouraccountbutton.setObjectName("entertoyouraccountbutton")
        self.newcustomerlable = QtWidgets.QLabel(Dialog)
        self.newcustomerlable.setGeometry(QtCore.QRect(450, 280, 121, 21))
        self.newcustomerlable.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.newcustomerlable.setObjectName("newcustomerlable")
        self.signupbutton = QtWidgets.QPushButton(Dialog)
        self.signupbutton.setGeometry(QtCore.QRect(340, 280, 93, 28))
        self.signupbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupbutton.setObjectName("signupbutton")
        self.anyquestionbutton = QtWidgets.QPushButton(Dialog)
        self.anyquestionbutton.setGeometry(QtCore.QRect(790, 410, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.anyquestionbutton.setFont(font)
        self.anyquestionbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.anyquestionbutton.setObjectName("anyquestionbutton")
        self.alishhdetaglable = QtWidgets.QLabel(Dialog)
        self.alishhdetaglable.setGeometry(QtCore.QRect(660, 30, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.alishhdetaglable.setFont(font)
        self.alishhdetaglable.setAlignment(QtCore.Qt.AlignCenter)
        self.alishhdetaglable.setObjectName("alishhdetaglable")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.entertoyouraccountbutton.setText(_translate("Dialog", "به حساب کاربری خود وارد شوید"))
        self.newcustomerlable.setText(_translate("Dialog", "کاربر جدید هستید ؟"))
        self.signupbutton.setText(_translate("Dialog", "! ثبت نام"))
        self.anyquestionbutton.setText(_translate("Dialog", "سوالی دارید ؟"))
        self.alishhdetaglable.setText(_translate("Dialog", "ALI SHHDE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

