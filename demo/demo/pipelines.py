# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from  openpyxl import   Workbook
class DemoPipeline(object):
    wb=Workbook()
    ws=wb.active
    ws.append(["标题","图片","简介"])

    def process_item(self, item, spider):
        titles=item["title"]
        for i in range(len(titles)):
           line=[item["title"][i],item["img"][i],item["dec"][i]]
           self.ws.append(line)
        self.wb.save("./data.xlsx")
        return item
