import sys
import time
import json
import urllib.parse
import requests
from datetime import datetime, date
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

# TODO: add Error Handling for all the threads, to connect to MessageBox


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

        # Purchase Now Button

        """ For Tables"""
        # product tables
        self.ui.submit_query.clicked.connect(self.get_products_api)

        # purchases tables
        self.ui.fetch_orders_button.clicked.connect(self.get_purchases_api)

        # requests tables
        self.ui.view_requests_button.clicked.connect(self.get_all_requests_api)

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
        _translate = QtCore.QCoreApplication.translate
        if ("success" in value):
            UIFunctions.messageBox(
                self, "Success", "Product Search", "Products Searched Successfully")
        else:
            UIFunctions.messageBox(
                self, "Error", "Product Search", value["error"])
        product_array = value["success"][0]
        none_found = "No Products Found"
        category_type = str(product_array[0])
        self.ui.price_amount_label.setText(_translate(
            "MainWindow", "$" + str(product_array[3]) if product_array[3] is not None else "$--"))
        self.ui.category_amount_label.setText(_translate(
            "MainWindow", category_type if product_array[0] is not None else "--"))
        self.ui.warranty_amount_label.setText(_translate("MainWindow", str(
            product_array[2]) + " Months" if product_array[2] is not None else "--"))
        self.ui.model_amount_label.setText(_translate("MainWindow", str(
            product_array[1]) if product_array[1] is not None else "--"))
        self.ui.inventory_amount_label.setText(_translate("MainWindow", str(
            product_array[4]) if product_array[4] is not None else none_found))

        if (category_type == "Locks"):
            self.ui.category_div.setStyleSheet("""
            QWidget { 
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);
                image: url(:/Item Chooser/padlock.png);
                border-radius: 20px;
            }
            """)
        elif (category_type == "Lights"):
            self.ui.category_div.setStyleSheet("""
            QWidget { 
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);
                image: url(:/Item Chooser/light-bulb.png);
                border-radius: 20px;
            }
            """)
        else:
            self.ui.category_div.setStyleSheet("""
            QWidget { 
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);
                image: url(:/Item Chooser/box.png);
                border-radius: 20px;
            }
            """)

        self.ui.purchase_now_button.clicked.connect(
            lambda: self.handle_purchase_now(product_array[-1])
        )

    def handle_purchase_now(self, item_id: str):
        # item_id is in CHAR(4)
        print(item_id)
        _translate = QtCore.QCoreApplication.translate
        self.ui.purchase_now_button.setText(
            _translate("MainWindow", "Purchasing..."))
        current_inventory_level = int(self.ui.inventory_amount_label.text())
        if current_inventory_level > 0:
            print(item_id)
            self.worker = Purchase_Product_Thread({
                "Customer ID": self.customer_info["Customer ID"],
                "Item ID": item_id
            })
            self.worker.start()
            # refresh table after purchase
            self.worker.finished.connect(
                self.get_products_api)  # refresh the table
            self.worker.finished.connect(lambda: UIFunctions.messageBox(
                self, "Success", "Purchasing Item", "Item Purchased Successfully!"))
        else:
            UIFunctions.messageBox(
                self, "Error", "Purchasing Error", "Product Out Of Stock")
        UIFunctions.fetch_table_data_response(self)
        return


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

