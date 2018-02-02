# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs,json
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors
import datetime
import pymysql.cursors
from douban.settings import *


class MysqlTwistedPipeline(object):
    #通过twisted框架调用adbapi实现异步的数据写入
    def __init__(self,dbpool):
        self.dbpool = dbpool


    @classmethod
    def from_settings(cls,settings):
        #通过settings中设置的数据库信息，将数据库导入到pool中
        dbparms =dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            password = settings["MYSQL_PASSWORD"],
            charset = "utf8mb4",
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb",**dbparms)
        return cls(dbpool)


    def process_item(self,item,spider):
        #调用twisted的api实现异步插入
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_err,item,spider)

    def handle_err(self,failure,item,spider):
        print(failure)

    def do_insert(self,cursor,item):
        #具体的插入函数
        #根据不同的item，构建不同的sql语句，并且插入到mysql中
        #plan1 if item.__class__.__name__ =="ArticleItem" (通过item的名字来区别sql语句的写入)

        #plan 2 见items
        insert_sql,params =item.get_sql()
        print(params)
        cursor.execute(insert_sql,params)



class MysqlPipeline(object):
    #采用同步的机制写入mysql
    def __init__(self):
        self.conn = MySQLdb.connect(
            host = MYSQL_HOST,
            db = MYSQL_DBNAME,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD,
            charset = "utf8",
            use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        inser_sql,params = item.get_sql()
        print(params)
        self.cursor.execute(inser_sql,params)
        self.conn.commit()
        return item




