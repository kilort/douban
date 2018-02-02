# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import  re
from scrapy.http import Request
import json
from douban.items import DoubanMovieItem,DoubanMusicItem,DoubanBookItem
from scrapy.loader import ItemLoader
from douban.Utills.comment import get_md5
import datetime
from scrapy_redis.spiders import RedisSpider



class BasicDoubanSpider(RedisSpider):
    name = 'basic_douban'
    redis_key = 'DouBan:start_urls'
    # allowed_domains = ['www.douban.com']
    # start_urls = [  'https://music.douban.com/tag/',#音乐所有分类
    #                 'https://movie.douban.com/tag/#/',#电影所有分类
    #                 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all',#书所有分类
    #                 ]

    def parse(self, response):
        if 'movie' in response.url:
            movie_api_list =['https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0',
                            'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E8%A7%86%E5%89%A7&start=0',
                            'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%BB%BC%E8%89%BA&start=0',
                            'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%8A%A8%E7%94%BB&start=0',
                            'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%9F%AD%E7%89%87&start=0'
                             ]

            for movie_api in movie_api_list:
                yield Request(url=movie_api, callback=self.parse_detial,meta={'cookiejar':1})

        else:
            all_urls = response.xpath('//a/@href').extract()
            if all_urls:
                all_urls = list(set([parse.urljoin(response.url,i) for i in all_urls]))
                for this_url in all_urls:
                    key_url = re.compile('(.*douban\.com/tag/.*)',re.DOTALL).findall(this_url)
                    if key_url:
                        key_url = key_url[0]
                        yield Request(url=key_url, callback=self.parse_detial,meta={'cookiejar':1})


    def parse_detial(self,response):
        if 'movie' in response.url:
            tag1='movie'
            movie_json = json.loads(response.text)
            movie_tag = re.compile('.*&tags=(.*?)&.*').findall(response.url)
            if movie_tag:
                movie_tag = parse.unquote(movie_tag[0])
            else:
                movie_tag="None"
            for detial_url in movie_json["data"]:
                detial_url = detial_url["url"]
                if detial_url:
                    yield Request(url =detial_url,callback=self.get_data,meta={'cookiejar':response.meta["cookiejar"],'tag1':tag1,'tag2':'{0}'.format(movie_tag)})
            start = re.match(r'.*start=(\d+)',response.url)
            if start:
                num = str(int(start.group(1))+20)
                page =re.compile('start=\d+')
                next_movie_api =page.sub('start={0}'.format(num),response.url)
                if next_movie_api:
                    yield Request(url=next_movie_api,callback=self.parse_detial,meta={'cookiejar':response.meta["cookiejar"]})

        else:
            anthor_tag = re.compile('tag/(.*?)($|\?.*)').findall(response.url)
            if anthor_tag:
                anthor_tag=parse.unquote(anthor_tag[0][0])
            else:
                anthor_tag="None"
            if 'music' in response.url:
                tag1 = 'music'
                detial_url_list =response.xpath('//table[@width="100%%"]/tr/td[@width="100"]/a/@href').extract()
            else:
                tag1='book'
                detial_url_list = response.xpath('//li[@class="subject-item"]/div[2]/h2/a/@href').extract()
            if detial_url_list:
                for detial_url in detial_url_list:
                    detial_url = parse.urljoin(response.url,detial_url)
                    yield Request(url=detial_url,callback=self.get_data,meta={'cookiejar':response.meta["cookiejar"],'tag1':tag1,'tag2':'{0}'.format(anthor_tag)})
            next_url = response.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href').extract()
            if next_url:
                next_url = parse.urljoin(response.url,next_url[0])
                yield Request(url=next_url,callback=self.parse_detial,meta={'cookiejar':response.meta["cookiejar"]})


    def get_data(self,response):
        if response.meta["tag1"] == 'movie':
            movie_item_loader =ItemLoader(item=DoubanMovieItem(),response=response)
            movie_item_loader.add_value('movie_url',response.url)
            movie_item_loader.add_value('movie_url_id',get_md5(response.url))
            movie_item_loader.add_xpath('movie','//div[@id="wrapper"]/div[@id="content"]/h1/span[1]/text()')
            movie_item_loader.add_value('movie_classify',response.meta.get("tag2",""))
            movie_item_loader.add_xpath('movie_director','//div[@class="subject clearfix"]/div[@id="info"]/span[1]/span[@class="attrs"]/a/text()')
            movie_item_loader.add_xpath('movie_scriptwriter','//div[@class="subject clearfix"]/div[@id="info"]/span[2]/span[@class="attrs"]/a/text()')
            movie_item_loader.add_xpath('movie_actor','//div[@class="subject clearfix"]/div[@id="info"]/span[@class="actor"]/span[@class="attrs"]/a/text()')
            movie_item_loader.add_xpath('movie_type','//span[@property="v:genre"]/text()')
            movie_item_loader.add_value('movie_country_areas',re.compile('制片国家/地区:.*?>(.*?)<',re.DOTALL).findall(response.text))
            movie_item_loader.add_value('movie_language',re.compile('语言:.*?>(.*?)<',re.DOTALL).findall(response.text))
            movie_item_loader.add_xpath('movie_screen_time','//span[@property="v:initialReleaseDate"]/text()')
            movie_item_loader.add_xpath('movie_score','//div[@class="rating_self clearfix"]/strong/text()')
            movie_item_loader.add_xpath('movie_comments_num','//div[@class="rating_self clearfix"]/div/div/a/span/text()')
            movie_item_loader.add_xpath('movie_hot_comments','//div[@id="hot-comments"]/div/div/p/text()')
            movie_item_loader.add_value('movie_crawl_time',datetime.datetime.now())
            movie_item = movie_item_loader.load_item()
            yield movie_item

        elif response.meta["tag1"] =="book":
            book_item_loader = ItemLoader(item=DoubanBookItem(), response=response)
            book_item_loader.add_value('book_url', response.url)
            book_item_loader.add_value('book_url_id', get_md5(response.url))
            book_item_loader.add_xpath('book', '//div[@id="wrapper"]/h1/span/text()')
            book_item_loader.add_value('book_writer',re.compile('作者</span>.*?<a.*?>(.*?)<',re.DOTALL).findall(response.text))
            book_item_loader.add_value('book_classify',response.meta.get("tag2",""))
            book_item_loader.add_value('book_publisher',re.compile('出版社:.*?>(.*?)<',re.DOTALL).findall(response.text))
            book_item_loader.add_value('book_publish_time',re.compile('出版年:.*?>(.*?)<',re.DOTALL).findall(response.text))
            book_item_loader.add_value('book_pages',re.compile('页数:.*?>(.*?)<',re.DOTALL).findall(response.text))
            book_item_loader.add_value('book_price',re.compile('定价:.*?>(.*?)<',re.DOTALL).findall(response.text))
            book_item_loader.add_value('book_type',re.compile('装帧:.*?>(.*?)<',re.DOTALL).findall(response.text))
            book_item_loader.add_value('book_ISBN',re.compile('ISBN:.*?>(.*?)<',re.DOTALL).findall(response.text))
            book_item_loader.add_xpath('book_score','//div[@class="rating_self clearfix"]/strong/text()')
            book_item_loader.add_xpath('book_comments_num','//div[@class="rating_self clearfix"]/div[@class="rating_right "]/div[@class="rating_sum"]/span/a/span/text()')
            book_item_loader.add_xpath('book_hot_comments','//div[@class="comment-list hot show"]/ul/li/div/p/text()')
            book_item_loader.add_value('book_crawl_time',datetime.datetime.now())
            book_item = book_item_loader.load_item()
            yield book_item

        elif response.meta["tag1"] =="music":
            music_item_loader = ItemLoader(item=DoubanMusicItem(), response=response)
            music_item_loader.add_value('music_url', response.url)
            music_item_loader.add_value('music_url_id', get_md5(response.url))
            music_item_loader.add_xpath('music', '//div[@id="wrapper"]/h1/span/text()')
            music_item_loader.add_value('music_performer',re.compile('表演者:.*?>(.*?)<', re.DOTALL).findall(response.text))
            music_item_loader.add_value('music_classify',response.meta.get("tag2",""))
            music_item_loader.add_value('music_media',re.compile('介质:.*?>(.*?)<', re.DOTALL).findall(response.text))
            music_item_loader.add_value('music_release_time',re.compile('发行时间:.*?>(.*?)<', re.DOTALL).findall(response.text))
            music_item_loader.add_value('music_publisher',re.compile('出版者:.*?>(.*?)<', re.DOTALL).findall(response.text))
            music_item_loader.add_xpath('music_score','//div[@class="rating_self clearfix"]/strong/text()')
            music_item_loader.add_xpath('music_comments_nums','//div[@class="rating_self clearfix"]/div[@class="rating_right "]/div[@class="rating_sum"]/a/span/text()')
            music_item_loader.add_xpath('music_hot_comments','//div[@class="comment-list hot show"]/ul/li/div/p/text()')
            music_item_loader.add_value('music_crawl_time',datetime.datetime.now())
            music_item = music_item_loader.load_item()
            yield music_item

        else:
            pass




