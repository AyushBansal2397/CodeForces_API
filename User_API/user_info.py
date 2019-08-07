import requests, json
from User.user_friends import *
from User.user_info import *
from User.user_rating import *
from tkinter import *

# returns user info
def user_info(handle, key, secret):
	url = "https://codeforces.com/api/user.info?handles=" + handle
	res = requests.get(url).json()
	result = res.get("result")[0]
	info = []
	info.append(["Handle : ", handle])
	info.append(["Key : ", key])
	info.append(["Secret : ", secret])
	info.append(["Contribution : ", str(result.get("contribution"))])
	info.append(["Current Rating : ", str(result.get("rating"))])
	info.append(["Email : ", str(result.get("email"))])
	info.append(["No. of Friends : ", str(result.get("friendOfCount"))])
	info.append(["Current Rank : ", str(result.get("rank"))])
	info.append(["Maximum Rating : ", str(result.get("maxRating"))])
	info.append(["Maximum Rank : ", str(result.get("maxRank"))])

	rating = user_rating(handle)

	friends = user_friends(key, secret).get("result")
	friend_list = [["Name", "Rating"]]
	for friend in friends:
		url = "https://codeforces.com/api/user.info?handles=" + friend
		res = requests.get(url).json()
		result = res.get("result")[0]
		friend_list.append([friend, str(result.get("rating"))])

	root = Tk()
	root.title("User Info - " + handle)

	Label(root, text = "Info :").grid(row=0, column=0, sticky=W)
	j = 1
	for i in info:
		Label(root, text = i[0]).grid(row=j, column=1, sticky=E)
		Label(root, text = i[1]).grid(row=j, column=2, sticky=W)
		j += 1


	Label(root, text = "\nFriend List :").grid(row=j, column=0, sticky=W)
	j += 1
	for i in friend_list:
		Label(root, text = i[0]).grid(row=j, column=1, sticky=W)
		Label(root, text = i[1]).grid(row=j, column=2, sticky=W)
		j += 1


	Label(root, text = "\nYour Rating in last contests :").grid(row=j, column=0, columnspan=2, sticky=W)
	j += 1
	for i in rating:
		Label(root, text = i[0]).grid(row=j, column=1)
		Label(root, text = i[1]).grid(row=j, column=2)
		Label(root, text = "  ").grid(row=j, column=3)
		Label(root, text = i[2]).grid(row=j, column=4)
		Label(root, text = "  ").grid(row=j, column=5)
		Label(root, text = i[3]).grid(row=j, column=6)
		Label(root, text = "  ").grid(row=j, column=7)
		Label(root, text = i[4]).grid(row=j, column=8)
		j += 1

	root.mainloop()

