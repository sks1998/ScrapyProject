# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NaukriItem(scrapy.Item):
    job_title = scrapy.Field()
    exp_req = scrapy.Field()
    loc = scrapy.Field()
    comp_name = scrapy.Field()
    key_skills = scrapy.Field()
    job_desp = scrapy.Field()
    sal = scrapy.Field()
    job_desp_page = scrapy.Field()

