# -*- coding: utf-8 -*-
import scrapy

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ["http://blog.jobbole.com/all-posts/"]

    def parse(self,response):
        pass