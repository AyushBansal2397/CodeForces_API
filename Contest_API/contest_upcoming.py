import requests, json
from tkinter import *

def contest_upcoming():

	urlc = "https://codeforces.com/api/contest.list?gym=false"
	response = requests.get(urlc,auth=('rw','rw'))
	contest = json.loads(response.content.decode('utf-8'))
	contest = contest["result"][0:5]
	contest_name = []
	for i in (contest):
		if( i['phase'] == 'BEFORE' ):
			contest_name.append(i['name'])

	root = Tk()
	root.title("Upcoming Contest")
	Label(root, text = "Upcoming Contest : ").grid(row=0, column=0, sticky=W)
	j = 1
	for i in contest_name:
		Label(root, text = i).grid(row=j, column=1, sticky=W)
		j += 1
