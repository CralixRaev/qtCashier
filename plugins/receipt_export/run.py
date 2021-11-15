import csv
import os
from datetime import datetime

from PyQt5.QtWidgets import QPushButton, QFileDialog
from docxtpl import DocxTemplate
from csv import DictWriter


def on_reload(application):
    run(application)


def run(application):
    def export():
        dialog = QFileDialog()
        result = dialog.getSaveFileName(application.ui.mainWidget, 'Выберите путь для сохранения',
                                        filter="Файлы CSV (*.csv)")
        if result[0]:
            receipts = application.modules["receiptModule"].receipt_system.receipts
            names = list(receipts[0].__dict__.keys())
            with open(result[0], 'w', encoding="utf-8", newline='') as f:
                writer = DictWriter(f, fieldnames=["item_id", "date_time", "is_returned", "comment",
                                                   "products"], delimiter=';',
                                    quoting=csv.QUOTE_NONNUMERIC)
                writer.writeheader()
                for receipt in receipts:
                    receipt = receipt.__dict__
                    to_write = {"item_id": receipt["item_id"],
                                "date_time": receipt["date_time"],
                                "is_returned": receipt["is_returned"],
                                "comment": receipt["comment"],
                                "products": [{"name": i.__dict__["name"],
                                              "price": i.__dict__["price"],
                                              "is_favorite": i.__dict__["is_favorite"],
                                              "quantity": i.__dict__["quantity"]} for i in
                                             receipt["products"]]}
                    writer.writerow(to_write)

    export_button = QPushButton('ЭКСПОРТИРОВАТЬ ЧЕКИ')
    application.ui.receiptListPage.layout().addWidget(export_button)
    export_button.clicked.connect(export)
