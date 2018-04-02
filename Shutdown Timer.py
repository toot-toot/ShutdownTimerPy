import os



from tkinter import *


master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print(e.get())
    os.system("shutdown -s -t " + e.get().zfill(4))


b = Button(master, text="Shutdown", width=10, command=callback)
b.pack()

mainloop()

