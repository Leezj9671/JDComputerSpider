# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class JdsPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['ID', '链接', '品牌', '商品名称', '电脑类型', '价格', '颜色', '屏幕尺寸',\
        '屏幕分辨率', 'cpu型号', '内存大小', '硬盘容量', '显卡型号', '显存容量', '系统', '重量',\
        '待机时长', '厚度', '1星评价', '2星评价', '3星评价', '4星评价', '5星评价', '评论总数'])
    
    def process_item(self, item, spider):
        # try:
        line = [item['ID'][0], item['link'][0], item['computerBrand'][0], item['computerName'], \
            item['computerType'], item['price'], item['color'], item['screenInches'], \
            item['screenFb'], item['cpu'], item['mem'], item['disk'], item['xianka'], \
            item['xiancun'], item['system'], item['weight'], item['daijishichang'], \
            item['houdu'], item['score1count'], item['score2count'], item['score3count'], \
            item['score4count'], item['score5count'], item['comment_num']
        ]
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('./jd_laptop.xlsx')  # 保存xlsx文件
        # except IndexError:
        #     print('*************************error****************************')
        #     print(item)
        
        return item
