# -*- coding: utf-8 -*-
import scrapy

import MySQLdb
import datetime
from scrapy.http import Request
from amthuc365.items import Amthuc365Item


class AmthucparseSpider(scrapy.Spider):
    name = "amthucparse"
    allowed_domains = ["amthuc365.vn"]
    start_urls = (
        'http://www.amthuc365.vn/',
    )
    def parse(self, response):
        self.conn=MySQLdb.connect(user='root',passwd='cobala15111994',db='amthuc365',host='127.0.0.1',charset="utf8",use_unicode='True')
        self.cursor=self.conn.cursor()
        sql = "SELECT * FROM dishes"
        try:
           # Execute the SQL command
           self.cursor.execute(sql)
           # Fetch all the rows in a list of lists.
           results = self.cursor.fetchall()
           for row in results:
				link = row[4]
				request = Request(link, callback=self.parse_item)
				request.meta['url'] = link
				yield request
        except:
           print "Error: unable to fecth data"

    def parse_item(self, response):
        for sel in response.xpath('//html/body/div[@id="container"]/div[@class="body-recipe recipe"]'):
            item = Amthuc365Item()
            item['link'] = response.meta['url']
        	# ten mon an
            title = sel.xpath('div[@class="content_recipe"]/div[@id="content"]/div[@class="wrap recipe_info_top_box"]/div[@class="r"]/h1[@class="title mb5"]/text()').extract()
            if title:
                title = title[0].encode('utf-8')
                title = title.strip()
                item['name'] = title
            else:
                item['name'] = ''

            #hinh dai dien
            image = sel.xpath('div[@class="content_recipe"]/div[@id="content"]/div[@class="wrap recipe_info_top_box"]/div[@class="box_photo_recipe"]/div[@class="img_recipe"]/img[@id="image_zoom"]/@src').extract()
            if image:
                image =image[0].encode('utf-8')
                image=image.strip()
                item['image'] = image
            else:
                item['image'] = ''

            # cong thuc
            guide = sel.xpath('//div[@class="recipe_guide"]/ul[@class="recipe_guide_list"]/li/text()').extract()

            if guide:
                guide = guide[0].encode('utf-8')
                guide = guide.strip()
                item['guide'] = guide
            else:
                item['guide'] = ''

            # nguyen lieu
            # nguyen_lieu = sel.xpath('//div[@class="recipe_component"]/ul[@class="recipe_component_list"]/li').extract()
            # if nguyen_lieu:
            #     nguyen_lieu = nguyen_lieu[0].encode('utf-8')
            #     nguyen_lieu = nguyen_lieu.strip()
            #     item['nguyen_lieu'] = nguyen_lieu
            # else:
            #     item['nguyen_lieu'] = ''

            # nhan
            # nhan = sel.xpath('div[@class="content_recipe"]/div[@id="content"]/div[@class="wrap recipe_info_top_box"]/div[@class="r"]/div[@class="recipe_group wrap mb5 mt10"]/a/text()').extract()
            # if nhan:
            #     nhan = nhan[0].encode('utf-8')
            #     nhan = nhan.strip()
            #     item['nhan'] = nhan
            # else:
            #     item['nhan'] = ''

            # so nguoi an
            num_of_people = sel.xpath('div[@class="content_recipe"]/div[@id="content"]/div[@class="wrap recipe_info_top_box"]/div[@class="r"]/div[@class="recipe_componemt mt20"]/ul/li[1]/text()').extract()
            if num_of_people:
                item['num_of_people'] = num_of_people
            else:
                item['num_of_people'] = response.meta['num_of_people']

            # thoi gian chuan bi
            time_to_prepare = sel.xpath('div[@class="content_recipe"]/div[@id="content"]/div[@class="wrap recipe_info_top_box"]/div[@class="r"]/div[@class="recipe_componemt mt20"]/ul/li[2]/text()').extract()
            if time_to_prepare:
                item['time_to_prepare'] = time_to_prepare
            else:
                item['time_to_prepare'] = response.meta['time_to_prepare']

            # thoi gian thuc hien
            time_to_cook = sel.xpath('div[@class="content_recipe"]/div[@id="content"]/div[@class="wrap recipe_info_top_box"]/div[@class="r"]/div[@class="recipe_componemt mt20"]/ul/li[3]/text()').extract()
            if time_to_cook:
                item['time_to_cook'] = time_to_cook
            else:
                item['time_to_cook'] = response.meta['time_to_cook']

            # thong tin them
            addition = sel.xpath('//div[@class="recipe_guide"]/div[@class="formatTextStandard"]/p/text()').extract()
            if addition:
                addition = addition[0].encode('utf-8')
                addition = addition.strip()
                item['addition'] = addition
            else:
                item['addition'] = ''
            yield item