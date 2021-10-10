import sys
import time
import json
import urllib.parse
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# GUI FILE
from Admin_UI import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

# TODO: Remove the db initialisation from Admin Login and Put it in Admin UI as a button instead
# TODO: Change the initialisation SQL script, to only drop every table EXCEPT customer and admin table!
# TODO: Create an Items Sold Category & Model Function
# TODO: Create a View Customers with Unpaid Fees Function
# TODO: Create a Display Sold & Unsold Items Function


class MainWindow(QMainWindow):
    def __init__(self, admin_info: dict):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.admin_info = admin_info

        # TOGGLE/BURGER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 320, True))

        # PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # PAGE 4
        self.ui.btn_page_5.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        # PAGE 5
        self.ui.btn_page_6.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))

        # Exit Button
        self.ui.btn_page_4.clicked.connect(
            lambda: UIFunctions.exit_mainwindow(self)
        )

        """ For the Page Buttons"""
        # Render Admin Table
        self.ui.refresh_button_admin.clicked.connect(
            self.get_sold_unsold_items_api)

        self.ui.view_items_category_model_button.clicked.connect(
            self.view_items_sold_cat_model_api)

        self.ui.view_customers_button.clicked.connect(
            self.view_customers_unpaid_fee_api)

        # Render Product Table
        self.ui.submit_query.clicked.connect(
            lambda: UIFunctions.get_products_api(self)
        )

        """ End Of Page Buttons"""

        print(admin_info)

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
######################### Page 1, Admin Functions Table ##################################

    # Sold & Unsold Items Button
    def get_sold_unsold_items_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.refresh_button_admin.setText(
            _translate("MainWindow", "Loading..."))
        self.ui.refresh_button_admin.setEnabled(False)
        self.worker = Get_Sold_Unsold_Items_Thread()
        self.worker.start()
        self.worker.finished.connect(
            lambda: UIFunctions.finished_loading_text(self))
        self.worker.api_data.connect(self.render_table_sold_unsold_items)

    def render_table_sold_unsold_items(self, value: dict):
        """ Check if theres a success or error """
        if ("success" in value):
            arrays = value["success"]

            """ First Set Up The Table """

            self.ui.admin_table.setColumnCount(3)
            self.ui.admin_table.horizontalHeader().setStretchLastSection(True)
            self.ui.admin_table.horizontalHeader().setDefaultSectionSize(550)

            """ Render Header Contents"""
            item = QtWidgets.QTableWidgetItem("IID")
            self.ui.admin_table.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem("""Number Of "SOLD" Items""")
            self.ui.admin_table.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem("""Number of "UNSOLD" Items""")
            self.ui.admin_table.setHorizontalHeaderItem(2, item)

            """ Render Column Contents From API"""
            table_row = 0
            self.ui.admin_table.setRowCount(len(arrays))
            for row in arrays:
                self.ui.admin_table.setItem(
                    table_row, 0, QtWidgets.QTableWidgetItem("    00" + str(row[0])))
                self.ui.admin_table.setItem(
                    table_row, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.ui.admin_table.setItem(
                    table_row, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                table_row += 1
            UIFunctions.messageBox(
                self, "Success", "Sold & Unsold Items", "Found All Items")

        else:
            UIFunctions.messageBox(
                self, "Error", "Sold & Unsold Items Error", value["error"])

    # Items Sold In Category and Model Button
    def view_items_sold_cat_model_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.view_items_category_model_button.setText(
            _translate("MainWindow", "Loading..."))
        self.ui.view_items_category_model_button.setEnabled(False)
        self.worker = Get_Items_Sold_Cat_Model_Thread()
        self.worker.start()
        self.worker.finished.connect(
            lambda: UIFunctions.finished_loading_text(self))
        self.worker.api_data.connect(self.render_table_sold_items_cat_model)

    def render_table_sold_items_cat_model(self, value: dict):
        """ Check if theres a success or error """
        if ("success" in value):
            arrays = value["success"]
            """ First Set Up The Table """
            self.ui.admin_table.setColumnCount(3)
            self.ui.admin_table.horizontalHeader().setStretchLastSection(True)
            self.ui.admin_table.horizontalHeader().setDefaultSectionSize(550)

            """ Render Header Contents """
            item = QtWidgets.QTableWidgetItem("Category")
            self.ui.admin_table.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem("""Model""")
            self.ui.admin_table.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem("""Number of "SOLD" Items""")
            self.ui.admin_table.setHorizontalHeaderItem(2, item)

            """ Render Column Contents From API"""
            table_row = 0
            self.ui.admin_table.setRowCount(len(arrays))
            for row in arrays:
                self.ui.admin_table.setItem(
                    table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.admin_table.setItem(
                    table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.admin_table.setItem(
                    table_row, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                table_row += 1
            UIFunctions.messageBox(
                self, "Success", "Sold Items", "Found All Items")
        else:
            UIFunctions.messageBox(
                self, "Error", "Sold Items Error", value["error"])

    # view Customers with unpaid service fees
    def view_customers_unpaid_fee_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.view_customers_button.setText(
            _translate("MainWindow", "Loading..."))
        self.ui.view_customers_button.setEnabled(False)
        self.worker = Customer_Unpaid_Fee_Thread()
        self.worker.start()
        self.worker.finished.connect(lambda: UIFunctions.finished_loading_text)
        self.worker.api_data.connect(self.render_table_customer_unpaid_fee)

    def render_table_customer_unpaid_fee(self, value: dict):
        """ Check if theres a success or error """
        if ("success" in value):
            arrays = value["success"]
            """ First Set Up The Table """
            self.ui.admin_table.setColumnCount(6)
            self.ui.admin_table.horizontalHeader().setStretchLastSection(False)
            self.ui.admin_table.horizontalHeader().setDefaultSectionSize(283)

            """ Render Header Contents """
            item = QtWidgets.QTableWidgetItem("Customer ID")
            self.ui.admin_table.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem("""Customer Name""")
            self.ui.admin_table.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem("""Gender""")
            self.ui.admin_table.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem("""Phone Number""")
            self.ui.admin_table.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem("""Email Address""")
            self.ui.admin_table.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem("""Address""")
            self.ui.admin_table.setHorizontalHeaderItem(5, item)

            """ Render Column Contents From API"""
            table_row = 0
            self.ui.admin_table.setRowCount(len(arrays))
            for row in arrays:
                self.ui.admin_table.setItem(
                    table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.admin_table.setItem(
                    table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.admin_table.setItem(
                    table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.admin_table.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.ui.admin_table.setItem(
                    table_row, 4, QtWidgets.QTableWidgetItem(row[4]))
                self.ui.admin_table.setItem(
                    table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
                table_row += 1
            UIFunctions.messageBox(
                self, "Success", "Unpaid Customer Fees", "Finished Fetching Unpaid Customers Data")
            UIFunctions.finished_loading_text(self)
            return
        else:
            UIFunctions.messageBox(
                self, "Error", "Unpaid Customer Fees", value["error"])

######################### Page 2, Products Page ##########################################

    def get_products_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.submit_query.setText(_translate("MainWindow", "Loading..."))
        self.worker = Get_Products_Thread()
        self.worker.start()  # start the parallel function
        # execute function once api done with no data
        self.worker.finished.connect(self.event_worker_finished)
        # pass Signal data into render_tables function
        self.worker.api_data.connect(self.render_tables)

    def render_tables(self, value):
        print(value)

    def event_worker_finished(self):
        QtWidgets.QMessageBox.information(self, "Done", "API Request Complete")
        _translate = QtCore.QCoreApplication.translate
        self.ui.submit_query.setText(_translate("MainWindow", "Submit"))
######################## END ###############################################################


class Get_Products_Thread(QThread):
    # package the data into a signal, signal takes in object/ dictionary
    api_data = pyqtSignal(object)

    def run(self):
        data = dict()
        info = 0
        for i in range(3):
            info += i
            time.sleep(1)
            print(i)
        data["numbers"] = info
        print("hello")
        # output the data after finished executing the script
        self.api_data.emit(data)


class Get_Sold_Unsold_Items_Thread(QThread):

    api_data = pyqtSignal(object)

    def run(self):
        r = requests.get(
            "http://localhost:5000/api/Admin/view/items_sold_unsold")
        response = r.json()
        self.api_data.emit(response)


class Get_Items_Sold_Cat_Model_Thread(QThread):

    api_data = pyqtSignal(object)

    def run(self):
        r = requests.get(
            "http://localhost:5000/api/Admin/view/items_sold_cat_model")
        response = r.json()
        self.api_data.emit(response)


class Customer_Unpaid_Fee_Thread(QThread):

    api_data = pyqtSignal(object)

    def run(self):
        r = requests.get(
            "http://localhost:5000/api/Admin/view/customers_unpaid")
        response = r.json()
        self.api_data.emit(response)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _input = json.loads(urllib.parse.unquote(sys.argv[-1]))
    print(_input)
    window = MainWindow(_input)
    sys.exit(app.exec_())
