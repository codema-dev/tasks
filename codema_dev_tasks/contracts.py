from pathlib import Path

def check_file_exists(product: str, filepath: str):
    filepath = Path(filepath)
    dirpath = filepath.parent
    filename = filepath.name
    assert filepath.exists(), f"Please upload {filename} to {dirpath}"