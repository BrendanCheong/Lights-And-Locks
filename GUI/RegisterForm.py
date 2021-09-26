"""
Updated 25 September 2021

"""
import requests
import uuid
from check_email import check as check_email
from AdminRegister import Ui_AdminRegisterForm as AdminRegisterForm
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterForm(object):
    def setupUi(self, RegisterForm, PROPS):
        RegisterForm.setObjectName("RegisterForm")
        RegisterForm.resize(1720, 1500)

        # Add Transparent Background, Only show the Widget and Not the GUI Frame
        RegisterForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        RegisterForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            RegisterForm.sizePolicy().hasHeightForWidth())
        RegisterForm.setSizePolicy(sizePolicy)
        RegisterForm.setToolTipDuration(0)
        self.LoginContainer = QtWidgets.QWidget(RegisterForm)
        self.LoginContainer.setEnabled(True)
        self.LoginContainer.setGeometry(QtCore.QRect(150, 20, 1591, 961))
        self.LoginContainer.setStyleSheet("background-color: transparent;")
        self.LoginContainer.setObjectName("LoginContainer")
        self.LeftSide = QtWidgets.QLabel(self.LoginContainer)
        self.LeftSide.setGeometry(QtCore.QRect(40, 20, 611, 911))
        self.LeftSide.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(37, 99, 235, 1), stop:1 rgba(79, 70, 229, 1));\n"
                                    "border-top-left-radius: 20px;\n"
                                    "border-bottom-left-radius: 20px;")
        self.LeftSide.setText("")
        self.LeftSide.setObjectName("LeftSide")
        self.login_details_container = QtWidgets.QLabel(self.LoginContainer)
        self.login_details_container.setGeometry(
            QtCore.QRect(500, 20, 1071, 911))
        self.login_details_container.setToolTipDuration(0)
        self.login_details_container.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "border-top-right-radius: 20px;\n"
                                                   "border-bottom-right-radius: 20px;")
        self.login_details_container.setText("")
        self.login_details_container.setObjectName("login_details_container")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.LoginContainer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 120, 521, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.RegisterTextContainer = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.RegisterTextContainer.setContentsMargins(0, 0, 0, 0)
        self.RegisterTextContainer.setSpacing(20)
        self.RegisterTextContainer.setObjectName("RegisterTextContainer")
        self.username_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.RegisterTextContainer.addWidget(self.username_label)
        self.firstname_enter = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.firstname_enter.sizePolicy().hasHeightForWidth())
        self.firstname_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.firstname_enter.setFont(font)
        self.firstname_enter.setStyleSheet("QLineEdit {\n"
                                           "    border: 10px;\n"
                                           "    border-color: transparent;\n"
                                           "    padding: 0 8px;\n"
                                           "    background: rgba(229, 231, 235, 1);\n"
                                           "    font-size: 16px;\n"
                                           "    border-top-right-radius: 10px;\n"
                                           "    border-top-left-radius: 10px;\n"
                                           "    border-bottom-right-radius: 10px;\n"
                                           "    border-bottom-left-radius: 10px;\n"
                                           "}")
        self.firstname_enter.setObjectName("firstname_enter")
        self.RegisterTextContainer.addWidget(self.firstname_enter)
        self.email_address_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.email_address_label.setFont(font)
        self.email_address_label.setObjectName("email_address_label")
        self.RegisterTextContainer.addWidget(self.email_address_label)
        self.email_address_enter = QtWidgets.QLineEdit(
            self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.email_address_enter.sizePolicy().hasHeightForWidth())
        self.email_address_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.email_address_enter.setFont(font)
        self.email_address_enter.setStyleSheet("QLineEdit {\n"
                                               "    border: 10px;\n"
                                               "    border-color: transparent;\n"
                                               "    padding: 0 8px;\n"
                                               "    background: rgba(229, 231, 235, 1);\n"
                                               "    font-size: 16px;\n"
                                               "    border-top-right-radius: 10px;\n"
                                               "    border-top-left-radius: 10px;\n"
                                               "    border-bottom-right-radius: 10px;\n"
                                               "    border-bottom-left-radius: 10px;\n"
                                               "}")
        self.email_address_enter.setObjectName("email_address_enter")
        self.RegisterTextContainer.addWidget(self.email_address_enter)
        self.address_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.address_label.setFont(font)
        self.address_label.setObjectName("address_label")
        self.RegisterTextContainer.addWidget(self.address_label)
        self.address_enter = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.address_enter.sizePolicy().hasHeightForWidth())
        self.address_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.address_enter.setFont(font)
        self.address_enter.setStyleSheet("QLineEdit {\n"
                                         "    border: 10px;\n"
                                         "    border-color: transparent;\n"
                                         "    padding: 0 8px;\n"
                                         "    background: rgba(229, 231, 235, 1);\n"
                                         "    font-size: 16px;\n"
                                         "    border-top-right-radius: 10px;\n"
                                         "    border-top-left-radius: 10px;\n"
                                         "    border-bottom-right-radius: 10px;\n"
                                         "    border-bottom-left-radius: 10px;\n"
                                         "}")
        self.address_enter.setObjectName("address_enter")
        self.RegisterTextContainer.addWidget(self.address_enter)
        self.register_button = QtWidgets.QPushButton(self.LoginContainer)
        self.register_button.setGeometry(QtCore.QRect(920, 730, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.register_button.setFont(font)
        self.register_button.setToolTipDuration(0)
        self.register_button.setStyleSheet("QPushButton#register_button {\n"
                                           "    border-top-right-radius: 10px;\n"
                                           "    border-top-left-radius: 10px;\n"
                                           "    border-bottom-right-radius: 10px;\n"
                                           "    border-bottom-left-radius: 10px;\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 212, 191, 1), stop:1 rgba(6, 182, 212, 1));\n"
                                           "    font: 22px;\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#register_button:hover {\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                           ", stop:1 #0E7490);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton#register_button:pressed {\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                           ", stop:1 #0E7490);\n"
                                           "    padding-left: 5px;\n"
                                           "    padding-top: 5px;\n"
                                           "}")
        self.register_button.setObjectName("register_button")
        self.register_now_callToAction = QtWidgets.QLabel(self.LoginContainer)
        self.register_now_callToAction.setEnabled(True)
        self.register_now_callToAction.setGeometry(
            QtCore.QRect(560, 40, 979, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.register_now_callToAction.sizePolicy().hasHeightForWidth())
        self.register_now_callToAction.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.register_now_callToAction.setFont(font)
        self.register_now_callToAction.setStyleSheet(
            "color: rgba(0, 0, 0, 200);")
        self.register_now_callToAction.setAlignment(QtCore.Qt.AlignCenter)
        self.register_now_callToAction.setObjectName(
            "register_now_callToAction")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.LoginContainer)
        self.verticalLayoutWidget_3.setGeometry(
            QtCore.QRect(540, 510, 1001, 201))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.password_container = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.password_container.setContentsMargins(0, 0, 0, 0)
        self.password_container.setObjectName("password_container")
        self.password_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.password_container.addWidget(self.password_label)
        self.password_enter = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.password_enter.sizePolicy().hasHeightForWidth())
        self.password_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.password_enter.setFont(font)
        self.password_enter.setStyleSheet("QLineEdit {\n"
                                          "    border: 10px;\n"
                                          "    border-color: transparent;\n"
                                          "    padding: 0 8px;\n"
                                          "    background: rgba(229, 231, 235, 1);\n"
                                          "    font-size: 16px;\n"
                                          "    border-top-right-radius: 10px;\n"
                                          "    border-top-left-radius: 10px;\n"
                                          "    border-bottom-right-radius: 10px;\n"
                                          "    border-bottom-left-radius: 10px;\n"
                                          "}")
        self.password_enter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_enter.setObjectName("password_enter")
        self.password_container.addWidget(self.password_enter)
        self.confirm_password_label = QtWidgets.QLabel(
            self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_password_label.setFont(font)
        self.confirm_password_label.setObjectName("confirm_password_label")
        self.password_container.addWidget(self.confirm_password_label)
        self.confirm_password_enter = QtWidgets.QLineEdit(
            self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.confirm_password_enter.sizePolicy().hasHeightForWidth())
        self.confirm_password_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.confirm_password_enter.setFont(font)
        self.confirm_password_enter.setStyleSheet("QLineEdit {\n"
                                                  "    border: 10px;\n"
                                                  "    border-color: transparent;\n"
                                                  "    padding: 0 8px;\n"
                                                  "    background: rgba(229, 231, 235, 1);\n"
                                                  "    font-size: 16px;\n"
                                                  "    border-top-right-radius: 10px;\n"
                                                  "    border-top-left-radius: 10px;\n"
                                                  "    border-bottom-right-radius: 10px;\n"
                                                  "    border-bottom-left-radius: 10px;\n"
                                                  "}")
        self.confirm_password_enter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_enter.setObjectName("confirm_password_enter")
        self.password_container.addWidget(self.confirm_password_enter)
        self.last_name_label = QtWidgets.QLabel(self.LoginContainer)
        self.last_name_label.setGeometry(QtCore.QRect(1070, 120, 519, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.last_name_label.setFont(font)
        self.last_name_label.setObjectName("last_name_label")
        self.last_name_enter = QtWidgets.QLineEdit(self.LoginContainer)
        self.last_name_enter.setGeometry(QtCore.QRect(1070, 171, 471, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.last_name_enter.sizePolicy().hasHeightForWidth())
        self.last_name_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.last_name_enter.setFont(font)
        self.last_name_enter.setStyleSheet("QLineEdit {\n"
                                           "    border: 10px;\n"
                                           "    border-color: transparent;\n"
                                           "    padding: 0 8px;\n"
                                           "    background: rgba(229, 231, 235, 1);\n"
                                           "    font-size: 16px;\n"
                                           "    border-top-right-radius: 10px;\n"
                                           "    border-top-left-radius: 10px;\n"
                                           "    border-bottom-right-radius: 10px;\n"
                                           "    border-bottom-left-radius: 10px;\n"
                                           "}")
        self.last_name_enter.setObjectName("last_name_enter")
        self.phone_number_enter = QtWidgets.QLineEdit(self.LoginContainer)
        self.phone_number_enter.setGeometry(QtCore.QRect(1070, 439, 471, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.phone_number_enter.sizePolicy().hasHeightForWidth())
        self.phone_number_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.phone_number_enter.setFont(font)
        self.phone_number_enter.setStyleSheet("QLineEdit {\n"
                                              "    border: 10px;\n"
                                              "    border-color: transparent;\n"
                                              "    padding: 0 8px;\n"
                                              "    background: rgba(229, 231, 235, 1);\n"
                                              "    font-size: 16px;\n"
                                              "    border-top-right-radius: 10px;\n"
                                              "    border-top-left-radius: 10px;\n"
                                              "    border-bottom-right-radius: 10px;\n"
                                              "    border-bottom-left-radius: 10px;\n"
                                              "}")
        self.phone_number_enter.setObjectName("phone_number_enter")
        self.phone_number_label = QtWidgets.QLabel(self.LoginContainer)
        self.phone_number_label.setGeometry(QtCore.QRect(1070, 388, 519, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.phone_number_label.setFont(font)
        self.phone_number_label.setObjectName("phone_number_label")
        self.gender_comboBox = QtWidgets.QComboBox(self.LoginContainer)
        self.gender_comboBox.setGeometry(QtCore.QRect(1075, 305, 461, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.gender_comboBox.setFont(font)
        self.gender_comboBox.setStyleSheet("QComboBox {\n"
                                           "    border: 1px solid gray;\n"
                                           "    border-radius: 3px;\n"
                                           "    border-color: #E2E8F0;\n"
                                           "    padding: 1px 18px 1px 3px;\n"
                                           "    min-width: 6em;\n"
                                           "    border-top-right-radius: 10px;\n"
                                           "    border-top-left-radius: 10px;\n"
                                           "    border-bottom-right-radius: 10px;\n"
                                           "    border-bottom-left-radius: 10px;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox:editable {\n"
                                           "    background: white;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                           "     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                           "                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                           "                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                                           "}\n"
                                           "\n"
                                           "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                           "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                           "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                           "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                           "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox:on { /* shift the text when the popup opens */\n"
                                           "    padding-top: 3px;\n"
                                           "    padding-left: 4px;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox::drop-down {\n"
                                           "    subcontrol-origin: padding;\n"
                                           "    subcontrol-position: top right;\n"
                                           "    width: 15px;\n"
                                           "\n"
                                           "    border-left-width: 1px;\n"
                                           "    border-left-color: gray;\n"
                                           "    border-left-style: solid; /* just a single line */\n"
                                           "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                           "    border-bottom-right-radius: 3px;\n"
                                           "    border-bottom-right-radius: 10px;\n"
                                           "    border-bottom-left-radius: 10px;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                           "    top: 1px;\n"
                                           "    left: 1px;\n"
                                           "}")
        self.gender_comboBox.setIconSize(QtCore.QSize(25, 25))

        # Add Drop down options to Gender options
        self.gender_comboBox.addItems(["Male", "Female", "Other"])
        self.gender_comboBox.setObjectName("gender_comboBox")

        self.gender_label = QtWidgets.QLabel(self.LoginContainer)
        self.gender_label.setGeometry(QtCore.QRect(1070, 250, 519, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gender_label.setFont(font)
        self.gender_label.setObjectName("gender_label")
        self.admin_registration_button = QtWidgets.QPushButton(
            self.LoginContainer)
        self.admin_registration_button.setGeometry(
            QtCore.QRect(870, 840, 391, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_registration_button.sizePolicy().hasHeightForWidth())
        self.admin_registration_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.admin_registration_button.setFont(font)
        self.admin_registration_button.setToolTipDuration(0)
        self.admin_registration_button.setStyleSheet("QPushButton#admin_registration_button {\n"
                                                     "    border-top-right-radius: 10px;\n"
                                                     "    border-top-left-radius: 10px;\n"
                                                     "    border-bottom-right-radius: 10px;\n"
                                                     "    border-bottom-left-radius: 10px;\n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3B82F6, stop:1 #6366F1);\n"
                                                     "    font: 22px;\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton#admin_registration_button:hover {\n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #1E40AF\n"
                                                     ", stop:1 #3730A3);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton#admin_registration_button:pressed {\n"
                                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #1E40AF, stop:1 #3730A3);\n"
                                                     "    padding-left: 5px;\n"
                                                     "    padding-top: 5px;\n"
                                                     "}")
        self.admin_registration_button.setObjectName(
            "admin_registration_button")
        self.already_have_an_account = QtWidgets.QLabel(self.LoginContainer)
        self.already_have_an_account.setGeometry(
            QtCore.QRect(880, 760, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(True)
        self.already_have_an_account.setFont(font)
        self.already_have_an_account.setToolTipDuration(0)
        self.already_have_an_account.setAlignment(QtCore.Qt.AlignCenter)
        self.already_have_an_account.setObjectName("already_have_an_account")
        self.login_now_button = QtWidgets.QPushButton(self.LoginContainer)
        self.login_now_button.setGeometry(QtCore.QRect(1100, 780, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setUnderline(True)
        self.login_now_button.setFont(font)
        self.login_now_button.setStyleSheet("QPushButton#login_now_button {\n"
                                            "    color: #6366F1;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton#login_now_button:hover {\n"
                                            "    color: #4338CA;\n"
                                            "}")
        self.login_now_button.setObjectName("login_now_button")

        self.retranslateUi(RegisterForm)
        self.gender_comboBox.setCurrentIndex(-1)
        """
        Button Functionalities Start
        """
        # Connect Admin Registration Button
        self.admin_registration_button.clicked.connect(
            self.open_admin_registration)
        self.admin_registration_button.clicked.connect(RegisterForm.close)

        # Connect Login Now Back Button
        self.login_now_button.clicked.connect(self.open_login_form_back)
        self.login_now_button.clicked.connect(RegisterForm.close)

        # Connect Register Button
        self.register_button.clicked.connect(self.register)
        """
        Button Functionalities End
        """
        QtCore.QMetaObject.connectSlotsByName(RegisterForm)

    def register(self):
        gender = self.gender_comboBox.currentText()
        name = self.firstname_enter.text()
        customer_id = self.last_name_enter.text()
        email_address = self.email_address_enter.text()
        address = self.address_enter.text()
        phone_number = self.phone_number_enter.text()
        password = self.password_enter.text()
        confirm_password = self.confirm_password_enter.text()
        # Collect all the textfield and check against them for validity
        if (gender and len(name) > 1 and email_address and address and phone_number and password and confirm_password and len(customer_id) > 1):
            if (confirm_password != password):
                return self.error_popup("Password Not The Same!")
            elif (len(phone_number) != 8):
                return self.error_popup("Invalid Phone Number")
            elif (not check_email(email_address)):
                return self.error_popup("Invalid Email!")
            else:
                # create payload for POST request to add Customer into SQLdb
                PAYLOAD = {
                    "Name": name,
                    "Email": email_address,
                    "Password": password,
                    "Customer ID": customer_id,
                    "Gender": gender,
                    "PhoneNumber": phone_number,
                    "Address": address
                }
                r = requests.post(
                    "http://localhost:5000/api/Customer/add", json=PAYLOAD)
                response = r.json()
                # check if successfully entered into SQLdb or not
                if ("success" in response):
                    return self.success_popup(name)
                else:
                    return self.error_popup("That User ID is already taken fool")

        else:
            return self.error_popup("One Of the Fields Is Not Filled!")

    def error_popup(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Oh No! An Error!")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Retry)

        x = msg.exec_()

    def success_popup(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Registration Success")
        msg.setText(text + " Registered Successfully")
        msg.setIcon(QtWidgets.QMessageBox.Information)

        y = msg.exec_()

    def open_admin_registration(self):
        self.admin_registration_widget = QtWidgets.QWidget()
        self.ui = AdminRegisterForm()
        self.ui.setupUi(self.admin_registration_widget)
        self.admin_registration_widget.show()

    def open_login_form_back(self):
        from LoginForm import Ui_LoginForm as LoginForm

        self.login_form_widget = QtWidgets.QWidget()
        self.ui = LoginForm()
        self.ui.setupUi(self.login_form_widget)
        self.login_form_widget.show()

    def retranslateUi(self, RegisterForm):
        _translate = QtCore.QCoreApplication.translate
        RegisterForm.setWindowTitle(_translate("RegisterForm", "Form"))
        self.username_label.setText(_translate("RegisterForm", "Full Name"))
        self.email_address_label.setText(
            _translate("RegisterForm", "Email Address"))
        self.address_label.setText(_translate("RegisterForm", "Address"))
        self.register_button.setText(_translate("RegisterForm", "Register!"))
        self.register_now_callToAction.setText(
            _translate("RegisterForm", "Register Now!"))
        self.password_label.setText(_translate("RegisterForm", "Password"))
        self.confirm_password_label.setText(
            _translate("RegisterForm", "Confirm Password"))
        self.last_name_label.setText(_translate("RegisterForm", "User ID"))
        self.phone_number_label.setText(
            _translate("RegisterForm", "Phone Number"))
        self.gender_label.setText(_translate("RegisterForm", "Gender"))
        self.admin_registration_button.setText(
            _translate("RegisterForm", "Admin Registration"))
        self.already_have_an_account.setText(
            _translate("RegisterForm", "Already Have An Account?"))
        self.login_now_button.setText(_translate("RegisterForm", "Login Now!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterForm = QtWidgets.QWidget()
    ui = Ui_RegisterForm()
    ui.setupUi(RegisterForm, PROPS=dict())
    RegisterForm.show()
    sys.exit(app.exec_())
