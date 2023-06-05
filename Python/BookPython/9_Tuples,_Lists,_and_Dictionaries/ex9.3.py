#1Create a tuple data with two values. The first value should be the
#tuple (1, 2) and the second value should be the tuple (3, 4).
tuple_data = ((1, 2), (3, 4))

#2. Write a for loop that loops over data and prints the sum of each
#nested tuple. The output should look like this:
#Row 1 sum: 3
#Row 2 sum: 7
row = 1
for tuple_small in tuple_data:
    result = sum(tuple_small)
    print(f"Row {row} sum: {result} ") 
    row += 1
#3. Create the following list [4, 3, 2, 1] and assign it to the variable numbers
numbers = [4, 3, 2, 1]


#4 Create a copy of the numbers list using the [:] slicing notation.
numbers_copy = numbers[:]

#5. Sort the numbers list in numerical order using the .sort() method
numbers.sort()
print(numbers)
print(numbers_copy)