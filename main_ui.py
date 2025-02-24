# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 637)
        icon = QIcon()
        icon.addFile(u":/images/ms_icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.action_dark_mode = QAction(MainWindow)
        self.action_dark_mode.setObjectName(u"action_dark_mode")
        self.action_dark_mode.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.input_group = QGroupBox(self.centralwidget)
        self.input_group.setObjectName(u"input_group")
        self.verticalLayout_2 = QVBoxLayout(self.input_group)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.date_label = QLabel(self.input_group)
        self.date_label.setObjectName(u"date_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        self.date_label.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        self.date_label.setFont(font)

        self.horizontalLayout.addWidget(self.date_label)

        self.date_joined = QDateEdit(self.input_group)
        self.date_joined.setObjectName(u"date_joined")
        sizePolicy.setHeightForWidth(self.date_joined.sizePolicy().hasHeightForWidth())
        self.date_joined.setSizePolicy(sizePolicy)
        self.date_joined.setMinimumSize(QSize(150, 0))
        self.date_joined.setFont(font)
        self.date_joined.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.date_joined)

        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.department_label = QLabel(self.input_group)
        self.department_label.setObjectName(u"department_label")
        sizePolicy.setHeightForWidth(self.department_label.sizePolicy().hasHeightForWidth())
        self.department_label.setSizePolicy(sizePolicy)
        self.department_label.setFont(font)

        self.horizontalLayout.addWidget(self.department_label)

        self.combobox_department = QComboBox(self.input_group)
        self.combobox_department.addItem("")
        self.combobox_department.addItem("")
        self.combobox_department.addItem("")
        self.combobox_department.addItem("")
        self.combobox_department.addItem("")
        self.combobox_department.addItem("")
        self.combobox_department.addItem("")
        self.combobox_department.setObjectName(u"combobox_department")
        sizePolicy.setHeightForWidth(self.combobox_department.sizePolicy().hasHeightForWidth())
        self.combobox_department.setSizePolicy(sizePolicy)
        self.combobox_department.setMinimumSize(QSize(150, 0))
        self.combobox_department.setFont(font)

        self.horizontalLayout.addWidget(self.combobox_department)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_firstname = QLineEdit(self.input_group)
        self.line_firstname.setObjectName(u"line_firstname")
        self.line_firstname.setFont(font)

        self.horizontalLayout_2.addWidget(self.line_firstname)

        self.line_lastname = QLineEdit(self.input_group)
        self.line_lastname.setObjectName(u"line_lastname")
        self.line_lastname.setFont(font)

        self.horizontalLayout_2.addWidget(self.line_lastname)

        self.line_jobtitle = QLineEdit(self.input_group)
        self.line_jobtitle.setObjectName(u"line_jobtitle")
        self.line_jobtitle.setFont(font)

        self.horizontalLayout_2.addWidget(self.line_jobtitle)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_add = QPushButton(self.input_group)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setFont(font)

        self.horizontalLayout_3.addWidget(self.button_add)

        self.button_update = QPushButton(self.input_group)
        self.button_update.setObjectName(u"button_update")
        self.button_update.setFont(font)

        self.horizontalLayout_3.addWidget(self.button_update)

        self.button_remove = QPushButton(self.input_group)
        self.button_remove.setObjectName(u"button_remove")
        self.button_remove.setFont(font)

        self.horizontalLayout_3.addWidget(self.button_remove)

        self.button_remove_all = QPushButton(self.input_group)
        self.button_remove_all.setObjectName(u"button_remove_all")
        self.button_remove_all.setFont(font)

        self.horizontalLayout_3.addWidget(self.button_remove_all)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.input_group)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.search_group = QGroupBox(self.centralwidget)
        self.search_group.setObjectName(u"search_group")
        self.verticalLayout_3 = QVBoxLayout(self.search_group)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_lastname_search = QLineEdit(self.search_group)
        self.line_lastname_search.setObjectName(u"line_lastname_search")
        self.line_lastname_search.setFont(font)

        self.gridLayout.addWidget(self.line_lastname_search, 0, 1, 1, 1)

        self.line_firstname_search = QLineEdit(self.search_group)
        self.line_firstname_search.setObjectName(u"line_firstname_search")
        self.line_firstname_search.setFont(font)

        self.gridLayout.addWidget(self.line_firstname_search, 0, 0, 1, 1)

        self.button_search = QPushButton(self.search_group)
        self.button_search.setObjectName(u"button_search")
        sizePolicy.setHeightForWidth(self.button_search.sizePolicy().hasHeightForWidth())
        self.button_search.setSizePolicy(sizePolicy)
        self.button_search.setMinimumSize(QSize(116, 0))
        self.button_search.setFont(font)

        self.gridLayout.addWidget(self.button_search, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.search_group)

        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 6):
            self.table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table.setObjectName(u"table")
        self.table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(False)
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 819, 22))
        self.menu_help = QMenu(self.menuBar)
        self.menu_help.setObjectName(u"menu_help")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menuBar)
