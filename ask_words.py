# !/usr/bin/python3
from tkinter import *
import tkinter as tk
from tkinter import messagebox

top = Tk()
top.geometry("200x100")


# master = tk.Tk()
# tk.Label(master, text="Type of the name country:").grid(row=0)
# e1 = tk.Entry(master)
# e1.grid(row=0, column=1)
# master.mainloop()


def helloCallBack():
    msg = messagebox.showinfo("Answer", "The capital of ..")


tl = Label(top, text="Type of the name country:").grid(row=0, column=1)
tb = Entry(top)
B = Button(top, text="OK", command=helloCallBack)
C = Button(top, text="Cancel", command=exit)
tb.grid(row=2, column=1)
B.place(x=50, y=50)
C.place(x=100, y=50)
top.mainloop()
