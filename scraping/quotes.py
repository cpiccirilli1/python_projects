# -*- coding: utf-8 -*-
import scrapy


class MultipleQuotesSpider(scrapy.Spider):
    name = 'multiple-quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
 
        for quote in response.xpath('//div[(@class="quote")]'):
        	info = {'Author': quote.css('small.author::text').extract_first(),
        	'Quote': quote.css('span.text::text').extract_first(),
        	'Tags': quote.css('a.tag::text').extract(),
        	}
        	

        	yield info

        next_page = response.css('li.next > a::attr(href)').extract_first()
        if next_page:
        	next_page = response.urljoin(next_page)
        	yield scrapy.Request(url=next_page, callback=self.parse)	
        	    	