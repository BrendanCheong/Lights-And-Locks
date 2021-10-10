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

    def finished_loading_text(self):
        _translate = QtCore.QCoreApplication.translate

        """Enable Buttons"""
        self.ui.refresh_button_admin.setEnabled(True)
        self.ui.view_items_category_model_button.setEnabled(True)
        self.ui.view_customers_button.setEnabled(True)
        self.ui.initialise_database_button.setEnabled(True)

        """Change Loading Text"""
        self.ui.refresh_button_admin.setText(_translate(
            "MainWindow", "Display Sold && Unsold Items"))
        self.ui.view_items_category_model_button.setText(
            _translate("MainWindow", "Items Sold in Category && Model"))
        self.ui.view_customers_button.setText(_translate(
            "MainWindow", "View Customers With Unpaid Fees"))
        self.ui.initialise_database_button.setText(
            _translate("MainWindow", "Initialise Database!"))

    def exit_mainwindow(self):
        self.close()
        os.system("cd .. && python LoginForm.py")
