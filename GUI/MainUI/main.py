import sys
import time
import json
import urllib.parse
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


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

############################################################################
    def get_products_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.submit_query.setText(_translate("MainWindow", "Loading..."))
        self.worker = Get_Products_Thread()
        self.worker.start()  # start the parallel function
        # execute function once api done with no data
        self.worker.finished.connect(self.fetch_table_data_response)
        # pass Signal data into render_tables function
        self.worker.api_data.connect(self.render_tables)

    def render_tables(self, value: dict):
        # NOTE: check if the value: dict has "success response"
        print(value)

    def fetch_table_data_response(self):
        _translate = QtCore.QCoreApplication.translate
        QtWidgets.QMessageBox.information(self, "Done", "API Request Complete")

        """Enable Buttons"""
        self.ui.submit_query.setEnabled(True)
        self.ui.fetch_orders_button.setEnabled(True)

        """Change Button Text"""
        self.ui.submit_query.setText(_translate("MainWindow", "Submit"))
        self.ui.fetch_orders_button.setText(
            _translate("MainWindow", "Fetch Purchases"))

############################################################################
    def get_purchases_api(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.fetch_orders_button.setText(
            _translate("MainWindow", "Loading..."))
        self.ui.fetch_orders_button.setEnabled(False)
        self.worker = Get_Purchases_Thread(self.customer_info)
        self.worker.start()

        self.worker.finished.connect(self.fetch_table_data_response)
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

    def handle_purchase_request_clicked(self):
        button = QtWidgets.qApp.focusWidget()
        # or button = self.sender()
        index = self.ui.item_table.indexAt(button.pos())
        if index.isValid():
            column_index = index.column()
            row_index = index.row()
            print(self.ui.item_table.selectionModel(
            ).currentIndex().sibling(row_index, column_index).data())


class Get_Products_Thread(QThread):
    # package the data into a signal, signal takes in object/ dictionary
    api_data = pyqtSignal(object)

    def run(self):
        data = dict()
        info = 0
        for i in range(3):
            info += i
            time.sleep(1)
        data["numbers"] = info
        # output the data after finished executing the script
        self.api_data.emit(data)


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
                "http://localhost:5000/api/Customer/purchases", json=PAYLOAD)
            # output the data after finished executing the script
            response = r.json()
            print(response["success"][0])
            self.api_data.emit(response)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _input = json.loads(urllib.parse.unquote(sys.argv[-1]))
    print(_input)
    window = MainWindow(_input)
    sys.exit(app.exec_())
