# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanloginprojectItem(scrapy.Item):
    name = scrapy.Field() #日记标题
    href = scrapy.Field() #日记标题链接
    time = scrapy.Field() #日记发布时间
    content = scrapy.Field() #日记内容

