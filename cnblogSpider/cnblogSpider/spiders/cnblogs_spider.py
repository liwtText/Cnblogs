import scrapy
from cssselect.parser import Selector
from cnblogSpider.items import CnblogspiderItem

class DmozSpider(scrapy.Spider): # 继承Spider类 执行语句 ：scrapy crawl cnblogs
    name = "cnblogs" # 爬虫的唯一标识,不能重复,启动爬虫的时候要用
    allowed_domains=["cnblogs.com"]#允许的域名
    start_urls=[
        "http://www.cnblogs.com/qiyeboy/default.html?page=1"
    ]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    def parse(self, response):
        #实现网页的解析    
        #首先抽取所有的文章
        papers=response.xpath(".//*[@class='day']")
        #从每篇文章中抽取数据
        for paper in papers:
            url=paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title=paper.xpath(".//*[@class='postTitle']/a/span/text()").extract()[0].replace(" ", "").replace("\n", "")
            time=paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content=''#paper.xpath(".//*[@class='postCon']/div/text()").extract()[0]
            item=CnblogspiderItem(url=url,title=title,time=time,content=content)
            request=scrapy.Request(url=url,callback=self.parse_body)
            request.meta['item']=item#将item暂存
            yield request
        next_page=response.xpath('//a[contains(@href, "page")]/@href').extract()[-1]
        # next_page=response.xpath(".//div[@id='nav_next_page']/a/@href").extract()[0]
        # print('下一页'+ next_page)
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse)
         
    def parse_body(self,response):
        item=response.meta['item']
        body=response.xpath(".//*[@class='postBody']")
        # list1=[]
        # list1.append(reurl)
        item['cimage_urls']=body.xpath('.//img//@src').extract()#提取图片链接 必须是list
        yield item

