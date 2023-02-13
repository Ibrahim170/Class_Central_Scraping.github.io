from bs4 import BeautifulSoup
import requests

link = 'https://pypi.org/project/selenium/'

s = requests.get(link)
soup = BeautifulSoup(s.content , 'lxml')
print(soup)