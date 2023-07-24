#dzien 81

def compare_numbers(x, y):
    x = float(x)
    y = float(y)
    epsilon = 1e-9
    
    
    if abs(x - y) < epsilon:
        print(True)
    else:
        print(False)
        
        
x = 0.1 + 0.2
y = 0.3

compare_numbers(x, y)