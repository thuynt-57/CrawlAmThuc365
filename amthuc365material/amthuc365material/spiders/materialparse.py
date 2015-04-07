# -*- coding: utf-8 -*-
import scrapy

import MySQLdb
import datetime
from scrapy.http import Request
from amthuc365material.items import Amthuc365MaterialItem


class AmthucparseSpider(scrapy.Spider):
    name = "materialparse"
    allowed_domains = ["amthuc365.vn"]
    start_urls = (
        'http://www.amthuc365.vn/',
    )
    def parse(self, response):
        self.conn=MySQLdb.connect(user='root',passwd='cobala15111994',db='amthuc365',host='127.0.0.1',charset="utf8",use_unicode='True')
        self.cursor=self.conn.cursor()
        sql = "SELECT * FROM dish_material"
        try:
           # Execute the SQL command
           self.cursor.execute(sql)
           # Fetch all the rows in a list of lists.
           results = self.cursor.fetchall()
           for row in results:
				link = row[0]
				request = Request(link, callback=self.parse_item)
				request.meta['url'] = link
				yield request
        except:
           print "Error: unable to fecth data"

    def parse_item(self, response):
        for sel in response.xpath('//div[@class="recipe_component"]/ul[@class="recipe_component_list"]/li'):
            item = Amthuc365MaterialItem()
            item['link'] = response.meta['url']
        	# material
            material = sel.xpath('span[@class="ingredient"]/span[@class="name"]/a/text()').extract()
            if material:
                material = material[0].encode('utf-8')
                material = material.strip()
                item['material'] = material
            else:
                item['material'] = ''

            #value
            value = sel.xpath('span[@class="ingredient"]/span[@class="amount"]/span[@class="value"]/text()').extract()
            if value:
                value = value[0].encode('utf-8')
                value = value.strip()
                item['value'] = value
            else:
                item['value'] = ''

            # type
            mytype = sel.xpath('span[@class="ingredient"]/span[@class="amount"]/span[@class="type"]/text()').extract()

            if mytype:
                mytype = mytype[0].encode('utf-8')
                mytype = mytype.strip()
                item['mytype'] = mytype
            else:
                item['mytype'] = ''

            yield item