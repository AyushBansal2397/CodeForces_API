def save(handle, password, key, secret):
	file = open("info.txt", "a")
	file.writelines("Handle : " + handle)
	file.writelines("\nPassword : " + password)
	file.writelines("\nKey : " + key)
	file.writelines("\nSecret : " + secret + "\n")
	file.close()