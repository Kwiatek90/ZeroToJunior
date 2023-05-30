#dzien 32


numbers1 = [1,3,6,12,1,23,43,12,11]




def minimum(numbers):
    n_min = numbers1[0]
    for n_current in numbers:
        if n_current < n_min:
            n_min = n_current
    return n_min

print(f"Najmniejsza liczba tego zbioru to: {minimum(numbers1)}")
    