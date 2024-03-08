# Datasets for assignments at Instituto Politécnico de Portalegre

This repository contains datasets for assignments at Instituto Politécnico de Portalegre. The goal is to automate the process of downloading datasets.

## Uploading a new dataset

It's important that the dataset is compressed in a `.tar.xz` file for its good compression rate. The file should contain a folder with the same name as the file, and the folder should contain the dataset in a `.csv` file.

## How to use

To download and extract a dataset, you can use the following code:

```python
from pathlib import Path
import tarfile
import urllib.request


def download_dataset(data_file: str, extension: str = ".tar.xz"):
    """Downloads a dataset from a github repository and extracts it to the datasets folder. 
    If the dataset is already downloaded, it will not be downloaded again.

    Args:
        data_file (str): Name of the dataset file.
        extension (str, optional): extension of the compressed file. Defaults to ".tar.xz".

    Returns:
        str: Path to the dataset file.
    """
    tarball_path = Path(f"datasets/{data_file + extension}")
    data_url = "https://github.com/joaoalexarruda/data_ipp/raw/main/" + data_file + extension

    if not tarball_path.is_file():
        Path("datasets").mkdir(exist_ok=True, parents=True)
        urllib.request.urlretrieve(data_url, tarball_path)
        with tarfile.open(tarball_path) as tar:
            tar.extractall(path="datasets")
    return f"datasets/{data_file}/{data_file}.csv"
