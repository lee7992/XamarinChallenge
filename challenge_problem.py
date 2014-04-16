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
import time
import re
from html import parser

from urllib.request import Request, urlopen   #lib for try/except
from urllib.error import URLError, HTTPError  #lib for try/except



website = urllib.request.urlopen('http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1')
websiteHTML = website.read()
    
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

soup =  BeautifulSoup(websiteHTML)

title_list = []
link_list = []
for n in soup.find_all('h4'):
    title = n.next_element.next_element
    #print(title)
    title_list.append(title)
    link = n.a['href']
    link_list.append(link)

#print(link_list)

newLink_list = []
for x in link_list:
    newLink = 'www.imdb.com'+x
    #print(newLink)
    newLink_list.append(newLink)

#print(title_list)    
#print(newLink_list)


if __name__ == '__main__':

    movielength = len(title_list)
    print('There are ', movielength, ' movies currently listed:')
    print('\n'.join(title_list))
    print('\n')

    linklength = len(newLink_list)
    print('There are ', linklength, ' links to movies listed:')
    print('\n'.join(newLink_list))
    time.sleep(10)


#print('title type: ', type(title_list[0]))
#print('link type: ', type(link_list[0]))
    #for link in soup.find_all('a'):
     #   print(link.get('href'))
        
#print(soup.find_all('h4'))
#websiteHTMLstr = bytes.decode(websiteHTML)
#links = re.findall('"((http|ftp)s?://.*?)"', websiteHTMLstr)





# List of Movie Titles as array list
'''
if __name__ == '__main__':
    
    print(title_list)
    time.sleep(10)
'''

# Time Record   
'''
Friday: ~6hrs studying/learning
Saturday: ~6hrs writing/coding
Wednesday: ~7hrs
'''


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
