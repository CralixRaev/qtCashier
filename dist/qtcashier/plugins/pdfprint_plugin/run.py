import os
from datetime import datetime

from docxtpl import DocxTemplate


def on_reload(application):
    run(application)


def run(application):
    signals = application.modules["receiptModule"].signals

    def print_receipt(receipt):
        tpl = DocxTemplate('./plugins/pdfprint_plugin/templates/receipt.docx')
        context = {'receipt_id': receipt['item_id'],
                   'date_time': datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                   'positions': receipt['products']}
        tpl.render(context)
        tpl.save('./plugins/pdfprint_plugin/templates/temp_print.docx')

    def print_return(receipt):
        tpl = DocxTemplate('./plugins/pdfprint_plugin/templates/return.docx')
        receipt = application.modules["receiptModule"].receipt_system.get_by_id
        context = {'receipt_id': receipt['item_id'],
                   'date_time': datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                   'positions': receipt['products']}
        tpl.render(context)
        tpl.save('./plugins/pdfprint_plugin/templates/temp_print.docx')


    signals.on_receipt.connect(print_receipt)
    signals.on_return.connect(print_return)
