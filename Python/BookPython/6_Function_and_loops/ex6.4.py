#1. Write a for loop that prints out the integers 2 through 10, each on
#a new line, by using the range() function.
for i in range(2, 11):
    print(i)

print("-----------------")


#2. Use a while loop that prints out the integers 2 through 10 (Hint:
#You’ll need to create a new integer first.)
n = 2
while n <= 10:
    print(n)
    n = n + 1

#3. Write a function called doubles() that takes one number as its input
#and doubles that number. Then use the doubles() function in a
#loop to double the number 2 three times, displaying each result on
#a separate line. Here is some sample output:
#4
#8
#16

def doubles(x):
    return x * 2

x = int(input("Write the number you want to double: "))

n = 0
while n < 3:
    x = doubles(x)
    print(x)
    n = n + 1
