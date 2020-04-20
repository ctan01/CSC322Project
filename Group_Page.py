import tkinter as tk
# Each Group Page has the following:
# request poll, log out, go to profile page, send complaint to SU, send compliment to SU, Leave group,
# post to group page, comment on post

def backToHome():
  print("Back to Home Page") # jump to home page 2
  
def jumpToInbox():
  print("Inbox")
  
def jumpToHomePage1():
  print("log out") 

def jumpToProfile(event):
  print("jump to profile page")
  
class GroupPage:
  height = 700
  width = 800
  
  root = tk.Tk()
  root.title ("Group Page")
  
  # set up : kept consistent through all the pages
  topFrame = tk.Frame(root)
  topFrame.pack(side=tk.TOP)
  bottomFrame = tk.Frame(root)
  bottomFrame.pack(side=tk.BOTTOM)
  
  root.mainloop()
