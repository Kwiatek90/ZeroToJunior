#1. Create a GoldenRetriever class that inherits from the Dog class. Give
#the sound argument of the GoldenRetriever.speak() method a default
#value of "Bark". Use the following code for your parent Dog class:
#class Dog:
#species = "Canis familiaris"
#def __init__(self, name, age):
#self.name = name
#self.age = age
#def __str__(self):
#return f"{self.name} is {self.age} years old"
#def speak(self, sound):
#return f"{self.name} says {sound}"
class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class GoldenRetriver(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

#2. Write a Rectangle class that must be instantiated with two attributed: length and width. Add a .area() method to the class that
#returns the area (length * width) of the rectangle. Then write
#a Square class that inherits from the Rectangle class and that is
#instantiated with a single attribute called side_length. Test your
#Square class by instantiating a Square with a side_length of 4. Calling
#the .area() method should return 16.


class Rectangle:
    translate = "Prostokąt"
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return int(self.length) * int(self.width)
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    