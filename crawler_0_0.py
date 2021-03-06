import requests
from bs4 import BeautifulSoup

url_array = []
with open("url's.txt", 'r') as url_s:
    for url in url_s:
        url_array += [url.strip()]
library = ['data/1.txt', 'data/2.txt', 'data/3.txt', 'data/4.txt', 'data/5.txt']

for i in range(len(url_array)):

    request = requests.get(url_array[i])

    soup = BeautifulSoup((request.text), "lxml")

    main_information = soup.find('div', {'id' : 'bodyContent'})

    if i == len(library):
        filename = str(i + 1) + '.txt'
        library += ['data/' + filename]

    with open(library[i], 'w', encoding='utf8') as file:
        file.write(main_information.text)
