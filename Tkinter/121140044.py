# Nama  : Ahmad Dwiky Zerro Dixxon
# NIM   : 121140044
# Kelas : RA

from tkinter import *
import tkinter
from tkinter import scrolledtext
from tkinter import filedialog
import sys
 

class AppTextEditor:
    title = 'Text Editor'
    newfile = 'New File'
    currentFilePath = newfile

    def __init__(self, master):
        self.master = master


        self.master.title(AppTextEditor.title + " - " + AppTextEditor.currentFilePath)
        self.master.geometry('500x400')
        # agar kolom bisa strech hingga 100%
        self.master.grid_columnconfigure(0, weight=1)

        # area untuk isi file (text)
        self.txt = scrolledtext.ScrolledText(self.master, height=999)
        self.txt.grid(row=1)

        # Master Menu
        self.menu = Menu(self.master)

        # menu dropdown
        self.fileDropdown = Menu(self.menu, tearoff=False)

        # Menambahkan new, open 
        self.fileDropdown.add_command(label='New', command=lambda: self.MenuDropdown("new"))
        self.fileDropdown.add_command(label='Open', command=lambda: self.MenuDropdown("open"))

        # Menambah separator (garis pemisah)
        self.fileDropdown.add_separator()

        # Menambakan save, save as
        self.fileDropdown.add_command(label='Save', command=lambda: self.MenuDropdown("save"))
        self.fileDropdown.add_command(label='Save as', command=lambda: self.MenuDropdown("saveAs"))

        # Menu utama
        self.menu.add_cascade(label='File', menu=self.fileDropdown)
        self.master.config(menu=self.menu)

    def MenuDropdown(self,action):
        current = AppTextEditor.currentFilePath

        # Opening a File
        if action == "open":
            file = filedialog.askopenfilename(defaultextension=".txt")

            self.master.title(AppTextEditor.title + " - " + file)

            current = file

            with open(file, 'r') as f:
                self.txt.delete(1.0,END)
                self.txt.insert(INSERT,f.read())

        # Making a new File
        elif action == "new":
            current = AppTextEditor.newfile
            self.txt.delete(1.0,END)
            self.master.title(AppTextEditor.title + " - " + current)

        # Saving a file
        elif action == "save" or action == "saveAs":
            if current == AppTextEditor.newfile or action == 'saveAs':
                current = filedialog.asksaveasfilename(defaultextension=".txt")

            with open(current, 'w') as f:
                f.write(self.txt.get('1.0','end'))

            self.master.title(AppTextEditor.title + " - " + current)


if __name__ == "__main__":
    root = tkinter.Tk()
    AppTextEditor(root)
    root.mainloop()
