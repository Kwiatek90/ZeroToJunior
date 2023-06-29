#dzien 61
#Napisz program, który losuje 5 liczb całkowitych z zakresu od 1 do 10, 
#a następnie prosi użytkownika o odgadnięcie co najmniej jednej z tych liczb. Program powinien odpowiedzieć, czy podana przez użytkownika liczba była jedną z wylosowanych lub nie

import random

random_list = random.sample(range(1,10), k=5)

type_random = int(input("Enter a value form 1 to 10: "))

if type_random in random_list:
    print("you Won")
else:
    print("You lose")

