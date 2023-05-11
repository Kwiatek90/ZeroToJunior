#1. Write a script that asks the user to input a number and then displays that number rounded to two decimal places. When run, your
#program should look like this:
#Enter a number: 5.432
#5.432 rounded to 2 decimal places is 5.43
num =  input("Enter a number" )
rounded = round(float(num), 2)
print(f"{num} rounded to 2 decimal places is {rounded}")


#2. Write a script that asks the user to input a number and then displays the absolute value of that number. When run, your program
#should look like this:
#Enter a number: -10
#The absolute value of -10 is 10.0
num1 = input("Enter a number: ")
absolute = abs(int(num1))
print(f"The absolute value of {num1} is {absolute}")



#3. Write a script that asks the user to input two numbers by using the
##input() function twice, then display whether or not the difference
#between those two number is an integer. When run, your program
#should look like this:
#Enter a number: 1.5
#Enter another number: .5
#The difference between 1.5 and .5 is an integer ? True!
#If the user inputs two numbers whose difference is not integral,
#the output should look like this:
#Enter a number: 1.5
#Enter another number: 1.0
#The difference between 1.5 and 1.0 is an integer? False!

num2 = input("Enter a number: ")
num3 = input("Enter another number: ")
result = (float(num2) - float(num3)).is_integer()
print(f"The diffrence beetwen {num2} and {num3} is an integer? {result}!")

