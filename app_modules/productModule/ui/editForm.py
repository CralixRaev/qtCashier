class EditForm()

def __init__(self, *args):
    super().__init__()
    self.initUI(args)


def initUI(self, args):
    self.setGeometry(300, 300, 300, 300)
    self.setWindowTitle('Вторая форма')
    self.lbl = QLabel(args[-1], self)
    self.lbl.adjustSize()