from pathlib import Path
import shutil
path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "l12.3"

new_dir = path / "new_directory"

#new_dir.mkdir()

nested_dir =  new_dir / "folder_a" / "folder_b"

#nested_dir.mkdir(parents=True)

file_path = new_dir / "file1.txt"

#file_path.touch()

file_path = new_dir / "folder_c" / "file2.txt"

#file_path.touch()

#for path in new_dir.glob("*.txt"):
#    print(path)

paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png"

]

#for path in paths:
#    path.touch()

#print(list(new_dir.glob("**/*.txt")))
#print(list(new_dir.rglob("*.py")))

source = new_dir / "file1.txt"
destination = new_dir / "folder_a" / "file1.txt"

#source.replace(destination)

file_path = new_dir / "program1.py"
#file_path.unlink()

folder_C = new_dir / "folder_c"

#for path in folder_C.iterdir():
#    path.unlink()
    
#folder_C.rmdir()

folder_a =  new_dir / "folder_a"
shutil.rmtree(folder_a)