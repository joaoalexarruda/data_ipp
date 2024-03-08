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
