import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1914, 1077)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setEnabled(True)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Btn_Toggle.setSizeIncrement(QtCore.QSize(0, 0))
        self.Btn_Toggle.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_Toggle.setStyleSheet("image: url(:/menuBurger/icons8-menu-48.png);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border: 0px solid;\n"
                                      "background-color: rgb(35, 35, 25);\n"
                                      "padding-left: 25px;")
        self.Btn_Toggle.setText("")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.title = QtWidgets.QLabel(self.frame_top)
        self.title.setGeometry(QtCore.QRect(640, 10, 641, 51))
        self.title.setMaximumSize(QtCore.QSize(641, 16777215))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: #C7D2FE;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "padding:1px;")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_1.setFont(font)
        self.btn_page_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_1.setStyleSheet("QPushButton {\n"
                                      "    \n"
                                      "    image: url(:/adminSideBar/icons8-home-48.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    \n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_3.addWidget(self.btn_page_1)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_2.setFont(font)
        self.btn_page_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_2.setStyleSheet("QPushButton {\n"
                                      "    \n"
                                      "    image: url(:/adminSideBar/icons8-products-49.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_3.addWidget(self.btn_page_2)
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_3.setFont(font)
        self.btn_page_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_3.setStyleSheet("QPushButton {\n"
                                      "    \n"
                                      "    \n"
                                      "    image: url(:/adminSideBar/icons8-product-management-48.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_3.addWidget(self.btn_page_3)
        self.btn_page_5 = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_page_5.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_5.setFont(font)
        self.btn_page_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_5.setStyleSheet("QPushButton {\n"
                                      "    \n"
                                      "    \n"
                                      "    image: url(:/adminSideBar/icons8-attract-customers-48.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    \n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_5.setObjectName("btn_page_5")
        self.verticalLayout_3.addWidget(self.btn_page_5)
        self.btn_page_6 = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_page_6.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_6.setFont(font)
        self.btn_page_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_6.setStyleSheet("QPushButton {\n"
                                      "    \n"
                                      "    \n"
                                      "    image: url(:/adminSideBar/icons8-service-48.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    \n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_6.setObjectName("btn_page_6")
        self.verticalLayout_3.addWidget(self.btn_page_6)
        self.btn_page_4 = QtWidgets.QPushButton(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_page_4.sizePolicy().hasHeightForWidth())
        self.btn_page_4.setSizePolicy(sizePolicy)
        self.btn_page_4.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(20)
        self.btn_page_4.setFont(font)
        self.btn_page_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_4.setStyleSheet("QPushButton {\n"
                                      "    image: url(:/SideBar/icons8-exit-48.png);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "    padding-right: 0px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2DD4BF, stop:1 #0EA5E9);\n"
                                      "    border-radius: 20px;\n"
                                      "}")
        self.btn_page_4.setObjectName("btn_page_4")
        self.verticalLayout_3.addWidget(self.btn_page_4)
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_3.addWidget(self.frame_top_menus)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 45, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.welcome_admin_label = QtWidgets.QLabel(self.page_1)
        self.welcome_admin_label.setGeometry(QtCore.QRect(670, 0, 461, 91))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(25)
        self.welcome_admin_label.setFont(font)
        self.welcome_admin_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "image: url(:/adminSideBar/icons8-home-48.png);\n"
                                               "padding-right:50px;")
        self.welcome_admin_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.welcome_admin_label.setObjectName("welcome_admin_label")
        self.admin_table = QtWidgets.QTableWidget(self.page_1)
        self.admin_table.setGeometry(QtCore.QRect(20, 325, 1761, 561))
        self.admin_table.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.admin_table.setFont(font)
        self.admin_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.admin_table.setAutoFillBackground(False)
        self.admin_table.setStyleSheet("QWidget {\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    alternate-background-color: rgb(241, 245, 249);\n"
                                       "    font: 10pt \"8514oem\";\n"
                                       "}\n"
                                       "QScrollBar:vertical {\n"
                                       "    border: none;\n"
                                       "    background: #94A3B8;\n"
                                       "    width: 14px;\n"
                                       "    margin: 15px 0 15px 0;\n"
                                       "    border-radius: 0px;\n"
                                       " }\n"
                                       "\n"
                                       "/*  HANDLE BAR VERTICAL */\n"
                                       "QScrollBar::handle:vertical {    \n"
                                       "    background-color: #E5E7EB;\n"
                                       "    min-height: 30px;\n"
                                       "    border-radius: 7px;\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical:hover{    \n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1 #7C3AED);\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical:pressed {    \n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4338CA, stop:1 #5B21B6);\n"
                                       "}\n"
                                       "\n"
                                       "/* BTN TOP - SCROLLBAR */\n"
                                       "QScrollBar::sub-line:vertical {\n"
                                       "    border: none;\n"
                                       "    background-color: #94A3B8;\n"
                                       "    height: 15px;\n"
                                       "    border-top-left-radius: 7px;\n"
                                       "    border-top-right-radius: 7px;\n"
                                       "    subcontrol-position: top;\n"
                                       "    subcontrol-origin: margin;\n"
                                       "}\n"
                                       "QScrollBar::sub-line:vertical:hover {    \n"
                                       "    background-color: rgb(255, 0, 127);\n"
                                       "}\n"
                                       "QScrollBar::sub-line:vertical:pressed {    \n"
                                       "    background-color: rgb(185, 0, 92);\n"
                                       "}\n"
                                       "\n"
                                       "/* BTN BOTTOM - SCROLLBAR */\n"
                                       "QScrollBar::add-line:vertical {\n"
                                       "    border: none;\n"
                                       "    background-color:#94A3B8;\n"
                                       "    height: 15px;\n"
                                       "    border-bottom-left-radius: 7px;\n"
                                       "    border-bottom-right-radius: 7px;\n"
                                       "    subcontrol-position: bottom;\n"
                                       "    subcontrol-origin: margin;\n"
                                       "}\n"
                                       "QScrollBar::add-line:vertical:hover {    \n"
                                       "    background-color: rgb(255, 0, 127);\n"
                                       "}\n"
                                       "QScrollBar::add-line:vertical:pressed {    \n"
                                       "    background-color: rgb(185, 0, 92);\n"
                                       "}\n"
                                       "\n"
                                       "/* RESET ARROW */\n"
                                       "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                       "    background: none;\n"
                                       "}\n"
                                       "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                       "    background: none;\n"
                                       "}\n"
                                       "")
        self.admin_table.setFrameShape(QtWidgets.QFrame.Box)
        self.admin_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.admin_table.setLineWidth(10)
        self.admin_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.admin_table.setAlternatingRowColors(True)
        self.admin_table.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.admin_table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.admin_table.setIconSize(QtCore.QSize(0, 0))
        self.admin_table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.admin_table.setRowCount(7)
        self.admin_table.setColumnCount(3)
        self.admin_table.setObjectName("admin_table")
        item = QtWidgets.QTableWidgetItem()
        self.admin_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_table.setHorizontalHeaderItem(2, item)
        self.admin_table.horizontalHeader().setCascadingSectionResizes(False)
        self.admin_table.horizontalHeader().setDefaultSectionSize(550)
        self.admin_table.horizontalHeader().setMinimumSectionSize(26)
        self.admin_table.horizontalHeader().setStretchLastSection(True)
        self.admin_table.verticalHeader().setDefaultSectionSize(87)
        self.admin_table.verticalHeader().setSortIndicatorShown(True)
        self.admin_table.verticalHeader().setStretchLastSection(False)
        self.refresh_button_admin = QtWidgets.QPushButton(self.page_1)
        self.refresh_button_admin.setGeometry(QtCore.QRect(1390, 250, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.refresh_button_admin.setFont(font)
        self.refresh_button_admin.setToolTipDuration(0)
        self.refresh_button_admin.setStyleSheet("QPushButton {\n"
                                                "    border-top-right-radius: 10px;\n"
                                                "    border-top-left-radius: 10px;\n"
                                                "    border-bottom-right-radius: 10px;\n"
                                                "    border-bottom-left-radius: 10px;\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 212, 191, 1), stop:1 rgba(6, 182, 212, 1));\n"
                                                "    font: 22px;\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                                ", stop:1 #0E7490);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                                ", stop:1 #0E7490);\n"
                                                "    padding-left: 5px;\n"
                                                "    padding-top: 5px;\n"
                                                "}")
        self.refresh_button_admin.setObjectName("refresh_button_admin")
        self.view_customers_button = QtWidgets.QPushButton(self.page_1)
        self.view_customers_button.setGeometry(QtCore.QRect(20, 250, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.view_customers_button.setFont(font)
        self.view_customers_button.setToolTipDuration(0)
        self.view_customers_button.setStyleSheet("QPushButton {\n"
                                                 "    border-radius: 10px;\n"
                                                 "    font: 22px;\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    border: 5px solid;\n"
                                                 "    border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1#7C3AED);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    border: 5px solid;\n"
                                                 "    border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3730A3, stop:1 #5B21B6);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "    border: 5px solid;\n"
                                                 "    border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3730A3\n"
                                                 ", stop:1 #5B21B6);\n"
                                                 "    padding-left: 5px;\n"
                                                 "    padding-top: 5px;\n"
                                                 "}")
        self.view_customers_button.setObjectName("view_customers_button")
        self.view_items_category_model_button = QtWidgets.QPushButton(
            self.page_1)
        self.view_items_category_model_button.setGeometry(
            QtCore.QRect(20, 170, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.view_items_category_model_button.setFont(font)
        self.view_items_category_model_button.setToolTipDuration(0)
        self.view_items_category_model_button.setStyleSheet("QPushButton {\n"
                                                            "    border-radius: 10px;\n"
                                                            "    font: 22px;\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    border: 5px solid;\n"
                                                            "    border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1#7C3AED);\n"
                                                            "}\n"
                                                            "\n"
                                                            "QPushButton:hover {\n"
                                                            "    border: 5px solid;\n"
                                                            "    border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3730A3, stop:1 #5B21B6);\n"
                                                            "}\n"
                                                            "\n"
                                                            "QPushButton:pressed {\n"
                                                            "    border: 5px solid;\n"
                                                            "    border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3730A3\n"
                                                            ", stop:1 #5B21B6);\n"
                                                            "    padding-left: 5px;\n"
                                                            "    padding-top: 5px;\n"
                                                            "}")
        self.view_items_category_model_button.setObjectName(
            "view_items_category_model_button")
        self.initialise_database_button = QtWidgets.QPushButton(self.page_1)
        self.initialise_database_button.setGeometry(
            QtCore.QRect(1390, 180, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.initialise_database_button.setFont(font)
        self.initialise_database_button.setToolTipDuration(0)
        self.initialise_database_button.setStyleSheet("QPushButton {\n"
                                                      "    border-top-right-radius: 10px;\n"
                                                      "    border-top-left-radius: 10px;\n"
                                                      "    border-bottom-right-radius: 10px;\n"
                                                      "    border-bottom-left-radius: 10px;\n"
                                                      "    background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1#7C3AED);\n"
                                                      "    font: 22px;\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "}\n"
                                                      "\n"
                                                      "QPushButton:hover {\n"
                                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3730A3\n"
                                                      ", stop:1 #5B21B6);\n"
                                                      "}\n"
                                                      "\n"
                                                      "QPushButton:pressed {\n"
                                                      "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3730A3\n"
                                                      ", stop:1 #5B21B6);\n"
                                                      "    padding-left: 5px;\n"
                                                      "    padding-top: 5px;\n"
                                                      "}")
        self.initialise_database_button.setObjectName(
            "initialise_database_button")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.submit_query = QtWidgets.QPushButton(self.page_2)
        self.submit_query.setGeometry(QtCore.QRect(1470, 250, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.submit_query.setFont(font)
        self.submit_query.setToolTipDuration(0)
        self.submit_query.setStyleSheet("QPushButton {\n"
                                        "    border-top-right-radius: 10px;\n"
                                        "    border-top-left-radius: 10px;\n"
                                        "    border-bottom-right-radius: 10px;\n"
                                        "    border-bottom-left-radius: 10px;\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #F59E0B, stop:1#E11D48);\n"
                                        "    font: 22px;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #B45309\n"
                                        ", stop:1 #9F1239);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #B45309\n"
                                        ", stop:1 #9F1239);\n"
                                        "    padding-left: 5px;\n"
                                        "    padding-top: 5px;\n"
                                        "}")
        self.submit_query.setObjectName("submit_query")
        self.Categories_label = QtWidgets.QLineEdit(self.page_2)
        self.Categories_label.setGeometry(QtCore.QRect(20, 10, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Categories_label.setFont(font)
        self.Categories_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color: rgba(255, 255, 255, 0);")
        self.Categories_label.setFrame(False)
        self.Categories_label.setObjectName("Categories_label")
        self.category_comboBox = QtWidgets.QComboBox(self.page_2)
        self.category_comboBox.setGeometry(QtCore.QRect(20, 37, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.category_comboBox.sizePolicy().hasHeightForWidth())
        self.category_comboBox.setSizePolicy(sizePolicy)
        self.category_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.category_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.category_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.category_comboBox.setFont(font)
        self.category_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.category_comboBox.setStyleSheet("QComboBox {\n"
                                             "    border: 1px solid gray;\n"
                                             "    border-radius: 10px;\n"
                                             "    padding: 1px 18px 1px 3px;\n"
                                             "    min-width: 6em;\n"
                                             "    font: 16pt \"8514oem\";\n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             "    \n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox:on { /* shift the text when the popup opens */\n"
                                             "    padding-top: 3px;\n"
                                             "    padding-left: 4px;\n"
                                             "    background: white;\n"
                                             "    border-radius: 10px;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::drop-down {\n"
                                             "    subcontrol-origin: padding;\n"
                                             "    subcontrol-position: top right;\n"
                                             "    width: 15px;\n"
                                             "    background-color:white;\n"
                                             "    border-left-width: 1px;\n"
                                             "    border-left-color: darkgray;\n"
                                             "    border-left-style: solid; /* just a single line */\n"
                                             "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                             "    border-bottom-right-radius: 3px;\n"
                                             "    border-radius: 10px;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                             "    top: 1px;\n"
                                             "    left: 1px;\n"
                                             "}\n"
                                             "QListView\n"
                                             "{\n"
                                             "background-color : #334155;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "}")
        self.category_comboBox.setEditable(False)
        self.category_comboBox.setFrame(True)
        self.category_comboBox.setObjectName("category_comboBox")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.gradient_backdrop = QtWidgets.QLabel(self.page_2)
        self.gradient_backdrop.setGeometry(QtCore.QRect(10, 0, 1781, 311))
        self.gradient_backdrop.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0D9488, stop:1 #0E7490);\n"
                                             "border-radius: 20px;")
        self.gradient_backdrop.setText("")
        self.gradient_backdrop.setObjectName("gradient_backdrop")
        self.Model_label = QtWidgets.QLineEdit(self.page_2)
        self.Model_label.setGeometry(QtCore.QRect(20, 110, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Model_label.setFont(font)
        self.Model_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgba(255, 255, 255, 0);")
        self.Model_label.setFrame(False)
        self.Model_label.setObjectName("Model_label")
        self.Price_label = QtWidgets.QLineEdit(self.page_2)
        self.Price_label.setGeometry(QtCore.QRect(20, 210, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Price_label.setFont(font)
        self.Price_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgba(255, 255, 255, 0);")
        self.Price_label.setFrame(False)
        self.Price_label.setObjectName("Price_label")
        self.model_comboBox = QtWidgets.QComboBox(self.page_2)
        self.model_comboBox.setGeometry(QtCore.QRect(20, 140, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.model_comboBox.sizePolicy().hasHeightForWidth())
        self.model_comboBox.setSizePolicy(sizePolicy)
        self.model_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.model_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.model_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.model_comboBox.setFont(font)
        self.model_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.model_comboBox.setStyleSheet("QComboBox {\n"
                                          "    border: 1px solid gray;\n"
                                          "    border-radius: 10px;\n"
                                          "    padding: 1px 18px 1px 3px;\n"
                                          "    min-width: 6em;\n"
                                          "    font: 16pt \"8514oem\";\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "    \n"
                                          "    color: rgb(0, 0, 0);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:on { /* shift the text when the popup opens */\n"
                                          "    padding-top: 3px;\n"
                                          "    padding-left: 4px;\n"
                                          "    background: white;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::drop-down {\n"
                                          "    subcontrol-origin: padding;\n"
                                          "    subcontrol-position: top right;\n"
                                          "    width: 15px;\n"
                                          "    background-color:white;\n"
                                          "    border-left-width: 1px;\n"
                                          "    border-left-color: darkgray;\n"
                                          "    border-left-style: solid; /* just a single line */\n"
                                          "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                          "    border-bottom-right-radius: 3px;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                          "    top: 1px;\n"
                                          "    left: 1px;\n"
                                          "}\n"
                                          "QListView\n"
                                          "{\n"
                                          "background-color : #334155;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "}")
        self.model_comboBox.setEditable(False)
        self.model_comboBox.setFrame(True)
        self.model_comboBox.setObjectName("model_comboBox")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.model_comboBox.addItem("")
        self.price_comboBox = QtWidgets.QComboBox(self.page_2)
        self.price_comboBox.setGeometry(QtCore.QRect(20, 240, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.price_comboBox.sizePolicy().hasHeightForWidth())
        self.price_comboBox.setSizePolicy(sizePolicy)
        self.price_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.price_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.price_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_comboBox.setFont(font)
        self.price_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.price_comboBox.setStyleSheet("QComboBox {\n"
                                          "    border: 1px solid gray;\n"
                                          "    border-radius: 10px;\n"
                                          "    padding: 1px 18px 1px 3px;\n"
                                          "    min-width: 6em;\n"
                                          "    font: 16pt \"8514oem\";\n"
                                          "    background-color: rgb(255, 255, 255);\n"
                                          "    \n"
                                          "    color: rgb(0, 0, 0);\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:on { /* shift the text when the popup opens */\n"
                                          "    padding-top: 3px;\n"
                                          "    padding-left: 4px;\n"
                                          "    background: white;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::drop-down {\n"
                                          "    subcontrol-origin: padding;\n"
                                          "    subcontrol-position: top right;\n"
                                          "    width: 15px;\n"
                                          "    background-color:white;\n"
                                          "    border-left-width: 1px;\n"
                                          "    border-left-color: darkgray;\n"
                                          "    border-left-style: solid; /* just a single line */\n"
                                          "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                          "    border-bottom-right-radius: 3px;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                          "    top: 1px;\n"
                                          "    left: 1px;\n"
                                          "}\n"
                                          "QListView\n"
                                          "{\n"
                                          "background-color : #334155;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "}")
        self.price_comboBox.setEditable(False)
        self.price_comboBox.setFrame(True)
        self.price_comboBox.setObjectName("price_comboBox")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.price_comboBox.addItem("")
        self.factory_comboBox = QtWidgets.QComboBox(self.page_2)
        self.factory_comboBox.setGeometry(QtCore.QRect(630, 140, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.factory_comboBox.sizePolicy().hasHeightForWidth())
        self.factory_comboBox.setSizePolicy(sizePolicy)
        self.factory_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.factory_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.factory_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.factory_comboBox.setFont(font)
        self.factory_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.factory_comboBox.setStyleSheet("QComboBox {\n"
                                            "    border: 1px solid gray;\n"
                                            "    border-radius: 10px;\n"
                                            "    padding: 1px 18px 1px 3px;\n"
                                            "    min-width: 6em;\n"
                                            "    font: 16pt \"8514oem\";\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            "    \n"
                                            "    color: rgb(0, 0, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox:on { /* shift the text when the popup opens */\n"
                                            "    padding-top: 3px;\n"
                                            "    padding-left: 4px;\n"
                                            "    background: white;\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox::drop-down {\n"
                                            "    subcontrol-origin: padding;\n"
                                            "    subcontrol-position: top right;\n"
                                            "    width: 15px;\n"
                                            "    background-color:white;\n"
                                            "    border-left-width: 1px;\n"
                                            "    border-left-color: darkgray;\n"
                                            "    border-left-style: solid; /* just a single line */\n"
                                            "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                            "    border-bottom-right-radius: 3px;\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                            "    top: 1px;\n"
                                            "    left: 1px;\n"
                                            "}\n"
                                            "QListView\n"
                                            "{\n"
                                            "background-color : #334155;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "}")
        self.factory_comboBox.setEditable(False)
        self.factory_comboBox.setFrame(True)
        self.factory_comboBox.setObjectName("factory_comboBox")
        self.factory_comboBox.addItem("")
        self.factory_comboBox.addItem("")
        self.factory_comboBox.addItem("")
        self.factory_comboBox.addItem("")
        self.Factory_label = QtWidgets.QLineEdit(self.page_2)
        self.Factory_label.setGeometry(QtCore.QRect(630, 110, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Factory_label.setFont(font)
        self.Factory_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(255, 255, 255, 0);")
        self.Factory_label.setFrame(False)
        self.Factory_label.setObjectName("Factory_label")
        self.production_year_label = QtWidgets.QLineEdit(self.page_2)
        self.production_year_label.setGeometry(QtCore.QRect(630, 210, 191, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.production_year_label.setFont(font)
        self.production_year_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "background-color: rgba(255, 255, 255, 0);")
        self.production_year_label.setFrame(False)
        self.production_year_label.setObjectName("production_year_label")
        self.colour_comboBox = QtWidgets.QComboBox(self.page_2)
        self.colour_comboBox.setGeometry(QtCore.QRect(630, 37, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.colour_comboBox.sizePolicy().hasHeightForWidth())
        self.colour_comboBox.setSizePolicy(sizePolicy)
        self.colour_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.colour_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.colour_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.colour_comboBox.setFont(font)
        self.colour_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.colour_comboBox.setStyleSheet("QComboBox {\n"
                                           "    border: 1px solid gray;\n"
                                           "    border-radius: 10px;\n"
                                           "    padding: 1px 18px 1px 3px;\n"
                                           "    min-width: 6em;\n"
                                           "    font: 16pt \"8514oem\";\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    \n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox:on { /* shift the text when the popup opens */\n"
                                           "    padding-top: 3px;\n"
                                           "    padding-left: 4px;\n"
                                           "    background: white;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox::drop-down {\n"
                                           "    subcontrol-origin: padding;\n"
                                           "    subcontrol-position: top right;\n"
                                           "    width: 15px;\n"
                                           "    background-color:white;\n"
                                           "    border-left-width: 1px;\n"
                                           "    border-left-color: darkgray;\n"
                                           "    border-left-style: solid; /* just a single line */\n"
                                           "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                           "    border-bottom-right-radius: 3px;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "\n"
                                           "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                           "    top: 1px;\n"
                                           "    left: 1px;\n"
                                           "}\n"
                                           "QListView\n"
                                           "{\n"
                                           "background-color : #334155;\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "}")
        self.colour_comboBox.setEditable(False)
        self.colour_comboBox.setFrame(True)
        self.colour_comboBox.setObjectName("colour_comboBox")
        self.colour_comboBox.addItem("")
        self.colour_comboBox.addItem("")
        self.colour_comboBox.addItem("")
        self.colour_comboBox.addItem("")
        self.colour_comboBox.addItem("")
        self.colour_comboBox.addItem("")
        self.Colour_label = QtWidgets.QLineEdit(self.page_2)
        self.Colour_label.setGeometry(QtCore.QRect(630, 10, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Colour_label.setFont(font)
        self.Colour_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(255, 255, 255, 0);")
        self.Colour_label.setFrame(False)
        self.Colour_label.setObjectName("Colour_label")
        self.production_year_comboBox = QtWidgets.QComboBox(self.page_2)
        self.production_year_comboBox.setGeometry(
            QtCore.QRect(630, 240, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.production_year_comboBox.sizePolicy().hasHeightForWidth())
        self.production_year_comboBox.setSizePolicy(sizePolicy)
        self.production_year_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.production_year_comboBox.setMaximumSize(
            QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.production_year_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.production_year_comboBox.setFont(font)
        self.production_year_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.production_year_comboBox.setStyleSheet("QComboBox {\n"
                                                    "    border: 1px solid gray;\n"
                                                    "    border-radius: 10px;\n"
                                                    "    padding: 1px 18px 1px 3px;\n"
                                                    "    min-width: 6em;\n"
                                                    "    font: 16pt \"8514oem\";\n"
                                                    "    background-color: rgb(255, 255, 255);\n"
                                                    "    \n"
                                                    "    color: rgb(0, 0, 0);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QComboBox:on { /* shift the text when the popup opens */\n"
                                                    "    padding-top: 3px;\n"
                                                    "    padding-left: 4px;\n"
                                                    "    background: white;\n"
                                                    "    border-radius: 10px;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QComboBox::drop-down {\n"
                                                    "    subcontrol-origin: padding;\n"
                                                    "    subcontrol-position: top right;\n"
                                                    "    width: 15px;\n"
                                                    "    background-color:white;\n"
                                                    "    border-left-width: 1px;\n"
                                                    "    border-left-color: darkgray;\n"
                                                    "    border-left-style: solid; /* just a single line */\n"
                                                    "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                                    "    border-bottom-right-radius: 3px;\n"
                                                    "    border-radius: 10px;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                                    "    top: 1px;\n"
                                                    "    left: 1px;\n"
                                                    "}\n"
                                                    "QListView\n"
                                                    "{\n"
                                                    "background-color : #334155;\n"
                                                    "color: rgb(255, 255, 255);\n"
                                                    "}")
        self.production_year_comboBox.setEditable(False)
        self.production_year_comboBox.setFrame(True)
        self.production_year_comboBox.setObjectName("production_year_comboBox")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.production_year_comboBox.addItem("")
        self.Power_supply_label = QtWidgets.QLineEdit(self.page_2)
        self.Power_supply_label.setGeometry(QtCore.QRect(1250, 10, 151, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Power_supply_label.setFont(font)
        self.Power_supply_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgba(255, 255, 255, 0);")
        self.Power_supply_label.setFrame(False)
        self.Power_supply_label.setObjectName("Power_supply_label")
        self.power_supply_comboBox = QtWidgets.QComboBox(self.page_2)
        self.power_supply_comboBox.setGeometry(QtCore.QRect(1250, 37, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.power_supply_comboBox.sizePolicy().hasHeightForWidth())
        self.power_supply_comboBox.setSizePolicy(sizePolicy)
        self.power_supply_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.power_supply_comboBox.setMaximumSize(
            QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.power_supply_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.power_supply_comboBox.setFont(font)
        self.power_supply_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.power_supply_comboBox.setStyleSheet("QComboBox {\n"
                                                 "    border: 1px solid gray;\n"
                                                 "    border-radius: 10px;\n"
                                                 "    padding: 1px 18px 1px 3px;\n"
                                                 "    min-width: 6em;\n"
                                                 "    font: 16pt \"8514oem\";\n"
                                                 "    background-color: rgb(255, 255, 255);\n"
                                                 "    \n"
                                                 "    color: rgb(0, 0, 0);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox:on { /* shift the text when the popup opens */\n"
                                                 "    padding-top: 3px;\n"
                                                 "    padding-left: 4px;\n"
                                                 "    background: white;\n"
                                                 "    border-radius: 10px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox::drop-down {\n"
                                                 "    subcontrol-origin: padding;\n"
                                                 "    subcontrol-position: top right;\n"
                                                 "    width: 15px;\n"
                                                 "    background-color:white;\n"
                                                 "    border-left-width: 1px;\n"
                                                 "    border-left-color: darkgray;\n"
                                                 "    border-left-style: solid; /* just a single line */\n"
                                                 "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                                 "    border-bottom-right-radius: 3px;\n"
                                                 "    border-radius: 10px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                                 "    top: 1px;\n"
                                                 "    left: 1px;\n"
                                                 "}\n"
                                                 "QListView\n"
                                                 "{\n"
                                                 "background-color : #334155;\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "}")
        self.power_supply_comboBox.setEditable(False)
        self.power_supply_comboBox.setFrame(True)
        self.power_supply_comboBox.setObjectName("power_supply_comboBox")
        self.power_supply_comboBox.addItem("")
        self.power_supply_comboBox.addItem("")
        self.power_supply_comboBox.addItem("")
        self.Warranty_label = QtWidgets.QLineEdit(self.page_2)
        self.Warranty_label.setGeometry(QtCore.QRect(1250, 113, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.Warranty_label.setFont(font)
        self.Warranty_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color: rgba(255, 255, 255, 0);")
        self.Warranty_label.setFrame(False)
        self.Warranty_label.setObjectName("Warranty_label")
        self.warranty_comboBox = QtWidgets.QComboBox(self.page_2)
        self.warranty_comboBox.setGeometry(QtCore.QRect(1250, 140, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.warranty_comboBox.sizePolicy().hasHeightForWidth())
        self.warranty_comboBox.setSizePolicy(sizePolicy)
        self.warranty_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.warranty_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.warranty_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.warranty_comboBox.setFont(font)
        self.warranty_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.warranty_comboBox.setStyleSheet("QComboBox {\n"
                                             "    border: 1px solid gray;\n"
                                             "    border-radius: 10px;\n"
                                             "    padding: 1px 18px 1px 3px;\n"
                                             "    min-width: 6em;\n"
                                             "    font: 16pt \"8514oem\";\n"
                                             "    background-color: rgb(255, 255, 255);\n"
                                             "    \n"
                                             "    color: rgb(0, 0, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox:on { /* shift the text when the popup opens */\n"
                                             "    padding-top: 3px;\n"
                                             "    padding-left: 4px;\n"
                                             "    background: white;\n"
                                             "    border-radius: 10px;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::drop-down {\n"
                                             "    subcontrol-origin: padding;\n"
                                             "    subcontrol-position: top right;\n"
                                             "    width: 15px;\n"
                                             "    background-color:white;\n"
                                             "    border-left-width: 1px;\n"
                                             "    border-left-color: darkgray;\n"
                                             "    border-left-style: solid; /* just a single line */\n"
                                             "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                             "    border-bottom-right-radius: 3px;\n"
                                             "    border-radius: 10px;\n"
                                             "}\n"
                                             "\n"
                                             "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                             "    top: 1px;\n"
                                             "    left: 1px;\n"
                                             "}\n"
                                             "QListView\n"
                                             "{\n"
                                             "background-color : #334155;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "}")
        self.warranty_comboBox.setEditable(False)
        self.warranty_comboBox.setFrame(True)
        self.warranty_comboBox.setObjectName("warranty_comboBox")
        self.warranty_comboBox.addItem("")
        self.warranty_comboBox.addItem("")
        self.warranty_comboBox.addItem("")
        self.warranty_comboBox.addItem("")
        self.warranty_comboBox.addItem("")
        self.category_div = QtWidgets.QLabel(self.page_2)
        self.category_div.setGeometry(QtCore.QRect(10, 340, 421, 541))
        self.category_div.setStyleSheet("QWidget { \n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);\n"
                                        "/**image: url(:/Choose_Item_div/light-bulb.png);*/\n"
                                        "/**image: url(:/Choose_Item_div/padlock.png);*/\n"
                                        "image: url(:/Choose_Item_div/box.png);\n"
                                        "border-radius: 20px;\n"
                                        "}")
        self.category_div.setText("")
        self.category_div.setObjectName("category_div")
        self.price_div = QtWidgets.QLabel(self.page_2)
        self.price_div.setGeometry(QtCore.QRect(460, 340, 971, 50))
        self.price_div.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);\n"
                                     "border-radius: 20px;")
        self.price_div.setText("")
        self.price_div.setObjectName("price_div")
        self.warranty_div = QtWidgets.QLabel(self.page_2)
        self.warranty_div.setGeometry(QtCore.QRect(460, 420, 971, 50))
        self.warranty_div.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);\n"
                                        "border-radius: 20px;")
        self.warranty_div.setText("")
        self.warranty_div.setObjectName("warranty_div")
        self.model_div = QtWidgets.QLabel(self.page_2)
        self.model_div.setGeometry(QtCore.QRect(460, 500, 971, 50))
        self.model_div.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);\n"
                                     "border-radius: 20px;")
        self.model_div.setText("")
        self.model_div.setObjectName("model_div")
        self.cost_div = QtWidgets.QLabel(self.page_2)
        self.cost_div.setGeometry(QtCore.QRect(460, 580, 971, 50))
        self.cost_div.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);\n"
                                    "border-radius: 20px;")
        self.cost_div.setText("")
        self.cost_div.setObjectName("cost_div")
        self.inventory_div = QtWidgets.QLabel(self.page_2)
        self.inventory_div.setGeometry(QtCore.QRect(1460, 340, 301, 241))
        self.inventory_div.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #F59E0B, stop:1#E11D48);\n"
                                         "border-radius: 20px;")
        self.inventory_div.setText("")
        self.inventory_div.setObjectName("inventory_div")
        self.sold_items_div = QtWidgets.QLabel(self.page_2)
        self.sold_items_div.setGeometry(QtCore.QRect(1460, 630, 301, 241))
        self.sold_items_div.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #F59E0B, stop:1#E11D48);\n"
                                          "border-radius: 20px;")
        self.sold_items_div.setText("")
        self.sold_items_div.setObjectName("sold_items_div")
        self.category_amount_label = QtWidgets.QLabel(self.page_2)
        self.category_amount_label.setGeometry(QtCore.QRect(20, 770, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.category_amount_label.setFont(font)
        self.category_amount_label.setStyleSheet("background-color: transparent;\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "font: 75 italic 18pt \"Segoe UI\";")
        self.category_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.category_amount_label.setObjectName("category_amount_label")
        self.choose_an_item_label = QtWidgets.QLabel(self.page_2)
        self.choose_an_item_label.setGeometry(QtCore.QRect(20, 360, 411, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.choose_an_item_label.setFont(font)
        self.choose_an_item_label.setStyleSheet("background-color: transparent;\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "font: 20pt \"Yu Gothic UI\";")
        self.choose_an_item_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_an_item_label.setObjectName("choose_an_item_label")
        self.inventory_level_label = QtWidgets.QLabel(self.page_2)
        self.inventory_level_label.setGeometry(
            QtCore.QRect(1460, 350, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.inventory_level_label.setFont(font)
        self.inventory_level_label.setStyleSheet("background-color: transparent;\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "font: 14pt \"Yu Gothic UI\";")
        self.inventory_level_label.setAlignment(QtCore.Qt.AlignCenter)
        self.inventory_level_label.setObjectName("inventory_level_label")
        self.sold_items_label = QtWidgets.QLabel(self.page_2)
        self.sold_items_label.setGeometry(QtCore.QRect(1460, 630, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sold_items_label.setFont(font)
        self.sold_items_label.setStyleSheet("background-color: transparent;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font: 14pt \"Yu Gothic UI\";")
        self.sold_items_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sold_items_label.setObjectName("sold_items_label")
        self.price_label = QtWidgets.QLabel(self.page_2)
        self.price_label.setGeometry(QtCore.QRect(400, 350, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.price_label.setFont(font)
        self.price_label.setStyleSheet("background-color: transparent;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 12pt \"Yu Gothic UI\";")
        self.price_label.setAlignment(QtCore.Qt.AlignCenter)
        self.price_label.setObjectName("price_label")
        self.warranty_label = QtWidgets.QLabel(self.page_2)
        self.warranty_label.setGeometry(QtCore.QRect(420, 420, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.warranty_label.setFont(font)
        self.warranty_label.setStyleSheet("background-color: transparent;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 12pt \"Yu Gothic UI\";")
        self.warranty_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warranty_label.setObjectName("warranty_label")
        self.model_label = QtWidgets.QLabel(self.page_2)
        self.model_label.setGeometry(QtCore.QRect(410, 500, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.model_label.setFont(font)
        self.model_label.setStyleSheet("background-color: transparent;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 12pt \"Yu Gothic UI\";")
        self.model_label.setAlignment(QtCore.Qt.AlignCenter)
        self.model_label.setObjectName("model_label")
        self.cost_label = QtWidgets.QLabel(self.page_2)
        self.cost_label.setGeometry(QtCore.QRect(400, 580, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cost_label.setFont(font)
        self.cost_label.setStyleSheet("background-color: transparent;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 12pt \"Yu Gothic UI\";")
        self.cost_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_label.setObjectName("cost_label")
        self.price_amount_label = QtWidgets.QLabel(self.page_2)
        self.price_amount_label.setGeometry(QtCore.QRect(1180, 340, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.price_amount_label.setFont(font)
        self.price_amount_label.setStyleSheet("background-color: transparent;\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "font: italic 12pt \"Yu Gothic UI\";")
        self.price_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.price_amount_label.setObjectName("price_amount_label")
        self.warranty_amount_label = QtWidgets.QLabel(self.page_2)
        self.warranty_amount_label.setGeometry(
            QtCore.QRect(1180, 420, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.warranty_amount_label.setFont(font)
        self.warranty_amount_label.setStyleSheet("background-color: transparent;\n"
                                                 "color: rgb(255, 255, 255);\n"
                                                 "font: italic 12pt \"Yu Gothic UI\";")
        self.warranty_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warranty_amount_label.setObjectName("warranty_amount_label")
        self.model_amount_label = QtWidgets.QLabel(self.page_2)
        self.model_amount_label.setGeometry(QtCore.QRect(1180, 500, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.model_amount_label.setFont(font)
        self.model_amount_label.setStyleSheet("background-color: transparent;\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "font: italic 12pt \"Yu Gothic UI\";")
        self.model_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.model_amount_label.setObjectName("model_amount_label")
        self.cost_amount_label = QtWidgets.QLabel(self.page_2)
        self.cost_amount_label.setGeometry(QtCore.QRect(1180, 580, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.cost_amount_label.setFont(font)
        self.cost_amount_label.setStyleSheet("background-color: transparent;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "font: italic 12pt \"Yu Gothic UI\";")
        self.cost_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_amount_label.setObjectName("cost_amount_label")
        self.inventory_amount_label = QtWidgets.QLabel(self.page_2)
        self.inventory_amount_label.setGeometry(
            QtCore.QRect(1460, 490, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.inventory_amount_label.setFont(font)
        self.inventory_amount_label.setStyleSheet("background-color: transparent;\n"
                                                  "color: rgb(255, 255, 255);\n"
                                                  "font: italic 16pt \"Yu Gothic UI\";")
        self.inventory_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.inventory_amount_label.setObjectName("inventory_amount_label")
        self.sold_items_amount_label = QtWidgets.QLabel(self.page_2)
        self.sold_items_amount_label.setGeometry(
            QtCore.QRect(1460, 780, 301, 91))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.sold_items_amount_label.setFont(font)
        self.sold_items_amount_label.setStyleSheet("background-color: transparent;\n"
                                                   "color: rgb(255, 255, 255);\n"
                                                   "font: italic 16pt \"Yu Gothic UI\";")
        self.sold_items_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sold_items_amount_label.setObjectName("sold_items_amount_label")
        self.color_div = QtWidgets.QLabel(self.page_2)
        self.color_div.setGeometry(QtCore.QRect(460, 660, 971, 50))
        self.color_div.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);\n"
                                     "border-radius: 20px;")
        self.color_div.setText("")
        self.color_div.setObjectName("color_div")
        self.production_year_div = QtWidgets.QLabel(self.page_2)
        self.production_year_div.setGeometry(QtCore.QRect(460, 740, 971, 50))
        self.production_year_div.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);\n"
                                               "border-radius: 20px;")
        self.production_year_div.setText("")
        self.production_year_div.setObjectName("production_year_div")
        self.power_supply_div = QtWidgets.QLabel(self.page_2)
        self.power_supply_div.setGeometry(QtCore.QRect(460, 820, 971, 50))
        self.power_supply_div.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0  #6D28D9 , stop:1 #4F46E5);\n"
                                            "border-radius: 20px;")
        self.power_supply_div.setText("")
        self.power_supply_div.setObjectName("power_supply_div")
        self.color_label = QtWidgets.QLabel(self.page_2)
        self.color_label.setGeometry(QtCore.QRect(400, 660, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.color_label.setFont(font)
        self.color_label.setStyleSheet("background-color: transparent;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 12pt \"Yu Gothic UI\";")
        self.color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_label.setObjectName("color_label")
        self.product_year_label = QtWidgets.QLabel(self.page_2)
        self.product_year_label.setGeometry(QtCore.QRect(460, 740, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.product_year_label.setFont(font)
        self.product_year_label.setStyleSheet("background-color: transparent;\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "font: 12pt \"Yu Gothic UI\";")
        self.product_year_label.setAlignment(QtCore.Qt.AlignCenter)
        self.product_year_label.setObjectName("product_year_label")
        self.power_supply_label = QtWidgets.QLabel(self.page_2)
        self.power_supply_label.setGeometry(QtCore.QRect(450, 820, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.power_supply_label.setFont(font)
        self.power_supply_label.setStyleSheet("background-color: transparent;\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "font: 12pt \"Yu Gothic UI\";")
        self.power_supply_label.setAlignment(QtCore.Qt.AlignCenter)
        self.power_supply_label.setObjectName("power_supply_label")
        self.color_amount_label = QtWidgets.QLabel(self.page_2)
        self.color_amount_label.setGeometry(QtCore.QRect(1180, 660, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.color_amount_label.setFont(font)
        self.color_amount_label.setStyleSheet("background-color: transparent;\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "font: italic 12pt \"Yu Gothic UI\";")
        self.color_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.color_amount_label.setObjectName("color_amount_label")
        self.producti_year_amount_label = QtWidgets.QLabel(self.page_2)
        self.producti_year_amount_label.setGeometry(
            QtCore.QRect(1180, 740, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.producti_year_amount_label.setFont(font)
        self.producti_year_amount_label.setStyleSheet("background-color: transparent;\n"
                                                      "color: rgb(255, 255, 255);\n"
                                                      "font: italic 12pt \"Yu Gothic UI\";")
        self.producti_year_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.producti_year_amount_label.setObjectName(
            "producti_year_amount_label")
        self.power_supply_amount_label = QtWidgets.QLabel(self.page_2)
        self.power_supply_amount_label.setGeometry(
            QtCore.QRect(1180, 820, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.power_supply_amount_label.setFont(font)
        self.power_supply_amount_label.setStyleSheet("background-color: transparent;\n"
                                                     "color: rgb(255, 255, 255);\n"
                                                     "font: italic 12pt \"Yu Gothic UI\";")
        self.power_supply_amount_label.setAlignment(QtCore.Qt.AlignCenter)
        self.power_supply_amount_label.setObjectName(
            "power_supply_amount_label")
        self.gradient_backdrop.raise_()
        self.submit_query.raise_()
        self.Categories_label.raise_()
        self.category_comboBox.raise_()
        self.Model_label.raise_()
        self.Price_label.raise_()
        self.model_comboBox.raise_()
        self.price_comboBox.raise_()
        self.factory_comboBox.raise_()
        self.Factory_label.raise_()
        self.production_year_label.raise_()
        self.colour_comboBox.raise_()
        self.Colour_label.raise_()
        self.production_year_comboBox.raise_()
        self.Power_supply_label.raise_()
        self.power_supply_comboBox.raise_()
        self.Warranty_label.raise_()
        self.warranty_comboBox.raise_()
        self.category_div.raise_()
        self.price_div.raise_()
        self.warranty_div.raise_()
        self.model_div.raise_()
        self.cost_div.raise_()
        self.inventory_div.raise_()
        self.sold_items_div.raise_()
        self.category_amount_label.raise_()
        self.choose_an_item_label.raise_()
        self.inventory_level_label.raise_()
        self.sold_items_label.raise_()
        self.price_label.raise_()
        self.warranty_label.raise_()
        self.model_label.raise_()
        self.cost_label.raise_()
        self.price_amount_label.raise_()
        self.warranty_amount_label.raise_()
        self.model_amount_label.raise_()
        self.cost_amount_label.raise_()
        self.inventory_amount_label.raise_()
        self.sold_items_amount_label.raise_()
        self.color_div.raise_()
        self.production_year_div.raise_()
        self.power_supply_div.raise_()
        self.color_label.raise_()
        self.product_year_label.raise_()
        self.power_supply_label.raise_()
        self.color_amount_label.raise_()
        self.producti_year_amount_label.raise_()
        self.power_supply_amount_label.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.item_search_label = QtWidgets.QLabel(self.page_3)
        self.item_search_label.setGeometry(QtCore.QRect(690, 0, 401, 91))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(25)
        self.item_search_label.setFont(font)
        self.item_search_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "image: url(:/adminSideBar/icons8-product-management-48.png);\n"
                                             "padding-right:50px;")
        self.item_search_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.item_search_label.setObjectName("item_search_label")
        self.item_table = QtWidgets.QTableWidget(self.page_3)
        self.item_table.setGeometry(QtCore.QRect(20, 325, 1761, 561))
        self.item_table.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.item_table.setFont(font)
        self.item_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_table.setAutoFillBackground(False)
        self.item_table.setStyleSheet("QWidget {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    alternate-background-color: rgb(241, 245, 249);\n"
                                      "    font: 10pt \"8514oem\";\n"
                                      "}\n"
                                      "QScrollBar:vertical {\n"
                                      "    border: none;\n"
                                      "    background: #94A3B8;\n"
                                      "    width: 14px;\n"
                                      "    margin: 15px 0 15px 0;\n"
                                      "    border-radius: 0px;\n"
                                      " }\n"
                                      "\n"
                                      "/*  HANDLE BAR VERTICAL */\n"
                                      "QScrollBar::handle:vertical {    \n"
                                      "    background-color: #E5E7EB;\n"
                                      "    min-height: 30px;\n"
                                      "    border-radius: 7px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:hover{    \n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1 #7C3AED);\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:pressed {    \n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4338CA, stop:1 #5B21B6);\n"
                                      "}\n"
                                      "\n"
                                      "/* BTN TOP - SCROLLBAR */\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "    border: none;\n"
                                      "    background-color: #94A3B8;\n"
                                      "    height: 15px;\n"
                                      "    border-top-left-radius: 7px;\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "    subcontrol-position: top;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:hover {    \n"
                                      "    background-color: rgb(255, 0, 127);\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical:pressed {    \n"
                                      "    background-color: rgb(185, 0, 92);\n"
                                      "}\n"
                                      "\n"
                                      "/* BTN BOTTOM - SCROLLBAR */\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "    border: none;\n"
                                      "    background-color:#94A3B8;\n"
                                      "    height: 15px;\n"
                                      "    border-bottom-left-radius: 7px;\n"
                                      "    border-bottom-right-radius: 7px;\n"
                                      "    subcontrol-position: bottom;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:hover {    \n"
                                      "    background-color: rgb(255, 0, 127);\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical:pressed {    \n"
                                      "    background-color: rgb(185, 0, 92);\n"
                                      "}\n"
                                      "\n"
                                      "/* RESET ARROW */\n"
                                      "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "    background: none;\n"
                                      "}\n"
                                      "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "    background: none;\n"
                                      "}\n"
                                      "")
        self.item_table.setFrameShape(QtWidgets.QFrame.Box)
        self.item_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.item_table.setLineWidth(10)
        self.item_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.item_table.setAlternatingRowColors(True)
        self.item_table.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.item_table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.item_table.setIconSize(QtCore.QSize(0, 0))
        self.item_table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.item_table.setRowCount(7)
        self.item_table.setColumnCount(12)
        self.item_table.setObjectName("item_table")
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.item_table.setItem(6, 6, item)
        self.item_table.horizontalHeader().setCascadingSectionResizes(False)
        self.item_table.horizontalHeader().setDefaultSectionSize(200)
        self.item_table.horizontalHeader().setMinimumSectionSize(26)
        self.item_table.horizontalHeader().setStretchLastSection(True)
        self.item_table.verticalHeader().setDefaultSectionSize(87)
        self.item_table.verticalHeader().setSortIndicatorShown(True)
        self.item_table.verticalHeader().setStretchLastSection(False)
        self.item_id_comboBox = QtWidgets.QComboBox(self.page_3)
        self.item_id_comboBox.setGeometry(QtCore.QRect(20, 250, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.item_id_comboBox.sizePolicy().hasHeightForWidth())
        self.item_id_comboBox.setSizePolicy(sizePolicy)
        self.item_id_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.item_id_comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.item_id_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.item_id_comboBox.setFont(font)
        self.item_id_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.item_id_comboBox.setStyleSheet("QComboBox {\n"
                                            "    border: 1px solid gray;\n"
                                            "    border-radius: 10px;\n"
                                            "    padding: 1px 18px 1px 3px;\n"
                                            "    min-width: 6em;\n"
                                            "    font: 16pt \"8514oem\";\n"
                                            "    background-color: rgb(255, 255, 255);\n"
                                            "    \n"
                                            "    color: rgb(0, 0, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox:on { /* shift the text when the popup opens */\n"
                                            "    padding-top: 3px;\n"
                                            "    padding-left: 4px;\n"
                                            "    background: white;\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox::drop-down {\n"
                                            "    subcontrol-origin: padding;\n"
                                            "    subcontrol-position: top right;\n"
                                            "    width: 15px;\n"
                                            "    background-color:white;\n"
                                            "    border-left-width: 1px;\n"
                                            "    border-left-color: darkgray;\n"
                                            "    border-left-style: solid; /* just a single line */\n"
                                            "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                            "    border-bottom-right-radius: 3px;\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                            "    top: 1px;\n"
                                            "    left: 1px;\n"
                                            "}\n"
                                            "QListView\n"
                                            "{\n"
                                            "background-color : #334155;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "}")
        self.item_id_comboBox.setEditable(True)
        self.item_id_comboBox.setCurrentText("")
        self.item_id_comboBox.setFrame(True)
        self.item_id_comboBox.setObjectName("item_id_comboBox")
        self.under_service_comboBox = QtWidgets.QComboBox(self.page_3)
        self.under_service_comboBox.setGeometry(QtCore.QRect(20, 100, 519, 51))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.under_service_comboBox.sizePolicy().hasHeightForWidth())
        self.under_service_comboBox.setSizePolicy(sizePolicy)
        self.under_service_comboBox.setMinimumSize(QtCore.QSize(143, 2))
        self.under_service_comboBox.setMaximumSize(
            QtCore.QSize(16777214, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.under_service_comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.under_service_comboBox.setFont(font)
        self.under_service_comboBox.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.under_service_comboBox.setStyleSheet("QComboBox {\n"
                                                  "    border: 1px solid gray;\n"
                                                  "    border-radius: 10px;\n"
                                                  "    padding: 1px 18px 1px 3px;\n"
                                                  "    min-width: 6em;\n"
                                                  "    font: 16pt \"8514oem\";\n"
                                                  "    background-color: rgb(255, 255, 255);\n"
                                                  "    \n"
                                                  "    color: rgb(0, 0, 0);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QComboBox:on { /* shift the text when the popup opens */\n"
                                                  "    padding-top: 3px;\n"
                                                  "    padding-left: 4px;\n"
                                                  "    background: white;\n"
                                                  "    border-radius: 10px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QComboBox::drop-down {\n"
                                                  "    subcontrol-origin: padding;\n"
                                                  "    subcontrol-position: top right;\n"
                                                  "    width: 15px;\n"
                                                  "    background-color:white;\n"
                                                  "    border-left-width: 1px;\n"
                                                  "    border-left-color: darkgray;\n"
                                                  "    border-left-style: solid; /* just a single line */\n"
                                                  "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                                  "    border-bottom-right-radius: 3px;\n"
                                                  "    border-radius: 10px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                                  "    top: 1px;\n"
                                                  "    left: 1px;\n"
                                                  "}\n"
                                                  "QListView\n"
                                                  "{\n"
                                                  "background-color : #334155;\n"
                                                  "color: rgb(255, 255, 255);\n"
                                                  "}")
        self.under_service_comboBox.setEditable(False)
        self.under_service_comboBox.setFrame(True)
        self.under_service_comboBox.setObjectName("under_service_comboBox")
        self.under_service_comboBox.addItem("")
        self.under_service_comboBox.addItem("")
        self.under_service_label = QtWidgets.QLineEdit(self.page_3)
        self.under_service_label.setGeometry(QtCore.QRect(20, 73, 241, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.under_service_label.setFont(font)
        self.under_service_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "background-color: rgba(255, 255, 255, 0);")
        self.under_service_label.setFrame(False)
        self.under_service_label.setObjectName("under_service_label")
        self.item_id_label = QtWidgets.QLineEdit(self.page_3)
        self.item_id_label.setGeometry(QtCore.QRect(20, 220, 131, 22))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(16)
        self.item_id_label.setFont(font)
        self.item_id_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(255, 255, 255, 0);")
        self.item_id_label.setFrame(False)
        self.item_id_label.setObjectName("item_id_label")
        self.item_search_button = QtWidgets.QPushButton(self.page_3)
        self.item_search_button.setGeometry(QtCore.QRect(1470, 250, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.item_search_button.setFont(font)
        self.item_search_button.setToolTipDuration(0)
        self.item_search_button.setStyleSheet("QPushButton {\n"
                                              "    border-top-right-radius: 10px;\n"
                                              "    border-top-left-radius: 10px;\n"
                                              "    border-bottom-right-radius: 10px;\n"
                                              "    border-bottom-left-radius: 10px;\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1 #7C3AED);\n"
                                              "    font: 22px;\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4338CA\n"
                                              ", stop:1 #5B21B6);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4338CA\n"
                                              ", stop:1 #5B21B6);\n"
                                              "    padding-left: 5px;\n"
                                              "    padding-top: 5px;\n"
                                              "}")
        self.item_search_button.setObjectName("item_search_button")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.request_table = QtWidgets.QTableWidget(self.page_4)
        self.request_table.setGeometry(QtCore.QRect(20, 215, 1761, 671))
        self.request_table.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.request_table.setFont(font)
        self.request_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.request_table.setAutoFillBackground(False)
        self.request_table.setStyleSheet("QWidget {\n"
                                         "    background-color: rgb(255, 255, 255);\n"
                                         "    alternate-background-color: rgb(241, 245, 249);\n"
                                         "    font: 10pt \"8514oem\";\n"
                                         "}\n"
                                         "QScrollBar:vertical {\n"
                                         "    border: none;\n"
                                         "    background: #94A3B8;\n"
                                         "    width: 14px;\n"
                                         "    margin: 15px 0 15px 0;\n"
                                         "    border-radius: 0px;\n"
                                         " }\n"
                                         "\n"
                                         "/*  HANDLE BAR VERTICAL */\n"
                                         "QScrollBar::handle:vertical {    \n"
                                         "    background-color: #E5E7EB;\n"
                                         "    min-height: 30px;\n"
                                         "    border-radius: 7px;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:hover{    \n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1 #7C3AED);\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:pressed {    \n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4338CA, stop:1 #5B21B6);\n"
                                         "}\n"
                                         "\n"
                                         "/* BTN TOP - SCROLLBAR */\n"
                                         "QScrollBar::sub-line:vertical {\n"
                                         "    border: none;\n"
                                         "    background-color: #94A3B8;\n"
                                         "    height: 15px;\n"
                                         "    border-top-left-radius: 7px;\n"
                                         "    border-top-right-radius: 7px;\n"
                                         "    subcontrol-position: top;\n"
                                         "    subcontrol-origin: margin;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical:hover {    \n"
                                         "    background-color: rgb(255, 0, 127);\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical:pressed {    \n"
                                         "    background-color: rgb(185, 0, 92);\n"
                                         "}\n"
                                         "\n"
                                         "/* BTN BOTTOM - SCROLLBAR */\n"
                                         "QScrollBar::add-line:vertical {\n"
                                         "    border: none;\n"
                                         "    background-color:#94A3B8;\n"
                                         "    height: 15px;\n"
                                         "    border-bottom-left-radius: 7px;\n"
                                         "    border-bottom-right-radius: 7px;\n"
                                         "    subcontrol-position: bottom;\n"
                                         "    subcontrol-origin: margin;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:hover {    \n"
                                         "    background-color: rgb(255, 0, 127);\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:pressed {    \n"
                                         "    background-color: rgb(185, 0, 92);\n"
                                         "}\n"
                                         "\n"
                                         "/* RESET ARROW */\n"
                                         "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                         "    background: none;\n"
                                         "}\n"
                                         "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                         "    background: none;\n"
                                         "}\n"
                                         "")
        self.request_table.setFrameShape(QtWidgets.QFrame.Box)
        self.request_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.request_table.setLineWidth(10)
        self.request_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.request_table.setAlternatingRowColors(True)
        self.request_table.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.request_table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.request_table.setIconSize(QtCore.QSize(0, 0))
        self.request_table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.request_table.setShowGrid(True)
        self.request_table.setRowCount(10)
        self.request_table.setColumnCount(7)
        self.request_table.setObjectName("request_table")
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.request_table.setHorizontalHeaderItem(6, item)
        self.request_table.horizontalHeader().setCascadingSectionResizes(False)
        self.request_table.horizontalHeader().setDefaultSectionSize(239)
        self.request_table.horizontalHeader().setMinimumSectionSize(26)
        self.request_table.horizontalHeader().setSortIndicatorShown(True)
        self.request_table.horizontalHeader().setStretchLastSection(True)
        self.request_table.verticalHeader().setDefaultSectionSize(81)
        self.request_table.verticalHeader().setSortIndicatorShown(True)
        self.request_table.verticalHeader().setStretchLastSection(False)
        self.fetch_requests_button = QtWidgets.QPushButton(self.page_4)
        self.fetch_requests_button.setGeometry(QtCore.QRect(20, 150, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fetch_requests_button.setFont(font)
        self.fetch_requests_button.setToolTipDuration(0)
        self.fetch_requests_button.setStyleSheet("QPushButton {\n"
                                                 "    border-top-right-radius: 10px;\n"
                                                 "    border-top-left-radius: 10px;\n"
                                                 "    border-bottom-right-radius: 10px;\n"
                                                 "    border-bottom-left-radius: 10px;\n"
                                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #F59E0B, stop:1#E11D48);\n"
                                                 "    font: 22px;\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #B45309\n"
                                                 ", stop:1 #9F1239);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:pressed {\n"
                                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #B45309\n"
                                                 ", stop:1 #9F1239);\n"
                                                 "    padding-left: 5px;\n"
                                                 "    padding-top: 5px;\n"
                                                 "}")
        self.fetch_requests_button.setObjectName("fetch_requests_button")
        self.all_requests_label = QtWidgets.QLabel(self.page_4)
        self.all_requests_label.setGeometry(QtCore.QRect(670, 0, 411, 91))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(25)
        self.all_requests_label.setFont(font)
        self.all_requests_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "image: url(:/adminSideBar/icons8-attract-customers-48.png);\n"
                                              "padding-right:50px;")
        self.all_requests_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.all_requests_label.setObjectName("all_requests_label")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.my_servicing_label = QtWidgets.QLabel(self.page_5)
        self.my_servicing_label.setGeometry(QtCore.QRect(650, 0, 461, 91))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(25)
        self.my_servicing_label.setFont(font)
        self.my_servicing_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "image: url(:/adminSideBar/icons8-service-48.png);\n"
                                              "padding-right:50px;")
        self.my_servicing_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.my_servicing_label.setObjectName("my_servicing_label")
        self.servicing_table = QtWidgets.QTableWidget(self.page_5)
        self.servicing_table.setGeometry(QtCore.QRect(20, 215, 1761, 671))
        self.servicing_table.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.servicing_table.setFont(font)
        self.servicing_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.servicing_table.setAutoFillBackground(False)
        self.servicing_table.setStyleSheet("QWidget {\n"
                                           "    background-color: rgb(255, 255, 255);\n"
                                           "    alternate-background-color: rgb(241, 245, 249);\n"
                                           "    font: 10pt \"8514oem\";\n"
                                           "}\n"
                                           "QScrollBar:vertical {\n"
                                           "    border: none;\n"
                                           "    background: #94A3B8;\n"
                                           "    width: 14px;\n"
                                           "    margin: 15px 0 15px 0;\n"
                                           "    border-radius: 0px;\n"
                                           " }\n"
                                           "\n"
                                           "/*  HANDLE BAR VERTICAL */\n"
                                           "QScrollBar::handle:vertical {    \n"
                                           "    background-color: #E5E7EB;\n"
                                           "    min-height: 30px;\n"
                                           "    border-radius: 7px;\n"
                                           "}\n"
                                           "QScrollBar::handle:vertical:hover{    \n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #6366F1, stop:1 #7C3AED);\n"
                                           "}\n"
                                           "QScrollBar::handle:vertical:pressed {    \n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4338CA, stop:1 #5B21B6);\n"
                                           "}\n"
                                           "\n"
                                           "/* BTN TOP - SCROLLBAR */\n"
                                           "QScrollBar::sub-line:vertical {\n"
                                           "    border: none;\n"
                                           "    background-color: #94A3B8;\n"
                                           "    height: 15px;\n"
                                           "    border-top-left-radius: 7px;\n"
                                           "    border-top-right-radius: 7px;\n"
                                           "    subcontrol-position: top;\n"
                                           "    subcontrol-origin: margin;\n"
                                           "}\n"
                                           "QScrollBar::sub-line:vertical:hover {    \n"
                                           "    background-color: rgb(255, 0, 127);\n"
                                           "}\n"
                                           "QScrollBar::sub-line:vertical:pressed {    \n"
                                           "    background-color: rgb(185, 0, 92);\n"
                                           "}\n"
                                           "\n"
                                           "/* BTN BOTTOM - SCROLLBAR */\n"
                                           "QScrollBar::add-line:vertical {\n"
                                           "    border: none;\n"
                                           "    background-color:#94A3B8;\n"
                                           "    height: 15px;\n"
                                           "    border-bottom-left-radius: 7px;\n"
                                           "    border-bottom-right-radius: 7px;\n"
                                           "    subcontrol-position: bottom;\n"
                                           "    subcontrol-origin: margin;\n"
                                           "}\n"
                                           "QScrollBar::add-line:vertical:hover {    \n"
                                           "    background-color: rgb(255, 0, 127);\n"
                                           "}\n"
                                           "QScrollBar::add-line:vertical:pressed {    \n"
                                           "    background-color: rgb(185, 0, 92);\n"
                                           "}\n"
                                           "\n"
                                           "/* RESET ARROW */\n"
                                           "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                           "    background: none;\n"
                                           "}\n"
                                           "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                           "    background: none;\n"
                                           "}\n"
                                           "")
        self.servicing_table.setFrameShape(QtWidgets.QFrame.Box)
        self.servicing_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.servicing_table.setLineWidth(10)
        self.servicing_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.servicing_table.setAlternatingRowColors(True)
        self.servicing_table.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.servicing_table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.servicing_table.setIconSize(QtCore.QSize(0, 0))
        self.servicing_table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.servicing_table.setRowCount(10)
        self.servicing_table.setColumnCount(5)
        self.servicing_table.setObjectName("servicing_table")
        item = QtWidgets.QTableWidgetItem()
        self.servicing_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.servicing_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.servicing_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.servicing_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.servicing_table.setHorizontalHeaderItem(4, item)
        self.servicing_table.horizontalHeader().setCascadingSectionResizes(False)
        self.servicing_table.horizontalHeader().setDefaultSectionSize(335)
        self.servicing_table.horizontalHeader().setMinimumSectionSize(26)
        self.servicing_table.horizontalHeader().setSortIndicatorShown(True)
        self.servicing_table.horizontalHeader().setStretchLastSection(False)
        self.servicing_table.verticalHeader().setDefaultSectionSize(81)
        self.servicing_table.verticalHeader().setSortIndicatorShown(True)
        self.servicing_table.verticalHeader().setStretchLastSection(False)
        self.refresh_servicing_button = QtWidgets.QPushButton(self.page_5)
        self.refresh_servicing_button.setGeometry(
            QtCore.QRect(20, 140, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.refresh_servicing_button.setFont(font)
        self.refresh_servicing_button.setToolTipDuration(0)
        self.refresh_servicing_button.setStyleSheet("QPushButton {\n"
                                                    "    border-top-right-radius: 10px;\n"
                                                    "    border-top-left-radius: 10px;\n"
                                                    "    border-bottom-right-radius: 10px;\n"
                                                    "    border-bottom-left-radius: 10px;\n"
                                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(45, 212, 191, 1), stop:1 rgba(6, 182, 212, 1));\n"
                                                    "    font: 22px;\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover {\n"
                                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                                    ", stop:1 #0E7490);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0F766E\n"
                                                    ", stop:1 #0E7490);\n"
                                                    "    padding-left: 5px;\n"
                                                    "    padding-top: 5px;\n"
                                                    "}")
        self.refresh_servicing_button.setObjectName("refresh_servicing_button")
        self.stackedWidget.addWidget(self.page_5)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Lights & Locks"))
        self.btn_page_1.setText(_translate(
            "MainWindow", "                 Home"))
        self.btn_page_2.setText(_translate(
            "MainWindow", "                  Products"))
        self.btn_page_3.setText(_translate(
            "MainWindow", "                 Items"))
        self.btn_page_5.setText(_translate(
            "MainWindow", "                 Requests"))
        self.btn_page_6.setText(_translate(
            "MainWindow", "                  Servicing"))
        self.btn_page_4.setText(_translate(
            "MainWindow", "                 Exit"))
        self.welcome_admin_label.setText(
            _translate("MainWindow", "Welcome Admin! "))
        self.admin_table.setSortingEnabled(True)
        item = self.admin_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IID"))
        item = self.admin_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Number of \"SOLD\" Items"))
        item = self.admin_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Number of \"UNSOLD\" Items"))
        self.refresh_button_admin.setText(_translate(
            "MainWindow", "Display Sold && Unsold Items"))
        self.view_customers_button.setText(_translate(
            "MainWindow", "View Customers With Unpaid Fees"))
        self.view_items_category_model_button.setText(
            _translate("MainWindow", "Items Sold in Category && Model"))
        self.initialise_database_button.setText(
            _translate("MainWindow", "Initialise Database!"))
        self.submit_query.setText(_translate("MainWindow", "Submit"))
        self.Categories_label.setText(_translate("MainWindow", "Categories"))
        self.category_comboBox.setCurrentText(_translate("MainWindow", "All"))
        self.category_comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.category_comboBox.setItemText(
            1, _translate("MainWindow", "Locks"))
        self.category_comboBox.setItemText(
            2, _translate("MainWindow", "Lights"))
        self.Model_label.setText(_translate("MainWindow", "Models"))
        self.Price_label.setText(_translate("MainWindow", "Price"))
        self.model_comboBox.setCurrentText(_translate("MainWindow", "All"))
        self.model_comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.model_comboBox.setItemText(1, _translate("MainWindow", "Light1"))
        self.model_comboBox.setItemText(2, _translate("MainWindow", "Light2"))
        self.model_comboBox.setItemText(
            3, _translate("MainWindow", "SmartHome1"))
        self.model_comboBox.setItemText(4, _translate("MainWindow", "Safe1"))
        self.model_comboBox.setItemText(5, _translate("MainWindow", "Safe2"))
        self.price_comboBox.setCurrentText(_translate("MainWindow", "All"))
        self.price_comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.price_comboBox.setItemText(1, _translate("MainWindow", "$50"))
        self.price_comboBox.setItemText(2, _translate("MainWindow", "$60"))
        self.price_comboBox.setItemText(3, _translate("MainWindow", "$100"))
        self.price_comboBox.setItemText(4, _translate("MainWindow", "$120"))
        self.price_comboBox.setItemText(5, _translate("MainWindow", "$125"))
        self.price_comboBox.setItemText(6, _translate("MainWindow", "$200"))
        self.factory_comboBox.setCurrentText(_translate("MainWindow", "All"))
        self.factory_comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.factory_comboBox.setItemText(1, _translate("MainWindow", "China"))
        self.factory_comboBox.setItemText(
            2, _translate("MainWindow", "Malaysia"))
        self.factory_comboBox.setItemText(
            3, _translate("MainWindow", "Philippines"))
        self.Factory_label.setText(_translate("MainWindow", "Factory"))
        self.production_year_label.setText(
            _translate("MainWindow", "Production year"))
        self.colour_comboBox.setCurrentText(_translate("MainWindow", "All"))
        self.colour_comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.colour_comboBox.setItemText(1, _translate("MainWindow", "Blue"))
        self.colour_comboBox.setItemText(2, _translate("MainWindow", "Black"))
        self.colour_comboBox.setItemText(3, _translate("MainWindow", "Green"))
        self.colour_comboBox.setItemText(4, _translate("MainWindow", "Yellow"))
        self.colour_comboBox.setItemText(5, _translate("MainWindow", "White"))
        self.Colour_label.setText(_translate("MainWindow", "Colour"))
        self.production_year_comboBox.setCurrentText(
            _translate("MainWindow", "All"))
        self.production_year_comboBox.setItemText(
            0, _translate("MainWindow", "All"))
        self.production_year_comboBox.setItemText(
            1, _translate("MainWindow", "2014"))
        self.production_year_comboBox.setItemText(
            2, _translate("MainWindow", "2015"))
        self.production_year_comboBox.setItemText(
            3, _translate("MainWindow", "2016"))
        self.production_year_comboBox.setItemText(
            4, _translate("MainWindow", "2017"))
        self.production_year_comboBox.setItemText(
            5, _translate("MainWindow", "2019"))
        self.production_year_comboBox.setItemText(
            6, _translate("MainWindow", "2020"))
        self.Power_supply_label.setText(
            _translate("MainWindow", "Power Supply"))
        self.power_supply_comboBox.setCurrentText(
            _translate("MainWindow", "All"))
        self.power_supply_comboBox.setItemText(
            0, _translate("MainWindow", "All"))
        self.power_supply_comboBox.setItemText(
            1, _translate("MainWindow", "Battery"))
        self.power_supply_comboBox.setItemText(
            2, _translate("MainWindow", "USB"))
        self.Warranty_label.setText(_translate("MainWindow", "Warranty"))
        self.warranty_comboBox.setCurrentText(_translate("MainWindow", "All"))
        self.warranty_comboBox.setItemText(0, _translate("MainWindow", "All"))
        self.warranty_comboBox.setItemText(1, _translate("MainWindow", "6"))
        self.warranty_comboBox.setItemText(2, _translate("MainWindow", "8"))
        self.warranty_comboBox.setItemText(3, _translate("MainWindow", "10"))
        self.warranty_comboBox.setItemText(4, _translate("MainWindow", "12"))
        self.category_amount_label.setText(_translate("MainWindow", "All"))
        self.choose_an_item_label.setText(
            _translate("MainWindow", "Choose An Item!"))
        self.inventory_level_label.setText(
            _translate("MainWindow", "Inventory Level"))
        self.sold_items_label.setText(
            _translate("MainWindow", "Sold Items Amount"))
        self.price_label.setText(_translate("MainWindow", "Price"))
        self.warranty_label.setText(_translate("MainWindow", "Warranty"))
        self.model_label.setText(_translate("MainWindow", "Model"))
        self.cost_label.setText(_translate("MainWindow", "Cost"))
        self.price_amount_label.setText(_translate("MainWindow", "$ --"))
        self.warranty_amount_label.setText(_translate("MainWindow", "--"))
        self.model_amount_label.setText(_translate("MainWindow", "--"))
        self.cost_amount_label.setText(_translate("MainWindow", "$ --"))
        self.inventory_amount_label.setText(_translate("MainWindow", "--"))
        self.sold_items_amount_label.setText(_translate("MainWindow", "--"))
        self.color_label.setText(_translate("MainWindow", "Color"))
        self.product_year_label.setText(
            _translate("MainWindow", "Production Year"))
        self.power_supply_label.setText(
            _translate("MainWindow", "Power Supply"))
        self.color_amount_label.setText(_translate("MainWindow", "--"))
        self.producti_year_amount_label.setText(_translate("MainWindow", "--"))
        self.power_supply_amount_label.setText(_translate("MainWindow", "--"))
        self.item_search_label.setText(_translate("MainWindow", "Item Search"))
        self.item_table.setSortingEnabled(True)
        item = self.item_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.item_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item ID"))
        item = self.item_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Production Year"))
        item = self.item_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Power Supply"))
        item = self.item_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Color"))
        item = self.item_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Factory"))
        item = self.item_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Purchase Status"))
        item = self.item_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Model"))
        item = self.item_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Category"))
        item = self.item_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Warranty"))
        item = self.item_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Price"))
        item = self.item_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Cost"))
        __sortingEnabled = self.item_table.isSortingEnabled()
        self.item_table.setSortingEnabled(False)
        self.item_table.setSortingEnabled(__sortingEnabled)
        self.under_service_comboBox.setCurrentText(
            _translate("MainWindow", "Yes"))
        self.under_service_comboBox.setItemText(
            0, _translate("MainWindow", "Yes"))
        self.under_service_comboBox.setItemText(
            1, _translate("MainWindow", "All Items Search"))
        self.under_service_label.setText(
            _translate("MainWindow", "Under Service?"))
        self.item_id_label.setText(_translate("MainWindow", "Item ID"))
        self.item_search_button.setText(_translate("MainWindow", "Search"))
        self.request_table.setSortingEnabled(True)
        item = self.request_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Request ID"))
        item = self.request_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Service ID"))
        item = self.request_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Customer ID"))
        item = self.request_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Admin ID"))
        item = self.request_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Item ID"))
        item = self.request_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Request Date"))
        item = self.request_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Approve Request"))
        self.fetch_requests_button.setText(
            _translate("MainWindow", "Fetch Requests"))
        self.all_requests_label.setText(_translate("MainWindow", "Requests"))
        self.my_servicing_label.setText(_translate("MainWindow", "Servicing"))
        self.servicing_table.setSortingEnabled(True)
        item = self.servicing_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Admin ID"))
        item = self.servicing_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Request ID"))
        item = self.servicing_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Service ID"))
        item = self.servicing_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Service Status"))
        item = self.servicing_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Complete Service"))
        self.refresh_servicing_button.setText(
            _translate("MainWindow", "Refresh"))
