from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.adamchoi.co.uk/overs/detailed")
driver.close()

