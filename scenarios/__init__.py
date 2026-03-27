import pkgutil
import importlib
from pathlib import Path

# 1. Get the path of the scenarios folder
_package_dir = Path(__file__).resolve().parent

# 2. Iterate through all files in this folder
for _, _module_name, _ in pkgutil.iter_modules([str(_package_dir)]):
    
    # 3. Import each module and add it to this package's namespace
    globals()[_module_name] = importlib.import_module(f".{_module_name}", package=__name__)
