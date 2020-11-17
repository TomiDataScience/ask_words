# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("200x100")


def helloCallBack():
    msg = messagebox.showinfo("Answer", "The capital of ..")


B = Button(top, text="OK", command=helloCallBack)
C = Button(top, text="Cancel", command=exit)
B.place(x=50, y=50)
C.place(x=100, y=50)
top.mainloop()
