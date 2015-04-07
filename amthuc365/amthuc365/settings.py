# -*- coding: utf-8 -*-

# Scrapy settings for amthuc365 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'amthuc365'

SPIDER_MODULES = ['amthuc365.spiders']
NEWSPIDER_MODULE = 'amthuc365.spiders'

ITEM_PIPELINES = {
    'amthuc365.pipelines.Amthuc365Pipeline':800,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'amthuc365 (+http://www.yourdomain.com)'
