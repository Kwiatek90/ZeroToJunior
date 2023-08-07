from pathlib import Path

path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "ex12.3"

my_folder = path / "my_folder"


#1. Create a new directory in your home folder called my_folder/.

#my_folder.mkdir(). 

#2. Inside my_folder/ create three files:

#• file1.txt
file_path = my_folder / "file1.txt"
#file_path.touch()

#• file2.txt

file_path = my_folder / "file2.txt"
#file_path.touch()

#•image1.png

file_path = my_folder / "image1.png"
#file_path.touch()

#3. Move the file image1.png to a new directory called images/ inside of
#the my_folder/ directory.

images = my_folder / "images"
#images.mkdir()
source = my_folder / "image1.png"
destination = images / "image1.png"

#source.replace(destination)

#4. Delete the file file1.txt
file_path = my_folder / "file1.txt"
#file_path.unlink()

#5. Delete the my_folder/ directory.
import shutil

shutil.rmtree(my_folder)