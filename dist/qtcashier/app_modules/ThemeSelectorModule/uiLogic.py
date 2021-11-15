from PyQt5 import QtGui
from PyQt5.QtWidgets import QActionGroup, QAction

from ..ABC.uiLogic import ABCUiLogic
from enum import Enum


class UiLogic(ABCUiLogic):
    def __init__(self, app):
        super().__init__(app)
        self.change_theme()
        self.init_ui()

    def change_theme(self):
        self.app.apply_stylesheet(self.app, theme=f'{self.config["current_theme"]}_blue.xml',
                                  invert_secondary=False if self.config['current_theme'] == 'dark' else True,
                                  extra={'font-family': 'Roboto'})

    def init_ui(self):
        self.ui.themeGroup = QActionGroup(self.app)
        self.ui.themeGroup.addAction(self.ui.darkTheme)
        self.ui.themeGroup.addAction(self.ui.lightTheme)

        if self.config['current_theme'] == 'dark':
            self.ui.darkTheme.setChecked(True)
        else:
            self.ui.lightTheme.setChecked(True)

        def change_theme(action: QAction):
            if action.text() == 'Тёмная':
                self.config['current_theme'] = 'dark'
            elif action.text() == 'Светлая':
                self.config['current_theme'] = 'light'
            self.change_theme()

        connects = ((self.ui.themeGroup.triggered, change_theme),)

        for action, function in connects:
            action.connect(function)

    def load(self):
        pass

    def on_app_close(self):
        pass