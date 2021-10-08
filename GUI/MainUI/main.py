import sys
import time
import json
import urllib.parse
import requests
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

# TODO: add Error Handling for all the threads, to connect to MessageBox
# TODO: add thr Request fetching thread
# TODO: Change the design of the product table!


class MainWindow(QMainWindow):
    def __init__(self, customer_info: dict):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.customer_info = customer_info
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

        # Exit Button
        self.ui.btn_page_4.clicked.connect(
            lambda: UIFunctions.exit_mainwindow(self)
        )

        # Change ComboBox for Category and Model
        self.ui.category_comboBox.currentTextChanged.connect(
            lambda: UIFunctions.change_category_model_comboBox(self)
        )

        """ For Tables"""
        # product tables
        self.ui.submit_query.clicked.connect(self.get_products_api)

        # purchases tables
        self.ui.fetch_orders_button.clicked.connect(self.get_purchases_api)

        """ For Tables"""
        print(customer_info)

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

###################### Get All Products API ############################
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
        self.worker.start()  # start the parallel function
        # execute function once api done with no data
        self.worker.finished.connect(
            lambda: UIFunctions.fetch_table_data_response(self))
        # pass Signal data into render_tables function
        self.worker.api_data.connect(self.render_product_table)

    def render_product_table(self, value: dict):
        # NOTE: check if the value: dict has "success response"
        if ("success" in value):
            UIFunctions.messageBox(
                self, "Success", "Product Search", "Products Searched Successfully")
        else:
            UIFunctions.messageBox(
                self, "Error", "Product Search", value["error"])
        product_array = value["success"][0]
        table_row = 0
        none_found = "No Products Found"
        self.ui.product_table.setRowCount(len(product_array))
        print(product_array)
        self.btn_purchase_now = QtWidgets.QPushButton("Purchase Now!")
        self.btn_purchase_now.clicked.connect(
            lambda: self.handle_purchase_now(product_array[-1])
        )

        self.ui.product_table.setItem(
            table_row, 0, QtWidgets.QTableWidgetItem(str(product_array[0]))) if product_array[0] is not None else self.ui.product_table.setItem(
            table_row, 0, QtWidgets.QTableWidgetItem(none_found))
        self.ui.product_table.setItem(
            table_row, 1, QtWidgets.QTableWidgetItem(str(product_array[1])))

        self.ui.product_table.setItem(
            table_row, 2, QtWidgets.QTableWidgetItem(str(product_array[2])))

        self.ui.product_table.setItem(
            table_row, 3, QtWidgets.QTableWidgetItem(
                "$ " + str(product_array[3]))
        )
        self.ui.product_table.setItem(
            table_row, 4, QtWidgets.QTableWidgetItem(str(product_array[4]))
        )

        if product_array[0] is not None:
            self.ui.product_table.setCellWidget(
                table_row, 5, self.btn_purchase_now)
        else:
            self.ui.product_table.setItem(
                table_row, 5, QtWidgets.QTableWidgetItem("Out Of Stock"))

    def handle_purchase_now(self, item_id: str):
        # item_id is in CHAR(4)
        current_inventory_level = int(self.ui.product_table.item(0, 4).text())
        self.ui.product_table.setCellWidget(
            0, 5, QtWidgets.QPushButton("Loading ..."))
        if current_inventory_level > 0:
            print(item_id)
            self.worker = Purchase_Product_Thread({
                "Customer ID": self.customer_info["Customer ID"],
                "Item ID": item_id
            })
            self.worker.start()
            # refresh table after purchase
            self.worker.finished.connect(self.get_products_api)
            self.worker.finished.connect(lambda: UIFunctions.messageBox(
                self, "Success", "Purchasing Item", "Item Purchased Successfully!"))
        else:
            item_id = 0


