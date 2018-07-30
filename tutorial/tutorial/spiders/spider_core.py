#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:05:14 2018

@author: dakotashen
"""

from scrapy.spider import Spider
from scrapy.selector import Selector
# from scrapy import log
from tutorial.items import TutorialItem


class SpiderCore(Spider):
    name = 'GameContent'
    allowed_domains = ["gamespot.com"]
    start_urls = []
    
    urls = open('uandt.txt')
    # print type(urls.readline())
    for url in urls.readlines():
        u, t = url.split(';')
        start_urls.append('https://www.gamespot.com' + u)
    '''
    start_urls = []
    start_urls.append(start_url[5])
    start_urls.append(start_url[6])
    start_urls.append(start_url[7])
    '''
    
    
    def parse(self, response):
        sel = Selector(response)
        # sites = sel.xpath('//*[@id="js-sort-filter-results"]/section/article') 
        items = []
        # for site in sites:
        item = TutorialItem()
        
        # .extract(): return list
        # title = sel.xpath('//*[@id="kubrick-lead"]/div/div[1]/div/div/div/h1/text()').extract()
        
        # extract all reviewparagraphs for a review
        review = ''
        i = 1
        prev = ''
        while(True):
            cur = ''
            path = '//*[@id="default-content"]/div/article/section[2]/div[1]/p[' + str(i) +']' + '/text()'
            temp = sel.xpath(path).extract()
            for t in temp:
                cur += t.encode('utf-8')
            if cur == '' or cur == prev:
                break
            review = review + '\n' + cur
            prev = cur
            i = i + 1
            # print temp
            # print type(temp)
        '''   
        item['title'] = [t.encode('utf-8') for t in title]
        
        # delete front and end spaces for title
        for i in range(len(item['title'])):
            if len(item['title'][i]) != 0:
                item['title'][i] = item['title'][i].strip()
        '''        
        item['review'] = [review]
        
        # delete front and end spaces for review
        for i in range(len(item['review'])):
            if len(item['review'][i]) != 0:
                item['review'][i] = item['review'][i].strip()

        items.append(item)
            
            # print "item appending"
            # log.msg("Appending Item",'INFO')
            
        # log.msg("Appending Done",'INFO')
        # print "item appended"
        return items

    
'''
inner url xpath
//*[@id="js-sort-filter-results"]/section/article[1]/a/@href


title xpath
//*[@id="kubrick-lead"]/div/div[1]/div/div/div/h1
//*[@id="kubrick-lead"]/div/div[1]/div/div/div/h1
//*[@id="kubrick-lead"]/div/div[1]/div/div/div/h1
//*[@id="kubrick-lead"]/div[1]/div/div/div[2]/h1
//*[@id="kubrick-lead"]/div/div[1]/div/div/div/h1

//*[@id="default-content"]/div/article/section[1]/h1
//*[@id="default-content"]/div/article/section[1]/h1

//*[@id="kubrick-lead"]/div/div[1]/div/div/div/h1

//*[@id="kubrick-lead"]/div/div[1]/div/div/div/h1

//*[@id="kubrick-lead"]/div[1]/div/div/div[2]/h1



review xpath
//*[@id="default-content"]/div/article/section[2]/div[1]/p[2]
//*[@id="default-content"]/div/article/section[2]/div[1]/p[2]
//*[@id="default-content"]/div/article/section[2]/div[1]/p[2]
//*[@id="default-content"]/div/article/section[2]/div[1]/p[1]
//*[@id="default-content"]/div/article/section[1]/h1

//*[@id="default-content"]/div/article/section[2]/div[1]/p[1]

//*[@id="default-content"]/div/article/section[2]/div[1]/p[1]/text()
//*[@id="default-content"]/div/article/section[2]/div[1]/p[2]/text()
//*[@id="default-content"]/div/article/section[2]/div[1]/p[3]/text()

//*[@id="default-content"]/div/article/section[2]/div[1]/p[5]/text()


//*[@id="default-content"]/div/article/section[2]/div[1]/p[2]


'''