import tkinter as tk
from tkinter import Toplevel, Button, Tk, Menu

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

  root = Tk()
  root.title("Inbox")
  
  topFrame = tk.Frame(root, height = 50, width = width)
  topFrame.pack(side=tk.TOP)
  botFrame = tk.Frame(root, height = height, width = width)

  # basic menu 
  menubar = Menu(root)
  navmenu = Menu(menubar, tearoff = 0, background ='lavender')
  menubar.add_cascade(label="Navigation", background = 'lavender', font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', menu = navmenu)

  navmenu.add_command(label="Profile", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*')
  navmenu.add_command(label="Home Page", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', command = backToHome)
  navmenu.add_separator()
  navmenu.add_command(label="Log Out", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', command = logOut)


  
  root.config(bg ='white', menu=menubar)
  root.minsize(700,700)
  root.maxsize(1000,0)
  root.mainloop()


  
