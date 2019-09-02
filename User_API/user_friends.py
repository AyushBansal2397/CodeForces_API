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
