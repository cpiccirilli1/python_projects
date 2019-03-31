# -*- coding: utf-8 -*-
import scrapy


class InspirationalSpider(scrapy.Spider):
    name = 'inspirational'
    allowed_domains = ['inspirationalshit.com']
    start_urls = ['http://inspirationalshit.com/quotes/']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        yield {"author": response.css('cite::text').extract(),
        "quote": response.xpath('//p[contains(@style, "vertical-align")]/text()').extract(),		
        }
