from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="white")
# can also use border width

e.pack()
e.insert(0, "Enter your Name")


def myClick():
    my_label = Label(root, text="Hello " + e.get())
    my_label.pack()


# can have state disabled if needed (state=DISABLED)

myButton = Button(root, text="Enter Your Name", padx=50, pady=50, command=myClick, fg="blue", bg="#05752a")

myButton.pack()

root.mainloop()
