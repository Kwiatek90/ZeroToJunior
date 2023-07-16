import glob
import os
import shutil
file_patern = "*"
files = glob.glob(file_patern)

print("Znaleziono pliki w tym folderze:")
for file in files:
    print(file)
    file_basename, file_extension = os.path.splitext(file)
    if not os.path.exists(file_extension):
        os.mkdir(file_extension)
    else:
        print(f"Folder {file_extension} już istnieje")
    source = file
    destination = file_extension
    
    shutil.move(source, destination)
    

    