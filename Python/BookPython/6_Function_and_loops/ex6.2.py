#1. Write a function called cube() with one number parameter and returns the value of that number raised to the third power. Test the
#function by displaying the result of calling your cube() function on
#a few different numbers.
def cub(x):
    result = x ** 3
    return result

x = input("Write the number which you want to raised to the third power: ")
result_end = cub(float(x))
print(f"The result of this action is {result_end}")



#2. Write a function called greet() that takes one string parameter
#called name and displays the text "Hello <name>!", where <name> is
#replaced with the value of the name parameter
def great(name):
        print(f"Hello {name}")

name = input("What is your name? ")
great(name)