from tkinter import *

root = Tk()

# Creating a label widget and "shoving" it on the screen
myLabel1 = Label(root, text="Hello Pranav!")
myLabel2 = Label(root, text="Hello Pranav!")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()

