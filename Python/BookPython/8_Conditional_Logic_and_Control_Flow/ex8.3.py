#1. Write a script that prompts the user to enter a word using the
#input() function, stores that input in a variable, and then displays
#whether the length of that string is less than 5 characters, greater
#than 5 characters, or equal to 5 characters by using a set of if, elif
#and else statements

word = input("Enter a word: ")

if len(word) > 5:
    print("This word length is greater than 5 characters ")
elif len(word) == 5:
    print("This word length is equal n 5 characters ")
else:   
    print("This word length is less than 5 characters ")
