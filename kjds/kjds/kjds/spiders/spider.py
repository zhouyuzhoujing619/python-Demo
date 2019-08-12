import scrapy
from kjds.items import KjdsItems
from  scrapy.selector import Selector

class  KjdsSpider(scrapy.Spider):
    name="kjds"
    allowed_domains=["192.168.19.130"]
    start_urls=["http://192.168.19.130/2.html"]


    base_url="http://192.168.19.130"

    start_page=1

    def parse(self, response):
         while self.start_page<101:
             url=self.base_url+"/"+str(self.start_page)+".html"
             self.start_page=self.start_page+1
             yield  scrapy.Request(url=url,callback=self.get_detail)

    def get_detail(self,response):
        item=KjdsItems();
        #开始循环
        sels=Selector(response).xpath("/html/body/table/tr")
        del sels[0]
        for sel in sels:
            item["seq"]=sel.xpath("//td[1]/text()").extract()
            item["trans_amt"] = sel.xpath("//td[2]/text()").extract()
            item["create_date"] = sel.xpath("//td[3]/text()").extract()
        yield item