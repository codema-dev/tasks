from pathlib import Path
import requests
from typing import Dict
from typing import Callable
from typing import Union

import icecream as ic
import hyperlink

from ._compat import import_optional_dependency

URL = Dict[str, Callable[[str, Union[hyperlink.URL, hyperlink.DecodedURL]], None]]

def _fetch_from_s3(savepath: Path, url: URL) -> None:

    fs = import_optional_dependency("fs", "fs is required to run fetch_s3_file")
    from fs.tools import copy_file_data

    bucket = url.host

    filename = savepath.name
    s3fs = fs.open_fs(bucket)
    with s3fs.open(filename, "rb") as remote_file:
        with open(savepath, "wb") as local_file:
            copy_file_data(remote_file, local_file)


def _fetch_from_http(savepath: Path, url: URL) -> None:
    r = requests.get(url)
    with open(savepath, "wb") as f:
        f.write(r.content)


def fetch_file(product: str, url: str, overwrite: bool = False):
    savepath = Path(product) 

    parsed_url = hyperlink.parse(url)
    _scheme_map = {
        "http": _fetch_from_http,
        "https": _fetch_from_http,
        "s3": _fetch_from_s3,
    }
    fetch = _scheme_map[parsed_url.scheme]

    file_exists = savepath.exists()
    if (file_exists and overwrite) or (not file_exists):
        ic(url, file_exists, overwrite, prefix="fetch_file downloading ->")
        fetch(savepath, parsed_url)
    else:
        ic(url, file_exists, overwrite, prefix="fetch_file skipped ->")
