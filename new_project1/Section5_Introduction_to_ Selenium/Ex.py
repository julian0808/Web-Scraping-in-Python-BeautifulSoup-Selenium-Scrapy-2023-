from selenium import webdriver


website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)
driver.quit()
