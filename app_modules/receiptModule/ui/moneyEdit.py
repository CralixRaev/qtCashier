# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Cralix\Desktop\qtCashier\app_modules\receiptModule\ui/moneyEdit.ui'
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
        Form.resize(350, 165)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.totalButton = QtWidgets.QPushButton(Form)
        self.totalButton.setObjectName("totalButton")
        self.gridLayout.addWidget(self.totalButton, 3, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.receiveLabel = QtWidgets.QLabel(Form)
        self.receiveLabel.setObjectName("receiveLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.receiveLabel)
        self.receiveEdit = QtWidgets.QLineEdit(Form)
        self.receiveEdit.setObjectName("receiveEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.receiveEdit)
        self.commentLabel = QtWidgets.QLabel(Form)
        self.commentLabel.setObjectName("commentLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.commentLabel)
        self.changeLabel = QtWidgets.QLabel(Form)
        self.changeLabel.setObjectName("changeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.changeLabel)
        self.changeEdit = QtWidgets.QLabel(Form)
        self.changeEdit.setObjectName("changeEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.changeEdit)
        self.commentEdit = QtWidgets.QPlainTextEdit(Form)
        self.commentEdit.setReadOnly(True)
        self.commentEdit.setObjectName("commentEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.commentEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "???????????? ????????"))
        self.totalButton.setText(_translate("Form", "?????????????? ??????"))
        self.receiveLabel.setText(_translate("Form", "???????????????? ?????????? ???? ????????????????????:"))
        self.receiveEdit.setPlaceholderText(_translate("Form", "999 999 ??????."))
        self.commentLabel.setText(_translate("Form", "??????????????????????: "))
        self.changeLabel.setText(_translate("Form", "??????????:"))
        self.changeEdit.setText(_translate("Form", "0 ????????????"))
        self.commentEdit.setPlaceholderText(_translate("Form", "?????? ??????????????????????."))
