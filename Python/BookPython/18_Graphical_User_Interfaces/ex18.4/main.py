#2. Write a program that displays a Button widget that is 50 text units
#wide and 25 text units tall and has a white background with blue
#text that reads "Click here".

import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window)
frame.pack()

button = tk.Button(master=frame, bg="white", fg="blue", width=50, height=25, text="Click here!")
button.pack()

window.mainloop()

#3. Write a program that displays an Entry widget that is 40 text units
#wide and has a white background and black text. Use the .insert()
#method to display text in it that reads "What is your name?"
import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window)
frame.pack()

entry = tk.Entry(master=frame, bg="white", fg="black", width=40)
entry.pack()
entry.insert(0, "Whats your name?")

window.mainloop()