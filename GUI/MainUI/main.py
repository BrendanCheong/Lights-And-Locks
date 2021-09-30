import sys
import time
import json
import urllib.parse
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self, hell):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        # Render Tables
        self.ui.submit_query.clicked.connect(
            lambda: UIFunctions.get_products_api(self)
        )

        print(hell)

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

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
        self.ui.submit_query.setText(_translate("MainWindow", "Test"))


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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _input = json.loads(urllib.parse.unquote(sys.argv[-1]))
    print(_input)
    window = MainWindow(_input)
    sys.exit(app.exec_())
