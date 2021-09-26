"""
Updated: 18 September 2021
TODO: Add Button logic
TODO: Copy over Error handling
"""
import requests
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminRegisterForm(object):
    def setupUi(self, AdminRegisterForm):
        AdminRegisterForm.setObjectName("AdminRegisterForm")
        AdminRegisterForm.resize(1720, 1500)

        # Add Transparent Background, Only show the Widget and Not the GUI Frame
        AdminRegisterForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        AdminRegisterForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            AdminRegisterForm.sizePolicy().hasHeightForWidth())
        AdminRegisterForm.setSizePolicy(sizePolicy)
        AdminRegisterForm.setToolTipDuration(0)
        self.RegisterContainer = QtWidgets.QWidget(AdminRegisterForm)
        self.RegisterContainer.setEnabled(True)
        self.RegisterContainer.setGeometry(QtCore.QRect(150, 20, 1591, 961))
        self.RegisterContainer.setStyleSheet("background-color: transparent;")
        self.RegisterContainer.setObjectName("RegisterContainer")
        self.LeftSide = QtWidgets.QLabel(self.RegisterContainer)
        self.LeftSide.setGeometry(QtCore.QRect(40, 20, 611, 911))
        self.LeftSide.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4F46E5, stop:1 #7C3AED);\n"
                                    "border-top-left-radius: 20px;\n"
                                    "border-bottom-left-radius: 20px;")
        self.LeftSide.setText("")
        self.LeftSide.setObjectName("LeftSide")
        self.admin_register_container = QtWidgets.QLabel(
            self.RegisterContainer)
        self.admin_register_container.setGeometry(
            QtCore.QRect(500, 20, 1071, 911))
        self.admin_register_container.setToolTipDuration(0)
        self.admin_register_container.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                    "border-top-right-radius: 20px;\n"
                                                    "border-bottom-right-radius: 20px;")
        self.admin_register_container.setText("")
        self.admin_register_container.setObjectName("admin_register_container")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.RegisterContainer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 120, 521, 241))
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
        self.admin_key = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.admin_key.setFont(font)
        self.admin_key.setObjectName("admin_key")
        self.RegisterTextContainer.addWidget(self.admin_key)
        self.admin_key_enter = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.admin_key_enter.sizePolicy().hasHeightForWidth())
        self.admin_key_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.admin_key_enter.setFont(font)
        self.admin_key_enter.setStyleSheet("QLineEdit {\n"
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
        self.admin_key_enter.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_key_enter.setObjectName("admin_key_enter")
        self.RegisterTextContainer.addWidget(self.admin_key_enter)
        self.register_button = QtWidgets.QPushButton(self.RegisterContainer)
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
        self.welcome_admin_message = QtWidgets.QLabel(self.RegisterContainer)
        self.welcome_admin_message.setEnabled(True)
        self.welcome_admin_message.setGeometry(QtCore.QRect(560, 40, 979, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.welcome_admin_message.sizePolicy().hasHeightForWidth())
        self.welcome_admin_message.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_admin_message.setFont(font)
        self.welcome_admin_message.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.welcome_admin_message.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_admin_message.setObjectName("welcome_admin_message")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.RegisterContainer)
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
        self.last_name_label = QtWidgets.QLabel(self.RegisterContainer)
        self.last_name_label.setGeometry(QtCore.QRect(1070, 120, 519, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.last_name_label.setFont(font)
        self.last_name_label.setObjectName("last_name_label")
        self.last_name_enter = QtWidgets.QLineEdit(self.RegisterContainer)
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
        self.phone_number_enter = QtWidgets.QLineEdit(self.RegisterContainer)
        self.phone_number_enter.setGeometry(QtCore.QRect(540, 439, 1001, 61))
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
        self.phone_number_label = QtWidgets.QLabel(self.RegisterContainer)
        self.phone_number_label.setGeometry(QtCore.QRect(540, 400, 519, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.phone_number_label.setFont(font)
        self.phone_number_label.setObjectName("phone_number_label")
        self.gender_comboBox = QtWidgets.QComboBox(self.RegisterContainer)
        self.gender_comboBox.setGeometry(QtCore.QRect(1075, 300, 461, 60))
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
        self.gender_label = QtWidgets.QLabel(self.RegisterContainer)
        self.gender_label.setGeometry(QtCore.QRect(1070, 250, 519, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gender_label.setFont(font)
        self.gender_label.setObjectName("gender_label")
        self.not_an_admin_label = QtWidgets.QLabel(self.RegisterContainer)
        self.not_an_admin_label.setGeometry(QtCore.QRect(880, 760, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(True)
        self.not_an_admin_label.setFont(font)
        self.not_an_admin_label.setToolTipDuration(0)
        self.not_an_admin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.not_an_admin_label.setObjectName("not_an_admin_label")
        self.go_back_button = QtWidgets.QPushButton(self.RegisterContainer)
        self.go_back_button.setGeometry(QtCore.QRect(1100, 780, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setUnderline(True)
        self.go_back_button.setFont(font)
        self.go_back_button.setStyleSheet("QPushButton#go_back_button {\n"
                                          "    color: #6366F1;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton#go_back_button:hover {\n"
                                          "    color: #4338CA;\n"
                                          "}")
        self.go_back_button.setObjectName("go_back_button")

        self.retranslateUi(AdminRegisterForm)
        self.gender_comboBox.setCurrentIndex(-1)
        """
        Button Functionalities Start
        """
        self.go_back_button.clicked.connect(self.open_register_form_back)
        self.go_back_button.clicked.connect(AdminRegisterForm.close)

        self.register_button.clicked.connect(self.register)
        """
        Button Functionalities End
        """
        QtCore.QMetaObject.connectSlotsByName(AdminRegisterForm)

    def register(self):
        name = self.firstname_enter.text()
        admin_id = self.last_name_enter.text()
        admin_key = self.admin_key_enter.text()
        gender = self.gender_comboBox.currentText()
        phone_number = self.phone_number_enter.text()
        password = self.password_enter.text()
        confirm_password = self.confirm_password_enter.text()
        if (gender and len(name) > 1 and len(admin_id) > 1 and phone_number and password and confirm_password and admin_key):
            if (confirm_password != password):
                return self.error_popup("Password Not The Same!")
            elif (len(phone_number) != 8):
                return self.error_popup("Invalid Phone Number")
            elif (admin_key != "group16"):
                return self.error_popup("Invalid Admin Key!")
            else:
                # create payload for POST request to add Customer into SQLdb
                PAYLOAD = {
                    "Name": name,
                    "Password": password,
                    "Admin ID": admin_id,
                    "Gender": gender,
                    "Phone Number": phone_number
                }
                r = requests.post(
                    "http://localhost:5000/api/Admin/add", json=PAYLOAD)
                response = r.json()
                # check if successfully entered into SQLdb or not
                if ("success" in response):
                    return self.success_popup(name)
                else:
                    return self.error_popup("That Admin ID is already taken fool")

        else:
            return self.error_popup("One Of the Fields Is Not Filled Properly!")

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

    def open_register_form_back(self):
        from RegisterForm import Ui_RegisterForm as RegisterForm

        self.register_form = QtWidgets.QWidget()
        self.ui = RegisterForm()
        self.ui.setupUi(self.register_form, PROPS=dict())
        self.register_form.show()

    def retranslateUi(self, AdminRegisterForm):
        _translate = QtCore.QCoreApplication.translate
        AdminRegisterForm.setWindowTitle(
            _translate("AdminRegisterForm", "Form"))
        self.username_label.setText(_translate(
            "AdminRegisterForm", "Name"))
        self.admin_key.setText(_translate("AdminRegisterForm", "Admin Key"))
        self.register_button.setText(
            _translate("AdminRegisterForm", "Register!"))
        self.welcome_admin_message.setText(_translate(
            "AdminRegisterForm", "Hello Future Administrator!"))
        self.password_label.setText(
            _translate("AdminRegisterForm", "Password"))
        self.confirm_password_label.setText(
            _translate("AdminRegisterForm", "Confirm Password"))
        self.last_name_label.setText(
            _translate("AdminRegisterForm", "Admin ID"))
        self.phone_number_label.setText(
            _translate("AdminRegisterForm", "Phone Number"))
        self.gender_label.setText(_translate("AdminRegisterForm", "Gender"))
        self.not_an_admin_label.setText(_translate(
            "AdminRegisterForm", "Not An Administrator?"))
        self.go_back_button.setText(_translate("AdminRegisterForm", "Go Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminRegisterForm = QtWidgets.QWidget()
    ui = Ui_AdminRegisterForm()
    ui.setupUi(AdminRegisterForm)
    AdminRegisterForm.show()
    sys.exit(app.exec_())
