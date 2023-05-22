
#1. Write a function called roll() that uses the randint() function to
#simulate rolling a fair die by returning a random integer between
#1 and 6.
import random
def roll():
    num1 =  random.randint(1, 6)
    print(num1)
    
roll()

#2. Write a script that simulates 10,000 rolls of a fair die and displays
#the average number rolled
    
suma = 0 
       
for i in range(10_000):
    num2 = random.randint(1,100)
    suma += num2
    
average = suma /  10_000
print(f"Avarege of this roll is {average}")
    
    
