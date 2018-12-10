# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class DoubanloginPipeline(object):
    def __init__(self):
        self.f = open("doubannote.csv", "w")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['日记标题', '日记链接', '日记发布时间', '日记内容'])

    def process_item(self, item, spider):
        # 循环写入本地文件
        for i in range(0, len(item["name"])):
            # 保存为csv文件
            dbnote_list = [item["name"][i], item["href"][i], item["time"][i], item["content"][i]]
            print("管道文件测试-> %s" % dbnote_list)  # 输出测试
            self.writer.writerow(dbnote_list)

        return item

    def close_spider(self, spider):
        self.f.close()

