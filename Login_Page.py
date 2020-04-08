import tkinter as tk

root = tk.Tk()
root.title("Login")

topFrame = tk.Frame(root)
topFrame.pack(side=tk.TOP)
bottomFrame = tk.Frame(root)
bottomFrame.pack(side=tk.BOTTOM)

# top menu bar
menu = tk.Menu(root)
root.config(menu=menu)

Button_back = tk.Button(menu)
menu.add_cascade(label="Back", menu=Button_back)

# TOP FRAME

Label_name = tk.Label(topFrame, text="Name").grid(row=0, sticky=tk.E)
Label_password = tk.Label(topFrame, text="Password").grid(row=1, sticky=tk.E)

Entry_name = tk.Entry(topFrame).grid(row=0, column=1)
Entry_password = tk.Entry(topFrame).grid(row=1, column=1)
Checkbutton_keepSignIn = tk.Checkbutton(topFrame, text="Keep me logged in").grid(columnspan=2)


# BOTTOM FRAME

def register(event):  # jumps to register page
    print("register")


Button_register = tk.Button(bottomFrame, text="Register")
Button_register.bind("<Button-1>", register)  # "<Button-1>" means left click
Button_register.pack(side=tk.LEFT)


def logIn(event):  # login with info entry
    print("Log in")


Button_logIn = tk.Button(bottomFrame, text="Log in")
Button_logIn.bind("<Button-1>", logIn)
Button_logIn.pack(side=tk.RIGHT)

root.mainloop()

