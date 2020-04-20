
import tkinter as tk

# Inbox Page has the following:
# invitations with accept or decline, accept all invitations, decline all invitations, log out 

def backToHome(): 
  print("back to home page")
  
def logOut(): # use logOut() or jumpToHomePage1() ?
  print("log out")
  
  
class InboxPage:
  # set up always the same
  height = 700
  width = 800

  root = tk.Tk()
  root.title("Inbox")
  
  topFrame = tk.Frame(root, height = 50, width = width)
  topFrame.pack(side=tk.TOP)
  botFrame = tk.Frame(root, height = height, width = width)

  root.mainloop()


  
