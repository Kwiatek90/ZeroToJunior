import tkinter as tk
import random

window = tk.Tk()


def change_color():
    colors = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]
    button["bg"] = colors[random.randint(0, len(colors))]
    
    
button = tk.Button(master=window, fg="black", text="Change color!", command=change_color)
button.grid(row=0, column=0)

window.mainloop()