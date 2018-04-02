import os
from tkinter import *


def callback():
    krazie = e.get()
    if krazie == "yes":
        print("Aborting shutdown")
        os.system("shutdown -a")



master = Tk()

e = Entry(master)
e.pack()

e.focus_set()


b = Button(master, text="Abort Shutdown", width=20, command=callback)
b.pack()

mainloop()

