#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 15 Task 3'''

import urllib2
from bs4 import BeautifulSoup

URL = 'http://sps.cuny.edu/whoweare/departments/it'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)


def sps_it_department():
    '''finds names and emails and puts in dict'''
    card_list = []

    cards = SOUP.find('div', {'class': 'list-view mam'})

    for person in cards:
        mailtos = cards.select('a[href^=mailto]')
        names = cards.findAll('span', {'class': 'name-bold'})

        for partof, entry in enumerate(names):
            last_first = entry.strip().split(',')
            card_dict = {
                'email': mailtos.get_text(),
                'first_name': last_first[1],
                'last_name': last_first[0]
            }
            return card_list.append(card_dict)


if __name__ == '__main__':
    sps_it_department()