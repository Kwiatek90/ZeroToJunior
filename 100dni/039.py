#dzien 39

#fix me 

fruits = ("apple", "banana", "cherry")

if "apple" in fruits:
    print("tak, 'apple' znajduje się w tuple o nazwie 'fruits'")
    
fruits1 = ("apple", "banana", "cherry")
fruits2 = ("orange",)

print("Pierwsza wersja: ", fruits1)

fruits1 += fruits2

print("Druga wersja: ", fruits1) 

fruits = ("apple", "banana", "cherry")

print(fruits.count("apple"))
print(fruits.index("banana"))