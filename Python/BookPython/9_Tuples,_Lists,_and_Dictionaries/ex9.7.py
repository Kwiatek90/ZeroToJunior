#Review your state capitals along with dictionaries and while loops!

#First, finish filling out the following dictionary with the remaining
#states and their associated capitals in a file called capitals.py

#capitals_dict = {
#'Alabama': 'Montgomery',
#'Alaska': 'Juneau',
#'Arizona': 'Phoenix',
#'Arkansas': 'Little Rock',
#'California': 'Sacramento',
#'Colorado': 'Denver',
#'Connecticut': 'Hartford',
#'Delaware': 'Dover',
#'Florida': 'Tallahassee',
#'Georgia': 'Atlanta',
#}

#Next, pick a random state name from the dictionary, and assign both
#the state and it’s capital to two variables. You’ll need to import the
#random module at the top of your program.

#Then display the name of the state to the user and ask them to enter
#the capital. If the user answers, incorrectly, repeatedly ask them for
#the capital name until they either enter the correct answer or type the
#word “exit”.

#If the user answers correctly, display "Correct" and end the program.

#owever, if the user exits without guessing correctly, display the correct answer and the word "Goodbye".

import random

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}


def guess_capital(library):
    state_random = random.choice(list(library))
    state = state_random
    capital= library[state_random]
    
    while True:
        guess = input(f"Enter the name of capital in state {state}: ")
        if guess == "exit":
            print("You exit the porgram, Goodbye")
            break
        elif guess == capital:
            print("You won")
            break
        else: 
            print("Try again")
            
guess_capital(capitals_dict)