# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Cralix\Desktop\qtCashier\app_modules\productModule\ui/productEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        mainWindow.resize(639, 524)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/window-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setHorizontalSpacing(24)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(-1, -1, 0, -1)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setObjectName("formLayout")
        self.formNameLabel = QtWidgets.QLabel(self.centralWidget)
        self.formNameLabel.setObjectName("formNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.formNameLabel)
        self.formNameEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.formNameEdit.setObjectName("formNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.formNameEdit)
        self.formPriceLabel = QtWidgets.QLabel(self.centralWidget)
        self.formPriceLabel.setObjectName("formPriceLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.formPriceLabel)
        self.formImageLabel = QtWidgets.QLabel(self.centralWidget)
        self.formImageLabel.setObjectName("formImageLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.formImageLabel)
        self.formUploadImage = QtWidgets.QPushButton(self.centralWidget)
        self.formUploadImage.setObjectName("formUploadImage")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.formUploadImage)
        self.formPriceEdit = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.formPriceEdit.setObjectName("formPriceEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.formPriceEdit)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.checkBox = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.gridLayout.addLayout(self.formLayout_2, 3, 1, 1, 1)
        self.imageLabel = QtWidgets.QLabel(self.centralWidget)
        self.imageLabel.setMinimumSize(QtCore.QSize(256, 256))
        self.imageLabel.setObjectName("imageLabel")
        self.gridLayout.addWidget(self.imageLabel, 0, 2, 7, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralWidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Редактирование товара | {ИМЯ ТОВАРА}"))
        self.formNameLabel.setText(_translate("mainWindow", "Наименование товара"))
        self.formNameEdit.setPlaceholderText(_translate("mainWindow", "Введите название товара..."))
        self.formPriceLabel.setText(_translate("mainWindow", "Цена товара"))
        self.formImageLabel.setText(_translate("mainWindow", "Изображение"))
        self.formUploadImage.setText(_translate("mainWindow", "Загрузить новое изображение"))
        self.label_3.setText(_translate("mainWindow", "Товар в избранном?"))
        self.checkBox.setText(_translate("mainWindow", "В избранном"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("mainWindow", "978020137962"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("mainWindow", "Редактирование штрихкодов:"))
        self.label_2.setText(_translate("mainWindow", "Выбранный штрихкод:"))
        self.lineEdit.setText(_translate("mainWindow", "978020137962"))
        self.imageLabel.setText(_translate("mainWindow", "Картинка"))
        self.pushButton_2.setText(_translate("mainWindow", "Готово"))
        self.pushButton.setText(_translate("mainWindow", "Новый штрихкод"))
import resources_rc
