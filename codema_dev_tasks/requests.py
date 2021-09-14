from pathlib import Path
import requests
from typing import Dict
from typing import Callable
from typing import Tuple
from typing import Union

import fsspec


def fetch_file(product: str, url: str, overwrite: bool = False):
    savepath = Path(product)
    file_exists = savepath.exists()
    if (file_exists and overwrite) or (not file_exists):
        with fsspec.open(url, "rb") as remote_file:
            with open(product, "wb") as local_file:
                remote_file_bytes = remote_file.read()
                local_file.write(remote_file_bytes)
