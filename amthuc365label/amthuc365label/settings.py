# -*- coding: utf-8 -*-

# Scrapy settings for amthuc365label project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'amthuc365label'

SPIDER_MODULES = ['amthuc365label.spiders']
NEWSPIDER_MODULE = 'amthuc365label.spiders'

ITEM_PIPELINES = {
    'amthuc365label.pipelines.Amthuc365LabelPipeline':800,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'amthuc365label (+http://www.yourdomain.com)'
