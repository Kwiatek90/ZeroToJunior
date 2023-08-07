import csv
from pathlib import Path

path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "l12.6"
file_path = path / "temperatures.csv"

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
    ]

with open(file_path, mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(daily_temperatures)

