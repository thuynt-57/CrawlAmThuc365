# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Amthuc365Item(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    guide = scrapy.Field()
    num_of_people = scrapy.Field()
    time_to_prepare = scrapy.Field()
    time_to_cook = scrapy.Field()
    addition = scrapy.Field()

