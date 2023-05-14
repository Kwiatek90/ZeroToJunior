#Write a script called temperature.py that defines two functions:
#1. convert_cel_to_far() which takes one float parameter representing
#degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula:
#F = C * 9/5 + 32
#2. convert_far_to_cel() which take one float parameter representing
#degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula:
#C = (F - 32) * 5/9
#The script should first prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature converted to Celsius.
#Then prompt the user to enter a temperature in degrees Celsius and
#display the temperature converted to Fahrenheit.
#All converted temperatures should be rounded to 2 decimal places.
#Here’s a sample run of the program:
#Enter a temperature in degrees F: 72
#72 degrees F = 22.22 degrees C
#Enter a temperature in degrees C: 37
#37 degrees C = 98.60 degrees F

def convert_cel_to_far(C):
    C = float(C)
    F = C * 9/5 + 32
    return F

def convert_far_to_cel(F):
    F = float(F)
    C = (F - 32) * 5/9
    return C

F = input("Enter a temperature in deegres F: ")
result1 = convert_far_to_cel(F)
print(f"{F} degrees F = {result1:.2f} degress C")

C = input("Enter a temperature in deegres C: ")
result2 = convert_cel_to_far(C)
print(F"{C} degress C = {result2:.2f} degress F")
    