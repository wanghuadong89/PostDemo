# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    # start_urls = ['http://baidu.com/']
    #
    # def parse(self, response):
    #     pass
    # 如果用post请求，需要重写下载的调度
    def start_requests(self):
        # 这个方法请求还没有发起的时候调用
        post_url = "http://fanyi.baidu.com/sug"
        # 请求体
        data = {
            "kw":"hello"
        }

        # 发起post请求
        yield scrapy.FormRequest(url=post_url,formdata=data,callback=self.parse_post)


    def parse_post(self,response):
        print(response.text)
        pass





