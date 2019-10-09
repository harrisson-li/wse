# -*- coding: utf-8 -*-
import json

import scrapy
import win_unicode_console

from wse.items import WseItem

win_unicode_console.enable()
import time


class CitySpider(scrapy.Spider):
    name = 'city'
    allowed_domains = ['wse.com.cn']
    start_urls = ['https://wse.com.cn/']

    def parse(self, response):
        request_url_list = ["https://wse.com.cn/zh/our-locations/centers/?cityId=CN-11-1",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-31-1",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-44-4",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-32-1",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-12-1",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-44-5",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-32-7",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-33-5",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-34-6",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-37-17",
                            "https://wse.com.cn/zh/our-locations/centers/?cityId=CN-44-13"
                            ]

        for url in request_url_list:
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        js = json.loads(response.body_as_unicode())

        city = WseItem()

        city['name'] = js['centers'][0]['address']['cityName']
        print(city['name'])

        city['number'] = len(js['centers'])
        print(len(js['centers']))

        city['center'] = []

        for center in js['centers']:
            print(center['centerName'])
            city['center'].append(center['centerName'])

        city['date'] = time.strftime("%Y-%m-%d")

        yield city
