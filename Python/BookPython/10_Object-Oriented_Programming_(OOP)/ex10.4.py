#In this assignment, you’ll create a simplified model of a farm. As you
#work through this assignment, keep in mind that there are a number
#of correct answers.

#The focus of this assignment is less about the Python class syntax
#and more about software design in general, which is highly subjective.
#This assignment is intentionally left open-ended to encourage you to
#think about how you would organize your code into classes.

#Before you write any code, grab a pen and paper and sketch out a
#model of your farm, identifying classes, attributes, and methods.
#think about inheritance. How can you prevent code duplication?
#Take the time to work through as many iterations as you feel are
#necessary.

#The actual requirements are open to interpretation, but try to adhere
#to these guidelines:

#1. You should have at least four classes: the parent Animal class, and
#then at least three child animal classes that inherit from Animal.

#2. Each class should have a few attributes and at least one method
#that models some behavior appropriate for a specific animal or all
#animals—such as walking, running, eating, sleeping, and so on.

#3. Keep it simple. Utilize inheritance. Make sure you output details
#about the animals and their behaviors


class Animal:
    
    stuff_in_belly = 0
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def talk(self, sound=None):
        
        if sound is None:
            return f"Helle, my name is {self.name}"
        return f"{self.name} says {self.sound}"
    
    def feed(self):
        self.stuff_in_belly = self.stuff_in_belly + 1
        if self.stuff_in_belly > 3:
            return self.poop()
        else:
            return f"{self.name} is eating."

    def is_hungry(self):
        if self.stuff_in_belly < 2:
            return f"{self.name} is hungry"
        else:
            return f"{self.name} is not hungry"

    def poop(self):
        self.stuff_in_belly = 0
        return "Ate too much ... need to find a bathroom"
            

class Horse(Animal):
    def talk(self, sound="Bark Bark!"):
        return super().talk(sound)

class Chicken(Animal):
    def talk(self, sound="Baaa Baaa"):
        return super().talk(sound)

class Pig(Animal):
   def talk(self, sound="Oink Oink"):
        return super().talk(sound)
    