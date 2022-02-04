from PyQt5 import QtCore, QtGui, QtWidgets

class Manager_First_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 351)
        Dialog.setStyleSheet("background-color: rgb(255, 190, 191);")
        self.registred_users_button = QtWidgets.QPushButton(Dialog)
        self.registred_users_button.setGeometry(QtCore.QRect(130, 50, 131, 41))
        self.registred_users_button.setObjectName("registred_users_button")
        self.number_of_user_lable_show = QtWidgets.QLabel(Dialog)
        self.number_of_user_lable_show.setGeometry(QtCore.QRect(54, 110, 71, 21))
        self.number_of_user_lable_show.setText("")
        self.number_of_user_lable_show.setObjectName("number_of_user_lable_show")
        self.warehousekeeper_registred_button = QtWidgets.QPushButton(Dialog)
        self.warehousekeeper_registred_button.setGeometry(QtCore.QRect(130, 110, 131, 41))
        self.warehousekeeper_registred_button.setObjectName("warehousekeeper_registred_button")
        self.number_of_house_keeper_show_lable = QtWidgets.QLabel(Dialog)
        self.number_of_house_keeper_show_lable.setGeometry(QtCore.QRect(70, 170, 61, 20))
        self.number_of_house_keeper_show_lable.setText("")
        self.number_of_house_keeper_show_lable.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.number_of_house_keeper_show_lable.setObjectName("number_of_house_keeper_show_lable")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 240, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.Allthefactorsformanger_button = QtWidgets.QPushButton(Dialog)
        self.Allthefactorsformanger_button.setGeometry(QtCore.QRect(90, 160, 201, 41))
        self.Allthefactorsformanger_button.setObjectName("Allthefactorsformanger_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.registred_users_button.setText(_translate("Dialog", "کاربران ثبت شده"))
        self.warehousekeeper_registred_button.setText(_translate("Dialog", "انبارداران ثبت شده"))
        self.pushButton.setText(_translate("Dialog", "خروج از حساب کاربری"))
        self.Allthefactorsformanger_button.setText(_translate("Dialog", "مشاهده تمام فاکتور های فروش"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Manager_First_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

