from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

web = "https://www.audible.com/search"
driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()
driver.close()

container = driver.find_element(By.CLASS_NAME , 'adbl-impression-container ')
products = container.find_elements(By.XPATH, './li')
#products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')

book_title = []
book_author = []
book_length = []


for product in products:
    book_title.append(product.find_element(By.XPATH, './/h3[contains(@class,"bc-heading")]').text)
    book_author.append(product.find_element(By.XPATH, './/li[contains(@class,"authorLabel")]').text)
    book_length.append(product.find_element(By.XPATH, './/li[contains(@class,"runtimeLabel")]').text)

driver.quit()
# Storing the data into a DataFrame and exporting to a csv file
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('books.csv', index=False)
