from bs4 import BeautifulSoup
import requests

#####################################################
# Extracting the links of multiple movie transcripts
#####################################################

# How To Get The HTML
root = 'https://subslikescript.com'  # this is the homepage of the website
website = f'{root}/movies_letter-A'  # concatenating the homepage with the movies section
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())  # prints the HTML of the website

# Pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

links = []
for page in range(1, int(last_page)+1)[:2]: # range(1, 2+1)
    # https: // subslikescript.com / movies_letter - A?page = 1
    result = requests.get(f'{website}?page={page}' )
    content = result.text
    soup = BeautifulSoup(content, 'lxml')


    # Locate the box that contains a list of movies
    box = soup.find('article', class_='main-article')

    for link in box.find_all('a', href=True):  # find_all returns a list
        links.append(link['href'])

    # print(links)

    for link in links:
        try:
            print(link)
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            title = ''.join(title.split('/'))
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            # Exporting data in a text file with the "title" name
            with open(f'{title}.txt', 'w', encoding='utf-8') as file:
                file.write(transcript)
        except:
            print('------- Link not working ------')
            print(link)



