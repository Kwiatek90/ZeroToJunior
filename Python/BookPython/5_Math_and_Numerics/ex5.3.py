#Write a script called exponent.py that receives two numbers from the
#user and displays the first number raised to the power of the second
#number.
#A sample run of the program should look like this (with example input
#that has been provided by the user included below):
#Enter a base: 1.2
#Enter an exponent: 3
#1.2 to the power of 3 = 1.7279999999999998
#Keep the following in mind:
#1. Before you can do anything with the user’s input, you will have to
#assign both calls to input() to new variables.
#2. The input() function returns a string, so you’ll need to convert the
#user’s input into numbers in order to do arithmetic.
#3. You can use an f-string to print the result.
#4. You can assume that the user will enter actual numbers as input.

num1 = input("Enter a base: ")
num2 = input("Enter an exponent: ")
result = float(num1) ** float(num2)

print(f"{num1} to the power of {num2} = {result}")