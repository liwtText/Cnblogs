# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from scrapy.exceptions import DropItem
import scrapy

class CnblogspiderPipeline:
    def process_item(self, item, spider):
        if item['title']:
            line=json.dumps(dict(item),ensure_ascii=False)+"\n"
            self.file.write(line)
            return item
        else: 
            raise DropItem("Missing title in %s"% item)
    def __init__(self):
         self.file=open('papers.json','w+',encoding='utf-8')

# class MyImagesPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info): 
#         for image_url in item['cimage_urls']:
#             yield scrapy.Request(image_url)
#     def item_completed(self, results, item, info): 
#         image_paths=[x['path'] for ok,x in results if ok]
#         if not image_paths: 
#             raise DropItem("Item contains no images")
#         item['cimages']=image_paths 
#         return item