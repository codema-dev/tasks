from pathlib import Path
import requests
from typing import Any

from _compat import import_optional_dependency


def fetch_file(product: str, url: str):
    filepath = Path(product)
    r = requests.get(url)
    with open(filepath, "wb") as f:
        f.write(r.content)
