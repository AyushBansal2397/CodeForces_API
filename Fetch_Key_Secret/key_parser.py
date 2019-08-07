from selenium import webdriver

def key_parser(handle, password):
	
	url = "https://codeforces.com/settings/api"
	driver = webdriver.Chrome()
	driver.get(url)

	# user login
	email = driver.find_element_by_id("handleOrEmail").send_keys(handle)
	pwd = driver.find_element_by_id("password").send_keys(password)
	rem = driver.find_element_by_id("remember").click()
	log = driver.find_element_by_class_name("submit").submit()
	del email, pwd, rem, log

	driver1 = webdriver.Chrome()
	driver1.get(url)

	xPath = "//*[@id='pageContent']/div[2]/div[5]/div/div[5]/div[6]/table/tbody/tr[2]/td"
	isExist = driver.find_element_by_xpath(xPath).text

	if isExist == "No items":
		del isExist

		xPath = '//*[@id="pageContent"]/div[2]/div[5]/div/div[4]/div/a'
		addapi = driver.find_element_by_xpath(xPath).click()
		
		xPath = "//*[@id='facebox']/div/div/div/form/table/tbody/tr[1]/td[2]/input"
		name = driver.find_element_by_xpath(xPath).send_keys("apikey")

		xPath = "//*[@id='facebox']/div/div/div/form/table/tbody/tr[2]/td[2]/input"
		password = driver.find_element_by_xpath(xPath).send_keys(password)

		xPath = "//*[@id='facebox']/div/div/div/form/table/tbody/tr[3]/td/div/input"
		generate = driver.find_element_by_xpath(xPath).click()
		
		del addapi, name, password, generate
		driver1.quit()
		driver1 = webdriver.Chrome()
		driver1.get(url)
		driver1.quit()

		xPath = "//*[@id='pageContent']/div[2]/div[5]/div/div[3]/div[2]/span"
		key = driver.find_element_by_xpath(xPath).text

		xPath = "//*[@id='pageContent']/div[2]/div[5]/div/div[3]/div[3]/span"
		secret = driver.find_element_by_xpath(xPath).text

	else:
		del isExist
		xPath = "//*[@id='pageContent']/div[2]/div[5]/div/div[5]/div[6]/table/tbody/tr[2]/td[5]/a"
		keyinfo = driver.find_element_by_xpath(xPath).click()

		xPath = "//*[@id='facebox']/div/div/div/form/table/tbody/tr[2]/td[2]/input"
		password = driver.find_element_by_xpath(xPath).send_keys(password)
		
		xPath = "//*[@id='facebox']/div/div/div/form/table/tbody/tr[4]/td/div/input"
		submit = driver.find_element_by_xpath(xPath).click()
		
		del keyinfo, password, submit
		driver1.quit()
		driver1 = webdriver.Chrome()
		driver1.get(url)
		driver1.quit()
		
		xPath = "//*[@id='facebox']/div/div/div/div/div[1]/span"
		key = driver.find_element_by_xpath(xPath).text
		
		xPath = "//*[@id='facebox']/div/div/div/div/div[2]/span"
		secret = driver.find_element_by_xpath(xPath).text
	a = []
	a.append(key.strip())
	a.append(secret.strip())
	driver.quit()
	return a