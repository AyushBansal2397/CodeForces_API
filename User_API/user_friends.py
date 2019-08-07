import requests, json, hashlib, random, time

def user_friends(ApiKey, secret):

	Time = str(int(time.time()))
	hashc = '721345/user.friends?apiKey=' + ApiKey + '&time=' + Time + '#' + secret
	hashc = bytes(hashc,'utf-8')
	hashc = hashlib.sha512(hashc).hexdigest()
	url = 'http://codeforces.com/api/user.friends?apiKey=' + ApiKey + '&time=' + Time
	url = url + '&apiSig=721345' + str(hashc)
	response = requests.get(url).json()
	return response


# xxx=input('Enter your codeforces key : ')
# yyy=input('Enter your codeforces secret : ')
# hashc='723456/user.friends?apiKey='+xxx+'&time='+time+'#'+yyy
# hashc=bytes(hashc,'utf-8')
# hashc=hashlib.sha512(hashc).hexdigest()
# urlf='http://codeforces.com/api/user.friends?apiKey='+xxx+'&time='+time+'&apiSig=723456'+str(hashc)
# #print(urlf)
# response = requests.get(urlf)
# me=json.loads(response.content.decode('utf-8'))
# me=(me['result'])