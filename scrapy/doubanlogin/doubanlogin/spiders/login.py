# -*- coding: utf-8 -*-
import scrapy
import urllib.request
# from scrapy.http import FormRequest
from doubanlogin.items import DoubanloginprojectItem



class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']

    def parse(self, response):
        # 首先获取验证图片地址并复制给 imgurl 变量
        imgurl = response.xpath('//img[@id="captcha_image"]/@src').extract()
        # 由于验证码时有时无，因此需要判断如果有就手动输入
        if len(imgurl) > 0:
            print("有验证码返回...")
            # 将验证图片保存到本地中
            local_path = r"C:/Users/Administrator/Desktop/yanzhangma/lcy.png"
            urllib.request.urlretrieve(imgurl[0], filename=local_path)
            # 定义接受验证码变量
            capt_value = input("请查看本地 lcy.png 图片并输入对应的验证码-> ")
            # 设置带有验证码的 post 信息
            data = {
                "redir": "https://www.douban.com/people/88923947/",  # 要跳转的链接
                "form_email": "1812587695@aa.com",  # 用户名
                "form_password": "zy123456789",  # 密码
                "captcha-solution": capt_value,  # 验证码
            }

        else:  # 此时不需要验证码
            print("无验证码登录...")
            # 设置无验证码请求的参数
            data = {
                "redir": "https://www.douban.com/people/88923947/",  # 要跳转的链接
                "form_email": "1812587695@aa.com",  # 用户名
                "form_password": "zy123456789",  # 密码
            }

        print("登录中......")
        # 带参的登录请求
        return [scrapy.FormRequest.from_response(response,
                                                 # 设置 cookie 信息   注：这两项在 settings.py 文件中设置即可
                                                 # meta={"cookiejar":response.meta["cookiejar"]}, #如果重写 start_requests()方法，那么该值必须对应请求里的 meta 中的键
                                                 # 设置请求头模拟成浏览器
                                                 # headers=self.headers,
                                                 # 设置 post 表单中的数据
                                                 formdata=data,
                                                 # 设置回调函数
                                                 callback=self.mynode,
                                                 url='https://accounts.douban.com/login'
                                                 )]

    # 之所以创建这个方法是因为如果直接打开日记链接：https://www.douban.com/people/178279892/notes 的话，不需要 cookie 也可以访问，因此为看到 cookie 的效果我们定义该方法
    def mynode(self, response):
        # 获取用户名
        my_name = response.xpath(r'//div[@class="info"]/h1/text()').extract_first()
        # 获取日记页面的链接
        note_url = response.xpath(r'//a[@id="usr-profile-nav-notes"]/@href').extract_first()
        print(note_url)
        # 回调方法处理的是请求之后的数据
        note_url = "https://www.douban.com/people/88923947/notes"
        return scrapy.Request(url=note_url, callback=self.next, dont_filter=True)


#获取日记信息方法
    def next(self, response):
        print("......此时已经登录完成并爬去了个人中心的日记数据......")
        #获取日记选项列表
        data_list = response.xpath(r'//div[@class="note-container"]')
        item = DoubanloginprojectItem() #获取实体对象
        for data in data_list:
            item["name"] = data.xpath(r'./div[1]/h3/a/text()').extract() #日记标题
            item["href"] = data.xpath(r'./div[1]/h3/a/@href').extract() #日记链接
            item["time"] = data.xpath(r'./div[1]/div/span/text()').extract()#日记发布时间
            item["content"] = data.xpath(r'./div[3]/text()').extract() #日记内容

            yield item


