# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import os

'''
class TutorialPipeline(object):
    def __init__(self):
        self.file = codecs.open('review.json', 'wb', encoding = 'utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        # print line
        self.file.write(line.decode('unicode_escape'));
        return item
'''
class TutorialPipeline(object):#需要在setting.py里设置'coolscrapy.piplines.CoolscrapyPipeline':300
     def process_item(self, item, spider):
         
         # 获取当前工作目录
         # base_dir = os.getcwd()
         # fiename = base_dir + '/url.txt'
         
         # write urls to url.txt
         '''
         filename = 'url.txt'
         # 从内存以追加的方式打开文件，并写入对应的数据
         
         
         with open(filename, 'a') as f:
             for url in item['url']:
                 print type(url)
                 f.write(url + '\n') 
             # print type(item['title'])
         return item
         
         # write title and review to txt
         filename = 'review2.txt'
         with open(filename, 'a') as f:
             for i in range(len(item['review'])):
                 if len(item['title']) != 0:
                     f.write(item['title'][i] + ',' + item['review'][i] + '\n') 
                 # print type(item['review'][i])
         return item
     
         # build several files, write title to filename and review to txt 
         for i in range(len(item['review'])):
             # review empty,continue 
             if len(item['review'][i]) == 0:
                 continue
             if i > len(item['title']) - 1:
                 break
             title = item['title'][i]
             if len(title) != 0:
                 filename = '/Users/dakotashen/Desktop/tm_project/data/tutorial/tutorial/spiders/reviews4/' + title + '.txt'
                 with open(filename, 'a') as f:
                     f.write(item['review'][i])
         return item
         
         
         # write urls and title to urland title.txt
         filename = 'uandt.txt'
         with open(filename, 'a') as f:
             for i in range(len(item['url'])):
                 f.write(item['url'][i] + ';' + item['title'][i] + '\n') 
         return item
         
         # 从内存以追加的方式打开文件，并写入对应的数据
         '''
         
         # build several files, write latest title to filename and review to txt 
         '''
         titles = open('uandt.txt')
         titleList = titles.readlines()
         print len(item['review'])
         '''
        
         # review empty,continue
         filename = '/Users/dakotashen/Desktop/tm_project/data/tutorial/tutorial/spiders/review3.txt'
         with open(filename, 'a') as f:
             if len(item['review']) == 0:
                 f.write('!!!' + '\n')
             else:
                 f.write(item['review'][0] + '!!!' + '\n')
         return item
         
         