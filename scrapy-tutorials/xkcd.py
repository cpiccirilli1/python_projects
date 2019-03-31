# -*- coding: utf-8 -*-
import scrapy


class XkcdSpider(scrapy.Spider):
    name = 'xkcd'
    allowed_domains = ['xkcd.com']
    start_urls = ['https://xkcd.com/']

    def parse(self, response):
        
    	img={"url": response.xpath('//img[(@srcset)]/@src').extract_first(),
    	}
    	yield img

    	prev = response.xpath('//a[(@accesskey="p")]/@href').extract_first()
    	if prev:
    		nextPG = response.urljoin(prev)
    		yield scrapy.Request(url=nextPG, callback=self.parse)



