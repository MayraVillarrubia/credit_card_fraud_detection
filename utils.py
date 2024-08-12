import zipfile

def extract_files(zipFile_name: str) -> None:
    with zipfile.ZipFile(zipFile_name, 'r') as file:
        file.extractall()


