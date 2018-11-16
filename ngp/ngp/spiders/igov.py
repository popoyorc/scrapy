# -*- coding: utf-8 -*-
import scrapy

class IgovSpider(scrapy.Spider):
    name = 'igov'
    allowed_domains = ['i.gov.ph']
    start_urls = ['http://i.gov.ph/']

    def parse(self, response):
        for link in response.css('div#content > div.post-box h2.entry-title a::attr(href)'):
            yield response.follow(link, self.parse_post)

        prev_page = response.css('div.nav-previous a::attr(href)').extract_first()
        if prev_page is not None:
            yield response.follow(prev_page, self.parse)


    def parse_post(self, response):
        uid = response.url
        description = response.xpath('//div[@id="content"]/article/div/p/text()').extract()
        title = response.xpath("//meta[@property='og:title']/@content").extract_first()
        yield {
                'groupId' : "20142",
                'uid' : uid,
                'scopeGroupId': "20142",
                'description': description,
                'version': "",
                'companyId': "20115",
                'entryClassPK': "37950",
                'status': "0",
                'head': "true",
                'title': "http://i.gov.ph",
                'visible': "true",
                'url': "<a href='" + uid + "'><strong>" + title + "</strong></a>",
                'entryClassName': "com.liferay.bookmarks.model.BookmarksEntry",
                'roleId': ["20122", "20123"]
                }
            
