# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from douban.Utills.comment import *


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_url = scrapy.Field()
    movie_url_id = scrapy.Field()
    movie = scrapy.Field()
    movie_classify = scrapy.Field()
    movie_director = scrapy.Field()
    movie_scriptwriter = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_type = scrapy.Field()
    movie_country_areas = scrapy.Field()
    movie_language = scrapy.Field()
    movie_screen_time = scrapy.Field()
    movie_score = scrapy.Field()
    movie_comments_num = scrapy.Field()
    movie_hot_comments = scrapy.Field()
    movie_crawl_time = scrapy.Field()
    movie_crawl_update_time = scrapy.Field()


    #对itemloader生成额的movie数据精加工并插入到数据库
    def get_sql(self):
        insert_sql = '''
                      insert into movie(
                                    url,url_id,movie,classify,director,scriptwriter,
                                    actor,score,comments_num,screen_time,movie_type,country_areas,language,
                                    hot_comments,crawl_time
                                    )values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                      '''

        url = "".join(self.get("movie_url",""))
        url_id = "".join(self.get("movie_url_id",""))
        movie = get_ration_element(self.get("movie",""))
        classify = get_ration_element(self.get("movie_classify",""))
        director = get_ration_element(self.get("movie_director",""))
        scriptwriter = get_ration_element(self.get("movie_scriptwriter",""))
        actor = get_ration_element(self.get("movie_actor",""))
        type =  get_ration_element(self.get("movie_type",""))
        country_areas = get_ration_element(self.get("movie_country_areas",""))
        language = get_ration_element(self.get("movie_language",""))
        screen_time = get_date(self.get("movie_screen_time",""))
        score = get_num2(self.get("movie_score",""))
        comments_num = get_num1(self.get("movie_comments_num",""))
        hot_comments = get_hot_comments(self.get("movie_hot_comments",""))
        crawl_time = now()

        params = (url,url_id,movie,classify,director,scriptwriter,
                  actor,score,comments_num,screen_time,type,country_areas,language,
                  hot_comments,crawl_time)

        return insert_sql,params




class DoubanBookItem(scrapy.Item):
    book_url = scrapy.Field()
    book_url_id = scrapy.Field()
    book = scrapy.Field()
    book_writer = scrapy.Field()
    book_classify = scrapy.Field()
    book_publisher = scrapy.Field()
    book_publish_time = scrapy.Field()
    book_pages = scrapy.Field()
    book_price = scrapy.Field()
    book_type = scrapy.Field()
    book_ISBN = scrapy.Field()
    book_score = scrapy.Field()
    book_comments_num =scrapy.Field()
    book_hot_comments =scrapy.Field()
    book_crawl_time = scrapy.Field()
    book_update_time = scrapy.Field()


    # 对itemloader生成额的book数据精加工并插入到数据库
    def get_sql(self):
        insert_sql = '''
                      insert into book(
                                    url,url_id,book,writer,classify,publisher,
                                    publisher_time,price,page,book_type,ISBN,score,comments_num,
                                    hot_comments,crawl_time
                                    )values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                      '''

        url = "".join(self.get("book_url",""))
        url_id = "".join(self.get("book_url_id",""))
        book = get_ration_element(self.get("book",""))
        writer = get_writer(self.get("book_writer",""))
        classify = get_ration_element(self.get("book_classify",""))
        publisher = get_ration_element(self.get("book_publisher",""))
        publisher_time = get_date(self.get("book_publisher_time",""))
        price = get_num2(self.get("book_price",""))
        page = get_num1(self.get("book_pages",""))
        type = get_ration_element(self.get("book_type",""))
        ISBN = get_num1(self.get("book_ISBN",""))
        score = get_num2(self.get("book_score",""))
        comments_num = get_num1(self.get("book_comments_num",""))
        hot_comments = get_hot_comments(self.get("book_hot_comments",""))
        crawl_time = now()

        params = (url,url_id,book,writer,classify,publisher,
                  publisher_time,price,page,type,ISBN,score,comments_num,
                  hot_comments,crawl_time)

        return insert_sql,params




class DoubanMusicItem(scrapy.Item):
    music_url = scrapy.Field()
    music_url_id = scrapy.Field()
    music = scrapy.Field()
    music_performer = scrapy.Field()
    music_classify = scrapy.Field()
    music_media = scrapy.Field()
    music_release_time = scrapy.Field()
    music_publisher = scrapy.Field()
    music_score = scrapy.Field()
    music_comments_nums = scrapy.Field()
    music_hot_comments = scrapy.Field()
    music_crawl_time = scrapy.Field()
    music_update_time = scrapy.Field()


    # 对itemloader生成额的music数据精加工并插入到数据库
    def get_sql(self):
        insert_sql = '''
                      insert into music(
                                    url,url_id,music,performer,classify,media,
                                    release_time,publisher,score,comments_num,
                                    hot_comments,crawl_time
                                    )values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                      '''

        url = "".join(self.get("music_url",))
        url_id = "".join(self.get("music_url_id",""))
        music = get_ration_element(self.get("music",))
        performer = get_ration_element(self.get("music_performer",))
        classify = get_ration_element(self.get("music_classify",))
        media = get_ration_element(self.get("music_media",))
        release_time = get_date(self.get("music_release_time",))
        publisher = get_ration_element(self.get("music_publisher",))
        score = get_num2(self.get("music_score",))
        comments_nums = get_num1(self.get("music_comments_nums",))
        hot_comments = get_hot_comments(self.get("music_hot_comments",))
        crawl_time = now()
        params =(url,url_id,music,performer,classify,media,
                 release_time,publisher,score,comments_nums,
                 hot_comments,crawl_time)

        return insert_sql,params





