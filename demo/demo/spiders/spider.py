
import scrapy
from demo.items import DemoItem
from scrapy.selector import  Selector

class  spider(scrapy.Spider):
    name="test"
    allowed_domins=["pianshen.com/"]
    start_urls=["http://pianshen.com/"]

    base_url="http://pianshen.com/list/"
    start_page=1

    def  parse(self,response):
        while self.start_page<11:
          url=  self.base_url+str(self.start_page)+"/"
          self.start_page=self.start_page+1
          yield scrapy.Request(url=url,callback=self.get_detail)


    def get_detail(self,response):
        print("进入子页面")
        item=DemoItem()
        sels=Selector(response).xpath("/html/body/div[3]/div/div[1]/div")
        for sel in sels:
            item['title'] = sel.xpath("//header/h3/a/text()").extract()

            item["img"] = sel.xpath("//a/img/@src").extract()
            item["dec"] = sel.xpath("//div/div/div[2]/p/text()").extract()



        yield item


