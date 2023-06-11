#dzien 40

def divide (a, b):
    return a / b, a % b

result, reminder = divide(10, 3)

print(f"Result: {result}")
print(f"Reminder: {reminder}")

#Zadanie
#Dzisiaj prościutko. Napisz funkcję, która z podanej listy zwróci wartość minimalną i maksymalną jednocześnie :)

nums = [3, 5, 2, 10, 6, 8]

def maximum(table):
    maximum =  nums[0]
    for num in table:
        if num > maximum:
            maximum = num
            
    return maximum

def minimum(table):
    minimum =  nums[0]
    for num in table:
        if num < minimum:
            minimum = num
            
    return minimum


print("Wartoś maskymalna listy: ", maximum(nums))
print("Wartoś minimalna listy: ",minimum(nums))

            