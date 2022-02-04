                                            ###################          WHAT          ###################
                                            ###################         DOESN'T        ###################
                                            ###################          KILL          ###################
                                            ###################          YOU           ###################
                                            ###################         MAKES          ###################
                                            ###################          YOU           ###################
                                            ###################        STRONGER        ###################
                                            ###################        ALI SHHDE       ###################
                                            ###############     S.T.NUM 971 229 200 12       #############
                                            ####### Shop Application Created By Ali shohadahoseini #######
import sys
from sqlite3 import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem, QMessageBox
from startpage import *
from Loginpage import *
from Signuppage import *
from CustomerBuyingPage import *
from WarehousingManagement import *
from DB import *
from string import *
from Factor_table import *
from tableofuserfactor import *
from EnterNewStuffToSave import *
from Update_items import *
from managehousekeeperByManager import * 
from manager_first_page import *
from manageUserByManager import *
from EdithousekeeperinfoByManager import *
from EditUserInfoByManager import *
from manager_add_new_customer import *
from manager_add_new_houskeeper import *
from allUserFactors import *
from tableforallthefactorsformanager import *

class Main_Window(QDialog):
    def __init__(self):
        super().__init__()
        self.buying_list_of_chosen = []
        self.start_page_ui = StartPage_ui()
        self.start_page_ui.setupUi(self)
        self.start_page_ui.entertoyouraccountbutton.clicked.connect(self.signin_page)   ## This will execute the signin page 
        self.start_page_ui.signupbutton.clicked.connect(self.signup_page)               ## This will Execute the signup page 
        try:
            self.connection = connect('ProjectsDataBase.db')
        except:
            print("Couldn't open database")
        self.cursor = self.connection.cursor()
        self.main_db = DataBase(self.connection)
        self.main_db.add_new_customer('Ali', 'Alishhde', '9012', 'al.shohadaee@gmail.com')
        self.main_db.add_new_warehouse_keeper('Ali', 'Alishhde', '9012', 'al.shohadaee@gmail.com')
        self.main_db.add_new_manager('Ali', 'Alishhde', '9012')

    def signin_page(self):          ## if User wants to signin
        self.signin_window = QtWidgets.QMainWindow()
        self.signin_ui = SigninPage_ui()
        self.signin_ui.setupUi(self.signin_window)
        window.hide()
        self.signin_window.show()
        self.signin_ui.backbutton.clicked.connect(self.back_to_start_from_signin)
        self.signin_ui.loginbutton.clicked.connect(self.if_we_know_user)

    def if_we_know_user(self):      ## This is for Sign in page if User has already signup
        if self.signin_ui.comboBox.currentText() == "مشتری":
            self.username_entered = self.signin_ui.usernamelineedit.text()
            self.password_entered = self.signin_ui.passwordlinedit.text()
            if self.main_db.if_customer_username_and_password_is_correct(self.username_entered, self.password_entered):
                self.customer_buying_window = QtWidgets.QMainWindow()
                self.customer_buying_ui = Customer_Buying_Page_ui()
                self.customer_buying_ui.setupUi(self.customer_buying_window)
                self.signin_window.hide()
                self.customer_buying_window.show()
                self.customer_buying_ui.backbutton.clicked.connect(self.back_to_signin_from_customer)
                self.customer_buying_ui.updatestuff_button.clicked.connect(self.load_exists_data_to_table_for_customer)
                self.customer_buying_ui.addtolistbutton.clicked.connect(self.add_customer_choose_to_list)
                self.customer_buying_ui.edit_button.clicked.connect(self.edit_customer_item_selected)
                self.customer_buying_ui.delete_button.clicked.connect(self.delete_customer_item_selected)
                self.customer_buying_ui.deleteall_button.clicked.connect(self.delete_all_customer_item)
                self.customer_buying_ui.stufflistchosenlistwidget.itemSelectionChanged.connect(self.get_item_choosen_by_user_to_buy) 
                self.customer_buying_ui.payingmoneybutton.clicked.connect(self.pay_money_page)
        
        elif self.signin_ui.comboBox.currentText() == "انباردار":
            self.username_entered = self.signin_ui.usernamelineedit.text()
            self.password_entered = self.signin_ui.passwordlinedit.text()
            if self.main_db.if_warehouse_keeper_username_and_password_correct(self.username_entered, self.password_entered):
                self.warehousing_window = QtWidgets.QMainWindow()
                self.warehousing_ui = Warehousing_Management_ui()
                self.warehousing_ui.setupUi(self.warehousing_window)
                self.signin_window.hide()
                self.warehousing_window.show()
                self.warehousing_ui.load_button.clicked.connect(self.load_data_to_table_in_warehouse)
                self.warehousing_ui.saveingnewstuffbutton.clicked.connect(self.enter_new_stuff_page)
                self.warehousing_ui.signoutbutton.clicked.connect(self.back_to_signin_page_from_warehouseing)
                self.warehousing_ui.update_button.clicked.connect(self.update_item_page)
                self.warehousing_ui.delete_button.clicked.connect(self.delete_item_asked)

        elif self.signin_ui.comboBox.currentText() == "مدیر فروش":
            self.username_entered = self.signin_ui.usernamelineedit.text()
            self.password_entered = self.signin_ui.passwordlinedit.text()
            if self.main_db.if_manager_username_and_password_correct(self.username_entered, self.password_entered):
                self.manager_first_window = QtWidgets.QMainWindow()
                self.manager_first_ui = Manager_First_ui()
                self.manager_first_ui.setupUi(self.manager_first_window)
                self.signin_window.hide()
                self.manager_first_window.show()
                self.manager_first_ui.pushButton.clicked.connect(self.back_to_signin_from_manager_page)
                self.manager_first_ui.registred_users_button.clicked.connect(self.mange_user_by_manager_page)
                self.manager_first_ui.warehousekeeper_registred_button.clicked.connect(self.mange_housekeeper_by_manager_page)
                self.manager_first_ui.Allthefactorsformanger_button.clicked.connect(self.all_factors_for_manager)

    def signup_page(self):          ## show Sign up page
        self.signup_window = QtWidgets.QMainWindow()
        self.signup_ui = SignupPage_ui()
        self.signup_ui.setupUi(self.signup_window)
        window.hide()
        self.signup_window.show()
        self.signup_ui.backbutton.clicked.connect(self.back_to_start_from_signup)
        self.signup_ui.signupbutton.clicked.connect(self.if_user_is_new_or_password_is_correct)

    def if_user_is_new_or_password_is_correct(self):            ## Check all the conditions for signing up
        self.signup_name = self.signup_ui.namelinedit.text()
        self.username_entered = self.signup_ui.usernamelineedit.text()
        self.signup_email = self.signup_ui.emaillineedit.text()
        self.password_entered = self.signup_ui.passwordlineedit.text()
        self.singup_passwordrep = self.signup_ui.passwordreplineedit.text()
        if self.signup_name == punctuation or self.signup_name == whitespace or self.signup_name == '':
            self.signup_ui.namealarm.setText("علائم غیر مجاز")
            pass
        else:
            self.signup_ui.namealarm.setText("")
            if self.main_db.if_this_username_exists_in_customers(self.username_entered) != False:
                self.signup_ui.usernamealarm.setText("نام کاربری موجود است")
            else:
                self.signup_ui.usernamealarm.setText("")
                if self.password_entered is not whitespace and self.password_entered is not "" and  self.password_entered == self.singup_passwordrep:
                    self.signup_ui.passalarm.setText("")
                    self.signup_ui.passrepalarm.setText("")
                    self.signup_name = self.signup_ui.namelinedit.text()
                    self.username_entered = self.signup_ui.usernamelineedit.text()
                    self.signup_email = self.signup_ui.emaillineedit.text()
                    self.password_entered = self.signup_ui.passwordlineedit.text()
                    self.singup_passwordrep = self.signup_ui.passwordreplineedit.text()
                    self.customer_buying_window = QtWidgets.QMainWindow()
                    self.customer_buying_ui = Customer_Buying_Page_ui()
                    self.customer_buying_ui.setupUi(self.customer_buying_window)
                    self.signup_window.hide()
                    self.customer_buying_window.show()
                    self.customer_buying_ui.backbutton.clicked.connect(self.back_to_signup_from_customer)
                    self.customer_buying_ui.updatestuff_button.clicked.connect(self.load_exists_data_to_table_for_customer)
                    self.customer_buying_ui.addtolistbutton.clicked.connect(self.add_customer_choose_to_list)
                    self.customer_buying_ui.edit_button.clicked.connect(self.edit_customer_item_selected)
                    self.customer_buying_ui.delete_button.clicked.connect(self.delete_customer_item_selected)
                    self.customer_buying_ui.deleteall_button.clicked.connect(self.delete_all_customer_item)
                    self.buying_list_of_chosen = []
                    self.customer_buying_ui.stufflistchosenlistwidget.itemSelectionChanged.connect(self.get_item_choosen_by_user_to_buy) 
                    self.customer_buying_ui.payingmoneybutton.clicked.connect(self.pay_money_page)
                    self.main_db.add_new_customer(self.signup_name, self.username_entered, self.password_entered, self.signup_email)          ## Save the new Customers Info
                else:
                    self.signup_ui.passalarm.setText("رمز عبور برابر نیست")
                    self.signup_ui.passrepalarm.setText("")

    def load_exists_data_to_table_for_customer(self):             ## This load all the exist data to table for user to buy one
        self.result = self.main_db.cnnt.execute("SELECT * FROM Anbar_stuffs_table")
        self.customer_buying_ui.stufftable.setRowCount(0)
        for self.row_number, self.row_data in enumerate(self.result):
            self.customer_buying_ui.stufftable.insertRow(self.row_number)
            for self.column_number, self.data in enumerate(self.row_data):
                self.customer_buying_ui.stufftable.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))

    def add_customer_choose_to_list(self):                        ## this will add the code of item which user like to listwidget
        self.customer_buying_ui.stufflistchosenlistwidget.addItem(self.customer_buying_ui.stuff_codelineedit.text())
        self.customer_buying_ui.stuff_codelineedit.setText('')
        self.customer_buying_ui.stuff_codelineedit.setFocus()

    def get_item_choosen_by_user_to_buy(self):                    ## Create a list of items which user wants to buy
        self.items = self.customer_buying_ui.stufflistchosenlistwidget.selectedItems()
        for i in list(self.items):
            if i.text() not in self.buying_list_of_chosen:
                self.buying_list_of_chosen.append(i.text())

    def pay_money_page(self):                                     ## Pay money pages appears
        self.factor_window = QtWidgets.QMainWindow()
        self.factor_ui = Factor_Table_ui()
        self.factor_ui.setupUi(self.factor_window)
        self.customer_buying_window.hide()
        self.factor_window.show()
        self.factor_ui.back_button.clicked.connect(self.back_to_customer_buying_page)
        for self.code in self.buying_list_of_chosen:
            self.rows = self.cursor.execute('''SELECT * from Anbar_stuffs_table where stuff_code = ? ''', (self.code, ))
            for self.row in self.rows:
                self.main_db.cnnt.execute('''INSERT INTO Temporary (temp_stuff_name, temp_stuff_kind, temp_stuff_money, temp_stuff_code) \
            VALUES (?, ?, ?, ?);''', (self.row[0], self.row[1], self.row[2], self.row[3]))
        self.main_db.cnnt.commit()
        self.factor_ui.update_factor_button.clicked.connect(self.load_shop_list_to_table)
        self.factor_ui.pay_button.clicked.connect(self.add_item_to_factor_list)
        self.factor_ui.delete_from_list_button.clicked.connect(self.delete_item_from_temp_factor)

    def delete_item_from_temp_factor(self):
        self.item_code_must_delete_from_factor = self.factor_ui.delete_item_lineedit.text()
        self.main_db.delete_item_from_temp_factor(self.item_code_must_delete_from_factor)
        self.factor_ui.delete_item_lineedit.clear()
        
    def back_to_customer_buying_page(self):                     ## Will Backs to customer window
        self.factor_window.hide()
        self.customer_buying_window.show()

    def load_shop_list_to_table(self):                          ## Show items in the list factor ready to pay
        self.result = self.main_db.cnnt.execute("SELECT * FROM Temporary")
        self.factor_ui.factor_table.setRowCount(0)
        for self.row_number, self.row_data in enumerate(self.result):
            self.factor_ui.factor_table.insertRow(self.row_number)
            for self.column_number, self.data in enumerate(self.row_data):
                self.factor_ui.factor_table.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))

    def add_item_to_factor_list(self):
        self.all_user_factors_window = QtWidgets.QMainWindow()
        self.all_user_factors_ui = All_User_Factor_UI()
        self.all_user_factors_ui.setupUi(self.all_user_factors_window)
        self.factor_window.hide()
        self.all_user_factors_window.show()
        for self.code in self.buying_list_of_chosen:
            self.rows = self.cursor.execute('''SELECT * from Anbar_stuffs_table where stuff_code = ? ''', (self.code, ))
            for self.row in self.rows:
                self.main_db.add_factor(self.username_entered, self.row[0], self.row[3],  self.row[2], 'date', 'warehouse keeper')
        self.main_db.cnnt.execute('''DELETE from Temporary ''')
        self.buying_list_of_chosen = []
        self.all_user_factors_ui.to_see_all_factors_button.clicked.connect(self.load_all_of_the_factors_for_this_user)
        self.all_user_factors_ui.rebuy_button.clicked.connect(self.back_to_customer_page_from_end)
        self.all_user_factors_ui.exit_button.clicked.connect(self.close_mssg)

    def load_all_of_the_factors_for_this_user(self):
        self.result = self.main_db.cnnt.execute("SELECT * from Factor_table where username = ?", (self.username_entered,))
        self.all_user_factors_ui.factortable.setRowCount(0)
        for self.row_number, self.row_data in enumerate(self.result):
            self.all_user_factors_ui.factortable.insertRow(self.row_number)
            for self.column_number, self.data in enumerate(self.row_data):
                self.all_user_factors_ui.factortable.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))

    def back_to_customer_page_from_end(self):
        self.all_user_factors_window.hide()
        self.customer_buying_ui.stufftable.clear()
        self.customer_buying_ui.stufflistchosenlistwidget.clear()
        self.main_db.delete_items_from_temp()
        self.buying_list_of_chosen = []
        self.customer_buying_window.show()

    def mange_housekeeper_by_manager_page(self):
        self.manager_housekeeper_window = QtWidgets.QMainWindow()
        self.manager_housekeeper_ui = Manager_Housekeeper_ui()
        self.manager_housekeeper_ui.setupUi(self.manager_housekeeper_window)
        self.manager_first_window.hide()
        self.manager_housekeeper_window.show()
        self.manager_housekeeper_ui.edit_housekeeper_info_button.clicked.connect(self.edit_housekeeper_info_page)
        self.manager_housekeeper_ui.back_button.clicked.connect(self.back_to_manager_first_page_from_managerhousekeeperpage)
        self.manager_housekeeper_ui.update_table_button.clicked.connect(self.load_housekeeper_registred_table)
        self.manager_housekeeper_ui.Delete_user_button.clicked.connect(self.delete_housekeeper_asked)
        self.manager_housekeeper_ui.add_new_housekeeper_button.clicked.connect(self.add_newhousekeeper_by_manager)

    def edit_housekeeper_info_page(self):
        self.edit_housekeeper_window = QtWidgets.QMainWindow()
        self.edit_housekeeper_ui = Edit_Housekeeper_ui()
        self.edit_housekeeper_ui.setupUi(self.edit_housekeeper_window)
        self.edit_housekeeper_window.show()
        self.edit_housekeeper_ui.back_button.clicked.connect(self.back_to_manager_housekeeper_window)
        self.edit_housekeeper_ui.edit_button.clicked.connect(self.update_housekeeper_info_with_username)

    def update_housekeeper_info_with_username(self):
        self.first_username = self.edit_housekeeper_ui.enter_housekeeper_wants_to_edit_lineedit.text()
        self.new_name = self.edit_housekeeper_ui.new_name_lineedit.text()
        self.new_username = self.edit_housekeeper_ui.newhousekeeperlineedit.text()
        self.new_passsword = self.edit_housekeeper_ui.new_password_lineedit.text()
        self.new_email = self.edit_housekeeper_ui.new_email_lineedit.text()
        self.main_db.update_housekeeper_info(self.new_name, self.new_username, self.new_passsword, self.new_email, self.first_username)
        self.edit_housekeeper_window.hide()

    def mange_user_by_manager_page(self):
        self.manager_user_window = QtWidgets.QMainWindow()
        self.manager_user_ui = Manager_User_ui()
        self.manager_user_ui.setupUi(self.manager_user_window)
        self.manager_first_window.hide()
        self.manager_user_window.show()
        self.manager_user_ui.edit_user_info_button.clicked.connect(self.edit_user_info_page)
        self.manager_user_ui.back_button.clicked.connect(self.back_to_manage_first_page_from_manageuserbymanager)
        self.manager_user_ui.update_table_button.clicked.connect(self.load_user_registred_table)
        self.manager_user_ui.Delete_user_button.clicked.connect(self.delete_user_asked)
        self.manager_user_ui.add_new_customer_button.clicked.connect(self.add_newcustomer_by_manager)

    def edit_user_info_page(self):
        self.edit_user_window = QtWidgets.QMainWindow()
        self.edit_user_ui = Edit_User_ui()
        self.edit_user_ui.setupUi(self.edit_user_window)
        self.edit_user_window.show()
        self.edit_user_ui.back_button.clicked.connect(self.back_to_manager_user_window)
        self.edit_user_ui.edit_button.clicked.connect(self.update_user_info_with_username)

    def update_user_info_with_username(self):
        self.first_username = self.edit_user_ui.enter_username_wants_to_edit_lineedit.text()
        self.new_name = self.edit_user_ui.new_name_lineedit.text()
        self.new_username = self.edit_user_ui.newusernamelineedit.text()
        self.new_passsword = self.edit_user_ui.new_password_lineedit.text()
        self.new_email = self.edit_user_ui.new_email_lineedit.text()
        self.main_db.update_user_info(self.new_name, self.new_username, self.new_passsword, self.new_email, self.first_username)
        self.edit_user_window.hide()

    def add_newhousekeeper_by_manager(self):
        self.add_new_housekeeper_window = QtWidgets.QMainWindow()
        self.add_new_housekeeper_ui = Add_New_housekeeper_ui()
        self.add_new_housekeeper_ui.setupUi(self.add_new_housekeeper_window)
        self.add_new_housekeeper_window.show()
        self.add_new_housekeeper_ui.add_button.clicked.connect(self.adding_new_housekeeper_to_database)
        self.add_new_housekeeper_ui.back_button.clicked.connect(self.back_add_housekeeper_page)
    
    def back_add_housekeeper_page(self):
        self.add_new_housekeeper_window.hide()

    def adding_new_housekeeper_to_database(self):
        self.name = self.add_new_housekeeper_ui.name_lineedit.text()
        self.username = self.add_new_housekeeper_ui.usernamelineedit.text()
        self.password = self.add_new_housekeeper_ui.password_lineedit.text()
        self.email = self.add_new_housekeeper_ui.email_lineedit.text()
        self.main_db.add_new_warehouse_keeper(self.name, self.username, self.password, self.email)
        self.add_new_housekeeper_window.hide()

    def add_newcustomer_by_manager(self):
        self.add_newcustomer_window = QtWidgets.QMainWindow()
        self.add_newcustomer_ui = Add_New_customer_ui()
        self.add_newcustomer_ui.setupUi(self.add_newcustomer_window)
        self.add_newcustomer_window.show()
        self.add_newcustomer_ui.add_button.clicked.connect(self.adding_new_customer_to_database)
        self.add_newcustomer_ui.back_button.clicked.connect(self.back_add_customer_page)

    def back_add_customer_page(self):
        self.add_newcustomer_window.hide()

    def adding_new_customer_to_database(self):
        self.name = self.add_newcustomer_ui.name_lineedit.text()
        self.username = self.add_newcustomer_ui.usernamelineedit.text()
        self.password = self.add_newcustomer_ui.password_lineedit.text()
        self.email = self.add_newcustomer_ui.email_lineedit.text()
        self.main_db.add_new_customer(self.name, self.username, self.password, self.email)
        self.add_newcustomer_window.hide()

    def delete_housekeeper_asked(self):
        self.user_must_delete = self.manager_housekeeper_ui.enter_username_to_delete_lineedit.text()
        self.main_db.delete_housekeeper_selected_from_database(self.user_must_delete)
        self.manager_housekeeper_ui.enter_username_to_delete_lineedit.clear()

    def load_housekeeper_registred_table(self):
        self.result = self.main_db.cnnt.execute("SELECT * FROM Warehousekeeper_info_table")
        self.manager_housekeeper_ui.show_registred_warehousekeeper_table.setRowCount(0)
        for self.row_number, self.row_data in enumerate(self.result):
            self.manager_housekeeper_ui.show_registred_warehousekeeper_table.insertRow(self.row_number)
            for self.column_number, self.data in enumerate(self.row_data):
                self.manager_housekeeper_ui.show_registred_warehousekeeper_table.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))

    def delete_user_asked(self):
        self.user_must_delete = self.manager_user_ui.enter_username_to_delete_lineedit.text()
        self.main_db.delete_user_selected_from_database(self.user_must_delete)
        self.manager_user_ui.enter_username_to_delete_lineedit.clear()

    def load_user_registred_table(self):
        self.result = self.main_db.cnnt.execute("SELECT * FROM Customer_info_table")
        self.manager_user_ui.show_registred_user_table.setRowCount(0)
        for self.row_number, self.row_data in enumerate(self.result):
            self.manager_user_ui.show_registred_user_table.insertRow(self.row_number)
            for self.column_number, self.data in enumerate(self.row_data):
                self.manager_user_ui.show_registred_user_table.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))

    def back_to_signin_from_manager_page(self):
        self.manager_first_window.hide()
        self.signin_window.show()

    def all_factors_for_manager(self):
        self.all_the_factors_window = QtWidgets.QMainWindow()
        self.all_the_factors_ui = All_The_Factors_ui()
        self.all_the_factors_ui.setupUi(self.all_the_factors_window)
        self.manager_first_window.hide()
        self.all_the_factors_window.show()
        self.all_the_factors_ui.enter_to_load_button.clicked.connect(self.show_all_the_factors_for_manager)
        self.all_the_factors_ui.back_button.clicked.connect(self.back_to_first_page_manager)
        self.all_the_factors_ui.logout_button.clicked.connect(self.back_to_signin_page)

    def back_to_first_page_manager(self):
        self.manager_first_window.show()
        self.all_the_factors_window.hide()

    def back_to_signin_page(self):
        self.signin_window.show()
        self.all_the_factors_window.hide()

    def show_all_the_factors_for_manager(self):
        self.result = self.main_db.cnnt.execute("SELECT * FROM Factor_table")
        self.all_the_factors_ui.tableWidget.setRowCount(0)
        for self.row_number, self.row_data in enumerate(self.result):
            self.all_the_factors_ui.tableWidget.insertRow(self.row_number)
            for self.column_number, self.data in enumerate(self.row_data):
                self.all_the_factors_ui.tableWidget.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))

    def back_to_manager_first_page_from_managerhousekeeperpage(self):
        self.manager_housekeeper_window.hide()
        self.manager_first_window.show()
    
    def back_to_manage_first_page_from_manageuserbymanager(self):
        self.manager_user_window.hide()
        self.manager_first_window.show()

    def back_to_manager_housekeeper_window(self):
        self.edit_housekeeper_window.hide()
        self.manager_housekeeper_window.show()

    def back_to_manager_user_window(self):
        self.edit_user_window.hide()
        self.manager_user_window.show()

    def delete_item_asked(self):            ## Delete func to delete the item which warehousing mangement wants to delete from database
        self.item_delete_code = self.warehousing_ui.get_code_item_delete_lineedit.text()
        self.main_db.delete_item_selected(self.item_delete_code)
        self.warehousing_ui.get_code_item_delete_lineedit.clear()

    def update_item_page(self):             ## Updates func to update the item which user wants to update it in Database
        self.update_page_window = QtWidgets.QMainWindow()
        self.update_page_ui = Update_Items_ui()
        self.update_page_ui.setupUi(self.update_page_window)
        self.update_page_window.show()
        self.update_page_ui.update_button.clicked.connect(self.getting_updates_item_and_change_them_in_database)
        self.update_page_ui.cancelbutton.clicked.connect(self.back_to_warehouse_from_update_page)

    def back_to_warehouse_from_update_page(self):
        self.update_page_window.hide()

    def getting_updates_item_and_change_them_in_database(self):         ## this will update the data base whith the item user asked
        self.code = self.update_page_ui.code_lineedit.text()
        self.name_update = self.update_page_ui.name_lineedit.text()
        self.kind_update = self.update_page_ui.brand_lineedit.text()
        self.money = self.update_page_ui.money_lineedit.text()
        self.num_update = self.update_page_ui.remain_lineedit.text()
        self.main_db.update_item_selected(self.code, self.name_update, self.kind_update, self.money, self.num_update)
        self.update_page_window.hide()

    def back_to_signin_page_from_warehouseing(self):
        self.signin_window.show()
        self.warehousing_window.hide()

    def enter_new_stuff_page(self):
        self.enter_new_stuff_window = QtWidgets.QMainWindow()
        self.enter_new_stuff_ui = Enter_new_stuff_ui()
        self.enter_new_stuff_ui.setupUi(self.enter_new_stuff_window)
        self.enter_new_stuff_window.show()
        self.enter_new_stuff_ui.back_button.clicked.connect(self.back_to_warehousing_window)
        self.enter_new_stuff_ui.save_button.clicked.connect(self.save_enter_new_stuff)
        
    def back_to_warehousing_window(self):
        self.enter_new_stuff_window.hide()
        self.warehousing_window.show()

    def save_enter_new_stuff(self):
        self.new_name = self.enter_new_stuff_ui.name_lineedit.text()
        self.new_brand = self.enter_new_stuff_ui.brand_lineedit.text()
        self.new_money = self.enter_new_stuff_ui.money_lineedit.text()
        self.new_remaining = self.enter_new_stuff_ui.reamaining_lineedit.text()
        self.main_db.add_stuff(self.new_name, self.new_brand, self.new_money, self.new_remaining)
        self.main_db.cnnt.commit()
        self.enter_new_stuff_window.hide()

    def load_data_to_table_in_warehouse(self):
        self.result = self.main_db.cnnt.execute("SELECT * FROM Anbar_stuffs_table")
        self.warehousing_ui.stufftable.setRowCount(0)
        for self.row_number, self.row_data in enumerate(self.result):
            self.warehousing_ui.stufftable.insertRow(self.row_number)
            for self.column_number, self.data in enumerate(self.row_data):
                self.warehousing_ui.stufftable.setItem(self.row_number, self.column_number, QtWidgets.QTableWidgetItem(str(self.data)))

    def back_to_start_from_signin(self):
        self.signin_window.hide()
        window.show()

    def back_to_start_from_signup(self):
        self.signup_window.hide()
        window.show()

    def back_to_signin_from_customer(self):
        self.customer_buying_window.hide()
        self.signin_window.show()

    def back_to_signup_from_customer(self):
        self.customer_buying_window.hide()
        self.signup_window.show()

    def edit_customer_item_selected(self):
        self.row = self.customer_buying_ui.stufflistchosenlistwidget.currentRow()
        newtext, ok= QInputDialog.getText(self, "Enter new text", "Enter new text")
        if ok and ( len(newtext) != 0 ):
            self.customer_buying_ui.stufflistchosenlistwidget.takeItem(self.customer_buying_ui.stufflistchosenlistwidget.currentRow())
            self.customer_buying_ui.stufflistchosenlistwidget.insertItem(self.row, QListWidgetItem(newtext))
        else:
            pass

    def delete_customer_item_selected(self):
        self.customer_buying_ui.stufflistchosenlistwidget.takeItem(self.customer_buying_ui.stufflistchosenlistwidget.currentRow())

    def delete_all_customer_item(self):
        self.customer_buying_ui.stufflistchosenlistwidget.clear()

    def keyPressEvent(self, e):                  ## Created For the escape button on keyboard
        if e.key() == Qt.Key_Escape:
            self.close_mssg()             ## When the escape button pushed this method will be call

    def close_mssg(self):                  ## This method will call when the quit button clicked
        self.main_db.cnnt.execute('''DELETE from Temporary ''')
        self.buying_list_of_chosen = []
        ans = QMessageBox.question(self, 'Message', "آیا از خروجتان مطمئنید ؟", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            self.connection.close()
            sys.exit(QApplication.instance().quit)
        else:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    window.main_db.cnnt.commit()
    sys.exit(app.exec_())
                                            ###################          WHAT          ###################
                                            ###################         DOESN'T        ###################
                                            ###################          KILL          ###################
                                            ###################          YOU           ###################
                                            ###################         MAKES          ###################
                                            ###################          YOU           ###################
                                            ###################        STRONGER        ###################
                                            ###################        ALI SHHDE       ###################
                                            ###############     S.T.NUM 971 229 200 12       #############
                                            ####### Shop Application Created By Ali shohadahoseini #######