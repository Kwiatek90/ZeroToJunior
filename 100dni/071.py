#dzien 70
import requests
from collections import Counter
#url =  'https://example.com/plik_tekstowy.txt'
#response = requests.get(url)

#if response.status_code == 200:
#    # Odczytaj zawartość pliku, uwzględniając odpowiednie kodowanie znaków
#    text = response.content.decode('UTF-8', errors='ignore')
#    print("Pobrany tekst:")
#    print(text)
#else:
#   print(f"Błąd pobierania pliku: {response.status_code}")
    
    
    
#zadanie na dzisiaj
#Twoim zadaniem jest napisanie kodu, który:
#
#Pobierze plik https://zerotojunior.dev/cezar.txt.
#Odszyfruje go (i automatycznie wykryje, że plik jest odszyfrowany).
#Wypisze odszyfrowany tekst na ekranie.

url =  'https://zerotojunior.dev/cezar.txt'
response = requests.get(url)

small = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
large = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"
alfabet = small + large
letter_to_move = 1
word = ""
final = ''
def check_list(letter, index_letter,letter_to_move):
    index_letter += letter_to_move
    if index_letter  >= len(letter):
        index_letter = index_letter - len(letter)
        return index_letter
    return index_letter

def move_letter_and_make_word(text,letter_to_move,word):
    for letter in text:
        if letter in alfabet:
            if letter.isupper():
                index_letter = large.index(letter)
                index_letter = check_list(large, index_letter,letter_to_move)
                letter = large[index_letter]
                word += letter        
            else:
                index_letter = small.index(letter)
                index_letter = check_list(small, index_letter,letter_to_move)
                letter = small[index_letter]
                word += letter
        else:
            word += letter
    return word
if response.status_code == 200:
    while True:
        text = response.content.decode('UTF-8', errors='ignore')
        word = move_letter_and_make_word(text,letter_to_move,word)
        final = Counter(word)
        final = final.most_common(2)[1][0]
        print("here" , final)
        if final == 'e':
            print(word)
        else:
            letter_to_move += 1
            continue
        
else:
    print(f"Błąd pobierania pliku: {response.status_code}")
    