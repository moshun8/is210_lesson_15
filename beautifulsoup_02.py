import urllib2
from bs4 import BeautifulSoup

URL = 'http://www.whitehouse.gov/net-neutrality'
DATA = urllib2.urlopen(URL).read()
HTML_SOUP = BeautifulSoup(DATA)

def obama_net_neutrality(HTML_SOUP):
    speech = HTML_SOUP.findAll('tt')
    for lines in speech:
        print lines
print obama_net_neutrality(HTML_SOUP)

# if __name__ == '__main__':
#     # You can use this conditional block for debugging
#     print HTML_SOUP
#     pass