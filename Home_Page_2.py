from tkinter import *


def doNothing():
    print("doNothing")


root = Tk()
root.title("Home Page")

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Menu", menu=subMenu)
subMenu.add_command(label="Profile", command=doNothing)
subMenu.add_command(label="Your Groups", command=doNothing)
subMenu.add_command(label="Inbox", command=doNothing)
subMenu.add_command(label="Search User", command=doNothing)

logoutButton = Button(menu)
menu.add_cascade(label="Logout", menu=logoutButton)

appName = Label(root, text="App Name", bg="green", fg="white")
appName.grid(row=0, column=0, columnspan=10)

root.mainloop()
