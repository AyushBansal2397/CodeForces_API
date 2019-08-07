import requests, json

# returns rating changes in contest
def contest_ratingChanges(handle):
	i = input(" Enter contest no. : ")
	url = "https://codeforces.com/api/contest.ratingChanges?contestId=" + i
	res = requests.get(url).json()
	result = res.get("result")
	print(" Contest No. : " + str(result[0].get("contestId")))
	print(" Contest Name : " + str(result[0].get("contestName")))
	print(" RANK\t\tHANDLE \t\tOLD RATING\tNEW RATING")
	
	for i in result:
		print(" " + str(i.get("rank")) + "\t",end = "")
		h = str(i.get("handle"))
		space = (25-len(h))*str(" ")
		h = h + space
		print(str(h) + "  " + str(i.get("oldRating")) + "\t\t   " + str(i.get("newRating")))
	
	print(result)