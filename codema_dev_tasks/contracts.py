from pathlib import Path

def check_file_exists(product: str, filepath: str, dirpath: str):
    filepath = Path(filepath)
    dirpath = Path(filepath)
    filename = filepath.name
    assert filepath.exists(), f"Please upload {filename} to {dirpath}"