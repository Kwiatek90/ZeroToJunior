#dzień 72
import os

filename = r"D:\Programowanie\ZeroToJunior\100dni\Pliki_do_zadan\072.txt"
if os.path.exists(filename):
    print(f"Plik {filename} istnieje")
else:
    print(f"Plik {filename} nie istnieje")
    
#kopiowanie plików
import shutil

source = r"D:\Programowanie\ZeroToJunior\100dni\Pliki_do_zadan\072.txt"
destination = r"D:\Programowanie\ZeroToJunior\100dni\Pliki_do_zadan\072_copy.txt"

shutil.copy(source, destination)
print(f"Skopiowane {source} do {destination}")

#tworzenie folderów

folder_name = "nowy_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Utworzonoe folder {folder_name}")
else:
    print(f"Folder {folder_name} już istnieje")
    
#wyszukiwanie plików

import glob

file_patern = ".py"
files = glob.glob(file_patern)

print("Znaleziono pliki:")
for file in files:
    print(file)
    

import os

filename = "przykladowy_plik.txt"
file_basename, file_extension = os.path.splitext(filename)

print(f"Nazwa pliku bez rozszerzenia: {file_basename}")
print(f"Rozszerzenie pliku: {file_extension}")