from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.adamchoi.co.uk/overs/detailed")
all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = []


for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home = match.find_element(By.XPATH, './td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team .append(match.find_element(By.XPATH, './td[4]').text)
#driver.close()