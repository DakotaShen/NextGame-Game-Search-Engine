#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:39:33 2018

@author: dakotashen
"""

from scrapy.spider import Spider
from scrapy.selector import Selector
# from scrapy import log
from tutorial.items import TutorialItem


class Spider(Spider):
    name = 'GameReview'
    allowed_domains = ["gamespot.com"]
    start_urls = []
    for page in range(502):
        if page == 0: continue
        url = 'https://www.gamespot.com/reviews/?page=' + str(page + 1)
        start_urls.append(url)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="js-sort-filter-results"]/section/article') 
        items = []
        
        for site in sites:
            item = TutorialItem()
            # title = site.xpath('a/div[2]/h3/text()').extract() 
            # content = site.xpath('a/div[2]/p/text()').extract() # //*[@id="js-sort-filter-results"]/section/article[2]/a/div[2]/p/text()
            # item['title'] = [t.encode('utf-8') for t in title]
            # item['content'] = [c.encode('utf-8') for c in content]
            url = site.xpath('a/@href').extract()
            title = site.xpath('a/div[2]/h3/text()').extract()
            item['url'] =  [u.encode('utf-8') for u in url]
            item['title'] = [t.encode('utf-8') for t in title]
            items.append(item)
            # print "item appending"
            # log.msg("Appending Item",'INFO')
            
        # log.msg("Appending Done",'INFO')
        # print "item appended"
        
        # print items
        '''
        print 'len item is: ' + str(len(item['url']))
        for i in range(len(item['url'])):
            print item['title'][i]
        '''
        return items
    
'''
inner url xpath
//*[@id="js-sort-filter-results"]/section/article[1]/a/@href


title xpath
//*[@id="kubrick-lead"]/div/div[1]/div/div/div/h1
//*[@id="kubrick-lead"]/div/div[1]/div/div/div/h1

url title 
review not exist and title file exist: continue

review xpath
//*[@id="default-content"]/div/article/section[2]/div[1]/p[2]
//*[@id="default-content"]/div/article/section[2]/div[1]/p[2]
'''