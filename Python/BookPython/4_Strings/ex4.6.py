#1. Create a string containing an integer, then convert that string into
#an actual integer object using int(). Test that your new object is
#a number by multiplying it by another number and displaying the
#result.

x = "10"
y = int(x)
result = y * 2
print(result)


#2. Repeat the previous exercise, but use a floating-point number and
#float().


xx = "10"
yy = float(x)
result1 = yy * 2
print(result1)


#3. Create a string object and an integer object, then display them sideby-side with a single print statement by using the str() function.
strObj = "Mam tyle lat: "
intObj = 20

print(strObj + str(intObj))


#4. Write a script that gets two numbers from the user using the
#input() function twice, multiplies the numbers together, and
#displays the result. If the user enters 2 and 4, your program should
#print the following text:
#The product of 2 and 4 is 8.0.

firstNum = input("Write first number: ")
secondNum = input("Write second number: ")
result2 =  int(firstNum) * int(secondNum)
print("The product of " + firstNum + " and " + secondNum + " is " + str(float(result2)))
