#dzien 87

#Listy

# Zamiast pętli for, możesz użyć list comprehension, aby uzyskać kwadraty liczb od 1 do 10
squares = [x ** 2 for x in range(1, 11)]
print(squares) # Wynik: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Sety

# Utwórz zbiór zawierający długości słów z podanej listy
words = ["apple", "banana", "cherry", "kiwi"]
word_lengths = {len(word) for word in words}
print(word_lengths) # Wynik: {4, 5, 6}

#Dictionary 


# Utwórz słownik, gdzie kluczem jest słowo, a wartością jego długość
word_length_dict = {word: len(word) for word in words}
print(word_length_dict) # Wynik: {'apple': 5, 'banana': 6, 'cherry': 6, 'kiwi': 4}


#Zadanie na dzisiaj
print("Lista uczniów: \n")

students = [("Ania", 3.5), ("Kamil", 4.5), ("Ola", 4.0), ("Piotr", 5.0), ("Ewa", 3.0)]

students_above_four = [item for item in students if item[1] >= 4]

students_dict = {name: rate for name, rate in students_above_four}

print(students_above_four)
print(students_dict)
