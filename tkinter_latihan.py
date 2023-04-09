from tkinter import *

def main():
	user = "budi"
	passs = "123"


	window = Tk()
	window.geometry('600x300')
	window.title("LOGIN")

	username = " "
	password = " "


	uLabel = Label(window, text="User Name").grid(row=0, column=0)
	uEntry = Entry(window, textvariable=username).grid(row=0, column=0)

	bt = Button(window, text="Masuk").grid(row=2, column=1)

	def cek():
		if username == user:
			benar = Label(window, text="benarr").grid(row=3, column=0)

	window.mainloop()

root = Tk()

l = Label(root, text="HELLO")
l.pack()

root.mainloop()