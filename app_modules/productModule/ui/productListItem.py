# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Cralix\Desktop\qtCashier\app_modules\productModule\ui/productListItem.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_productListItem(object):
    def setupUi(self, productListItem):
        productListItem.setObjectName("productListItem")
        productListItem.resize(237, 89)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(productListItem.sizePolicy().hasHeightForWidth())
        productListItem.setSizePolicy(sizePolicy)
        productListItem.setMaximumSize(QtCore.QSize(16777215, 16777215))
        productListItem.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.gridLayout = QtWidgets.QGridLayout(productListItem)
        self.gridLayout.setObjectName("gridLayout")
        self.productPrice = QtWidgets.QLabel(productListItem)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.productPrice.setFont(font)
        self.productPrice.setObjectName("productPrice")
        self.gridLayout.addWidget(self.productPrice, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.productImage = QtWidgets.QLabel(productListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productImage.sizePolicy().hasHeightForWidth())
        self.productImage.setSizePolicy(sizePolicy)
        self.productImage.setMinimumSize(QtCore.QSize(64, 64))
        self.productImage.setMaximumSize(QtCore.QSize(64, 64))
        self.productImage.setText("")
        self.productImage.setPixmap(QtGui.QPixmap(":/images/no-image.png"))
        self.productImage.setScaledContents(True)
        self.productImage.setObjectName("productImage")
        self.gridLayout.addWidget(self.productImage, 0, 0, 2, 1)
        self.favoriteCheckBox = QtWidgets.QCheckBox(productListItem)
        self.favoriteCheckBox.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/favorite.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.favoriteCheckBox.setIcon(icon)
        self.favoriteCheckBox.setObjectName("favoriteCheckBox")
        self.gridLayout.addWidget(self.favoriteCheckBox, 1, 1, 1, 1)
        self.productName = QtWidgets.QLabel(productListItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productName.sizePolicy().hasHeightForWidth())
        self.productName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.productName.setFont(font)
        self.productName.setTextFormat(QtCore.Qt.PlainText)
        self.productName.setScaledContents(True)
        self.productName.setWordWrap(True)
        self.productName.setObjectName("productName")
        self.gridLayout.addWidget(self.productName, 0, 1, 1, 3)

        self.retranslateUi(productListItem)
        QtCore.QMetaObject.connectSlotsByName(productListItem)

    def retranslateUi(self, productListItem):
        _translate = QtCore.QCoreApplication.translate
        productListItem.setWindowTitle(_translate("productListItem", "Form"))
        self.productPrice.setText(_translate("productListItem", "0 ??????"))
        self.productName.setText(_translate("productListItem", "?????????? ?????????? ?????????? ?????????????? ???????????????? ????????????"))
import resources_rc
