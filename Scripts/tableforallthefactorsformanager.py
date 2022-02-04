from PyQt5 import QtCore, QtGui, QtWidgets

class All_The_Factors_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(819, 580)
        Dialog.setStyleSheet("background-color: rgb(112, 212, 255);")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(290, 30, 511, 461))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.enter_to_load_button = QtWidgets.QPushButton(Dialog)
        self.enter_to_load_button.setGeometry(QtCore.QRect(90, 40, 181, 31))
        self.enter_to_load_button.setObjectName("enter_to_load_button")
        self.back_button = QtWidgets.QPushButton(Dialog)
        self.back_button.setGeometry(QtCore.QRect(550, 520, 91, 31))
        self.back_button.setObjectName("back_button")
        self.logout_button = QtWidgets.QPushButton(Dialog)
        self.logout_button.setGeometry(QtCore.QRect(652, 520, 131, 31))
        self.logout_button.setObjectName("logout_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "نام کالا"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "کد کالا"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "قیمت کالا"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "نام کاربری"))
        self.enter_to_load_button.setText(_translate("Dialog", "برای به روز رسانی کلیک کنید"))
        self.back_button.setText(_translate("Dialog", "قبلی"))
        self.logout_button.setText(_translate("Dialog", "خروج از حساب کاربری"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = All_The_Factors_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

