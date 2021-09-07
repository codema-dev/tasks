from pathlib import Path
import requests
from typing import Any

from _compat import import_optional_dependency


def fetch_s3_file(product: str, bucket: str) -> None:

    fs = import_optional_dependency("fs", "fs is required to run fetch_s3_file")
    from fs.tools import copy_file_data

    filepath = Path(product)
    filename = filepath.name
    if not filepath.exists():
        s3fs = fs.open_fs(bucket)
        with s3fs.open(filename, "rb") as remote_file:
            with open(filepath, "wb") as local_file:
                copy_file_data(remote_file, local_file)


def fetch_file(product: str, url: str):
    filepath = Path(product)
    r = requests.get(url)
    with open(filepath, "wb") as f:
        f.write(r.content)
