#dzien 59 


#Napisz funkcję, która przyjmuje listę liczb całkowitych i zwraca listę zawierającą tylko unikalne wartości z tej listy.


def uniq_value(tab_list):
    return list(set(tab_list))

lista = [1,2,3,4,5,6,7,8,9,10]

print(uniq_value(lista))