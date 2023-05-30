#dzień 31


numbers1 = [1,3,6,12,1,23,43,12,11]
numbers2 = [1,3,6,12,1,23,43,12,12]
numbers3 = [1,3,6,12,1,23,43,12,13]

numbers = [numbers1, numbers2, numbers3]

def print_avg(value):
    print("Średnia wynosi: ", value)

def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg # zwracam wyliczoną średnią, jako rezultat funkcji

def max_num(value):
    return max(value)

for nums in numbers:
    avg = average(nums)
    print(f"Największa wartość z tego zbioru to: {max_num(nums)}")
    print_avg(avg)
    
#Zadanie dodatkowe:
#Dopisz funkcję, która znajduje i wypisuje na ekranie, największą liczbę z danej listy. 
#Dodaj jej wywołanie do pętli, tak, żeby mieć na zmianę informację o średniej oraz maksymalnej wartości.