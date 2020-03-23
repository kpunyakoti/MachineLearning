from tkinter import *
from tkinter import ttk

class HelloApp():

    def _init_(self, master):

        self.label = ttk.Label(master, text = 'Hello World')
        self.label.grid(row=0, column=0, coulmnspan=2)

        ttk.Button(master, text = 'Texas',
                   command = self.texas_hello).grid(row=1, column=0)
        
        ttk.Button(master, text = 'India',
                   command = self.india_hello).grid(row=1, column=1)

        def texas_hello(self):
            self.label.config(text = 'Howdy Texas')

        def india_hello(self):
            self.label.config(text = 'Namaste India')

def main():

    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if _name_ == "_main_": main()
