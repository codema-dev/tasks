import os
import sys
from typing import Union

from ._compat import import_optional_dependency

if sys.version_info >= (3, 6):
    _PathLike = os.PathLike
else:
    _PathLike = str

def load_environmental_variables(dotenv_path: Union[str, _PathLike, None]):
    dotenv = import_optional_dependency("dotenv", "python-dotenv is required to run load_environmental_variables")
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=dotenv_path)