#1. Write a script that writes the following list of lists to a file called
#numbers.csv in your home directory:
#numbers = [
#[1, 2, 3, 4, 5],
#[6, 7, 8, 9, 10],
#[11, 12, 13, 14, 15],
#]
from pathlib import Path
import csv
path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "ex12.6"
file_path = path / "numbers.csv"

numbers = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
]

with open(file_path, mode="w", encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(numbers)
    
#2. Write a script that reads the numbers in the numbers.csv file from
#Exercise 1 into a list of lists of integers called numbers. Print the list
#of lists. Your output should like the following:
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

numbers = []
with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(value) for value in row]
        numbers.append(int_row)
    print(numbers)
        

#3. Write a script that writes the following list of dictionaries to a file
#called favorite_colors.csv in your home directory:
#favorite_colors = [
#{"name": "Joe", "favorite_color": "blue"},
#{"name": "Anne", "favorite_color": "green"},
#{"name": "Bailey", "favorite_color": "red"},
#]
#The output CSV file should have the following format:
#name,favorite color
#Joe,blue
#Anne,green
#Bailey,red

favorite_colors = [
{"name": "Joe", "favorite_color": "blue"},
{"name": "Anne", "favorite_color": "green"},
{"name": "Bailey", "favorite_color": "red"},
]

file_path = path / "favorite_colors.csv"

with open(file_path, mode="w", encoding="utf-8", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "favorite_color"])
    writer.writeheader()
    writer.writerows(favorite_colors)
#4. Write a script that reads the data from the favorite_colors.csv file
#from Exercise 3 into a list of dictionaries called favorite_colors.
#Print the list of dictionaries. The output should look something
#like this:
#[{"name": "Joe", "favorite_color": "blue"},
#{"name": "Anne", "favorite_color": "green"},
#{"name": "Bailey", "favorite_color": "red"}]
with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

