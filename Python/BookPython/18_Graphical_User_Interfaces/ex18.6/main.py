import tkinter as tk

window = tk.Tk()


window.rowconfigure([0, 1, 2], weight=1)
window.columnconfigure(0, weight=1, minsize=200)


#frame 
frame_input = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=1)
frame_input.grid(column=0, row=0)

frame_buttons = tk.Frame(master=window, borderwidth=1)
frame_buttons.grid(column=0, row=1, sticky=tk.E)


#input i labele 
label_user_name = tk.Label(master=frame_input, text="User name:", width=15, anchor=tk.E)
label_user_name.grid(row=0, column=0, sticky=tk.E) #nieechce sie wyrownac
entry_user_name = tk.Entry(master=frame_input, width=50)
entry_user_name.grid(row=0, column=1)

label_last_name = tk.Label(master=frame_input, text="Last name:", width=15, anchor=tk.E)
label_last_name.grid(row=1, column=0, sticky=tk.E) #nieechce sie wyrownac
entry_last_name = tk.Entry(master=frame_input, width=50)
entry_last_name.grid(row=1, column=1)

label_adr1 = tk.Label(master=frame_input, text="Address line 1:", width=15, anchor=tk.E)
label_adr1.grid(row=2, column=0, sticky=tk.E) #nieechce sie wyrownac
entry_adr1 = tk.Entry(master=frame_input, width=50)
entry_adr1.grid(row=2, column=1)


### zrovbic styl i wyplenic label i inputami


button_1 = tk.Button(master= frame_buttons ,text="Click")
button_1.grid(row=0, column=0, padx=5)
button_2 = tk.Button(master= frame_buttons ,text="Submit!")
button_2.grid(row=0, column=1)

window.mainloop()

