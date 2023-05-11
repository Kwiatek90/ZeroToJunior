#1. Create a float object named weight with the value 0.2, and create
#a string object named animal with the value "newt". Then use these
#objects to print the following string using only string concatenation:
#0.2 kg is the weight of the newt.
weight = 0.2
animal = "newt"
print(str(weight) + " is the weight of the " + animal)

#2. Display the same string by using the .format() method and empty
#{} place-holders.
print("{} is the weight of the {}".format(weight, animal))

#3. Display the same string using an f-string
print(f"{weight} is the weight of the {animal}")