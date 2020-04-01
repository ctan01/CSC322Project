from tkinter import *

root = Tk()
root.title("Home Page")


menu = Menu(root)
root.config(menu=menu)

loginButton = Button(menu)
menu.add_cascade(label="Login", menu=loginButton)



appName = Label(root, text="App Name", bg="green", fg="white")
appName.grid(row=0, column=0, columnspan=10)


root.mainloop()
