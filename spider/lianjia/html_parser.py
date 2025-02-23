# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:00:31 2018

@author: zhangying
"""

from bs4 import BeautifulSoup
from spider.lianjia.log import MyLog

class HtmlParser():
    """网页解析模块"""

    def __init__(self):
        """构造函数，初始化属性"""
        self.log = MyLog("html_parser", "logs")

    def get_ershoufang_data(self, html_cont, detail_url, id):
        """获取二手房页面详细数据"""
        if html_cont is     None:
            self.log.logger.error("页面解析(detail)：传入页面为空！")
            print("页面解析(detail)：传入页面为空！")
            return

        ershoufang_data = []
        communityName = "null"
        areaName = "null"
        total = "null"
        unitPriceValue = "null"

        bsObj = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        tag_com = bsObj.find("div", {"class": "communityName"}).find("a")
        if tag_com is not None:
            communityName = tag_com.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到communityName标签！")

        # 过滤 communityName
        if '天润城' not in communityName:
            return None

        tag_area = bsObj.find("div", {"class": "areaName"}).find("span", {"class": "info"}).find("a")
        if tag_area is not None:
            areaName = tag_area.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到areaName标签！")

        tag_total = bsObj.find("span", {"class": "total"})
        if tag_total is not None:
            total = tag_total.get_text()
        else:
            self.log.logger.error("页面解析(detail)：找不到total标签！")

        tag_unit = bsObj.find("span", {"class": "unitPriceValue"})
        tag_unit = tag_unit.get_text().replace("元/平米", "")
        if tag_unit is not None:
            unitPriceValue = tag_unit
        else:
            self.log.logger.error("页面解析(detail)：找不到total标签！")

        id = detail_url.replace("https://nj.lianjia.com/ershoufang/", "").replace(".html", "")
        ershoufang_data.append(id)
        ershoufang_data.append(communityName)
        ershoufang_data.append(areaName)
        ershoufang_data.append(total)
        ershoufang_data.append(unitPriceValue)

        # 基本信息
        counta = 12
        for a_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "base"}).find("div", {"class": "content"}).ul.findAll("li"):
            # print(child1)
            [s.extract() for s in a_child("span")]
            information = a_child.get_text()

            # 套内面积处理 暂无数据的使用户型分间计算
            # if counta == 8:
            #     print('套内面积: ' + information)
            #     if information == '暂无数据':
            #         a = bsObj.find("div", {"id": "infoList"}).find("div", {"class": "base"}).find("div", {"class": "content"}).ul.findAll("li")

            # 删除㎡
            if '㎡' in information:
                information = information.replace('㎡', '')
            ershoufang_data.append(information)
            counta = counta - 1

        while counta > 0:
            ershoufang_data.append("null")
            counta = counta - 1

        # 交易属性
        countb = 8
        for b_child in bsObj.find("div", {"class": "introContent"}).find("div", {"class": "transaction"}).find("div", {"class": "content"}).ul.findAll("li"):
            information = b_child.span.next_sibling.next_sibling.get_text()
            if countb == 2:
                information = information.strip()
            ershoufang_data.append(information)
            countb = countb - 1

        while countb > 0:
            ershoufang_data.append("null")
            countb = countb - 1

        ershoufang_data.append(detail_url)

        self.log.logger.info("2.3 页面解析(detail)：页面解析成功！")
        print("2.3 页面解析(detail)：页面解析成功！")
        return ershoufang_data

    def get_erhoufang_urls(self, html_cont):
        """获取二手房页面的链接"""
        if html_cont is None:
            self.log.logger.error("页面解析(page)：pg页面为空！")
            print("页面解析(page)：pg页面为空！")
            return

        ershoufang_urls = set()
        bsObj = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        sellListContent = bsObj.find("ul", {"class": "sellListContent"})

        if sellListContent is not None:
            for child in sellListContent.children:
                if child["class"][0] == "clear":
                    ershoufang_urls.add(child.a["href"])
                    # test
                    # print("1.3 页面解析：pg页面解析成功！")
                    # return ershoufang_urls
                    self.log.logger.info(child.a["href"])
                    # print(child.find("a",{"class":"img"})["href"])
        else:
            self.log.logger.error("页面解析(page)：找不到sellListContent标签！")

        self.log.logger.info("1.3 PG页面解析：pg页面解析成功！")
        print("1.3 页面解析：pg页面解析成功！")
        return ershoufang_urls
