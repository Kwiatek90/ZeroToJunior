#dzień 20
owoce = ["jablko","banan", "wisnia"]
owoce[0] = "gruszka"
print(owoce)


#Zadanie
#1 Utwórz listę z pięcioma swoimi ulubionymi owocami.
#2 Wypisz na ekranie drugi owoc z listy.
#3 Zmień trzeci owoc na coś innego.
#4 Wypisz na ekranie pierwszy i trzeci owoc z listy.

owoce1 =["jablko", "banan", "mango", "antonowka", "kokos"]
owoce1[2] = "melon"
print(owoce[1])
print(owoce1[0], owoce1[2])


#Zadanie dodatkowe
#Stwórz listę przechowującą nazwy Twoich ulubionych napojów. 
# Następnie, przy pomocy komendy if (poznanej niedawno), 
# wyświetl na ekranie "Ta nazwa jest krótka",
#jeśli nazwa 1 elementu listy jest krótsza od 10 znaków, 
# lub "Ta nazwa jest długa", jeśli jest dłuższa niż 10 znaków.

#Dla przypomnienia, określenie długości tekstu było w lekcji 9.

napoje = ["Cola", "Oranzada", "Coca cola zero", "Sprite", "Fanta"]

for napoj in napoje:
    if len(napoj) > 10:
        print(f"{napoj} : Ta nazwa jest długa ")
    else:
        print(f"{napoj} : Ta nazwa jest krótka ")
    
