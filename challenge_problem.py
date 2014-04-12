#############
# Rachel Lee
# Xamarin Challenge Problem
# Release Engineer
############

import urllib
import json
import requests
import string
from bs4 import BeautifulSoup

from urllib.request import Request, urlopen   #lib for try/except
from urllib.error import URLError, HTTPError  #lib for try/except

website = urllib.request.urlopen('http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1')
websiteHTML = website.read()
#print(websiteHTML)

req = Request('http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1')
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    print('URL has been opened.')

soup = BeautifulSoup(websiteHTML)

title_list = []
for n in soup.find_all('h4'):
    title = n.next_element.next_element
    print(title)
    title_list.append(title)
    






# Code to list all tags under 'h4'
"""
head4_tag = soup.find_all('h4')
print(head4_tag, end=' ')
"""

# Unnessary code, personal trial/error reference
"""
newsoup = BeautifulSoup(head4_tag)
x=newsoup.find_all('h4')
    #print(soup.find_all('a'))
   

for title in head4_tag:
    print(head4_tag.findAll)
 

#print(soup.find_all('h4'))
#print(soup.h4.contents)
"""
