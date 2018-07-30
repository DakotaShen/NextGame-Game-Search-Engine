#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:12:13 2018

@author: dakotashen
"""

titles = open('/Users/dakotashen/Desktop/tm_project/data/tutorial/tutorial/spiders/uandt.txt')
reviews = open('/Users/dakotashen/Desktop/tm_project/data/tutorial/tutorial/spiders/review3.txt')

reviewsString = reviews.read()
uandtList = titles.readlines()


reviewList = reviewsString.split('!!!' + '\n')

for i in range(len(uandtList)):
    u, t = uandtList[i].split(';')
    t = t.strip()
    # print t 
    
    if '/' in t:
        t = t.replace('/', ':')
    firstWord = t.split('Review')[0].strip()
    if ':' in firstWord:
        firstWordList = firstWord.split(':')
        firstWord = firstWordList[len(firstWordList) - 1].strip()   
    if i > len(reviewList) - 1:
        break
    for j in range(len(reviewList)):
        if(reviewList[j] == ''):
            continue
        if firstWord in reviewList[j]:
            filename = '/Users/dakotashen/Desktop/tm_project/data/tutorial/tutorial/spiders/reviews3/' + t + '.txt'
            with open(filename, 'w') as f:
                f.write(reviewList[j])
    