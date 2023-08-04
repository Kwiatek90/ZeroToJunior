#1. In a new project folder called package_exercises/, create a package
#called helpers with three modules: __init__.py, string.py, and
#math.py.
#In the string.py module, add a function called shout() that
#takes a single string parameter and returns a new string with all
#of the letters in uppercase.
#In the math.py module, as a function called area() that takes
#two parameters called length and width and returns their product
#length * width.

#2. In the root project folder, create a module called main.py that imports the shout() and area() functions. Use the shout() and area()
#functions to print the following output:
#THE AREA OF A 5-BY-8 RECTANGLE IS 40

from helpers.string import shout
from helpers.math import area

text = "The area of 5-by-8 rectangle is"

print(f"{shout(text)} {area(5,8)}")