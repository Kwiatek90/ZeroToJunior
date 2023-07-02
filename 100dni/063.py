
x = "Try not to forget the variables next time ;)"

try:
    print(x)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
    
    
#Dzisiaj mega proste zadanko. 
#Napisz kod, który będzie prosił o dwie liczby i będzie je dzielił. Zadbaj przy pomocy try / except, o blokadę dzielenia przez 0.

num1 = int(input("Enter first number to divide: "))
num2 = int(input("Enter second number to divide: "))

try:
    result = num1 / num2
    print(f"{num1} divide {num2} is {result}")
except:
    print("Don't divide by zero!")
