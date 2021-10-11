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

# TODO: Add Specific Item ID searching for item table
# TODO: Add Function and Render UI to handle items under servicing or not
# TODO: Complete the Admin Product Search Table


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

        # Change ComboBox for Category and Model
        self.ui.category_comboBox.currentTextChanged.connect(
            lambda: UIFunctions.change_category_model_comboBox(self)
        )

        # Exit Button
        self.ui.btn_page_4.clicked.connect(
            lambda: UIFunctions.exit_mainwindow(self)
        )

        """ For the Page Buttons"""

        """Page 1"""
        # Render Admin Table
        self.ui.refresh_button_admin.clicked.connect(
            self.get_sold_unsold_items_api)

        self.ui.view_items_category_model_button.clicked.connect(
            self.view_items_sold_cat_model_api)

        self.ui.view_customers_button.clicked.connect(
            self.view_customers_unpaid_fee_api)

        # Initialise Database
        self.ui.initialise_database_button.clicked.connect(
            self.initialise_database_api)

        """Page 2"""
        # Render Product Table
        self.ui.submit_query.clicked.connect(self.get_products_api)  # help la

        """Page 3"""
        self.ui.item_search_button.clicked.connect(
            self.view_all_items_api)

        """ End Of Page Buttons"""

        print(self.admin_info)

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

    def initialise_database_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.initialise_database_button.setText(
            _translate("MainWindow", "Initialising..."))
        self.ui.initialise_database_button.setEnabled(False)
        self.worker = Initialise_Database_Thread()
        self.worker.start()
        self.worker.api_data.connect(self.initialise_error_handling)

    def initialise_error_handling(self, value: dict):
        if ("success" in value):
            UIFunctions.messageBox(
                self, "Success", "Initialisation Success", "Initialisation Complete, Product and Items Restocked!")  # only Admin and Customers remain
            UIFunctions.finished_loading_text(self)
            return
        else:
            UIFunctions.messageBox(
                self, "Error", "Initialise Database Error", value["error"])

######################### Page 2, Products Page ##########################################

    def get_products_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.submit_query.setText(_translate("MainWindow", "Loading..."))
        content = {
            "Category": self.ui.category_comboBox.currentText(),
            "Model": self.ui.model_comboBox.currentText(),
            "Price": self.ui.price_comboBox.currentText().replace("$", ""),
            "Color": self.ui.colour_comboBox.currentText(),
            "Factory": self.ui.factory_comboBox.currentText(),
            "Production Year": self.ui.production_year_comboBox.currentText(),
            "Power Supply": self.ui.power_supply_comboBox.currentText(),
            "Warranty": self.ui.warranty_comboBox.currentText()
        }
        self.worker = Get_Products_Thread(content)
        self.worker.start()
        self.worker.finished.connect(
            lambda: UIFunctions.finished_loading_text(self))
        self.worker.api_data.connect(self.render_product_table_admin)

    def render_product_table_admin(self, value: dict):
        _translate = QtCore.QCoreApplication.translate
        if ("success" in value):
            product_array = value["success"][0]
            none_found = "No Products Found"
            category_type = str(product_array[0])

            """ Render Table Contents from API """
            print(product_array)
            self.ui.category_amount_label.setText(_translate(
                "MainWindow", category_type if product_array[0] is not None else "--"))
            self.ui.price_amount_label.setText(_translate("MainWindow", "$ " + str(
                product_array[1]) if product_array[1] is not None else "$ --"))
            self.ui.warranty_amount_label.setText(_translate("MainWindow", str(
                product_array[2]) + " Months" if product_array[2] is not None else "--"))
            self.ui.model_amount_label.setText(_translate("MainWindow", str(
                product_array[3]) if product_array[3] is not None else "--"))
            self.ui.cost_amount_label.setText(_translate("MainWindow", "$ " + str(
                product_array[4]) if product_array[4] is not None else "$ --"))
            self.ui.inventory_amount_label.setText(_translate("MainWindow", str(
                product_array[-2]) if product_array[-2] is not None else none_found))
            self.ui.sold_items_amount_label.setText(_translate("MainWindow", str(
                product_array[-1]) if product_array[-1] != 0 else none_found))

            if (category_type == "Locks"):
                self.ui.category_div.setStyleSheet("""
                QWidget { 
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);
                    image: url(:/Choose_Item_div/padlock.png);
                    border-radius: 20px;
                }
                """)
            elif (category_type == "Lights"):
                self.ui.category_div.setStyleSheet("""
                QWidget { 
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);
                    image: url(:/Choose_Item_div/light-bulb.png);
                    border-radius: 20px;
                }
                """)
            else:
                self.ui.category_div.setStyleSheet("""
                QWidget { 
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);
                    image: url(:/Choose_Item_div/box.png);
                    border-radius: 20px;
                }
                """)
            UIFunctions.messageBox(
                self, "Success", "Product Search", "Product Search Successful")
        else:
            UIFunctions.messageBox(
                self, "Error", "Product Search", value["error"])

