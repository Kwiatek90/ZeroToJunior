#1. Write the following text to file called starships.txt in your home
#directory:
#Discovery
#Enterprise
#Defiant
#Voyager
#Each word should be on a separate line.
from pathlib import Path

path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "ex12.5"
starships_file = path / "starships.txt"

#starships_file.touch()

starships = ["Discovery\n", "Enterprise\n", "Defiant\n", "Voyager\n"]

#with open(starships_file, mode="w", encoding="utf-8") as f:
#    f.writelines(starships)



#2. Read the file starhips.txt you created in Exercise 1 and print each
#line of text in the file. The output should not have extra blank lines
#between each word.
with open(starships_file, mode="r", encoding="utf-8") as f:
    print(f.read())
    
#3. Read the file startships.txt and print the names of the starships
#that start with the letter D.
with open(starships_file, mode="r", encoding="utf-8") as f:
    for line in f.readlines():
        if line.startswith("D"):
            print(line, end="")