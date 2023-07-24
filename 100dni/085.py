#dzien 85
def add_one(x):
    return x + 1

def double(x, function):
    return function(x) * 2

print(double(5, add_one))