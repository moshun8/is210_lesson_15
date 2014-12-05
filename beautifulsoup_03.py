import urllib2
from bs4 import BeautifulSoup

URL = 'http://sps.cuny.edu/whoweare/departments/it'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)

def sps_it_department():
    '''finds names and emails and puts in dict'''
    card_list = []
    cards = SOUP.find_all('div', {'class': 'card unit size1of2'})
    names = cards.find_all('span', {'class': 'name-bold'})
    email = cards.find_all('a', {'href': 'mailto:'})
    name_dict = {}
    first = names[0]
    print first
    last = names[1]
    print last
    # name_dict[staff] = (first, last, email)

print sps_it_department

if __name__ == '__main__':
    # You can use this conditional block for debugging
    # print SOUP
    pass