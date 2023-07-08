from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re

r = urllib.request.urlopen('https://analytics.usa.gov/').read()
soup = BeautifulSoup(r, "lxml")
type(soup)

print(soup.prettify()[:100])

for link in soup.find_all('a'):
    print(link.get('href'))
