from pathlib import Path
import requests
from typing import Dict
from typing import Callable
from typing import Union

import hyperlink

from ._compat import import_optional_dependency

URL = Dict[str, Callable[[str, Union[hyperlink.URL, hyperlink.DecodedURL]], None]]


def _fetch_from_s3(savepath: Path, url: URL) -> None:

    fs = import_optional_dependency("fs", "fs-s3fs is required to run _fetch_from_s3")
    from fs.tools import copy_file_data
    from botocore.exceptions import NoCredentialsError

    bucket_name = url.host
    bucket_link = "s3://" + bucket_name
    s3fs = fs.open_fs(bucket_link)
    filename = savepath.name
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
        fetch(savepath, parsed_url)
