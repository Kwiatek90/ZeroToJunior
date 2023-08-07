from pathlib import Path

path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "l12.6"
file_path = path / "temperatures.csv"

with open(file_path, mode="r", encoding="utf-8") as file:
    text = file.read()
    temperatures = text.split(",")
    int_temperatures = [int(temp) for temp  in temperatures]
    print(int_temperatures)