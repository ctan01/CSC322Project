import tkinter as tk


def backToHome():
    print("back to home page")


def register():  # jumps to register page
    print("register")


def logIn():  # login with info entry
    print("Log in")


class LoginPage:
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
    menu.add_command(label="Back", command=backToHome)

    # TOP FRAME

    Label_name = tk.Label(topFrame, text="Name").grid(row=0, sticky=tk.E)
    Label_password = tk.Label(topFrame, text="Password").grid(row=1, sticky=tk.E)

    Entry_name = tk.Entry(topFrame).grid(row=0, column=1)
    Entry_password = tk.Entry(topFrame).grid(row=1, column=1)
    Checkbutton_keepSignIn = tk.Checkbutton(topFrame, text="Keep me logged in").grid(columnspan=2)

    # BOTTOM FRAME

    Button_register = tk.Button(bottomFrame, text="Register")
    Button_register.bind("<Button-1>", register)  # "<Button-1>" means left click
    Button_register.pack(side=tk.LEFT)

    Button_logIn = tk.Button(bottomFrame, text="Log in")
    Button_logIn.bind("<Button-1>", logIn)
    Button_logIn.pack(side=tk.RIGHT)

    root.mainloop()
