from PyQt5 import QtCore, QtGui, QtWidgets

class Table_of_user_factos_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(565, 646)
        self.factor_table_for_warehouse = QtWidgets.QTableWidget(Dialog)
        self.factor_table_for_warehouse.setGeometry(QtCore.QRect(60, 50, 401, 421))
        self.factor_table_for_warehouse.setObjectName("factor_table_for_warehouse")
        self.factor_table_for_warehouse.setColumnCount(3)
        self.factor_table_for_warehouse.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.factor_table_for_warehouse.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.factor_table_for_warehouse.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.factor_table_for_warehouse.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.factor_table_for_warehouse.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.factor_table_for_warehouse.setHorizontalHeaderItem(2, item)
        self.back_button = QtWidgets.QPushButton(Dialog)
        self.back_button.setGeometry(QtCore.QRect(430, 550, 93, 28))
        self.back_button.setObjectName("back_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.factor_table_for_warehouse.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.factor_table_for_warehouse.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.factor_table_for_warehouse.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "نام"))
        item = self.factor_table_for_warehouse.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "کالا"))
        item = self.factor_table_for_warehouse.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "تاریخ"))
        self.back_button.setText(_translate("Dialog", "برگشت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Table_of_user_factos_ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

