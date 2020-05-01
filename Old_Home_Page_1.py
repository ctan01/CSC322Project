import tkinter as tk


def logIn():
    print("jump to login page")


class HomePage1:
    height = 700
    width = 800

    root = tk.Tk()
    root.title("Home Page")

    # top menu bar
    menu = tk.Menu(root)
    root.config(menu=menu)

    Button_logIn = tk.Button(menu)
    menu.add_command(label="Login", command=logIn)

    # main body
    topFrame = tk.Frame(root, height=50, width=width)
    topFrame.grid(row=0, column=0)
    botFrame = tk.Frame(root, height=height, width=width)
    botFrame.grid(row=1, column=0)

    appName = tk.Label(topFrame, text="App Name", bg="green", fg="white").place(relwidth=1, relheight=1)

    root.mainloop()
