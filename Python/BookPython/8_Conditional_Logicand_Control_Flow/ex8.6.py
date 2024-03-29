#1. Write a script that repeatedly asks the user to input an integer,
#displaying a message to “try again” by catching the ValueError that
#is raised if the user did not enter an integer.
#Once the user enters an integer, the program should display
#the number back to the user and end without crashing.
try:
    num1 = int(input("Enter a integer: "))
    print(num1)
except(ValueError):
    print("Try Again!")

#2. Write a program that asks the user to input a string and an integer
#n. Then display the character at index n in the string.
#Use error handling to make sure the program doesn’t crash
#if the user does not enter an integer or the index is out of bounds.
#The program should display a different message depending on
#what error occurs
try:
    word = input("Enter a word: ")
    num2 = int(input("Enter a integer:"))
    print(word[num2])
except(ValueError):
    print("Put a integer!")
except(IndexError):
    print("Put a integer that contains length of the word")