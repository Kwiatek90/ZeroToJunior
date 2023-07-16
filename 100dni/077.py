#dzień 77

x = 5

print("Przed wywołaniem funkcji zmienna x wynosi", x)

def my_function():
    global x
    x = 10
    print("Wewnątrz funkcji x wynosi", x)

my_function()

print("Poza funkcją x wynosi", x)