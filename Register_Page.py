import tkinter as tk

root = tk.Tk()
root.title("Registration Page")

canvas = tk.Canvas(root, height=300, width=300)
canvas.pack()


frame = tk.Frame(canvas)
frame.place(relwidth=1, relheight=1)

Label_firstName = tk.Label(frame, text="First Name:").grid(row=0, column=0, sticky=tk.E)
Label_lastName = tk.Label(frame, text="Last Name:").grid(row=1, column=0, sticky=tk.E)
Label_email = tk.Label(frame, text="Email:").grid(row=2, column=0, sticky=tk.E)
Label_phone = tk.Label(frame, text="Phone Number: ").grid(row=3, column=0, sticky=tk.E)
Label_reference1 = tk.Label(frame, text="Reference 1: ").grid(row=4, column=0, sticky=tk.E)
Label_reference2 = tk.Label(frame, text="Reference 2: ").grid(row=5, column=0, sticky=tk.E)
Label_interests = tk.Label(frame, text="Interest: ").grid(row=6, column=0, sticky=tk.E)
Label_skillSets = tk.Label(frame, text="Skill sets: ").grid(row=7, column=0, sticky=tk.E)
Label_username = tk.Label(frame, text="Username: ").grid(row=8, column=0, sticky=tk.E)
Label_password = tk.Label(frame, text="Password: ").grid(row=9, column=0, sticky=tk.E)

Entry_firstName = tk.Entry(frame).grid(row=0, column=1)
Entry_lastName = tk.Entry(frame).grid(row=1, column=1)
Entry_email = tk.Entry(frame).grid(row=2, column=1)
Entry_phone = tk.Entry(frame).grid(row=3, column=1)
Entry_reference1 = tk.Entry(frame).grid(row=4, column=1)
Entry_reference2 = tk.Entry(frame).grid(row=5, column=1)
Entry_interests = tk.Entry(frame).grid(row=6, column=1)
Entry_skillSets = tk.Entry(frame).grid(row=7, column=1)
Entry_username = tk.Entry(frame).grid(row=8, column=1)
Entry_password = tk.Entry(frame).grid(row=9, column=1)

Button_submit = tk.Button(frame, text="Submit").grid(row=11, columnspan=2)


root.mainloop()




