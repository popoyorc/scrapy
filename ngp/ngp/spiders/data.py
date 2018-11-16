# -*- coding: utf-8 -*-
import scrapy


class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['dev.data.gov.ph']
    start_urls = ['http://dev.data.gov.ph/search/type/dataset']
    def parse(self, response):
        for link in response.css('div.view-content > div > article > div.search-result a::attr(href)'):
            yield response.follow(link, self.parse_dataset)

        next_page =response.css('ul.pagination.pager > li.pager-next > a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page,self.parse)

    def parse_dataset(self, response):
        ds = response.css("div.radix-layouts-content h2.pane-title::text").extract_first().strip()
        
        uid = response.url
        description = response.css('div.radix-layouts-content > div > div > div > article > div > div > div > div p::text').extract()
        assetTagNames = response.css('ul.resource-list li div >  a::text').extract()
        yield{
                    'groupId' : "20142",
                    'scopeGroupId' : "20142",
                    'version' : "",
                    'status' : "0",
                    'head' : "true",
                    'visible' : "true",
                    'companyId': "20115",
                    'entryClassPK' : "41051",
                    'entryClassName' : "com.liferay.bookmarks.model.BookmarksEntry",

                    'assetTagNames' : assetTagNames,
                    'description' : description,
                    'uid' : uid,
                    'title' : "htt://data.gov.ph",
                    
                    'url' : "<a href='"+ uid +"'><strong>" + ds + "</strong></a>",
                    'roleId' : ["20122", "20123"]
                }

