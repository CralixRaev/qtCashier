from PyQt5.QtCore import QStringListModel

from .pluginSystem import PluginSystem
from ..ABC.uiLogic import ABCUiLogic


class UiLogic(ABCUiLogic):
    def __init__(self, app):
        super().__init__(app)
        self.plugin_system = PluginSystem(self.app)

        self.init_pluginsystem()

    def init_pluginsystem(self):
        """
        ИНИЦИАЛИЗАЦИЯ ПЛАГИН СИСТЕМЫ
        """
        self.plugin_system.discover_plugins()

    def init_ui(self):
        """
        ИНИЦИАЛИЗАЦИЯ UI
        """
        # Создаём модельку
        self.model = QStringListModel([i[1]['name'] for i in self.plugin_system.plugins.values()])
        self.ui.settingsPluginsList.setModel(self.model)
        # Добавляем страницу с плагинами в stacked widget
        self.ui.mainStackedWidget.addWidget(self.ui.settingsPluginsPage)

        # Создаём функции
        def pluginlist_open():
            nonlocal self
            self.ui.productsDock.hide()
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.settingsPluginsPage)

        def pluginlist_close():
            nonlocal self
            self.ui.mainStackedWidget.setCurrentWidget(self.ui.sellPage)
            self.ui.productsDock.show()

        def pluginlist_select(index):
            nonlocal self
            # FIXME: Переделать отображение информации о плагине
            data = list(self.plugin_system.plugins.values())[index.row()][1].items()
            item = ""
            for i in data:
                item += f'{i[0]} - {i[1]}\n'
            self.ui.settingsPluginsInfo.setText(item)

        def pluginlist_reload():
            nonlocal self
            index = self.ui.settingsPluginsList.selectedIndexes()[0].row()
            self.plugin_system.reload_plugin(list(self.plugin_system.plugins.values())[index][0])

        # Соединяем сигналы с функциями
        connects = ((self.ui.settingsPlugins.triggered, pluginlist_open),
                    (self.ui.settingsPluginsListBack.clicked, pluginlist_close),
                    (self.ui.settingsPluginsList.clicked, pluginlist_select),
                    (self.ui.settingsPluginsListReload.clicked, pluginlist_reload))

        for action, function in connects:
            action.connect(function)

    def get_opened_classes(self):
        return {'pluginSystem': self.plugin_system}

    def load(self):
        self.init_ui()
