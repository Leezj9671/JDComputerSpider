# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.org/en/latest/topics/items.html

from scrapy import Item, Field

class JdsItem(Item):
    link = Field()   #链接1
    ID = Field() #ID1
    computerBrand = Field() #品牌1
    computerName = Field()  #名字1
    computerType = Field()   #电脑类型，待商榷1
    price = Field()  #价格
    color = Field()  #颜色1
    screenInches = Field()   #屏幕尺寸1
    screenFb = Field()   #屏幕分辨率1
    cpu = Field()    #cpu型号1
    mem = Field()    #内存大小1 
    disk = Field()   #硬盘容量1
    xianka = Field() #显卡型号1
    xiancun = Field()    #显存
    system = Field() #系统1
    weight = Field() #重量1
    daijishichang = Field()  #待机时长1
    houdu = Field()  #厚度1

    comment_num= Field() #顾客评论数
    score1count = Field()  # 评分为1星的人数
    score2count = Field()  # 评分为2星的人数
    score3count = Field()  # 评分为3星的人数
    score4count = Field()  # 评分为4星的人数
    score5count = Field()  # 评分为5星的人数
    # commentVersion = Field()  # 为了得到评论的地址需要该字段

class ItemDict():
    itemDict = {
        '商品名称': 'computerName',
        '系统': 'system',
        '厚度': 'houdu',
        '内存容量': 'mem',
        '分辨率' : 'screenFb',
        '显卡型号': 'xianka',
        '待机时长': 'daijishichang',
        '处理器': 'cpu',
        '裸机重量': 'weight',
        '硬盘容量': 'disk',
        '显存容量': 'xiancun',
        '分类': 'computerType',
        '屏幕尺寸': 'screenInches',
        '颜色': 'color'
    }
