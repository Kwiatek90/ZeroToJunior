#dzień 30


numbers1 = [1,3,6,12,1,23,43,12,11]
numbers2 = [1,3,6,12,1,23,43,12,12]
numbers3 = [1,3,6,12,1,23,43,12,13]

def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg # zwracam średnią, jako rezultat
    print(avg) # ten print po return nie zostanie wykonany

print(average(numbers1))
average(numbers2)
average(numbers3)

#Zadanie
#Napisz funkcję printavg(value), która wydrukuje komunikat: "Średnia wynosi: ", a następnie wyświetli wyliczoną wartość.

def printavg(value):
    sums = sum(value)
    length = len(value)
    average = sums / length
    print(f"Srednia wynosi: {average}")
    
values = [5, 2, 56, 23, 10, 1]
printavg(values)
