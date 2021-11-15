# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Cralix\Desktop\qtCashier\app_modules\receiptModule\ui/checkItem.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_receiptItem(object):
    def setupUi(self, receiptItem):
        receiptItem.setObjectName("receiptItem")
        receiptItem.resize(499, 82)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(receiptItem.sizePolicy().hasHeightForWidth())
        receiptItem.setSizePolicy(sizePolicy)
        receiptItem.setMaximumSize(QtCore.QSize(16777215, 82))
        self.gridLayout_3 = QtWidgets.QGridLayout(receiptItem)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.itemTotal = QtWidgets.QLabel(receiptItem)
        self.itemTotal.setMinimumSize(QtCore.QSize(64, 0))
        self.itemTotal.setMaximumSize(QtCore.QSize(96, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(12)
        self.itemTotal.setFont(font)
        self.itemTotal.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.itemTotal.setObjectName("itemTotal")
        self.gridLayout_3.addWidget(self.itemTotal, 0, 3, 1, 1)
        self.itemImage = QtWidgets.QLabel(receiptItem)
        self.itemImage.setMinimumSize(QtCore.QSize(64, 64))
        self.itemImage.setMaximumSize(QtCore.QSize(64, 64))
        self.itemImage.setSizeIncrement(QtCore.QSize(64, 64))
        self.itemImage.setBaseSize(QtCore.QSize(64, 64))
        self.itemImage.setText("")
        self.itemImage.setPixmap(QtGui.QPixmap(":/images/no-image.png"))
        self.itemImage.setScaledContents(True)
        self.itemImage.setObjectName("itemImage")
        self.gridLayout_3.addWidget(self.itemImage, 0, 1, 1, 1)
        self.itemId = QtWidgets.QLabel(receiptItem)
        self.itemId.setMaximumSize(QtCore.QSize(32, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.itemId.setFont(font)
        self.itemId.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.itemId.setObjectName("itemId")
        self.gridLayout_3.addWidget(self.itemId, 0, 0, 1, 1)
        self.itemInfo = QtWidgets.QGridLayout()
        self.itemInfo.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.itemInfo.setObjectName("itemInfo")
        self.itemName = QtWidgets.QLabel(receiptItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemName.sizePolicy().hasHeightForWidth())
        self.itemName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.itemName.setFont(font)
        self.itemName.setScaledContents(False)
        self.itemName.setWordWrap(True)
        self.itemName.setIndent(-1)
        self.itemName.setObjectName("itemName")
        self.itemInfo.addWidget(self.itemName, 0, 2, 1, 3)
        self.itemPricesLayout = QtWidgets.QHBoxLayout()
        self.itemPricesLayout.setObjectName("itemPricesLayout")
        self.itemPricesQuantity = QtWidgets.QLabel(receiptItem)
        self.itemPricesQuantity.setMaximumSize(QtCore.QSize(32, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.itemPricesQuantity.setFont(font)
        self.itemPricesQuantity.setTextFormat(QtCore.Qt.PlainText)
        self.itemPricesQuantity.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.itemPricesQuantity.setWordWrap(False)
        self.itemPricesQuantity.setObjectName("itemPricesQuantity")
        self.itemPricesLayout.addWidget(self.itemPricesQuantity)
        self.itemPricesSeparator = QtWidgets.QLabel(receiptItem)
        self.itemPricesSeparator.setMaximumSize(QtCore.QSize(16, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.itemPricesSeparator.setFont(font)
        self.itemPricesSeparator.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.itemPricesSeparator.setObjectName("itemPricesSeparator")
        self.itemPricesLayout.addWidget(self.itemPricesSeparator)
        self.iremPricesPrice = QtWidgets.QLabel(receiptItem)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.iremPricesPrice.setFont(font)
        self.iremPricesPrice.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.iremPricesPrice.setObjectName("iremPricesPrice")
        self.itemPricesLayout.addWidget(self.iremPricesPrice)
        self.itemInfo.addLayout(self.itemPricesLayout, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.itemInfo, 0, 2, 1, 1)

        self.retranslateUi(receiptItem)
        QtCore.QMetaObject.connectSlotsByName(receiptItem)

    def retranslateUi(self, receiptItem):
        _translate = QtCore.QCoreApplication.translate
        receiptItem.setWindowTitle(_translate("receiptItem", "Form"))
        self.itemTotal.setText(_translate("receiptItem", "0.0"))
        self.itemId.setText(_translate("receiptItem", "0."))
        self.itemName.setText(_translate("receiptItem", "Очень-очень длинное название товара ведь длинные названия это хорошо ;)"))
        self.itemPricesQuantity.setText(_translate("receiptItem", "999"))
        self.itemPricesSeparator.setText(_translate("receiptItem", "x"))
        self.iremPricesPrice.setText(_translate("receiptItem", "722 000,00"))
import resources_rc