# -*- coding: utf-8 -*-
import scrapy
import json
import re
from zhifu.items import ZhifuItem


class UserinfoSpider(scrapy.Spider):
    name = 'userinfo'
    allowed_domains = ['zhihu.com']
    start_urls = [
        'https://www.zhihu.com/api/v4/members/liuyu-43-97/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20']

    def parse(self, response):
        # print(response.body.decode("utf-8"))
        print("===============================================================")
        print(response)
        temp_data = json.loads(response.body.decode('utf-8'))['data']

        # print(len(temp_data))
        # print("*"*20)
        count = len(temp_data)
        if count < 20:
            pass
        else:
            # 继续调用本身
            # print(response.url)
            page_offset = int(re.findall("&offset=(.*?)&", response.url)[0])
            new_page_offset = page_offset + 20
            next_page_url = response.url.replace("&offset=" + str(page_offset) + "&",
                                                 "&offset=" + str(new_page_offset) + "&")
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)

        for ene_user in temp_data:
            # print(ene_user)
            item = ZhifuItem()
            item['name'] = ene_user['name']
            item['url_token'] = ene_user['url_token']
            item['headline'] = ene_user['headline']
            item['follower_count'] = ene_user['follower_count']
            item['answer_count'] = ene_user['answer_count']
            item['articles_count'] = ene_user['articles_count']
            item['uid'] = ene_user['id']
            item['gender'] = ene_user['gender']
            item['type'] = ene_user['user_type']

            with open("userinfo.txt") as f:
                user_list = f.read()
            if ene_user['url_token'] not in user_list:
                with open("userinfo.txt", "a") as f:
                    f.write(ene_user['url_token'] + '-------')
                yield item

                new_url = "https://www.zhihu.com/api/v4/members/" + ene_user[
                    'url_token'] + "/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20"
                yield scrapy.Request(url=new_url, callback=self.parse, dont_filter=True)




















