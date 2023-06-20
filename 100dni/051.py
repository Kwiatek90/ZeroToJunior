#dzień 51

#zadanie
#Uwaga: do wykonania tego zadania, przydadzą Ci się metody Stringa: join() oraz split()

#Napisz aplikację, która:

#pobierze wiele linii, wpisanego na ekranie tekstu
#policzy wszystkie wyrazy i wypisze ich ilość na ekranie


def calc_words(text):
    text = text.split()
    length = 0
    for word in text:
        length += 1
    return length    
    

text = input("Enter some text: ")

print(calc_words(text))
