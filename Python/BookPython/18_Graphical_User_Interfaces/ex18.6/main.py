import tkinter as tk

window = tk.Tk()

window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10], weight=1, minsize=50)
window.columnconfigure(0, minsize=200)

#frame 
frame_input = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_input.grid(column=0, row=0)

frame_buttons = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
frame_buttons.grid(column=0, row=1)


#input i labele 
label_user_name = tk.Label(master=frame_input, text="User name:")
label_user_name.grid(row=0, column=0)

entry1 = tk.Entry(master=frame_input, width=50)
entry1.grid(row=0, column=1)
### zrovbic styl i wyplenic label i inputami


button_1 = tk.Button(master= frame_buttons ,text="Click")
button_1.grid()

window.mainloop()

