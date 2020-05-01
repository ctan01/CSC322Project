import tkinter as tk


def jumpToProfile(event):
    print("jump to profile page")


def jumpToGroupPage():
    print("jump to group page")


def jumpToInbox():
    print("jump to inbox")


def jumpToUserSearch():
    print("jump to user search")


def jumpToHomePage1():
    print("log out and jump to home page 1")


class HomePage2:
    height = 700
    width = 800

    root = tk.Tk()
    root.title("Home Page")

    # menu bar

    Menu_main = tk.Menu(root)
    root.config(menu=Menu_main)

    Menu_sub = tk.Menu(Menu_main)
    Menu_main.add_cascade(label="Menu", menu=Menu_sub)
    Menu_sub.add_command(label="Profile", command=jumpToProfile("<Button-1>"))
    Menu_sub.add_command(label="Inbox", command=jumpToInbox)
    Menu_sub.add_cascade(label="Your Groups", command=jumpToGroupPage)
    Menu_sub.add_command(label="Search User", command=jumpToUserSearch)

    logoutButton = tk.Button(Menu_main)
    Menu_main.add_command(label="Logout", command=jumpToHomePage1)

    # main body

    topFrame = tk.Frame(root, height=50, width=width)
    topFrame.grid(row=0, column=0)
    botFrame = tk.Frame(root, height=height, width=width)
    botFrame.grid(row=1, column=0)

    appName = tk.Label(topFrame, text="App Name", bg="green", fg="white").place(relwidth=1, relheight=1)


    root.mainloop()
