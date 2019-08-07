from save import save
from Key.key_parser import *
from getpass import getpass
from tkinter import *
from main import call

root = Tk()
root.title("CodeForces")
root.geometry("250x80+"+str(int(root.winfo_screenwidth()/2-125))+"+"+str(int(root.winfo_screenheight()/2-40)))
name_entry = Entry(root)
pass_entry = Entry(root)

def print_crap(event):
	global name_entry, pass_entry, flag
	if name_entry.get() != "" and pass_entry.get() != "":
		transfer(name_entry.get(), pass_entry.get())

#GUI Part
def GUI():
	name = Label(root, text="Handle :")
	password = Label(root, text="Password :")
	button = Button(root, text="Submit")
	name.grid(row=0, column=0, pady=2, padx=2, sticky=E)
	password.grid(row=1, column=0, sticky=E)
	name_entry.grid(row=0, column=1)
	pass_entry.grid(row=1, column=1)
	button.grid(row=2, column=1, columnspan=2)
	button.bind("<Button-1>", print_crap)
	root.mainloop()

def transfer(handle, password):
	root.destroy()
	a = key_parser(handle, password)
	key = str(a[0])
	secret = str(a[1])
	save(handle, password, key, secret)
	call(handle, key, secret)

if __name__ == "__main__":
	GUI()
