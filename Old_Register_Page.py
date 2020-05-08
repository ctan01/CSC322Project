import tkinter as tk


def submit(event):
    print("submit and go back to home page")


def backToHome():
    print("back to home page")


class RegisterPage:
    height = 600
    width = 800

    root = tk.Tk()
    root.title("Registration Page")

    # top menu bar
    menu = tk.Menu(root)
    root.config(menu=menu)

    Button_back = tk.Button(menu)
    menu.add_command(label="Back", command=backToHome)

    # main body

    canvas = tk.Canvas(root, height=height, width=width)
    canvas.pack()

    frame = tk.Frame(canvas)
    frame.place(relwidth=1, relheight=1)

    Label_firstName = tk.Label(frame, text="First Name:").grid(row=0, column=0, sticky=tk.E)
    Label_lastName = tk.Label(frame, text="Last Name:").grid(row=1, column=0, sticky=tk.E)
    Label_email = tk.Label(frame, text="Email:").grid(row=2, column=0, sticky=tk.E)
    Label_phone = tk.Label(frame, text="Phone Number: ").grid(row=3, column=0, sticky=tk.E)
    Label_reference1 = tk.Label(frame, text="Reference 1: ").grid(row=4, column=0, sticky=tk.E)
    Label_reference2 = tk.Label(frame, text="Reference 2: ").grid(row=5, column=0, sticky=tk.E)
    Label_username = tk.Label(frame, text="Username: ").grid(row=8, column=0, sticky=tk.E)
    Label_password = tk.Label(frame, text="Password: ").grid(row=9, column=0, sticky=tk.E)
    Label_interests = tk.Label(frame, text="Interest: ").grid(row=6, column=0)
    Label_skillSets = tk.Label(frame, text="Skill sets: ").grid(row=7, column=0)

    Entry_firstName = tk.Entry(frame).grid(row=0, column=1)
    Entry_lastName = tk.Entry(frame).grid(row=1, column=1)
    Entry_email = tk.Entry(frame).grid(row=2, column=1)
    Entry_phone = tk.Entry(frame).grid(row=3, column=1)
    Entry_reference1 = tk.Entry(frame).grid(row=4, column=1)
    Entry_reference2 = tk.Entry(frame).grid(row=5, column=1)
    Entry_username = tk.Entry(frame).grid(row=8, column=1)
    Entry_password = tk.Entry(frame).grid(row=9, column=1)
    Checkbutton_interests1 = tk.Checkbutton(frame, text="Finance").grid(row=6, column=1, sticky=tk.W)
    Checkbutton_interests2 = tk.Checkbutton(frame, text="Coding").grid(row=6, column=2, sticky=tk.W)
    Checkbutton_interests3 = tk.Checkbutton(frame, text="Management").grid(row=6, column=3, sticky=tk.W)
    Checkbutton_interests4 = tk.Checkbutton(frame, text="Research").grid(row=6, column=4, sticky=tk.W)
    Checkbutton_interests5 = tk.Checkbutton(frame, text="Education").grid(row=6, column=5, sticky=tk.W)
    Checkbutton_skillSets1 = tk.Checkbutton(frame, text="c++").grid(row=7, column=1, sticky=tk.W)
    Checkbutton_skillSets2 = tk.Checkbutton(frame, text="python").grid(row=7, column=2, sticky=tk.W)
    Checkbutton_skillSets3 = tk.Checkbutton(frame, text="java").grid(row=7, column=3, sticky=tk.W)
    Checkbutton_skillSets4 = tk.Checkbutton(frame, text="communication").grid(row=7, column=4, sticky=tk.W)
    Checkbutton_skillSets5 = tk.Checkbutton(frame, text="Data analysis").grid(row=7, column=5, sticky=tk.W)


    Button_submit = tk.Button(frame, text="Submit")
    Button_submit.bind("<Button-1>", submit)
    Button_submit.grid(row=11, columnspan=2)

    root.mainloop()
