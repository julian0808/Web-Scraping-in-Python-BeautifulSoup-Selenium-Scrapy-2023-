#!/usr/bin/python3
#

from bs4 import BeautifulSoup
import requests

url = 'http://nos.nl/artikel/2093082-steeds-meer-nekklachten-bij-kinderen-door-gebruik-tablets.html'
file_name=url.rsplit('/',1)[1].rsplit('.')[0]

r  = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
data = soup.find_all('article', {'class': 'article'})


content=''.join('''{}\n{}\n\n{}\n{}'''.format( item.contents[0].find_all('time', {'datetime': '2016-03-16T09:50:30+0100'})[0].text,
                                               item.contents[0].find_all('a', {'class': 'link-grey'})[0].text,
                                               item.contents[0].find_all('img', {'class': 'media-full'})[0],
                                               item.contents[1].find_all('div', {'class': 'article_textwrap'})[0].text,
                                             ) for item in data)

with open('./{}.txt'.format(file_name), mode='wt', encoding='utf-8') as file:
    file.write(content)