
import tkinter as tk

# Inbox Page has the following:
# invitations with accept or decline, accept all invitations, decline all invitations, log out 

def backToHome(): 
  print("back to home page")
  
def logOut():
  print("log out")
  
  
class InboxPage:
  # set up always the same
  root = tk.Tk()
  root.title("Inbox")
  
  topFrame = tk.Frame(root)
  topFrame.pack(side=tk.TOP)
  bottomFrame = tk.Frame(root)
  bottomFrame.pack(side = tk.BOTTOM)
  
  root.mainloop()
  
