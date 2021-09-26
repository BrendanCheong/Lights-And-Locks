"""
Updated: 15 September 2021
TODO: Add in props attribute to the function
"""
import requests
import os
import urllib.parse
import json
from check_email import check as check_email
from RegisterForm import Ui_RegisterForm as RegisterForm
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        PROPS = dict()
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(1331, 867)

        # Add Transparent Background, Only show the Widget and Not the GUI Frame
        LoginForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LoginForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            LoginForm.sizePolicy().hasHeightForWidth())
        LoginForm.setSizePolicy(sizePolicy)
        LoginForm.setToolTipDuration(0)
        self.LoginContainer = QtWidgets.QWidget(LoginForm)
        self.LoginContainer.setEnabled(True)
        self.LoginContainer.setGeometry(QtCore.QRect(29, 29, 1250, 800))
        self.LoginContainer.setStyleSheet("background-color: transparent;")
        self.LoginContainer.setObjectName("LoginContainer")
        self.LeftSide = QtWidgets.QLabel(self.LoginContainer)
        self.LeftSide.setGeometry(QtCore.QRect(49, 49, 541, 710))
        self.LeftSide.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(37, 99, 235, 1), stop:1 rgba(79, 70, 229, 1));\n"
                                    "border-top-left-radius: 20px;\n"
                                    "border-bottom-left-radius: 20px;")
        self.LeftSide.setText("")
        self.LeftSide.setObjectName("LeftSide")
        self.login_details_container = QtWidgets.QLabel(self.LoginContainer)
        self.login_details_container.setGeometry(
            QtCore.QRect(420, 49, 791, 710))
        self.login_details_container.setToolTipDuration(0)
        self.login_details_container.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "border-top-right-radius: 20px;\n"
                                                   "border-bottom-right-radius: 20px;")
        self.login_details_container.setText("")
        self.login_details_container.setObjectName("login_details_container")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.LoginContainer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 90, 581, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LoginTextContainer = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.LoginTextContainer.setContentsMargins(0, 0, 0, 0)
        self.LoginTextContainer.setSpacing(20)
        self.LoginTextContainer.setObjectName("LoginTextContainer")
        self.welcome_message = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.welcome_message.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.welcome_message.sizePolicy().hasHeightForWidth())
        self.welcome_message.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_message.setFont(font)
        self.welcome_message.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.welcome_message.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_message.setObjectName("welcome_message")
        self.LoginTextContainer.addWidget(self.welcome_message)
        self.username_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.LoginTextContainer.addWidget(self.username_label)
        self.username_enter = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.username_enter.sizePolicy().hasHeightForWidth())
        self.username_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.username_enter.setFont(font)
        self.username_enter.setStyleSheet("QLineEdit {\n"
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
        self.username_enter.setObjectName("username_enter")
        self.LoginTextContainer.addWidget(self.username_enter)
        self.password_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.LoginTextContainer.addWidget(self.password_label)
        self.password_enter = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.password_enter.sizePolicy().hasHeightForWidth())
        self.password_enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
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
        self.LoginTextContainer.addWidget(self.password_enter)
        self.login_button = QtWidgets.QPushButton(self.LoginContainer)
        self.login_button.setGeometry(QtCore.QRect(670, 470, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_button.setFont(font)
        self.login_button.setToolTipDuration(0)
        self.login_button.setStyleSheet("QPushButton#login_button {\n"
                                        "    border-top-right-radius: 10px;\n"
                                        "    border-top-left-radius: 10px;\n"
                                        "    border-bottom-right-radius: 10px;\n"
                                        "    border-bottom-left-radius: 10px;\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 212, 191, 1), stop:1 rgba(6, 182, 212, 1));\n"
                                        "    font-size: 16px;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#login_button:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                        ", stop:1 #0E7490);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#login_button:pressed {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                        ", stop:1 #0E7490);\n"
                                        "    padding-left: 5px;\n"
                                        "    padding-top: 5px;\n"
                                        "}")
        self.login_button.setObjectName("login_button")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.LoginContainer)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(620, 540, 391, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(0)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.register_now_button = QtWidgets.QPushButton(
            self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.register_now_button.sizePolicy().hasHeightForWidth())
        self.register_now_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.register_now_button.setFont(font)
        self.register_now_button.setToolTipDuration(0)
        self.register_now_button.setStyleSheet("QPushButton#register_now_button {\n"
                                               "    border-top-right-radius: 10px;\n"
                                               "    border-top-left-radius: 10px;\n"
                                               "    border-bottom-right-radius: 10px;\n"
                                               "    border-bottom-left-radius: 10px;\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #EF4444, stop:1 #F97316);\n"
                                               "    font-size: 16px;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton#register_now_button:hover {\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #B91C1C\n"
                                               ", stop:1 #C2410C);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton#register_now_button:pressed {\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #B91C1C\n"
                                               ", stop:1 #C2410C);\n"
                                               "    padding-left: 5px;\n"
                                               "    padding-top: 5px;\n"
                                               "}")
        self.register_now_button.setObjectName("register_now_button")
        self.verticalLayout.addWidget(self.register_now_button)
        self.Admin_layout = QtWidgets.QWidget(self.LoginContainer)
        self.Admin_layout.setGeometry(
            QtCore.QRect(620, 640, 391, 81))
        self.Admin_layout.setObjectName("Admin_layout")
        self.Admin_login = QtWidgets.QVBoxLayout(self.Admin_layout)
        self.Admin_login.setContentsMargins(0, 0, 0, 0)
        self.Admin_login.setObjectName("Admin_login")
        self.admin_prompt = QtWidgets.QLabel(self.Admin_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(True)
        self.admin_prompt.setFont(font)
        self.admin_prompt.setToolTipDuration(0)
        self.admin_prompt.setAlignment(QtCore.Qt.AlignCenter)
        self.admin_prompt.setObjectName("admin_prompt")
        self.Admin_login.addWidget(self.admin_prompt)
        self.Admin_login_button = QtWidgets.QPushButton(
            self.Admin_layout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Admin_login_button.sizePolicy().hasHeightForWidth())
        self.Admin_login_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.Admin_login_button.setFont(font)
        self.Admin_login_button.setToolTipDuration(0)
        self.Admin_login_button.setStyleSheet("QPushButton#Admin_login_button {\n"
                                              "    border-top-right-radius: 10px;\n"
                                              "    border-top-left-radius: 10px;\n"
                                              "    border-bottom-right-radius: 10px;\n"
                                              "    border-bottom-left-radius: 10px;\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 212, 191, 1), stop:1 rgba(6, 182, 212, 1));\n"
                                              "    font-size: 16px;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton#Admin_login_button:hover {\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                              ", stop:1 #0E7490);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton#Admin_login_button:pressed {\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                              ", stop:1 #0E7490);\n"
                                              "    padding-left: 5px;\n"
                                              "    padding-top: 5px;\n"
                                              "}")
        self.Admin_login_button.setObjectName("Admin_login_button")
        self.Admin_login.addWidget(self.Admin_login_button)

        # Add Drop Shadow effect to selected Widgets
        self.login_button.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=15, xOffset=0, yOffset=6))
        self.LoginContainer.setGraphicsEffect(
            QtWidgets.QGraphicsDropShadowEffect(blurRadius=15, xOffset=0, yOffset=6))

        # This will be our success messageBox to be used later for Loging in
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Registration Success")

        """
        Button Functionalities Start Here
        """
        # Connect to Register Now Page
        self.register_now_button.clicked.connect(lambda:
                                                 self.open_register_form(PROPS))
        self.register_now_button.clicked.connect(LoginForm.close)

        # Connect to Admin Login Page
        self.Admin_login_button.clicked.connect(self.open_admin_login)
        self.Admin_login_button.clicked.connect(LoginForm.close)

        # Connect to Login Function
        self.login_button.clicked.connect(self.login)
        """
        Button Functionalities End
        """
        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def login(self):
        """Start Query, if Query is Correct, then Open new Page with Data"""
        _user_id = self.username_enter.text()
        _password = self.password_enter.text()

        if (_user_id and len(_password) > 1):
            PAYLOAD = {
                "Customer ID": _user_id,
                "Password": _password
            }
            # create JSON payload to send to server to find if Customer exists in SQLdb
            r = requests.post(
                "http://localhost:5000/api/Customer/login", json=PAYLOAD)
            response = r.json()

            # Check successful or not
            if ("success" in response):
                resp = response["success"]
                print(resp["Customer ID"], resp["Email"], resp["Name"])
                return self.success_popup({
                    "Customer ID": resp["Customer ID"],
                    "Email": resp["Email"],
                    "Name": resp["Name"]
                })
            else:
                return self.error_popup(response["error"])
        else:
            return self.error_popup("Email or Password Invalid")

    def success_popup(self, data):
        # msg = QtWidgets.QMessageBox()
        # msg.setWindowTitle("Registration Success")
        self.msg.setText("Login Success!")
        self.msg.setInformativeText("Click ok to Login To Lights and Locks!")
        self.msg.setIcon(QtWidgets.QMessageBox.Information)

        self.msg.buttonClicked.connect(
            lambda info, arg=data: self.popup_button_controller(info, arg))
        x = self.msg.exec_()
        if (x == 1024):
            self.msg.close()

    def error_popup(self, error):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Oh No! Its an Error")
        msg.setText(error)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Retry)

        msg.buttonClicked.connect(self.popup_button_controller)
        y = msg.exec_()

    def popup_button_controller(self, info, data):
        information = info.text()
        if (information == "OK"):
            # If the Login Details are correct
            # Close the Login Form and Open the Main UI menu & pass the data
            # uses system to redirect to MainUI file to open main.py
            LoginForm.close()
            self.msg.close()
            dict1 = urllib.parse.quote(json.dumps(data))
            os.system(f"cd GUI/MainUI && python main.py {dict1}")

    def open_register_form(self, PROPS):
        """ Make sure that the RegisterForm.py setupUI form has PROPS
        in its arguments. 

        Args:
            PROPS (Dict(str)): [key in the User's Textfield inputs in dictionary]
        """
        self.register_widget = QtWidgets.QWidget()
        self.ui = RegisterForm()
        self.ui.setupUi(self.register_widget, PROPS)
        self.register_widget.show()

    def open_admin_login(self):
        from AdminLogin import Ui_AdminLogin as AdminLoginForm
        self.admin_login_widget = QtWidgets.QWidget()
        self.ui = AdminLoginForm()
        self.ui.setupUi(self.admin_login_widget)
        self.admin_login_widget.show()

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.welcome_message.setText(_translate(
            "LoginForm", "Welcome to Light & Locks!"))
        self.username_label.setText(_translate("LoginForm", "User ID"))
        self.password_label.setText(_translate("LoginForm", "Password"))
        self.login_button.setText(_translate("LoginForm", "Login"))
        self.label_2.setText(_translate(
            "LoginForm", "Don\'t Have An Account?"))
        self.register_now_button.setText(
            _translate("LoginForm", "Register Now!"))
        self.admin_prompt.setText(_translate(
            "LoginForm", "Already An Admin?"))
        self.Admin_login_button.setText(
            _translate("LoginForm", "Admin Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())
