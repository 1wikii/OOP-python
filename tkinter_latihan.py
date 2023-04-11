from tkinter import *
root = Tk()

file = open("text.txt", "r")

# LABEL GRID
# l = Label(root, text="HELLO").grid(row=0,column=0)

# BUTTONS
# Button(root, text="CLICK!", padx=50, pady=50, state=DISABLED)

ent = Entry(root, borderwidth=5)
ent.pack()  # for avoid 'non type' return from .pack()
ent.insert(0, file.read())

def click():
	word = "That work man, " + ent.get()
	tam = Label(root, text=word).pack()


bt = Button(root, text="CLICK!", padx=50, pady=50, command=click, fg="white", bg="black").pack()

root.mainloop()

