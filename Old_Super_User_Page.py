import tkinter as tk

# Super User Page has the following
# log out, inbox, profile page, issue warning to user, view registration requests

def backToHome():
  print("back to home page")
  
def logOut():
  print("log out")
  
def toInbox():
  print("to inbox")
  
class SuperUserPage:
  root = tk.Tk()
  root.title("Super User Page")
  
  # set up, the same throughout
  topFrame = tk.Frame(root)
  topFrame.pack(side = tk.TOP)
  bottomFrame = tk.Frame(root)
  bottomFrame.pack(side = tk.BOTTOM)
  
  root.mainloop()
