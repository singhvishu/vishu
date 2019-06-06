from selenium import webdriver
driver = webdriver.Chrome('C:/Program Files/Python37/library/chromedriver.exe')
driver.get('https://en-gb.facebook.com/r.php?locale=en_GB')
driver.find_element_by_name('firstname').send_keys('vishu')
driver.find_element_by_name('lastname').send_keys('singh')
driver.find_element_by_name('reg_email__').send_keys('0987654321')
driver.find_element_by_name('reg_passwd__').send_keys('123456')

