#dzien 026
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("--Kolejna iteracja")
    print(fruit)
    if fruit == "banana":
        print("Funkcja break")
        break
        
print("Koniec programu :)")