#if QT_CONFIG(shortcut)
        self.date_label.setBuddy(self.date_joined)
        self.department_label.setBuddy(self.combobox_department)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.date_joined, self.combobox_department)
        QWidget.setTabOrder(self.combobox_department, self.line_firstname)
        QWidget.setTabOrder(self.line_firstname, self.line_lastname)
        QWidget.setTabOrder(self.line_lastname, self.line_jobtitle)
        QWidget.setTabOrder(self.line_jobtitle, self.button_add)
        QWidget.setTabOrder(self.button_add, self.button_update)
        QWidget.setTabOrder(self.button_update, self.button_remove)
        QWidget.setTabOrder(self.button_remove, self.button_remove_all)
        QWidget.setTabOrder(self.button_remove_all, self.line_firstname_search)
        QWidget.setTabOrder(self.line_firstname_search, self.line_lastname_search)
        QWidget.setTabOrder(self.line_lastname_search, self.button_search)
        QWidget.setTabOrder(self.button_search, self.table)

        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.actionAbout_Qt)
        self.menuSettings.addAction(self.action_dark_mode)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple SQL Program", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.action_dark_mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.input_group.setTitle(QCoreApplication.translate("MainWindow", u"Input Employee Information", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date Joined:", None))
        self.date_joined.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MMM-dd-yyyy", None))
        self.department_label.setText(QCoreApplication.translate("MainWindow", u"Department:", None))
        self.combobox_department.setItemText(0, QCoreApplication.translate("MainWindow", u"Executive", None))
        self.combobox_department.setItemText(1, QCoreApplication.translate("MainWindow", u"HR", None))
        self.combobox_department.setItemText(2, QCoreApplication.translate("MainWindow", u"Accounting", None))
        self.combobox_department.setItemText(3, QCoreApplication.translate("MainWindow", u"Engineering", None))
        self.combobox_department.setItemText(4, QCoreApplication.translate("MainWindow", u"Entertainment", None))
        self.combobox_department.setItemText(5, QCoreApplication.translate("MainWindow", u"Shopping", None))
        self.combobox_department.setItemText(6, QCoreApplication.translate("MainWindow", u"Billing", None))

        self.line_firstname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.line_lastname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.line_jobtitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Job Title", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"Add Employee", None))
        self.button_update.setText(QCoreApplication.translate("MainWindow", u"Update Employee", None))
        self.button_remove.setText(QCoreApplication.translate("MainWindow", u"Remove Employee", None))
        self.button_remove_all.setText(QCoreApplication.translate("MainWindow", u"Remove All", None))
        self.search_group.setTitle(QCoreApplication.translate("MainWindow", u"Search Employee Information", None))
        self.line_lastname_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.line_firstname_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.button_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"First name", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Job Title", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Join Date", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

