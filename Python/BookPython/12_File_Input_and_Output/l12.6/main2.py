import csv
from pathlib import Path

path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "l12.6"
file_path = path / "employees.csv"

def process_row(row):
    row["salary"] = float(row["salary"])
    return row

#with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(process_row(row))
        
file_path = path / "people.csv"

people = [
{"name": "Veronica", "age": 29},
{"name": "Audrey", "age": 32},
{"name": "Sam", "age": 24},
]
with open(file_path, mode="w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writerows(people)
        