########################## Page 3, Item Search Page ########################################

    def view_all_items_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.item_search_button.setText(
            _translate("MainWindow", "Loading..."))
        self.ui.item_search_button.setEnabled(False)

        """get the info from comboBox"""
        service_status = self.ui.under_service_comboBox.currentText()
        item_id = self.ui.item_id_comboBox.currentText()
        PAYLOAD = {
            "ITEM RESPONSE": service_status,
            "Item ID": item_id
        }
        self.worker = Item_Search_Thread(PAYLOAD)
        self.worker.start()
        self.worker.finished.connect(
            lambda: UIFunctions.finished_loading_text(self))
        self.worker.api_data.connect(self.render_items_table)

    def render_items_table(self, value: dict):
        if ("success" in value):
            arrays = value["success"]

            """ Render Contents from API """
            table_row = 0
            self.ui.item_table.setRowCount(len(arrays))
            for row in arrays:
                self.ui.item_table.setItem(
                    table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.ui.item_table.setItem(
                    table_row, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.ui.item_table.setItem(
                    table_row, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.ui.item_table.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.ui.item_table.setItem(
                    table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                self.ui.item_table.setItem(
                    table_row, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                self.ui.item_table.setItem(
                    table_row, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                self.ui.item_table.setItem(
                    table_row, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                self.ui.item_table.setItem(
                    table_row, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                self.ui.item_table.setItem(
                    table_row, 9, QtWidgets.QTableWidgetItem(str(row[9])))
                self.ui.item_table.setItem(
                    table_row, 10, QtWidgets.QTableWidgetItem(str(row[10])))
                self.ui.item_table.setItem(
                    table_row, 11, QtWidgets.QTableWidgetItem(str(row[11])))
                table_row += 1
            UIFunctions.messageBox(
                self, "Success", "Fetch Items", "Finished Fetching Items")
            UIFunctions.finished_loading_text(self)
        else:
            UIFunctions.messageBox(
                self, "Error", "Item Search Error", value["error"])

######################## END ###############################################################


class Get_Products_Thread(QThread):
    # package the data into a signal, signal takes in object/ dictionary
    api_data = pyqtSignal(object)

    # create constructor for signal to pass in arguments
    def __init__(self, info: dict, parent=None):
        QThread.__init__(self, parent)
        # contains product info like category, model, price, etc...
        self.info = info

    def run(self):
        PAYLOAD = {
            "Category": self.info["Category"],
            "Model": self.info["Model"],
            "Price": self.info["Price"],
            "Color": self.info["Color"],
            "Factory": self.info["Factory"],
            "Production Year": self.info["Production Year"],
            "Power Supply": self.info["Power Supply"],
            "Warranty": self.info["Warranty"]
        }
        r = requests.post(
            "http://localhost:5000/api/Admin/search/products", json=PAYLOAD)
        response = r.json()
        self.api_data.emit(response)


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


class Initialise_Database_Thread(QThread):

    api_data = pyqtSignal(object)

    def run(self):
        r = requests.get("http://localhost:5000/api/Initialise")
        response = r.json()
        self.api_data.emit(response)


class Item_Search_Thread(QThread):

    api_data = pyqtSignal(object)

    def __init__(self, info: dict, parent=None):
        QThread.__init__(self, parent)
        self.info = info  # contains Item ID and service status search

    def run(self):
        PAYLOAD = {
            "Item ID": self.info["Item ID"],
            "ITEM RESPONSE": self.info["ITEM RESPONSE"]
        }
        r = requests.post(
            "http://localhost:5000/api/Admin/view/all_items", json=PAYLOAD)
        response = r.json()
        self.api_data.emit(response)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _input = json.loads(urllib.parse.unquote(sys.argv[-1]))
    print(_input)
    window = MainWindow(_input)
    sys.exit(app.exec_())
