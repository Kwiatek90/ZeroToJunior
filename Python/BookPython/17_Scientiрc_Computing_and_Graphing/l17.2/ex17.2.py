
#2. It is a well-documented fact that the number of pirates in the world
#is correlated with a rise in global temperatures. Write a script
#pirates.py that visually examines this relationship:
#• Read in the file pirates.csv from the Chapter 17 practice files
#folder.
#• Create a line graph of the average world temperature in degrees
#Celsius as a function of the number of pirates in the world—
#that is, graph Pirates along the x-axis and Temperature along
#the y-axis.
#• Add a graph title and label your graph’s axes.
#• Save the resulting graph out as a PNG image file.
#• Bonus: Label each point on the graph with the appropriate
#Year. You should do this programmatically by looping through
#the actual data points rather than specifying the individual position of each annotation.

from matplotlib import pyplot as plt
import csv

csv_file = r"D:\Programowanie\ZeroToJunior\Python\BookPython\17_Scientiрc_Computing_and_Graphing\l17.2\pirates.csv"


years = []
temperatures = []
pirates = []

with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    
    for year, temperature, pirate in reader:
        years.append(year)
        temperatures.append(temperature)
        pirates.append(pirate)
        


plt.xlabel("Prates")
plt.ylabel("Avarage temperature")
plt.title("Prates by the avrages temperature")
plt.plot(pirates, temperatures)
plt.show()