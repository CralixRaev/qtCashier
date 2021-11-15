import importlib
import os
import json
from importlib import resources


class PluginDescriptionError(Exception):
    pass


class PluginRunException(Exception):
    pass


def _check_plugin(name):
    # для начала проверим наличие необходимых полей в plugin.json
    required = ['name', 'description', 'version']
    data = json.loads(resources.read_text(f'plugins.{name}', 'plugin.json'))
    for i in required:
        if i not in data.keys():
            raise PluginDescriptionError(f'У плагина {name} нет поля {i} в plugin.json, но оно '
                                         f'необходимо')
    else:
        return data


class PluginSystem:
    def __init__(self, application):
        self.plugins = {}
        self.application = application

    def discover_plugins(self):
        # os.chdir('plugins')
        path = os.getcwd()
        for plugin in os.listdir(os.path.join(path, 'plugins')):
            if plugin == 'stubs':
                continue
            description = _check_plugin(plugin)

            try:
                self.load_plugin(plugin, description)
            except ImportError as e:
                raise ImportError(
                    f'Не получилось загрузить {plugin} - необработанное исключение: {e}')
            if description['enabled']:
                try:
                    run_func = getattr(self.plugins[plugin][0], 'run')
                except KeyError:
                    raise AttributeError(
                        f'Не получилось запустить {plugin} - у {plugin} нет run функции')

                try:
                    run_func(self.application)
                except Exception as e:
                    raise PluginRunException(
                        f'Не получилось запустить {plugin} - необработанное исключение: {e}')

    def reload_plugin(self, plugin):
        self.plugins[plugin.__name__.split('.')[1]][0] = importlib.reload(plugin)
        self.plugins[plugin.__name__.split('.')[1]][0].on_reload(self.application)

    def load_plugin(self, name, data):
        importlib.invalidate_caches()
        self.plugins[name] = [importlib.import_module(f'plugins.{name}.run'), data]
