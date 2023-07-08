from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

#options = Options()
#options.headless = False
#options.add_argument('window-size=1920x1080')

web = "https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=08b836ae-73e5-4c8c-9a3d-71c5be252964&pf_rd_r=J9Y4F1JWCE5VJS7P88EZ&pageLoadId=q2COyziL7mdejrRg&creativeId=1642b4d1-12f3-4375-98fa-4938afc1cedc"
driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()

#pagination
pagination = driver.find_element(By.XPATH , '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

current_page = 1

book_title = []
book_author = []
book_length = []

while current_page <= last_page:
    time.sleep(2)
    container = driver.find_element(By.CLASS_NAME , 'adbl-impression-container ')
    products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')

    for product in products:
        book_title.append(product.find_element(By.XPATH, './/h3[contains(@class,"bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text)

    current_page = current_page + 1

    try:
        next_page = driver.find_element(By.XPATH , '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()

# Storing the data into a DataFrame and exporting to a csv file
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books_headless.csv', index=False)
