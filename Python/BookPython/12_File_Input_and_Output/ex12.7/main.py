#In the Chapter 12 Practice Files folder, there is a CSV file called
#scores.csv containing data about game players and their scores. The
#first few lines of the file look like this:
#name, score
#LLCoolDave,23
#LLCoolDave,27
#red,12
#LLCoolDave,26
#tom123,26
#Write a script that reads the data from this CSV file and creates a new
#file called high_scores.csv where each row contains the player name
#and their highest score.
#The output CSV file should look like this:
#name,high_score
#LLCoolDave,27
#red,12
#tom123,26
#O_O,7
#Misha46,25
#Empiro,23
#MaxxT,25
#L33tH4x,42
#johnsmith,30


from pathlib import Path
import csv

path = Path.cwd() / "Python" / "BookPython" / "12_File_Input_and_Output" / "ex12.7"
file_path = path / "scores.csv"
file_path_save = path / "high_scores.csv"

    
with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    result = sorted(reader, key=lambda d: int(d['score']), reverse=True)

    writer = csv.DictWriter(open(file_path_save, 'w', newline=''), reader.fieldnames,)
    writer.writeheader()
    writer.writerows(result)

