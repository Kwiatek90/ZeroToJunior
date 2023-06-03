#dzien 34

this_list = ["apple", "banana", "cherry"]
this_list.append("orange")
this_list.insert(0, "ananas")
print(this_list)

#Zadanie 

#WYpisanie listy na której będziemy pracować
fruits = ["apple", "banana", "cherry"]
print("Lista startowa: ", fruits)

#Usuwa wartość "banana" z listy
fruits.remove("banana")
print("Remove: ", fruits)

#usuwa wartośc z kolumny o zadanym indexie
fruits = ["apple", "banana", "cherry"]
fruits.pop(0)
print("pop(0): " , fruits)

#usuwa wartośc z kolumny, czyi ostatnią wartośc z listy
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print("pop(): ", fruits)

#czyści listę
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print("Clear(): ", fruits)




