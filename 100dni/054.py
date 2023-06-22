#dzien 54

#Dzisiaj BARDZO proste :)

#Substring, jest jedną z najczęściej używanych funkcji podczas pracy ze stringami.

#Twoim zadaniem jest stworzenie WŁASNEJ funkcji substring. Nie używaj systemowej, tylko napisz ją od zera (nie używaj slice(), ani [x:y])

#A jak już zaimplementujesz, wykonaj przy jej pomocy następujące zadania testowe -

#Z "Zero To Junior" wyciągnij 4 pierwsze znaki
#Z "Zero To Junior" wyciągnij 5 ostatnich znaków
#Znajdź w "Zero To Junior" ciąg "To" i pobierz wszystkie znaki od litery T do końca
#Wyciągnij z "Zero To Junior" znaki od 3 do 8

def iteration_substring(value, x, y):
    i = 0
    letters = []
    for letter in value:
        if i >= x and i<= y:
            letters += letter
        i += 1
    result = "".join(letters)
    print(result)
    
def substring(value, x, y):
    length_value = len(value)
    if y == ":":
        i = 0
        letters = []
        for letter in value:
            if i >= x:
                letters += letter
            i += 1
        result = "".join(letters)
        print(result)
    elif x < 0:
        x = length_value - abs(x)
        y = length_value - abs(y)
        iteration_substring(value, x, y)
    else:
        iteration_substring(value, x, y)
    
def string_find_and_print(value_to_find, value):
    index = value.find(value_to_find)
    y = ":"
    substring(value, index, y)
    
    
    
text = "Zero To junior"
string_to_find = "To"

#Z "Zero To Junior" wyciągnij 4 pierwsze znaki
substring(text, 0, 3)

#Z "Zero To Junior" wyciągnij 5 ostatnich znaków
substring(text, -3, -1)

##Znajdź w "Zero To Junior" ciąg "To" i pobierz wszystkie znaki od litery T do końca
string_find_and_print(string_to_find, text)

#Wyciągnij z "Zero To Junior" znaki od 3 do 8
substring(text, 3, 8)


