#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 15 Task 02 """

import urllib2
from bs4 import BeautifulSoup

URL = 'http://www.whitehouse.gov/net-neutrality'
DATA = urllib2.urlopen(URL).read()
HTML_SOUP = BeautifulSoup(DATA)


def obama_net_neutrality():
    '''obama speech docstring'''
    speech = HTML_SOUP.find_all('p', {'class': 'intro-paragraph'})
    for lines in speech:
        together = lines.contents[0]
    return together