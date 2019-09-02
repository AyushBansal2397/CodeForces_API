from save import save
from Fetch_Key_Secret.key_parser import *
from getpass import getpass
from tkinter import *
from main import call

root = Tk()
root.title("CodeForces")
root.geometry("250x100+"+str(int(root.winfo_screenwidth()/2-125))+"+"+str(int(root.winfo_screenheight()/2-40)))
name_entry = Entry(root)
pass_entry = Entry(root)
exist = IntVar();

def print_crap(event):
	global name_entry, pass_entry, flag
	if name_entry.get() != "" and pass_entry.get() != "":
		transfer(name_entry.get(), pass_entry.get(), exist.get())

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
	checkBox = Checkbutton(root, text="Key & Secret exist!", variable=exist)
	checkBox.grid(row=3, column=1)
	root.mainloop()

def transfer(handle, password, exist):
	root.destroy()
	key = secret = ""
	with open("info.txt", "r") as f:
		text = f.readlines()
	Len = len(text)
	if exist and Len%4 == 0 and Len <= 1001:
		for i in range(int(Len/4)):
			Handle = text[i*4].split(":")[1]
			Handle = Handle[1 : len(Handle)-1]
			Password = text[i*4+1].split(":")[1]
			Password = Password[1 : len(Password)-1]
			if handle == Handle and Password == password:
				key = text[i*4+2].split(":")[1]
				key = key[1 : len(key)-1]
				secret = text[i*4+3].split(":")[1]
				secret = secret[1 : len(secret)-1]
	else:
		a = key_parser(handle, password)
		key = str(a[0])
		secret = str(a[1])
	save(handle, password, key, secret)
	call(handle, key, secret)

if __name__ == "__main__":
	GUI()
