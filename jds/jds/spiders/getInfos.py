import scrapy
import re
import json
from jds.items import JdsItem, ItemDict

class getInfosSpider(scrapy.Spider):
    name = "getInfos"
    start_urls = ['https://list.jd.com/list.html?cat=670,671,672&page='+str(i) for i in range(1, 100)]
    
    def parse(self, response):  # 解析搜索页  
        sel = scrapy.Selector(response)  # Xpath选择器  //*[@id="plist"]/ul/li[1]
        goods = sel.xpath('//li[@class="gl-item"]')  
        # print('****goods: {}'.format(len(goods)))
        for good in goods:
            item1 = JdsItem()
            item1['ID'] = good.xpath('./div/@data-sku').extract()
            # print(good.xpath('./div/div[@class="p-name"]/a/@href').extract())
            
            try:
                item1['link'] = good.xpath('./div/div[@class="p-name"]/a/@href').extract()
                url = "http:" + item1['link'][0]
            except Exception:
                pass
                # print(good.xpath('./div/div[@class="p-name"]/a').extract())
            yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_detail)

    def parse_detail(self, response):
        item1 = response.meta['item']
        sel = scrapy.Selector(response)
        #收集相关信息
        item1['computerBrand'] = sel.xpath('//*[@id="parameter-brand"]/li/a[1]/text()').extract()
        infos_lst = sel.xpath('//ul[@class="parameter2 p-parameter-list"]/li/text()').extract()
        #可能没有电脑类型和厚度，先赋值以防错误
        item1["computerType"] = ""
        item1["houdu"] = ""

        for info in infos_lst:
            kv = info.split('：')
            if kv[0] in ItemDict.itemDict:
                item1[ItemDict.itemDict[kv[0]]] = kv[1]
            else:
                pass        
        # print("*****brand: {}".format(item1['computerBrand']))
        # print(item1)

        infos_lst = sel.xpath('//div[@class="Ptable"]/div[1]/dl/dd/text()|//div[@class="Ptable"]/div[1]/dl/dt/text()').extract()
        for i in range(len(infos_lst)):
            if infos_lst[i] == '颜色':
                item1['color'] = infos_lst[i+1]
                break
        # print('***************:{}'.format(infos_lst))

        #给显卡判定是否抓取成功，否则进行详细参数抓取 
        if item1['xianka'] == '其他':
            try:
                xkcheck = sel.xpath('//div[@class="Ptable"]/div/h3[contains(text(),"显卡")]/parent::*/dl/dt/text()|//div[@class="Ptable"]/div/h3[contains(text(),"显卡")]/parent::*/dl/dd/text()').extract()
                for i in range(len(xkcheck)):
                    if xkcheck[i] == '显示芯片':
                        item1['xianka'] = xkcheck[i+1]
                        break
            except:
                pass
        if item1['screenInches'] == '其他':
            try:
                str1 = sel.xpath('//div[@class="sku-name"]/text()').extract()
                item1['screenInches'] = re.search('(\d*)\.(\d*)英寸',str1[0]).group(0)
            except Exception:
                print("error")

        url = "http://club.jd.com/clubservice.aspx?method=GetCommentsCount&referenceIds=" + str(item1['ID'][0])
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_getCommentnum)
    
    def parse_getCommentnum(self, response):  
        item1 = response.meta['item']  
        # response.body是一个json格式的  
        # print(response.body)
        try:
            js = json.loads(response.body)
        except Exception:
            print(response.body)
        # js = json.loads(str)
        # print(js['CommentsCount'][0]['Score1Count'])
        item1['score1count'] = js['CommentsCount'][0]['Score1Count']  
        item1['score2count'] = js['CommentsCount'][0]['Score2Count']
        item1['score3count'] = js['CommentsCount'][0]['Score3Count']  
        item1['score4count'] = js['CommentsCount'][0]['Score4Count']  
        item1['score5count'] = js['CommentsCount'][0]['Score5Count']  
        item1['comment_num'] = js['CommentsCount'][0]['CommentCount']
        num = item1['ID']  # 获得商品ID
        s1 = str(num)
        url = "http://pm.3.cn/prices/pcpmgets?callback=jQuery&skuids=" + s1[2:-2] + "&origin=2"
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_price)  

    def parse_price(self, response):  
        item1 = response.meta['item']
        # print("*******json:{}".format(s))
        # print("*******json:{}".format(response.body))
        js = json.loads(re.search('{(.*?)}', str(response.body)).group(0))
        item1['price'] = js['p']
        try:
            item1['price'] = js['pcp']
        except:
            pass
        return item1  