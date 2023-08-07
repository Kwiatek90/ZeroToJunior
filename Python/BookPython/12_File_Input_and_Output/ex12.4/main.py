from pathlib import Path

path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "ex12.4"

images = path / "images"
#images.mkdir()


documents = Path.home() / "OneDrive" / "Dokumenty"


for path in documents.glob("image?.*"):
    destination = images / path.name 
    path.replace(destination)