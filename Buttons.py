from tkinter import *

root = Tk()


def myClick():
    my_label = Label(root, text="Clicked!")
    my_label.pack()


# can have state disabled if needed (state=DISABLED)

myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick, fg="blue", bg="#05752a")

myButton.pack()

root.mainloop()
