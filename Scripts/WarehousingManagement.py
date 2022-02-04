from PyQt5 import QtCore, QtGui, QtWidgets

class Warehousing_Management_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(999, 691)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(198, 255, 252);")
        self.ALISHHDE_LABLE = QtWidgets.QLabel(Dialog)
        self.ALISHHDE_LABLE.setGeometry(QtCore.QRect(10, 670, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        self.ALISHHDE_LABLE.setFont(font)
        self.ALISHHDE_LABLE.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ALISHHDE_LABLE.setObjectName("ALISHHDE_LABLE")
        self.stufftable = QtWidgets.QTableWidget(Dialog)
        self.stufftable.setGeometry(QtCore.QRect(330, 50, 651, 561))
        self.stufftable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stufftable.setObjectName("stufftable")
        self.stufftable.setColumnCount(5)
        self.stufftable.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.stufftable.setHorizontalHeaderItem(4, item)
        self.signoutbutton = QtWidgets.QPushButton(Dialog)
        self.signoutbutton.setGeometry(QtCore.QRect(790, 630, 171, 31))
        self.signoutbutton.setObjectName("signoutbutton")
        self.creatingaoffcodebutton = QtWidgets.QPushButton(Dialog)
        self.creatingaoffcodebutton.setGeometry(QtCore.QRect(60, 90, 181, 41))
        self.creatingaoffcodebutton.setObjectName("creatingaoffcodebutton")
        self.existencestufflable = QtWidgets.QLabel(Dialog)
        self.existencestufflable.setGeometry(QtCore.QRect(340, 20, 121, 20))
        self.existencestufflable.setAlignment(QtCore.Qt.AlignCenter)
        self.existencestufflable.setObjectName("existencestufflable")
        self.saveingnewstuffbutton = QtWidgets.QPushButton(Dialog)
        self.saveingnewstuffbutton.setGeometry(QtCore.QRect(10, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.saveingnewstuffbutton.setFont(font)
        self.saveingnewstuffbutton.setObjectName("saveingnewstuffbutton")
        self.offcode_lable = QtWidgets.QLabel(Dialog)
        self.offcode_lable.setGeometry(QtCore.QRect(90, 150, 121, 31))
        self.offcode_lable.setText("")
        self.offcode_lable.setObjectName("offcode_lable")
        self.load_button = QtWidgets.QPushButton(Dialog)
        self.load_button.setGeometry(QtCore.QRect(100, 310, 93, 28))
        self.load_button.setObjectName("load_button")
        self.load_details_lable = QtWidgets.QLabel(Dialog)
        self.load_details_lable.setGeometry(QtCore.QRect(40, 280, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.load_details_lable.setFont(font)
        self.load_details_lable.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.load_details_lable.setObjectName("load_details_lable")
        self.delete_button = QtWidgets.QPushButton(Dialog)
        self.delete_button.setGeometry(QtCore.QRect(230, 410, 71, 21))
        self.delete_button.setObjectName("delete_button")
        self.detailslable = QtWidgets.QLabel(Dialog)
        self.detailslable.setGeometry(QtCore.QRect(20, 370, 241, 21))
        self.detailslable.setObjectName("detailslable")
        self.get_code_item_delete_lineedit = QtWidgets.QLineEdit(Dialog)
        self.get_code_item_delete_lineedit.setGeometry(QtCore.QRect(10, 410, 201, 21))
        self.get_code_item_delete_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.get_code_item_delete_lineedit.setObjectName("get_code_item_delete_lineedit")
        self.update_button = QtWidgets.QPushButton(Dialog)
        self.update_button.setGeometry(QtCore.QRect(160, 220, 121, 31))
        self.update_button.setObjectName("update_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ALISHHDE_LABLE.setText(_translate("Dialog", "©ALI SHHDE"))
        item = self.stufftable.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.stufftable.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.stufftable.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.stufftable.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.stufftable.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.stufftable.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.stufftable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "نام"))
        item = self.stufftable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "برند"))
        item = self.stufftable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "قیمت"))
        item = self.stufftable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "کد"))
        item = self.stufftable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "موجودی"))
        self.signoutbutton.setText(_translate("Dialog", "خروج از حساب کاربری"))
        self.creatingaoffcodebutton.setText(_translate("Dialog", "درست کردن کد تخفیف"))
        self.existencestufflable.setText(_translate("Dialog", "کالا های موجود"))
        self.saveingnewstuffbutton.setText(_translate("Dialog", "افزودن کردن کالای جدید"))
        self.load_button.setText(_translate("Dialog", "LOAD"))
        self.load_details_lable.setText(_translate("Dialog", "برای به روز شدن انبار دکمه زیر را فشار دهید"))
        self.delete_button.setText(_translate("Dialog", "حذف"))
        self.detailslable.setText(_translate("Dialog", "کد ایتمی که میخواهید حذف کنید را وارد کنید"))
        self.update_button.setText(_translate("Dialog", "بروز رسانی داده"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Warehousing_Management_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
