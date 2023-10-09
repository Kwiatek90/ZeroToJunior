import tkinter as tk


window = tk.Tk()
events_list = []

def handle_keyboard(event):
    print(event.char)

window.mainloop()  

while True:
    if events_list == []:
        continue
    event = events_list[0]
    
    if event.type =="keypress":
        handle_keyboard(event)
        
