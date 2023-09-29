# Form implementation generated from reading ui file 'src/main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 614)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.income_table = QtWidgets.QTableWidget(parent=self.layoutWidget)
        self.income_table.setRowCount(1)
        self.income_table.setColumnCount(1)
        self.income_table.setObjectName("income_table")
        self.verticalLayout.addWidget(self.income_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.income_new = QtWidgets.QToolButton(parent=self.layoutWidget)
        self.income_new.setObjectName("income_new")
        self.horizontalLayout.addWidget(self.income_new)
        self.income_remove = QtWidgets.QToolButton(parent=self.layoutWidget)
        self.income_remove.setObjectName("income_remove")
        self.horizontalLayout.addWidget(self.income_remove)
        self.income_edit = QtWidgets.QToolButton(parent=self.layoutWidget)
        self.income_edit.setObjectName("income_edit")
        self.horizontalLayout.addWidget(self.income_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.expense_table = QtWidgets.QTableWidget(parent=self.layoutWidget)
        self.expense_table.setObjectName("expense_table")
        self.expense_table.setColumnCount(0)
        self.expense_table.setRowCount(0)
        self.verticalLayout_2.addWidget(self.expense_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.expense_new = QtWidgets.QToolButton(parent=self.layoutWidget)
        self.expense_new.setObjectName("expense_new")
        self.horizontalLayout_2.addWidget(self.expense_new)
        self.expense_remove = QtWidgets.QToolButton(parent=self.layoutWidget)
        self.expense_remove.setObjectName("expense_remove")
        self.horizontalLayout_2.addWidget(self.expense_remove)
        self.expense_edit = QtWidgets.QToolButton(parent=self.layoutWidget)
        self.expense_edit.setObjectName("expense_edit")
        self.horizontalLayout_2.addWidget(self.expense_edit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.plot_frame = QtWidgets.QFrame(parent=self.layoutWidget)
        self.plot_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.plot_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.plot_frame.setObjectName("plot_frame")
        self.gridLayout.addWidget(self.plot_frame, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.investment_table = QtWidgets.QTableWidget(parent=self.layoutWidget)
        self.investment_table.setObjectName("investment_table")
        self.investment_table.setColumnCount(0)
        self.investment_table.setRowCount(0)
        self.verticalLayout_3.addWidget(self.investment_table)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.investment_new = QtWidgets.QToolButton(parent=self.layoutWidget)
        self.investment_new.setObjectName("investment_new")
        self.horizontalLayout_3.addWidget(self.investment_new)
        self.investments_remove = QtWidgets.QToolButton(parent=self.layoutWidget)
        self.investments_remove.setObjectName("investments_remove")
        self.horizontalLayout_3.addWidget(self.investments_remove)
        self.investments_edit = QtWidgets.QToolButton(parent=self.layoutWidget)
        self.investments_edit.setObjectName("investments_edit")
        self.horizontalLayout_3.addWidget(self.investments_edit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.income_new.setText(_translate("MainWindow", "New"))
        self.income_remove.setText(_translate("MainWindow", "Remove"))
        self.income_edit.setText(_translate("MainWindow", "Edit"))
        self.expense_new.setText(_translate("MainWindow", "New"))
        self.expense_remove.setText(_translate("MainWindow", "Remove"))
        self.expense_edit.setText(_translate("MainWindow", "Edit"))
        self.investment_new.setText(_translate("MainWindow", "New"))
        self.investments_remove.setText(_translate("MainWindow", "Remove"))
        self.investments_edit.setText(_translate("MainWindow", "Edit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
