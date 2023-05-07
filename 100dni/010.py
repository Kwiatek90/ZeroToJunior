#Dzień 10
nazwaBloga = "Zero To Junior"

print(nazwaBloga.upper())
print(nazwaBloga.lower())
print(nazwaBloga.startswith("Junior")) # sprawdza czy zmienna zaczyna sie od wyrazu "Junior" i zwraca true lub false
print(nazwaBloga.endswith("Junior"))
print(nazwaBloga.count("o"))

#Zadanie dodatkowe - test powinien zwraca wartość True
print(nazwaBloga.startswith("Zero"))

#Zadanie Ekstra dodatkowe
dlugiCiagZnakow = "Nauka Python jest super"
d = len(dlugiCiagZnakow)
l = 6

cuting = dlugiCiagZnakow[l:d]
print(cuting)