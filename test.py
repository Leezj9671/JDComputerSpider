import scrapy
import re


text = '''<ul class="parameter2 p-parameter-list">
                                    <li title="戴尔燃7000">商品名称：戴尔燃7000</li>
    <li title="3474436">商品编号：3474436</li>
                         <li title="2.63kg">商品毛重：2.63kg</li>
            <li title="中国大陆">商品产地：中国大陆</li>
                                    <li title="Windows 10">系统：Windows 10</li>
                  <li title="15.1mm—20.0mm">厚度：15.1mm—20.0mm</li>
                  <li title="4G">内存容量：4G</li>
                  <li title="全高清屏（1920×1080）">分辨率：全高清屏（1920×1080）</li>
                  <li title="GT940M">显卡型号：GT940M</li>
                  <li title="9小时以上">待机时长：9小时以上</li>
                  <li title="Intel i5低功耗版">处理器：Intel i5低功耗版</li>
                  <li title="背光键盘">特性：背光键盘</li>
                  <li title="入门级游戏独立显卡">显卡类别：入门级游戏独立显卡</li>
                  <li title="1.5-2kg">裸机重量：1.5-2kg</li>
                  <li title="128G+500G">硬盘容量：128G+500G</li>
                  <li title="2G">显存容量：2G</li>
                  <li title="轻薄本">分类：轻薄本</li>
                  <li title="14.0英寸">屏幕尺寸：14.0英寸</li>
                                              </ul>'''

itemDict = {
    '商品名称': 'computerName',
    '系统': 'system',
    '厚度': 'houdu',
    '内存容量': 'mem',
    '分辨率' : 'screenFb',
    '显卡型号': 'xianka',
    '待机时长': 'daijishichang',
    '处理器': 'cpu',
    '特性': 'texing',
    '裸机重量': 'weight',
    '硬盘容量': 'disk',
    '显存容量': 'xiancun',
    '分类': 'computerType',
    '屏幕尺寸': 'screenInches',
    '颜色': 'color'
}
m = re.findall('<li (.*?)>(.*?)：(.*?)</li>',text)
print(m)
for i in m:
    print(i[1])
