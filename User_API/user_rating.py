import requests, json

# returns rating changes
def user_rating(handle):
	
	url = "https://codeforces.com/api/user.rating?handle=" + handle
	res = requests.get(url).json()
	result = res.get("result")
	rating = [["CONTEST NO.", "CONTEST NAME", "RANK", "OLD RATING", "NEW RATING"]]
	for i in result:
		rating.append([ str(i.get("contestId")), 
						str(i.get("contestName")), 
						str(i.get("rank")), 
						str(i.get("oldRating")), 
						str(i.get("newRating")) ])

	return rating