from pathlib import Path

path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "l12.5"
hello = path / "hello.txt"

#hello.touch()

lines_of_text = [
    "Hello from Line 1\n",
    "Hello from Line 2\n",
    "Hello from Line 3 \n",
]

with open(hello, mode="r", encoding="utf-8") as file:
    #file.writelines(lines_of_text)
    text = file.read()
    print(text)