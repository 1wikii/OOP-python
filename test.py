from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
import ctypes
import sys

window = Tk()

window.title('main')
window.geometry('500x400')

menu = Menu(window, font="inherit")
new_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="New",menu=new_menu)

save_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Save", menu=save_menu)

save_as_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Save as", menu=save_as_menu)

open_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Open", menu=open_menu)

window.config(menu=menu)
window.mainloop()