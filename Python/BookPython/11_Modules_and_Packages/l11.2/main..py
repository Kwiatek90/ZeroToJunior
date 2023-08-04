# main.py

from mypackage.module1 import greet
from mypackage.module2 import depart
from mypackage.mysubpackage.module3 import people

greet("Pythonista")
depart("Pythonista")

for person in people:
    greet(person)

