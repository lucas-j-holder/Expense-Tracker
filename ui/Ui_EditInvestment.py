# Form implementation generated from reading ui file 'src/EditInvestment.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditInvestment(object):
    def setupUi(self, EditInvestment):
        EditInvestment.setObjectName("EditInvestment")
        EditInvestment.resize(352, 179)
        self.widget = QtWidgets.QWidget(parent=EditInvestment)
        self.widget.setGeometry(QtCore.QRect(0, 0, 351, 178))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.name = QtWidgets.QLineEdit(parent=self.widget)
        self.name.setObjectName("name")
        self.horizontalLayout_6.addWidget(self.name)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.principal = QtWidgets.QSpinBox(parent=self.widget)
        self.principal.setObjectName("principal")
        self.horizontalLayout_5.addWidget(self.principal)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.return_rate = QtWidgets.QSpinBox(parent=self.widget)
        self.return_rate.setObjectName("return_rate")
        self.horizontalLayout_4.addWidget(self.return_rate)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.compound_frequency = QtWidgets.QComboBox(parent=self.widget)
        self.compound_frequency.setObjectName("compound_frequency")
        self.horizontalLayout_3.addWidget(self.compound_frequency)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.additional_contribution_amount = QtWidgets.QSpinBox(parent=self.widget)
        self.additional_contribution_amount.setObjectName("additional_contribution_amount")
        self.horizontalLayout_2.addWidget(self.additional_contribution_amount)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.additional_contribution_frequency = QtWidgets.QComboBox(parent=self.widget)
        self.additional_contribution_frequency.setObjectName("additional_contribution_frequency")
        self.horizontalLayout.addWidget(self.additional_contribution_frequency)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(parent=self.widget)
        self.buttonBox_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.horizontalLayout_7.addWidget(self.buttonBox_2)

        self.retranslateUi(EditInvestment)
        QtCore.QMetaObject.connectSlotsByName(EditInvestment)

    def retranslateUi(self, EditInvestment):
        _translate = QtCore.QCoreApplication.translate
        EditInvestment.setWindowTitle(_translate("EditInvestment", "Dialog"))
        self.label.setText(_translate("EditInvestment", "Name:"))
        self.label_2.setText(_translate("EditInvestment", "Principal:"))
        self.label_3.setText(_translate("EditInvestment", "Return Rate"))
        self.label_4.setText(_translate("EditInvestment", "Compound"))
        self.label_6.setText(_translate("EditInvestment", "Additional Contribution:"))
        self.label_5.setText(_translate("EditInvestment", "Add. Contrib. Frequency:"))
