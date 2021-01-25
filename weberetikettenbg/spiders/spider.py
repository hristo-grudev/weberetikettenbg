import re

import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import WeberetikettenbgItem


class WeberetikettenbgSpider(scrapy.Spider):
	name = 'weberetikettenbg'
	start_urls = ['http://weberetikettenbg.com/en/news.html',
	              'http://weberetikettenbg.com/bg/news.html',
	              'http://weberetikettenbg.com/ro/news.html']

	def parse(self, response, **kwargs):
		post_links = response.xpath('//div[@class="blog-container"]/a[@class="btn btn-gray"]/@href')
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//div[@class="col-lg-8 col-md-7 col-sm-12 col-xs-12"]/h1/text()').get().strip()
		description = response.xpath('//div[@class="col-lg-8 col-md-7 col-sm-12 col-xs-12"]/p').getall()
		description = ' '.join([remove_tags(p) for p in description]).strip()
		date = response.xpath('//div[@class="col-lg-8 col-md-7 col-sm-12 col-xs-12"]/div/ul/li/text()').get()
		lang = response.xpath('(//nav/ul/li/a)[2]/text()').get().strip()

		item = ItemLoader(item=WeberetikettenbgItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)
		item.add_value('lang', lang)
		print(title)

		return item.load_item()
