#dzień 41

#Dzisiaj będzie trudniej :) Masz napisać kalkulator :)

#Poproś użytkownika o dwie liczby (najpierw jedną, potem drugą)
#Poproś użytkownika o działanie, jakie ma być wykonane (+,-,/,*)
#Wyświetl rezultat działania na ekranie :)
#Wróć na początek.
#Wpisanie exit powinno zakończyć działanie kalkulatora.


def kalkulator(num1, num2, dzialanie):
    if dzialanie == "+":
        return num1 + num2
    if dzialanie == "-":
        return num1 - num2
    if dzialanie == "/":
        return num1 / num2
    if dzialanie == "*":
        return num1 * num2
    

print("KALKULATOR")

cont = ""
while cont != "exit":
    num1 = int(input("Podaj pierwszą liczbę: "))
    num2 = int(input("Podaj drugą liczbę: "))
    dzialanie = input("Podaj jakie działanie ma być wykonane (+,-,/,*): ")

    result = kalkulator(num1, num2, dzialanie)
    print(f"Wynikiem {dzialanie} dwóch liczb {num1} i {num2}  jest {result}")
    
    cont = input("Jeżeli chcesz zakończyć działanie programu napisz exit: ")



