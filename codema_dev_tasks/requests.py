from pathlib import Path
import requests
from typing import Dict
from typing import Callable
from typing import Union

import hyperlink

from ._compat import import_optional_dependency

URL = Dict[str, Callable[[str, Union[hyperlink.URL, hyperlink.DecodedURL]], None]]


def _fetch_from_s3(product: str, url: URL) -> None:

    fs = import_optional_dependency("fs", "fs is required to run fetch_s3_file")
    from fs.tools import copy_file_data

    bucket = url.host

    filepath = Path(product)
    filename = filepath.name
    if not filepath.exists():
        s3fs = fs.open_fs(bucket)
        with s3fs.open(filename, "rb") as remote_file:
            with open(filepath, "wb") as local_file:
                copy_file_data(remote_file, local_file)


def _fetch_from_http(product: str, url: URL) -> None:
    filepath = Path(product)
    r = requests.get(url)
    with open(filepath, "wb") as f:
        f.write(r.content)


def fetch_file(product: str, url: str):
    parsed_url = hyperlink.parse(url)
    _scheme_map = {
        "http": _fetch_from_http,
        "https": _fetch_from_http,
        "s3": _fetch_from_s3,
    }
    fetch = _scheme_map[parsed_url.scheme]
    fetch(product, parsed_url)
