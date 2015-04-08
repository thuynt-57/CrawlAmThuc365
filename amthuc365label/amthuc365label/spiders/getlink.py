# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from amthuc365label.items import Amthuc365LabelItem


class Amthuc365getterSpider(scrapy.Spider):
    name = "getlink"
    allowed_domains = ["amthuc365.vn"]
    start_urls = (
        'http://www.amthuc365.vn',
    )

    retryProxy = False

    handle_httpstatus_list = [404]

    def start_requests(self):
        print 'Crawling............'
        yield Request(self.start_urls[0], callback=self.parse_category)

    def parse_category(self,response):
        if response.status != 404 and response.body:
            sel = Selector(response)

        link_cat = "http://www.amthuc365.vn/cong-thuc/trang-2.html"
        request = Request(link_cat, callback=self.parse_product)
        request.meta['link_cat'] = "http://www.amthuc365.vn/cong-thuc"
        request.meta['page'] = 2
        yield request


    def parse_product(self, response):
        sel = Selector(response)
        link_cat = response.meta['link_cat']
        page = response.meta['page']

        product_link =sel.xpath('/html/body/div[3]/div[3]/div[5]/div/div/ul/li/div/h3/a/@href').extract()

       
        if product_link:
            page +=1
            link = link_cat + "/trang-"+ str(page) +".html"
            request = Request(link, callback=self.parse_product)
            request.meta['link_cat'] = link_cat
            request.meta['page'] = page
            yield request

            for i in range(len(product_link)):
                item = Amthuc365LabelItem()
                item['link'] = self.start_urls[0] + product_link[i]
                yield item