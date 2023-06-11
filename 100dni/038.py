#dzień 38
fruits = ("apple", "banana", "cheryy")

print(fruits[1])


x = 5
y = 10

(y, x) = (x, y)

print(f" x = {x}")
print(f" y = {y}")


#Zadanie
print("ZADANIE")
#Zsumuj liczby parzyste (i oczywiście wydrukuj rezultat)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result = 0 

for num in numbers:
    if num % 2 == 0:
        result += num
        
print(f"Suma liczby parzystych wynosi: {result}")