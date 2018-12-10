# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class ProxytempSpider(scrapy.Spider):
    name = 'proxytemp'
    allowed_domains = ['chinaz.com']
    # start_urls = ['http://chinaz.com/']

    def start_requests(self):
        for _ in range(1,20):
            url = "http://2018.ip138.com/ic.asp"
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # print(response.css("center::text").extract_first)
        print(Selector(text=response.body.decode("gb2312")).xpath('//center/text()').extract())
