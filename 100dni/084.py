#dzien 84

import math

number1 = 3.14159
number2 =  42

text = "Liczba pi to {:.2f}, a odpowiedz na pytanie o życie, wszechświat i całą resztę to {}"

print(text.format(number1, number2))

#zadanie na dzisiaj

def circle_field(r):
    r = float(r)
    square = math.pi * r**2
    print(f"Pole koła wynosi {square:.2f} cm ")

r = input("Podaj promień koła w cm: ")


circle_field(r)