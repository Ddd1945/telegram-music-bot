import requests
from bs4 import BeautifulSoup


def parse_page(archive_url):
    response_first = requests.get(archive_url).text
    soup_first = BeautifulSoup(response_first, 'lxml')

    block_first = soup_first.find('main', class_='content')
    block_second = block_first.find('div', class_='container')
    block_third = block_second.find('div', id='pjax-container')
    block_fourth = block_third.find('div', class_='content-inner')
    block_fifth = block_fourth.find('div', class_='p-info p-inner')
    block_sixth = block_fifth.find('ul', class_='tracks__list')
    block_seventh = block_sixth.find_all('li', class_='tracks__item track mustoggler')
    soup_second = BeautifulSoup(str(block_seventh), 'lxml').find_all('div', 'track__info-r')

    links = []
    for tag in soup_second:
        links.append(tag.a.get('href'))

    return links
