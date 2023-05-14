#In this challenge, you will write a program called invest.py that tracks
#the growing amount of an investment over time.
#An initial deposit, called the principal amount, is made. Each year,
#the amount increases by a fixed percentage, called the annual rate of
#return.
#For example, a principal amount of $100 with an annual rate of return
#of 5% increases the first year by $5. The second year, the increase is
#5% of the new amount $105, which is $5.25.
#rite a function called invest with three parameters: the principal
#amount, the annual rate of return, and the number of years to calculate. The function signature might look something like this:
#def invest(amount, rate, years):
#The function then prints out the amount of the investment, rounded
#to 2 decimal places, at the end of each year for the specified number
#of years.
#For example, calling invest(100, .05, 4) should print the following:
#year 1: $105.00
#year 2: $110.25
#year 3: $115.76
#year 4: $121.55
#To finish the program, prompt the user to enter an initial amount, an
#annual percentage rate, and a number of years. Then call invest() to
#display the calculations for the values entered by the user.

def invest(amount, rate):
    """amount - ile chce wpłacic
        rate - na jakie oprocentowanie
        years - na ile lat
    """
    
    amount = amount + (amount * rate)
    return amount
    
    
    
    
amount = float(input("How mouch amount you want to grown? "))
rate = float(input("How much rate the invest will be(example 0.05 is 5%)? "))
years = int(input("How many years will it stay on you account? "))

n = 1
while n in range(0,years + 1):
    amount = invest(amount, rate)
    print(f"year {n}: ${amount:.2f}")
    n = n + 1

