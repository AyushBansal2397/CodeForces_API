from tkinter import *
import tkinter.messagebox
from Contest.contest_upcoming import *
from User.user_info import *

Key = ""
Handle = ""
Secret = ""

def quit_gamebtn(e):
	ans = tkinter.messagebox.askokcancel('Confirm Exit', 'Are you sure want to exit?')
	if ans:
		quit()

def Button_1(e):
	global Key, Handle, Secret
	user_info(Handle, Key, Secret)

def Button_2(e):
	contest_upcoming()

def call(handle, key, secret):
	global Key, Handle, Secret
	Key = key
	Handle = handle
	Secret = secret
	
	root = Tk()
	root.title("CodeForces")
	root.geometry("300x500+0+0")

	# Main Window
	top = Frame(root)
	top.pack(expand=300)

	button_1 = Button(top, text=" User Info ")
	button_2 = Button(top, text=" Upcoming Contest ")
	button_3 = Button(top, text="Quit")

	button_1.bind("<Button-1>", Button_1)
	button_2.bind("<Button-1>", Button_2)
	button_3.bind("<Button-1>", quit_gamebtn)

	button_1.pack(pady=10, fill=X, ipady=3)
	button_2.pack(pady=10, fill=X, ipady=3)
	button_3.pack(pady=10, fill=X, ipady=3)
	root.mainloop()
