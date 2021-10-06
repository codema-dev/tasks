from os import PathLike
from pathlib import Path
from typing import Optional

from ._compat import import_optional_dependency


def fetch_file(
    product: PathLike,
    url: str,
    dotenv_path: Optional[PathLike] = None,
    overwrite: bool = False,
):
    """Fetch files via fsspec
    
    Args:
        product (PathLike): Filepath to output
        url (str): URL to file
        dotenv_path (Optional[PathLike], optional): Filepath to .env file of
            environmental variables. Defaults to None.
        overwrite (bool, optional): Overwrite existing file. Defaults to False.
    """
    fsspec = import_optional_dependency(
        "fsspec", "fsspec is required to run fetch_file"
    )
    if dotenv_path:
        dotenv = import_optional_dependency(
            "dotenv", "python-dotenv is required to load_dotenv in fetch_file"
        )
        dotenv.load_dotenv(dotenv_path=dotenv_path)
    savepath = Path(product)
    file_exists = savepath.exists()
    if (file_exists and overwrite) or (not file_exists):
        with fsspec.open(url, "rb") as remote_file:
            with open(product, "wb") as local_file:
                remote_file_bytes = remote_file.read()
                local_file.write(remote_file_bytes)
