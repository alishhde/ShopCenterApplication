from PyQt5 import QtCore, QtGui, QtWidgets

class Add_New_housekeeper_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(277, 324)
        Dialog.setStyleSheet("background-color: rgb(225, 255, 238);")
        self.password_lable = QtWidgets.QLabel(Dialog)
        self.password_lable.setGeometry(QtCore.QRect(200, 140, 55, 16))
        self.password_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lable.setObjectName("password_lable")
        self.back_button = QtWidgets.QPushButton(Dialog)
        self.back_button.setGeometry(QtCore.QRect(40, 240, 71, 28))
        self.back_button.setObjectName("back_button")
        self.email_lineedit = QtWidgets.QLineEdit(Dialog)
        self.email_lineedit.setGeometry(QtCore.QRect(30, 180, 151, 21))
        self.email_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_lineedit.setObjectName("email_lineedit")
        self.email_lable = QtWidgets.QLabel(Dialog)
        self.email_lable.setGeometry(QtCore.QRect(200, 180, 55, 16))
        self.email_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.email_lable.setObjectName("email_lable")
        self.usernamelineedit = QtWidgets.QLineEdit(Dialog)
        self.usernamelineedit.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.usernamelineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.usernamelineedit.setObjectName("usernamelineedit")
        self.namelable = QtWidgets.QLabel(Dialog)
        self.namelable.setGeometry(QtCore.QRect(200, 60, 55, 16))
        self.namelable.setAlignment(QtCore.Qt.AlignCenter)
        self.namelable.setObjectName("namelable")
        self.password_lineedit = QtWidgets.QLineEdit(Dialog)
        self.password_lineedit.setGeometry(QtCore.QRect(30, 140, 151, 21))
        self.password_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_lineedit.setObjectName("password_lineedit")
        self.add_button = QtWidgets.QPushButton(Dialog)
        self.add_button.setGeometry(QtCore.QRect(118, 240, 71, 28))
        self.add_button.setObjectName("add_button")
        self.usernamelable = QtWidgets.QLabel(Dialog)
        self.usernamelable.setGeometry(QtCore.QRect(200, 100, 55, 16))
        self.usernamelable.setAlignment(QtCore.Qt.AlignCenter)
        self.usernamelable.setObjectName("usernamelable")
        self.name_lineedit = QtWidgets.QLineEdit(Dialog)
        self.name_lineedit.setGeometry(QtCore.QRect(30, 60, 151, 20))
        self.name_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.name_lineedit.setObjectName("name_lineedit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.password_lable.setText(_translate("Dialog", "رمز عبور"))
        self.back_button.setText(_translate("Dialog", "برگشت"))
        self.email_lable.setText(_translate("Dialog", "ایمیل"))
        self.namelable.setText(_translate("Dialog", "نام"))
        self.add_button.setText(_translate("Dialog", "اضافه کردن"))
        self.usernamelable.setText(_translate("Dialog", "نام کاربری"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Add_New_housekeeper_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

