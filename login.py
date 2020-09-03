from selenium import webdriver

# initialize the driver for firefox 
driver = webdriver.Firefox(executable_path="/home/drei/Desktop/AutoLogin/geckodriver")


# initialize the target url which is facebook 
driver.get("https://www.facebook.com")

# find and get the id value for username,password and login button 
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit = driver.find_element_by_id("loginbutton")

# add your username and password
username.send_keys("username")
password.send_keys("password")

# Submit the value
submit.click()
