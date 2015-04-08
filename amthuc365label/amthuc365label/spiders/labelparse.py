
# -*- coding: utf-8 -*-
import scrapy

import MySQLdb
import datetime
from scrapy.http import Request
from amthuc365label.items import Amthuc365LabelItem


class AmthucparseSpider(scrapy.Spider):
    name = "labelparse"
    allowed_domains = ["amthuc365.vn"]
    start_urls = (
        'http://www.amthuc365.vn/',
    )
    def parse(self, response):
        self.conn=MySQLdb.connect(user='root',passwd='cobala15111994',db='amthuc365',host='127.0.0.1',charset="utf8",use_unicode='True')
        self.cursor=self.conn.cursor()
        sql = "SELECT * FROM dish_label"
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
        for sel in response.xpath('//div[@class="recipe_group wrap mb5 mt10"]/a[@class="recipe_group_link mr5"]'):
            item = Amthuc365LabelItem()
            item['link'] = response.meta['url']
        	# label
            label = sel.xpath('text()').extract()
            if label:
                label = label[0].encode('utf-8')
                label = label.strip()
                item['label'] = label
            else:
                item['label'] = ''

            yield item