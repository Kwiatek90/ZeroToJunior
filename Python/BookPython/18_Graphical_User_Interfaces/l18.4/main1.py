import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="Iam frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="Iam frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()


window.mainloop()
