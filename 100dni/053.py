#dzien 53

#Przygotuj prosty słownik (dosłownie) polsko - angielski. 10-20 wyrazów max.

#astępnie komputer ma poprosić o wpisanie przez Ciebie zdania. 
#Po jego wprowadzeniu ma przetłumaczyć wszystkie wyrazy, które znajdzie w słowniku i wydrukować przetworzone zdanie na ekranie.

#Wyrazy, które odnalazł, mają być przetłumaczone. Wyrazy, których nie odnalazł w słowniku. 
#mają być wypisane, tak jak zostały wprowadzone, ale dodatkowo z * na końcu.

#Zadbaj o to, żeby pierwsza litera w zdaniu była pisana dużą literą.

#Przykład.

#Yesterday wieczorem learn się programować*.

words = {"samochód" : "car",
         "piasek" : "sand",
         "pływać" : "swim",
         "grać" : "play",
         "wczoraj" : "yesterday",
         "dzisiaj" : "today",
         "spotkanie" : "meeting",
         "order" : "zamówienie",
         "shoe" : "but",
         "spódniczka" : "skirt",
         "niebieski" : "blue",
         "stół" : "table",
         "herbata" : "tea",
         "dane" : "data",
         "kopanie" : "mining",
         "matka" : "mother",
         "analiza" : "analize",
         "ja" : "i",
         "chce" : "want", 
         "nauczyć" : "learn",
         "oprogramowanie" : "software"}


def translate():
    #sentence = input("Enter a sentence in polsih that you want to translate to english: ")
    sentence = "Ja chce bardzo nauczyć się biegać. lubię herbata"
    dic_sentence = sentence.lower().split()
    translate_sentence = []
    
    for word in dic_sentence:
        if word in words:
            translate_word = words[word]
            translate_sentence.append(translate_word)
        else:
            word += "*"
            translate_sentence.append(word)
    
    translate_sentence[0] = translate_sentence[0].upper() 
    
    english_sentence = " ".join(translate_sentence)
    print(english_sentence)
    
translate()