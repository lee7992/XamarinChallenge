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



# input 'dob' is string
def BirthDate(dob):
    length = len(dob)
    if length == 6:
        year = dob[0:4]
        #print('Year: ', year)
        month = dob[4]
        #print('Month: ', month)
        day = dob[5]
        #print('Day: ', day)
        #print('\n')
    elif length == 7:
        year = dob[0:4]
        #print('Year: ', year)
        month = dob[4]
        #print('Month: ', month)
        day = dob[5:length]
        #print('Day: ', day)
        #print('\n')
    elif length == 8:
        year = dob[0:4]
        #print('Year: ', year)
        month = dob[4:6]
        #print('Month: ', month)
        day = dob[6:length]
        #print('Day: ', day)
        #print('\n')
    else:
        print('Error: DOB is not of specified length\n')

    year = int(year)
    month = int(month)
    day = int(day)

    return(year, month, day)




website = urllib.request.urlopen('http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1')
websiteHTML = website.read()
    
req = Request('http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1')
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.\n')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.\n')
    print('Reason: ', e.reason)
else:
    print('URL has been opened.\n')

soup =  BeautifulSoup(websiteHTML)

title_list = []
link_list = []
for n in soup.find_all('h4'):
    title = n.next_element.next_element
    #print(title)
    title_list.append(title)
    link = n.a['href']
    link_list.append(link)

print(link_list)

movLink_list = []
for x in link_list:
    movLink = 'http://www.imdb.com'+x
    #print(movLink)
    movLink_list.append(movLink)

print(title_list)    
print(movLink_list)

#print(newLink_list[0])

actor_list = []
actor_siteList = []
actorLink_list = []

l = len(link_list)
print('Number of links: ', l, '\n')

for x in range(l):
    mov_site = urllib.request.urlopen(movLink_list[x])
    mov_siteHTML = mov_site.read()
    
    new_req = Request(movLink_list[x])
    try:
        response = urlopen(new_req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print('URL has been opened.')

    movie_soup = BeautifulSoup(mov_siteHTML)

    print('Actor list ', x, '\n')
    for table in movie_soup.find_all('td', {"class":"primary_photo"}):
        actor = table.img['title']
        actor_list.append(actor)
        #print(actor)
        actor_site = table.a['href']
        actor_siteList.append(actor_site)
        #print('Link: ', actor_site)

        actorLink = 'http://www.imdb.com'+actor_site
        #print('\t', actorLink)
        actorLink_list.append(actorLink)
    print('\n')
print(actor_list)
print(actorLink_list)


l2 = len(actorLink_list)
print('Number of links: ', l2, '\n')
cur_Date = time.strftime("%Y%m%d")
cur_Y, cur_M, cur_D = BirthDate(cur_Date)

for x2 in range(l2):
    act_site = urllib.request.urlopen(actorLink_list[x2])
    act_siteHTML = act_site.read()

    act_req = Request(actorLink_list[x2])
    try:
        response = urlopen(act_req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print('URL has been opened.')

    actor_soup = BeautifulSoup(act_siteHTML)

    print('Actor: ', actor_list[x2])
    print(actorLink_list[x2])  


        
    for date in actor_soup.find_all('div', {"id":"name-born-info"}):
        
        try:
            dob = date.time['datetime']
        except TypeError:
            print('There is no DOB available.\n')
            continue
        else:
            pass
        
        print('DOB: ', dob)
        dob = dob.replace("-", "")
        print(dob)

        year, month, day = BirthDate(dob)

        print('Year: ', year)
        print('Month: ', month)
        print('Day: ', day)

        cur_Y, cur_M, cur_D

        if cur_M > month:
            age = cur_Y - year
        elif cur_M < month:
            age = cur_Y - year - 1
        elif cur_M == month:
            if cur_D >= day:
                age = cur_Y - year
            else:
                age = cur_Y - year - 1

        
        

        
'''
    # input 'dob' is string
    def BirthDate(dob):
        length = len(dob)
        if length == 6:
            year = dob[0:4]
            print('Year: ', year)
            month = dob[4]
            print('Month: ', month)
            day = dob[5]
            print('Day: ', day)
            print('\n')
        elif length == 7:
            year = dob[0:4]
            print('Year: ', year)
            month = dob[4]
            print('Month: ', month)
            day = dob[5:length]
            print('Day: ', day)
            print('\n')
        elif length == 8:
            year = dob[0:4]
            print('Year: ', year)
            month = dob[4:6]
            print('Month: ', month)
            day = dob[6:length]
            print('Day: ', day)
            print('\n')
        else:
            print('Error: DOB is not of specified length\n')

        year = int(year)
        month = int(month)
        day = int(day)

        return('Year: ':year, '\nMonth: ':month, '\nDay: ':day)
 '''       


# input 'ages' should be list
def average_age(ages):
    total = 0
    for n in range(len(ages)):
        total = avg + ages[n]
    avg = total/len(ages)
    print(avg)
    return avg


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
Wednesday: ~9hrs
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
