#dzień 91 

class InvalidAgeException(Exception):
    pass 


def check_age(age):
    if age < 0:
        raise InvalidAgeException("Wiek nie może być ujmeny")
    print(f"Wiek wynosi {age} lat")
    
    
    
try:
    check_age(-5)
except InvalidAgeException as e:
    print(f"Błąd: {e}")
    
    
#Zadanie na dzisiaj


class NegativeNumberException(Exception):
    pass

def divide(a, b):
    
    if isinstance(a, (str, bool)) or isinstance(b, (str, bool)):
        if b == 0:
            raise ZeroDivisionError("Nie dzieli się przez zero!")
        raise TypeError("Wpisałeś złą liczbę!")
    
    if a < 0  or b < 0:
        raise NegativeNumberException('Liczby są ujemne!')
    
    result = a / b
    print(f"Wynik: {result}")
    
  
try:
    divide(2, 2)
except TypeError as e:
    print(f"Błąd: {e}")
except ZeroDivisionError as z:
    print(f"Błąd: {z}")
except NegativeNumberException as n:
    print(f"Błąd: {n}")
    