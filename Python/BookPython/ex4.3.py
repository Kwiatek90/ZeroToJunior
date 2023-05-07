#1. Write a script that converts the following strings to lowercase: "Animals", "Badger", "Honey Bee", "Honeybadger". Print each 
#lowercase string on a separate line.
print("Ex1")
print("Animals".lower())
print("Badger".lower())
print("Honey Bee".lower())
print("Honeybadger".lower())
print("-------------")

#2. Repeat Exercise 1, but convert each string to uppercase instead of
#lowercase.
print("Ex2")
print("Animals".upper())
print("Badger".upper())
print("Honey Bee".upper())
print("Honeybadger".upper())
print("-------------")

#3. Write a script that removes whitespace from the following strings:
#string1 = " Filet Mignon"
#string2 = "Brisket "
#string3 = " Cheeseburger "
#Print out the strings with the whitespace removed.
print("Ex3")
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())
print("-------------")


#4. Write a script that prints out the result of .startswith("be") on each
#of the following strings:
#string1 = "Becomes"
#string2 = "becomes"
#string3 = "BEAR"
#string4 = " bEautiful"
print("Ex4")
string11 = "Becomes"
string22 = "becomes"
string33 = "BEAR"
string44 = " bEautiful"
print(string11.startswith("be"))
print(string22.startswith("be"))
print(string33.startswith("be"))
print(string44.startswith("be"))
print("-------------")

#5. Using the same four strings from Exercise 4, write a script that
#uses string methods to alter each string so that .startswith("be")
#returns True for all of them
print("Ex5")
print(string11.lower().startswith("be"))
print(string22.startswith("be"))
print(string33.lower().startswith("be"))
print(string44.lower().lstrip().startswith("be"))
print("-------------")