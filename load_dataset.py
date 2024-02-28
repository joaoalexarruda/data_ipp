from pathlib import Path
import tarfile
import urllib.request
import pandas as pd


def load_dataset(data_file: str, extension: str = ".tar.xz"):
    """Download and extract a a file from a URL, and load a CSV file into a DataFrame.

    Args:
        data_file (str): name of the CSV file
        extension (str, optional): extension of the compressed file. Defaults to ".tar.xz".

    Returns:
        _type_: pandas.DataFrame
    """
    tarball_path = Path(f"datasets/{data_file + extension}")
    data_url = "https://github.com/joaoalexarruda/data_ipp/raw/main/" + data_file + extension
    if not tarball_path.is_file():
        Path("datasets").mkdir(exist_ok=True, parents=True)
        urllib.request.urlretrieve(data_url, tarball_path)
        with tarfile.open(tarball_path) as tar:
            tar.extractall(path="datasets")
    return pd.read_csv(f"datasets/{data_file}/{data_file}.csv")