#1. Create a new Path object to a file called my_file.txt in a folder called
#my_folder/ in your computer’s home directory. Assign this Path object to the variable name file_path.
import pathlib

file_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\12_File_Input_and_Output\ex12.2\my_folder\my_file.txt"
path =  pathlib.Path(file_path)

#2. Check whether or not the path assigned to file_path exists.
print(path.exists())

#3. Print the name of the path assigned to file_path. The output
#should be my_file.txt.
print(path.name)

#4. Print the name of the parent directory of the path assigned to
#file_path. The output should be my_folder.
print(path.parent)