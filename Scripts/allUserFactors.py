from PyQt5 import QtCore, QtGui, QtWidgets

class All_User_Factor_UI(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 577)
        self.successfull_lable = QtWidgets.QLabel(Dialog)
        self.successfull_lable.setGeometry(QtCore.QRect(210, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.successfull_lable.setFont(font)
        self.successfull_lable.setObjectName("successfull_lable")
        self.factortable = QtWidgets.QTableWidget(Dialog)
        self.factortable.setGeometry(QtCore.QRect(20, 100, 511, 381))
        self.factortable.setObjectName("factortable")
        self.factortable.setColumnCount(4)
        self.factortable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.factortable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.factortable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.factortable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.factortable.setHorizontalHeaderItem(3, item)
        self.rebuy_button = QtWidgets.QPushButton(Dialog)
        self.rebuy_button.setGeometry(QtCore.QRect(420, 510, 93, 28))
        self.rebuy_button.setObjectName("rebuy_button")
        self.to_see_all_factors_button = QtWidgets.QPushButton(Dialog)
        self.to_see_all_factors_button.setGeometry(QtCore.QRect(242, 67, 231, 31))
        self.to_see_all_factors_button.setObjectName("to_see_all_factors_button")
        self.exit_button = QtWidgets.QPushButton(Dialog)
        self.exit_button.setGeometry(QtCore.QRect(310, 510, 93, 28))
        self.exit_button.setObjectName("exit_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.successfull_lable.setText(_translate("Dialog", "پرداخت موفقیت آمیز انجام شد"))
        item = self.factortable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "نام کالا"))
        item = self.factortable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "کد کالا"))
        item = self.factortable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "قیمت کالا"))
        item = self.factortable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "تاریخ خرید "))
        self.rebuy_button.setText(_translate("Dialog", "خرید مجدد"))
        self.to_see_all_factors_button.setText(_translate("Dialog", "برای دیدن فاکتور های خودتان کلیک کنید"))
        self.exit_button.setText(_translate("Dialog", "خروج از برنامه"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = All_User_Factor_UI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

