from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.wikipedia.org/")
query = driver.find_element("id", "searchInput")
query.send_keys("Hello World")
query.submit()
print(driver.find_element("id", "firstHeading").text)
assert driver.title == "\"Hello, World!\" program - Wikipedia"
driver.close()