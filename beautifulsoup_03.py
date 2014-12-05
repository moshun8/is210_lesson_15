import urllib2
from bs4 import BeautifulSoup

URL = 'http://sps.cuny.edu/whoweare/departments/it'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)

def sps_it_department():
    '''finds names and emails and puts in dict'''
    card_list = []

    cards = SOUP.find_all('div', {'class': 'card unit size1of2'})   
    # cards = SOUP.find('div', {'class':'card unit size1of2'})

    names = SOUP.find_all('span', {'class': 'name-bold'})

    mailtos = SOUP.select('a[href^=mailto]')

    name_dict = {}

    for entry in cards:
        card_dict = {}

    # name_dict[staff] = (first, last, email)


if __name__ == '__main__':
    sps_it_department()