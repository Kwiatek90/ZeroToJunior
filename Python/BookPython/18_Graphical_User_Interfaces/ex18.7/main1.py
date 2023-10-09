#1. Write a program that displays a single button with the default
#background color and black text that reads"Click me".
#When the user clicks on the button, the button background
#should change to a color randomly selected from the following
#list:
#["red", "orange", "yellow", "blue", "green", "indigo", "violet"]
#2. Write a program that simulates rolling a six-sided die. There
#should be one button with the text "Roll". When the user clicks
#the button, a random integer from 1 to 6 should be displaye
#d.
#The application window should look something like this:

import tkinter as tk
import random

window = tk.Tk()


def random_number():
    lbl_value["text"] = str(random.randint(1,6))
    
window.rowconfigure([0,1], weight=1, minsize=50)
window.columnconfigure(0, weight=1, minsize=50)

btn_roll = tk.Button(master=window,text="Roll", command=random_number)
btn_roll.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="4")
lbl_value.grid(row=1, column=0)

window.mainloop()