from pathlib import Path
import requests
from typing import Dict
from typing import Callable
from typing import Tuple
from typing import Union

from ._compat import import_optional_dependency

def fetch_file(product: str, url: str, overwrite: bool = False):
    fsspec = import_optional_dependency("fsspec", "python-dotenv is required to run fetch_file")
    savepath = Path(product)
    file_exists = savepath.exists()
    if (file_exists and overwrite) or (not file_exists):
        with fsspec.open(url, "rb") as remote_file:
            with open(product, "wb") as local_file:
                remote_file_bytes = remote_file.read()
                local_file.write(remote_file_bytes)
