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

        self.joindate_edit = QDateEdit(self.input_group)
        self.joindate_edit.setObjectName(u"joindate_edit")
        sizePolicy.setHeightForWidth(self.joindate_edit.sizePolicy().hasHeightForWidth())
        self.joindate_edit.setSizePolicy(sizePolicy)
        self.joindate_edit.setMinimumSize(QSize(150, 0))
        self.joindate_edit.setFont(font)
        self.joindate_edit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.joindate_edit)

        self.horizontalSpacer = QSpacerItem(90, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.department_label = QLabel(self.input_group)
        self.department_label.setObjectName(u"department_label")
        sizePolicy.setHeightForWidth(self.department_label.sizePolicy().hasHeightForWidth())
        self.department_label.setSizePolicy(sizePolicy)
        self.department_label.setFont(font)

        self.horizontalLayout.addWidget(self.department_label)

        self.department_combobox = QComboBox(self.input_group)
        self.department_combobox.addItem("")
        self.department_combobox.addItem("")
        self.department_combobox.addItem("")
        self.department_combobox.addItem("")
        self.department_combobox.addItem("")
        self.department_combobox.addItem("")
        self.department_combobox.addItem("")
        self.department_combobox.setObjectName(u"department_combobox")
        sizePolicy.setHeightForWidth(self.department_combobox.sizePolicy().hasHeightForWidth())
        self.department_combobox.setSizePolicy(sizePolicy)
        self.department_combobox.setMinimumSize(QSize(150, 0))
        self.department_combobox.setFont(font)

        self.horizontalLayout.addWidget(self.department_combobox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.firstname_edit = QLineEdit(self.input_group)
        self.firstname_edit.setObjectName(u"firstname_edit")
        self.firstname_edit.setFont(font)

        self.horizontalLayout_2.addWidget(self.firstname_edit)

        self.lastname_edit = QLineEdit(self.input_group)
        self.lastname_edit.setObjectName(u"lastname_edit")
        self.lastname_edit.setFont(font)

        self.horizontalLayout_2.addWidget(self.lastname_edit)

        self.jobtitle_edit = QLineEdit(self.input_group)
        self.jobtitle_edit.setObjectName(u"jobtitle_edit")
        self.jobtitle_edit.setFont(font)

        self.horizontalLayout_2.addWidget(self.jobtitle_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_button = QPushButton(self.input_group)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setFont(font)

        self.horizontalLayout_3.addWidget(self.add_button)

        self.update_button = QPushButton(self.input_group)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setFont(font)

        self.horizontalLayout_3.addWidget(self.update_button)

        self.remove_button = QPushButton(self.input_group)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setFont(font)

        self.horizontalLayout_3.addWidget(self.remove_button)

        self.remove_all_button = QPushButton(self.input_group)
        self.remove_all_button.setObjectName(u"remove_all_button")
        self.remove_all_button.setFont(font)

        self.horizontalLayout_3.addWidget(self.remove_all_button)


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
        self.lastname_search = QLineEdit(self.search_group)
        self.lastname_search.setObjectName(u"lastname_search")
        self.lastname_search.setFont(font)

        self.gridLayout.addWidget(self.lastname_search, 0, 1, 1, 1)

        self.firstname_search = QLineEdit(self.search_group)
        self.firstname_search.setObjectName(u"firstname_search")
        self.firstname_search.setFont(font)

        self.gridLayout.addWidget(self.firstname_search, 0, 0, 1, 1)

        self.search_button = QPushButton(self.search_group)
        self.search_button.setObjectName(u"search_button")
        sizePolicy.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setMinimumSize(QSize(116, 0))
        self.search_button.setFont(font)

        self.gridLayout.addWidget(self.search_button, 1, 0, 1, 1)


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
        MainWindow.setMenuBar(self.menuBar)
#if QT_CONFIG(shortcut)
        self.date_label.setBuddy(self.joindate_edit)
        self.department_label.setBuddy(self.department_combobox)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.joindate_edit, self.department_combobox)
        QWidget.setTabOrder(self.department_combobox, self.firstname_edit)
        QWidget.setTabOrder(self.firstname_edit, self.lastname_edit)
        QWidget.setTabOrder(self.lastname_edit, self.jobtitle_edit)
        QWidget.setTabOrder(self.jobtitle_edit, self.add_button)
        QWidget.setTabOrder(self.add_button, self.update_button)
        QWidget.setTabOrder(self.update_button, self.remove_button)
        QWidget.setTabOrder(self.remove_button, self.remove_all_button)
        QWidget.setTabOrder(self.remove_all_button, self.firstname_search)
        QWidget.setTabOrder(self.firstname_search, self.lastname_search)
        QWidget.setTabOrder(self.lastname_search, self.search_button)
        QWidget.setTabOrder(self.search_button, self.table)

        self.menuBar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple SQL Program", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.input_group.setTitle(QCoreApplication.translate("MainWindow", u"Input Employee Information", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date Joined:", None))
        self.joindate_edit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MMM-dd-yyyy", None))
        self.department_label.setText(QCoreApplication.translate("MainWindow", u"Department:", None))
        self.department_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Executive", None))
        self.department_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"HR", None))
        self.department_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Accounting", None))
        self.department_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Engineering", None))
        self.department_combobox.setItemText(4, QCoreApplication.translate("MainWindow", u"Entertainment", None))
        self.department_combobox.setItemText(5, QCoreApplication.translate("MainWindow", u"Shopping", None))
        self.department_combobox.setItemText(6, QCoreApplication.translate("MainWindow", u"Billing", None))

        self.firstname_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lastname_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.jobtitle_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Job Title", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add Employee", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"Update Employee", None))
        self.remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove Employee", None))
        self.remove_all_button.setText(QCoreApplication.translate("MainWindow", u"Remove All", None))
        self.search_group.setTitle(QCoreApplication.translate("MainWindow", u"Search Employee Information", None))
        self.lastname_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.firstname_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
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
    # retranslateUi

