#1. Using break, write a program that repeatedly asks the user for some
#input and only quits if the user enters "q" or "Q".

for i in range(0,100):
    char =  input("Enter a word: ")
    print("If you put'q' or 'Q' the program will end")
    if (char == "q" or char == "Q"):
        break
else:
    print(f"Your text {char}")
    i += 1

#2. Using continue, write a program that loops over the numbers 1 to
#50 and prints all numbers that are not multiples of 3.
for j in range(1, 51):
    if j % 3 == 0:
        continue
    print(j)
    