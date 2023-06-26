#dzień 56

#Stwórz generator hasła.

# Hasło musi zawierać co najmniej jedną cyfrę.
# Hasło musi zawierać co najmniej jedną dużą literę.
# Hasło musi zawierać co najmniej jedną małą literę.
# Hasło musi zawierać co najmniej jeden znak specjalny.
# Hasło musi mieć między 10 a 15 znaków.
# Hasło nie może zawierać znaków "mylących", 1, I, O, 0.
#_Hint

#wyszukaj w Google: random number generator pytho
import random
import string
def generate_password():
    all_signs = string.ascii_letters + string.digits + string.punctuation
    confusing_signs = ["1", "I", "0", "O"]
    
    while True:
        password = "".join(random.choice(all_signs) for _ in range(random.randint(10,15)))
            
        if  not any(char.isdigit() for char in password):
            continue
        if  not any(char.isupper() for char in password):
            continue
        if  not any(char.islower() for char in password):
            continue
        if  not any(char in string.punctuation for char in password):
            continue
        if  not any(char in confusing_signs for char in password):
            continue
        
        return password
    
    

  

    
    
    
    
    


print(generate_password())