class ABCUiLogic:
    def __init__(self, app):
        self.app = app
        self.ui = app.ui
        self.config = app.config

    def set_opened_classes(self, opened_classes):
        self.opened_classes = opened_classes

    def get_opened_classes(self):
        return {}