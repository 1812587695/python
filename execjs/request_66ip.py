import re

import execjs
import requests
from fake_useragent import UserAgent, FakeUserAgentError
from pyquery import PyQuery as pq


def get_page(url, options={}):
    try:
        ua = UserAgent()
    except FakeUserAgentError:
        pass
    base_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    headers = dict(base_headers, **options)
    # print('Getting', url)
    try:
        r521 = requests.get(url, headers=headers)
        # print(r521.text)
        re_compile = re.compile('(function.*?)</script>')
        js_func = re_compile.findall(r521.text)
        # print(js_func)
        # 修改JS函数，使其返回Cookie内容
        js_func = js_func[0].replace('eval("qo=eval;qo(po);")', 'return po')
        # print(js_func)

        # 提取其中执行JS函数的参数
        js_arg = re.findall(r'setTimeout\(\"(\D+)\((\d+)\)\"', r521.text)
        # print(js_arg)
        # print(type(js_arg[0][0]))
        # print(type(js_arg[0][1]))
        #
        # quit()

        jsContext = execjs.compile(js_func)
        antipas = jsContext.call(js_arg[0][0], js_arg[0][1])
        _ydclearance = re.findall(r'document.cookie=\'_ydclearance=(.*?); expires=', antipas)
        # print(_ydclearance)
        # quit()
        c = {
            '_ydclearance' : _ydclearance[0],
            'yd_cookie': r521.cookies['yd_cookie']
        }

        r = requests.get(url, headers=headers, cookies=c)
        print('Getting result', url, r.status_code)
        if r.status_code == 200:
            return r.text
    except ConnectionError:
        print('Crawling Failed', url)
        return None



def crawl_daili66(page_count=4):
    start_url = 'http://www.66ip.cn/{}.html'
    urls = [start_url.format(page) for page in range(1, page_count + 1)]
    for url in urls:
        # print('Crawling', url)
        html = get_page(url)
        if html:
            doc = pq(html)
            trs = doc('.containerbox table tr:gt(0)').items()

            for tr in trs:
                ip = tr.find('td:nth-child(1)').text()
                port = tr.find('td:nth-child(2)').text()
                yield ':'.join([ip, port])

for ip in crawl_daili66():
    print(ip)
