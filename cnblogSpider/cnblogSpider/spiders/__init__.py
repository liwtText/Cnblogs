# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__=='__main__':
    # process=CrawlerProcess({'USER_AGENT':' Mozi11a/4.0(compatible; MSIE 7.0; Windows NT 5.1)'}
    # process.crawl(CnblogsSpider)
    # process.start()
    process=CrawlerProcess(get_project_settings())
    process.crawl('cnblogs')
    process.start()