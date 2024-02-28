# Datasets for assignments at Instituto Politécnico de Portalegre

This repository contains datasets for assignments at Instituto Politécnico de Portalegre. The goal is to automate the process of downloading datasets.

## Uploading a new dataset

It's important that the dataset is compressed in a `.tar.xz` file for its good compression rate. The file should contain a folder with the same name as the file, and the folder should contain the dataset in a `.csv` file.

## How to use

To download, extract and load a dataset, you can use the following code:

```python
import pandas as pd
import urllib.request
import tarfile
from pathlib import Path


def load_dataset(data_url: str, data_file: str, extension: str = ".tar.xz"):
    """Download and extract a a file from a URL, and load a CSV file into a DataFrame.

    Args:
        data_url (str): url to the raw data
        data_file (str): name of the CSV file
        extension (str, optional): extension of the compressed file. Defaults to ".tar.xz".

    Returns:
        _type_: pandas.DataFrame
    """
    tarball_path = Path(f"datasets/{data_file + extension}")
    if not tarball_path.is_file():
        Path("datasets").mkdir(exist_ok=True, parents=True)
        urllib.request.urlretrieve(data_url, tarball_path)
        with tarfile.open(tarball_path) as tar:
            tar.extractall(path="datasets")
    return pd.read_csv(f"datasets/{data_file}/{data_file}.csv")
