#dzień 22

x = 5
print(x > 3 and x < 10)
print(not(x > 3 and x < 10))

#Zadanie
#Napisz kod, który pyta użytkownika o wiek i sprawdza, czy jest on 
#pełnoletni. Jeśli tak, to program powinien wyświetlić 
#"Jesteś pełnoletni!", w przeciwnym razie "Nie jesteś jeszcze pełnoletni.". 
#(Pamiętaj, żeby wiek pobierać jako liczbę)

wiek = int(input("Podaj swój wiek: \n"))

if wiek >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni :(")

#Zadanie dodatkowe
#Napisz kod, który pyta użytkownika o ocenę z testu (od 1 do 6) i 
#sprawdza, czy jest ona powyżej lub równa 4. Jeśli tak, to program
#powinien wyświetlić "Gratulacje, zdałeś!", w przeciwnym razie
#Niestety, nie zdałeś.". (Pamiętaj, żeby ocenę pobierać jako liczbę)

ocena = int(input("Podaj swoją ocene z testu (od 1 do 6)"))

if ocena >= 4:
    print("Gratulacje zdałeś!")
else:
    print("Niestety nie zdałeś :(")