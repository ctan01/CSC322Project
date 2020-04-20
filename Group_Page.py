import tkinter as tk

def backToHome():
   print("Back to Home Page") # jump to home page 2
  
def toInbox():
  print("Inbox")
  
def logOut(); 
   print("log out")
  
class groupPage:
  root = tk.Tk()
  root.title ("Group Page")
  
  # set up : kept consistent through all the pages
  topFrame = tk.Frame(root)
  topFrame.pack(side=tk.TOP)
  bottomFrame = tk.Frame(root)
  bottomFrame.pack(side=tk.BOTTOM)
  
  
  root.mainloop()
