# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DaomubijiItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookOrder = Field()  # 书编号
    bookName = Field()  # 书标号
    chapterFirst = Field()  # 章节类别
    chapterMid = Field()  # 章节序号
    chapterLast = Field()  # 章节名称
    content = Field()
