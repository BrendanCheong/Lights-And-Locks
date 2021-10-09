import os
from main import MainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *


class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 100

            # set Max Width
            if width == 100:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(
                self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def fetch_table_data_response(self):
        _translate = QtCore.QCoreApplication.translate

        """Enable Buttons"""
        self.ui.submit_query.setEnabled(True)
        self.ui.fetch_orders_button.setEnabled(True)
        self.ui.view_requests_button.setEnabled(True)

        """Change Button Text"""
        self.ui.submit_query.setText(_translate("MainWindow", "Submit"))
        self.ui.fetch_orders_button.setText(
            _translate("MainWindow", "Fetch Purchases"))
        self.ui.view_requests_button.setText(
            _translate("MainWindow", "View Requests"))
        self.ui.purchase_now_button.setText(
            _translate("MainWindow", "Purchase Now"))

    def change_category_model_comboBox(self):
        category_comboBox_text = self.ui.category_comboBox.currentText()
        model_comboBox_text = self.ui.model_comboBox.currentText()
        if (category_comboBox_text == "Locks"):
            self.ui.model_comboBox.clear()
            self.ui.model_comboBox.addItems(
                ["All", "SmartHome1", "Safe1", "Safe2"])
        elif (category_comboBox_text == "Lights"):
            self.ui.model_comboBox.clear()
            self.ui.model_comboBox.addItems(
                ["All", "SmartHome1", "Light1", "Light2"])

    def messageBox(self, status: str, title: str, message: str):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QtWidgets.QMessageBox.Information) if status == "Success" else msg.setIcon(
            QtWidgets.QMessageBox.Warning)
        msg.setText(message)
        if (status == "Error"):
            msg.setStandardButtons(QtWidgets.QMessageBox.Retry)
            msg.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #EA580C, stop:1 #E11D48);
                color: rgb(255, 255, 255);
            }
            """)
        else:
            msg.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #14B8A6, stop:1 #0891B2);
                color: rgb(255, 255, 255);
            }
            """)

        x = msg.exec_()

    def decrease_inventory_by_one(self):
        current_inventory_level = self.ui.product_table.item(0, 4).text()
        if (int(current_inventory_level) > 0):
            self.ui.product_table.setItem(0, 4, QtWidgets.QTableWidgetItem(
                str(int(current_inventory_level) - 1)))

    def exit_mainwindow(self):
        self.close()
        os.system("cd .. && python LoginForm.py")
