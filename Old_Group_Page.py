import tkinter as tk
from tkinter import Toplevel, Button, Tk, Menu
# Each Group Page has the following:
# request poll, log out, go to profile page, send complaint to SU, send compliment to SU, Leave group,
# post to group page, comment on post

def backToHome():
  print("Back to Home Page") # jump to home page 2
  
def jumpToInbox():
  print("Inbox")
  
def logOut():
  print("log out") 

def jumpToProfile(event):
  print("jump to profile page")

def leaveGroup(event):
  print("leave group")
  
class GroupPage:
  height = 700
  width = 800
  
  root = tk.Tk()
  root.title ("Group Page")
  
  # set up : kept consistent through all the pages
  topFrame = tk.Frame(root, height = 50, width = width)
  topFrame.pack(side=tk.TOP)
  botFrame = tk.Frame(root, height = height, width = width)

  # basic menu 
  menubar = Menu(root)

  # navigation menu
  navmenu = Menu(menubar, tearoff = 0, background ='lavender')
  menubar.add_cascade(label="Navigation", background = 'lavender', font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', menu = navmenu)
  navmenu.add_command(label="Profile", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', command = jumpToProfile)
  navmenu.add_command(label="Home Page", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', command = backToHome)
  navmenu.add_command(label="Inbox", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', command = jumpToInbox)
  navmenu.add_separator()
  navmenu.add_command(label="Log Out", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', command = logOut)

  # group page menu
  groupmenu = Menu(menubar, tearoff = 0, background = 'lavender')
  menubar.add_cascade(label="Group Options", background = 'lavender', font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', menu = groupmenu)
  groupmenu.add_command(label ="File complaint against user to SU", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*')
  groupmenu.add_command(label = "File compliment towards uder to SU", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*')
  groupmenu.add_separator()
  groupmenu.add_command(label="Leave Group", font='-*-verdana-*-r-*-*-*-120-*-*-*-*-*-*', command = leaveGroup)

  

  root.config(bg ='white', menu=menubar)
  root.minsize(700,700)
  root.maxsize(1000,0)
  root.mainloop()
