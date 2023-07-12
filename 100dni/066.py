#dzien 66

file_path = r"D:\Programowanie\ZeroToJunior\100dni\Pliki_do_zadan\066.txt"

f = open(file_path,"r")
try:
    print(f.readline())
finally:
    f.close()
    

#Zadnaie

#Teraz napisz program,
#który odczyta plik tekstowy zawierający listę tych produktów. 
#Następnie program powinien wyświetlić na ekranie nazwy produktów, których cena jest mniejsza niż 8 złotych.

file_path1 = r"D:\Programowanie\ZeroToJunior\100dni\Pliki_do_zadan\066_1.txt"
dic = {}

with open(file_path1) as file:
    for line in file:
        name, price = line.strip().split(",")
        dic[name] = float(price)
    
    for name, price in dic.items():
        if price < 8:
            print(name)