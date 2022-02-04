from PyQt5 import QtCore, QtGui, QtWidgets

class Edit_User_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 403)
        Dialog.setStyleSheet("alternate-background-color: rgb(255, 215, 227);")
        self.new_name_lineedit = QtWidgets.QLineEdit(Dialog)
        self.new_name_lineedit.setGeometry(QtCore.QRect(90, 170, 151, 20))
        self.new_name_lineedit.setObjectName("new_name_lineedit")
        self.newusernamelineedit = QtWidgets.QLineEdit(Dialog)
        self.newusernamelineedit.setGeometry(QtCore.QRect(90, 210, 151, 21))
        self.newusernamelineedit.setObjectName("newusernamelineedit")
        self.new_password_lineedit = QtWidgets.QLineEdit(Dialog)
        self.new_password_lineedit.setGeometry(QtCore.QRect(90, 250, 151, 21))
        self.new_password_lineedit.setObjectName("new_password_lineedit")
        self.new_email_lineedit = QtWidgets.QLineEdit(Dialog)
        self.new_email_lineedit.setGeometry(QtCore.QRect(90, 290, 151, 21))
        self.new_email_lineedit.setObjectName("new_email_lineedit")
        self.detailslable = QtWidgets.QLabel(Dialog)
        self.detailslable.setGeometry(QtCore.QRect(100, 130, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.detailslable.setFont(font)
        self.detailslable.setStyleSheet("color: rgb(255, 42, 0);")
        self.detailslable.setObjectName("detailslable")
        self.new_name_lable = QtWidgets.QLabel(Dialog)
        self.new_name_lable.setGeometry(QtCore.QRect(280, 170, 55, 16))
        self.new_name_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.new_name_lable.setObjectName("new_name_lable")
        self.new_username_lable = QtWidgets.QLabel(Dialog)
        self.new_username_lable.setGeometry(QtCore.QRect(260, 210, 91, 20))
        self.new_username_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.new_username_lable.setObjectName("new_username_lable")
        self.new_password_lable = QtWidgets.QLabel(Dialog)
        self.new_password_lable.setGeometry(QtCore.QRect(280, 250, 55, 16))
        self.new_password_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.new_password_lable.setObjectName("new_password_lable")
        self.new_email_lable = QtWidgets.QLabel(Dialog)
        self.new_email_lable.setGeometry(QtCore.QRect(280, 290, 55, 16))
        self.new_email_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.new_email_lable.setObjectName("new_email_lable")
        self.details_labl = QtWidgets.QLabel(Dialog)
        self.details_labl.setGeometry(QtCore.QRect(120, 40, 261, 20))
        self.details_labl.setObjectName("details_labl")
        self.enter_username_wants_to_edit_lineedit = QtWidgets.QLineEdit(Dialog)
        self.enter_username_wants_to_edit_lineedit.setGeometry(QtCore.QRect(20, 70, 201, 21))
        self.enter_username_wants_to_edit_lineedit.setObjectName("enter_username_wants_to_edit_lineedit")
        self.edit_button = QtWidgets.QPushButton(Dialog)
        self.edit_button.setGeometry(QtCore.QRect(180, 340, 93, 28))
        self.edit_button.setObjectName("edit_button")
        self.back_button = QtWidgets.QPushButton(Dialog)
        self.back_button.setGeometry(QtCore.QRect(80, 340, 93, 28))
        self.back_button.setObjectName("back_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.detailslable.setText(_translate("Dialog", "هشدار : تمام فیلد های زیر جایگزین خواهند شد"))
        self.new_name_lable.setText(_translate("Dialog", "نام جدید"))
        self.new_username_lable.setText(_translate("Dialog", "نام کاربری جدید"))
        self.new_password_lable.setText(_translate("Dialog", "رمز عبور"))
        self.new_email_lable.setText(_translate("Dialog", "ایمیل"))
        self.details_labl.setText(_translate("Dialog", "نام کاربری، کاربری که میخواهید تصحیح کنید ؟"))
        self.edit_button.setText(_translate("Dialog", "تصحیح"))
        self.back_button.setText(_translate("Dialog", "برگشت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Edit_User_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
