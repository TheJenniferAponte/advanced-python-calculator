import os
import importlib
import logging

logger = logging.getLogger(__name__)

class Command:
    def execute(self, calculator, *args):
        raise NotImplementedError

def load_plugins():
    plugins = {}
    plugin_dir = os.path.dirname(__file__)
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = importlib.import_module(f"calculator.plugins.{module_name}")
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, Command) and obj != Command:
                    plugins[obj.__name__.lower()] = obj()
    logger.info(f"Loaded plugins: {list(plugins.keys())}")
    return plugins