############################# View All Requests ###############################
    def get_all_requests_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.view_requests_button.setText(
            _translate("MainWindow", "Loading..."))
        self.ui.view_requests_button.setEnabled(False)
        data = {
            "Customer ID": self.customer_info["Customer ID"]
        }
        self.worker = Fetch_Request(data)
        self.worker.start()
        self.worker.finished.connect(
            lambda: UIFunctions.fetch_table_data_response(self))
        self.worker.api_data.connect(self.render_requests_table)

    def render_requests_table(self, value: dict):
        if ("success" in value):
            arrays = value["success"]

            table_row = 0
            self.ui.requests_table.setRowCount(len(arrays))
            for row in arrays:
                self.btn_cancel = QtWidgets.QPushButton('Cancel')
                self.btn_pay_service_fee = QtWidgets.QPushButton('Pay Fee!')

                # connect buttons
                self.btn_pay_service_fee.clicked.connect(
                    self.pay_service_fee_clicked)

                self.btn_cancel.clicked.connect(self.cancel_request_clicked)

                self.ui.requests_table.setItem(
                    table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.requests_table.setItem(
                    table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.requests_table.setItem(
                    table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.requests_table.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.ui.requests_table.setCellWidget(
                    table_row, 4, self.btn_cancel)
                self.ui.requests_table.setCellWidget(
                    table_row, 5, self.btn_pay_service_fee)
                self.ui.requests_table.setItem(
                    table_row, 6, QtWidgets.QTableWidgetItem("No Fee" if row[4] is None else "{:.2f}".format(float(row[4]))))
                self.ui.requests_table.setItem(
                    table_row, 7, QtWidgets.QTableWidgetItem(row[-1]))
                table_row += 1
        else:
            UIFunctions.messageBox(
                self, "Error", "View Requests", value["error"])
############################ Pay Service Fee If Can ###########################

    def pay_service_fee_clicked(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.ui.requests_table.indexAt(button.pos())
        if index.isValid():
            column_index = index.column()
            row_index = index.row()
            item_id = self.ui.requests_table.item(row_index, 0).text()
            current_status = self.ui.requests_table.item(row_index, 3).text()
            if current_status == "Canceled":
                UIFunctions.messageBox(
                    self, "Error", "Service Fee Error", "You can't pay for an item with a request that's canceled")
            elif current_status == "In Progress" or current_status == "Approved":
                UIFunctions.messageBox(
                    self, "Error", "Service Fee Error", "You already paid for this Request!")
            elif current_status == "Submitted":
                UIFunctions.messageBox(
                    self, "Error", "Service Fee Error", "You don't have to pay for items under warranty")
            elif current_status == "Completed":
                UIFunctions.messageBox(
                    self, "Error", "Service Fee Error", "Request has already been serviced. There's nothing to pay fool")
            else:
                self.ui.requests_table.setCellWidget(
                    row_index, column_index, QtWidgets.QPushButton('Paying...'))
                self.worker = Pay_Service_Fee_Thread({
                    "Customer ID": self.customer_info["Customer ID"],
                    "Item ID": item_id,
                    "Row": row_index,
                    "Column": column_index
                })
                self.worker.start()
                self.worker.api_data.connect(self.service_fee_message_box)
                self.worker.api_data.connect(self.service_fee_change_table)

    def service_fee_change_table(self, response: dict):
        if ("success" in response):
            service_fee = "{:.2f}".format(float(response["success"]))
            row_index = response["Row"]
            column_index = response["Column"]
            today = date.today()
            curr_date = str(today.strftime('%A, %B %d %Y'))
            self.ui.requests_table.setItem(
                row_index, 6, QtWidgets.QTableWidgetItem(service_fee))
            self.ui.requests_table.setCellWidget(
                row_index, column_index, QtWidgets.QPushButton("Pay Fee!"))
            self.ui.requests_table.setItem(
                row_index, 3, QtWidgets.QTableWidgetItem("In Progress"))
            self.ui.requests_table.setItem(
                row_index, 7, QtWidgets.QTableWidgetItem(curr_date))

    def service_fee_message_box(self, response: dict):
        if ("success" in response):
            UIFunctions.messageBox(
                self, "Success", "Service Fee", "Service Fee Successfully Paid For!")
        elif ('error' in response):
            UIFunctions.messageBox(
                self, "Error", "Request Failed!", response["error"])

############################# Cancel Request ############################################
    def cancel_request_clicked(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.ui.requests_table.indexAt(button.pos())
        if index.isValid():
            column_index = index.column()
            row_index = index.row()
            item_id = self.ui.requests_table.item(row_index, 0).text()
            current_status = self.ui.requests_table.item(row_index, 3).text()
            if current_status == "Approved":
                UIFunctions.messageBox(
                    self, "Error", "Canceling Error", "You can't cancel an Approved Request!")
            elif current_status == "Canceled":
                UIFunctions.messageBox(
                    self, "Error", "Canceling Error", "You already canceled that request!")
            elif current_status == "Completed":
                UIFunctions.messageBox(
                    self, "Error", "Canceling Error", "You can't cancel a completed request")
            else:
                self.ui.requests_table.setCellWidget(
                    row_index, column_index, QtWidgets.QPushButton('Canceling...'))
                self.worker = Cancel_Request_Thread({
                    "Customer ID": self.customer_info["Customer ID"],
                    "Request Status": "Canceled",
                    "Item ID": item_id,
                    "Row": row_index,
                    "Column": column_index
                })
                self.worker.start()
                # connect worker to functions
                self.worker.api_data.connect(self.cancel_request_change_table)
                self.worker.api_data.connect(self.canceling_message_box)

    def cancel_request_change_table(self, response: dict):
        if ("success" in response):
            row_index = response["Row"]
            column_index = response["Column"]
            self.ui.requests_table.setCellWidget(
                row_index, column_index, QtWidgets.QPushButton("Cancel"))
            self.ui.requests_table.setItem(
                row_index, 3, QtWidgets.QTableWidgetItem("Canceled"))

    def canceling_message_box(self, response: dict):
        if ("success" in response):
            UIFunctions.messageBox(
                self, "Success", "Cancel Request", "Request Successfully Canceled!")
        elif ('error' in response):
            UIFunctions.messageBox(
                self, "Error", "Cancel Failed!", response["error"])
############################# END #######################################################


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


class Fetch_Request(QThread):

    api_data = pyqtSignal(object)

    def __init__(self, info: dict, parent=None):
        QThread.__init__(self, parent)
        self.info = info  # contains customer ID and Name

    def run(self):
        PAYLOAD = {
            "Customer ID": self.info["Customer ID"]
        }
        r = requests.post(
            "http://localhost:5000/api/Customer/get/request", json=PAYLOAD)
        response = r.json()
        self.api_data.emit(response)


class Pay_Service_Fee_Thread(QThread):
    api_data = pyqtSignal(object)

    def __init__(self, info: dict, parent=None):
        QThread.__init__(self, parent)
        self.info = info  # contains customer ID and Name

    def run(self):
        PAYLOAD = {
            "Customer ID": self.info["Customer ID"],
            "Item ID": self.info["Item ID"]
        }
        r = requests.patch(
            "http://localhost:5000/api/Customer/update/request/payment", json=PAYLOAD)
        response = r.json()
        response["Row"] = self.info["Row"]
        response["Column"] = self.info["Column"]
        self.api_data.emit(response)


class Cancel_Request_Thread(QThread):
    api_data = pyqtSignal(object)

    def __init__(self, info: dict, parent=None):
        QThread.__init__(self, parent)
        self.info = info  # contains customer ID and Name

    def run(self):
        PAYLOAD = {
            "Customer ID": self.info["Customer ID"],
            "Item ID": self.info["Item ID"],
            "Request Status": self.info["Request Status"]
        }
        r = requests.patch(
            "http://localhost:5000/api/Customer/update/request", json=PAYLOAD)
        response = r.json()
        response["Row"] = self.info["Row"]
        response["Column"] = self.info["Column"]
        self.api_data.emit(response)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _input = json.loads(urllib.parse.unquote(sys.argv[-1]))
    print(_input)
    window = MainWindow(_input)
    sys.exit(app.exec_())