####################### Get Purchases API ##############################


    def get_purchases_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.fetch_orders_button.setText(
            _translate("MainWindow", "Loading..."))
        self.ui.fetch_orders_button.setEnabled(False)
        self.worker = Get_Purchases_Thread(self.customer_info)
        self.worker.start()

        self.worker.finished.connect(
            lambda: UIFunctions.fetch_table_data_response(self))
        self.worker.api_data.connect(self.render_purchase_table)

    def render_purchase_table(self, value: dict):
        # NOTE: check if the value: dict has "success response"
        if ("success" in value):
            arrays = value["success"]
            table_row = 0
            self.ui.item_table.setRowCount(len(arrays))
            for row in arrays:
                # Create request button to put in the table
                self.btn_request = QtWidgets.QPushButton('Request!')
                self.btn_request.clicked.connect(
                    self.handle_purchase_request_clicked)

                self.ui.item_table.setItem(
                    table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.item_table.setCellWidget(
                    table_row, 1, self.btn_request)
                self.ui.item_table.setItem(
                    table_row, 2, QtWidgets.QTableWidgetItem("SGD $" + str(row[1])))
                self.ui.item_table.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.item_table.setItem(
                    table_row, 4, QtWidgets.QTableWidgetItem(row[3]))
                self.ui.item_table.setItem(
                    table_row, 5, QtWidgets.QTableWidgetItem(str(row[4]) + " Months"))
                self.ui.item_table.setItem(
                    table_row, 6, QtWidgets.QTableWidgetItem(row[5]))
                self.ui.item_table.setItem(
                    table_row, 7, QtWidgets.QTableWidgetItem(row[7]))
                self.ui.item_table.setItem(
                    table_row, 8, QtWidgets.QTableWidgetItem(row[6]))
                self.ui.item_table.setItem(
                    table_row, 9, QtWidgets.QTableWidgetItem(row[-2]))
                self.ui.item_table.setItem(
                    table_row, 10, QtWidgets.QTableWidgetItem(row[-1]))
                table_row += 1
            UIFunctions.messageBox(
                self, "Success", "Get Purchases", "Found All Purchases")
        else:
            UIFunctions.messageBox(
                self, "Error", "Product Search", value["error"])

    def handle_purchase_request_clicked(self):
        button = QtWidgets.qApp.focusWidget()
        # or button = self.sender()
        index = self.ui.item_table.indexAt(button.pos())
        if index.isValid():
            column_index = index.column()
            row_index = index.row()
            entire_row = [
                self.ui.item_table.item(row_index, 0).text(),
                self.ui.item_table.item(row_index, 4).text(),
            ]
            date = datetime.strptime(entire_row[-1], '%a, %d %b %Y %X GMT')
            print(str(date))

            data = {
                "Customer ID": self.customer_info["Customer ID"],
                "Item ID": entire_row[0],
                "Warranty End": str(date).replace(" 00:00:00", "")
            }
            self.worker = Request_Item(data)
            self.worker.start()
            self.worker.send_data.connect(self.request_message_box)
            self.ui.item_table.setCellWidget(
                row_index, column_index, QtWidgets.QPushButton('Item Requested'))

    def request_message_box(self, response: dict):
        if ("success" in response):
            UIFunctions.messageBox(
                self, "Success", "Request Added", "Request Successfully Added")
        elif ('error' in response):
            UIFunctions.messageBox(
                self, "Error", "Request Failed!", response["error"])


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
        try:
            r = requests.post(
                "http://localhost:5000/api/Customer/search/products", json=PAYLOAD)
            response = r.json()
            self.api_data.emit(response)
        except Exception as e:
            print(str(e))
        # output the data after finished executing the script


class Get_Purchases_Thread(QThread):

    api_data = pyqtSignal(object)

    # create constructor for signal to pass in arguments
    def __init__(self, info: dict, parent=None):
        QThread.__init__(self, parent)
        self.info = info  # contains customer ID and Name

    def run(self):

        PAYLOAD = {
            "Customer ID": self.info["Customer ID"]
        }

        try:
            r = requests.post(
                "http://localhost:5000/api/Customer/get/purchases", json=PAYLOAD)
            # output the data after finished executing the script
            response = r.json()
            print(response["success"][0])
            self.api_data.emit(response)
        except Exception as e:
            print(str(e))


class Purchase_Product_Thread(QThread):

    api_data = pyqtSignal(object)

    # create constructor for signal to pass in arguments
    def __init__(self, info: dict, parent=None):
        QThread.__init__(self, parent)
        self.info = info  # contains customer ID and Name

    def run(self):
        PAYLOAD = {
            "Customer ID": self.info["Customer ID"],
            "Item ID": self.info["Item ID"]
        }
        try:
            r = requests.post(
                "http://localhost:5000/api/Customer/add/purchases", json=PAYLOAD)
            response = r.json()
            print(response["success"])
            self.api_data.emit(response)
        except Exception as e:
            print(str(e))


class Request_Item(QThread):

    send_data = pyqtSignal(object)

    # create constructor for signal to pass in arguments
    def __init__(self, info: dict, parent=None):
        QThread.__init__(self, parent)
        self.info = info  # contains customer ID and Name

    def run(self):
        PAYLOAD = {
            "Customer ID": self.info["Customer ID"],
            "Item ID": self.info["Item ID"],
            "Warranty End": self.info["Warranty End"]
        }
        r = requests.post(  # handle all problems through a message box? so we always send it. But what if we immediately connect to a messagebox?
            "http://localhost:5000/api/Customer/add/request", json=PAYLOAD)
        response = r.json()
        self.send_data.emit(response)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _input = json.loads(urllib.parse.unquote(sys.argv[-1]))
    print(_input)
    window = MainWindow(_input)
    sys.exit(app.exec_())
