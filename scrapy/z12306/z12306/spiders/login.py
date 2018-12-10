# -*- coding: utf-8 -*-
import scrapy
import re
import urllib
import time
import random


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['12306.cn']
    # start_urls = ['https://kyfw.12306.cn/otn/resources/login.html']
    timerandom = str(int(time.time())) + str(random.randint(000, 999))
    # start_urls = ["https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&"+ timerandom +"&callback=jQuery19109724833773027055_1544068470447&_=" + timerandom]
    start_urls = ["https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&1544080750569&callback=jQuery19107142999150496183_1544080750559&_=1544080750569"]

    def parse(self, response):
        print(response.status)

        img_url = re.findall(
            r"/\*\*/jQuery19107142999150496183_1544080750559\(\{\"result_message\":\"生成验证码成功\",\"result_code\":\"0\",\"image\":\"(.+?)\"\}\);",
            response.body.decode("utf8"))

        local_path = r"C:/Users/Administrator/Desktop/yanzhangma/a.png"
        urllib.request.urlretrieve("data:image/jpg;base64," + img_url[0], filename=local_path)

        code = ['40,45', '112,41', '190,41', '261,38', '46,114', '113,116', '188,115', '267,114']

        capt_value = input("请查看本地 lcy.png 图片并输入对应的验证码-> ")

        captcha_url = "https://kyfw.12306.cn/passport/captcha/captcha-check?callback=jQuery19109724833773027055_1544068470447&answer=" + capt_value + "&rand=sjrand&login_site=E&_=timerandom"

        print("---------------------------------------------")
        print(captcha_url)
        print("---------------------------------------------")
        # 带参的登录请求
        yield scrapy.Request(url=captcha_url, callback=self.mynode)

        # 登录
        # login_url = 'https://kyfw.12306.cn/passport/web/login'
        # data = {
        #     "username": "747033638@qq.com",
        #     "password": "zy123456789",
        #     "appid": "otn",
        #     "answer": capt_value,
        # }
        # yield scrapy.FormRequest(
        #                                        # 设置 cookie 信息   注：这两项在 settings.py 文件中设置即可
        #                                        # meta={"cookiejar":response.meta["cookiejar"]}, #如果重写 start_requests()方法，那么该值必须对应请求里的 meta 中的键
        #                                        # 设置请求头模拟成浏览器
        #                                        # headers=self.headers,
        #                                        # 设置 post 表单中的数据
        #                                        formdata=data,
        #                                        # 设置回调函数
        #                                        callback=self.logindo,
        #                                        url=login_url
        #                                        )

    def mynode(self, response):
        print(response.body.decode("utf8"))

    def logindo(self, response):
        print(response.body.decode("utf8"))