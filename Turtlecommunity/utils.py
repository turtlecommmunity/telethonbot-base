import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"Turtlecommunity/plugins/{plugin_name}.py")
    name = "Turtlecommunity.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Turtlecommunity.plugins." + plugin_name] = load
    print("Imported These Plugins--> " + plugin_name)
