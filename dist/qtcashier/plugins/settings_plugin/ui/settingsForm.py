# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Cralix\Desktop\qtCashier\plugins\settings_plugin\ui/settingsForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(376, 103)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.close = QtWidgets.QPushButton(Form)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 1, 1, 1, 1)
        self.receiptGroup = QtWidgets.QGroupBox(Form)
        self.receiptGroup.setObjectName("receiptGroup")
        self.formLayout_2 = QtWidgets.QFormLayout(self.receiptGroup)
        self.formLayout_2.setObjectName("formLayout_2")
        self.receiptRoundingCheck = QtWidgets.QCheckBox(self.receiptGroup)
        self.receiptRoundingCheck.setObjectName("receiptRoundingCheck")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.receiptRoundingCheck)
        self.gridLayout.addWidget(self.receiptGroup, 0, 1, 1, 1)
        self.databaseGroup = QtWidgets.QGroupBox(Form)
        self.databaseGroup.setObjectName("databaseGroup")
        self.formLayout = QtWidgets.QFormLayout(self.databaseGroup)
        self.formLayout.setObjectName("formLayout")
        self.dbNameLabel = QtWidgets.QLabel(self.databaseGroup)
        self.dbNameLabel.setObjectName("dbNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dbNameLabel)
        self.dbNameEdit = QtWidgets.QLineEdit(self.databaseGroup)
        self.dbNameEdit.setObjectName("dbNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dbNameEdit)
        self.gridLayout.addWidget(self.databaseGroup, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.close.setText(_translate("Form", "Готово"))
        self.receiptGroup.setTitle(_translate("Form", "Настройки чека"))
        self.receiptRoundingCheck.setText(_translate("Form", "Округление копеек"))
        self.databaseGroup.setTitle(_translate("Form", "Настройки базы"))
        self.dbNameLabel.setText(_translate("Form", "Имя файла БД: "))
