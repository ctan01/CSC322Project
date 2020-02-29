from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


# TOP FRAME


label_1 = Label(topFrame, text="Username")
label_2 = Label(topFrame, text="Password")
entry_1 = Entry(topFrame)
entry_2 = Entry(topFrame)


label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(topFrame, text="Keep me logged in")
c.grid(columnspan=2)


# BOTTOM FRAME

def register(event):
    print("register")


button_1 = Button(bottomFrame, text="Register")
button_1.bind("<Button-1>", register)
button_1.pack(side=LEFT)


def logIn(event):
    print("Log in")


button_2 = Button(bottomFrame, text="Log in")
button_2.bind("<Button-1>", logIn)
button_2.pack(side=RIGHT)


root.mainloop()
