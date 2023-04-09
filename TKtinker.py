import tkinter

class App:
    def __init__(self, window):
        window.title('PBO')

        label1 = tkinter.Label(window, text = 'Username')
        label2 = tkinter.Label(window, text = 'Password:')
        label3 = tkinter.Label(window, text = ':')
        label4 = tkinter.Label(window, text = ':')
        self.entry1 = tkinter.Entry(window)
        self.entry2 = tkinter.Entry(window)

        label1.grid(row = 0, column = 0, sticky = 'W')
        label2.grid(row = 1, column = 0, sticky = 'W')
        label3.grid(row = 0, column = 1, sticky = 'W')
        label4.grid(row = 1, column = 1, sticky = 'W')
        self.entry1.grid(row = 0, column = 2, sticky = 'W')
        self.entry2.grid(row = 1, column = 2, sticky = 'W')

        button = tkinter.Button(window, text = 'Login', command = self.button_command)
      
        button.grid(row = 2, column = 2, sticky = 'W')

    def button_command(self):
        Action(tkinter.Tk(), self.entry1.get(), self.entry2.get())

class Action:
    __Username = "Eko"
    __Password = "Eko"

    def __init__(self, window, username, password):
        window.title('Validasi')
        
        if username == Action.__Username and password == Action.__Password:
            tkinter.Message(window, text = "Success").pack()
        else:
            tkinter.Message(window, text = "Failed").pack()

if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(root)
