#lesson 10.2

class Dog:

    #Class Attribute
    species = "Cannis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #Replace .description() with __str__()
    def __str__(self):
        return  f"{self.name} is {self.age} years old"
    
    #Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

        
        
# buddy = Dog("Buddy", 9)
# miles = Dog("Miles", 4)