import json
import re
from urllib.parse import urlencode

from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import requests


def get_page_index(offset, keyword):
    data = {
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": '20',
        "cur_tab": 3
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("url error+++++++++++++++++++++++++++++++++++++++++++++")
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("url error+++++++++++++++++++++++++++++++++++++++++++++")
        return None

def parse_page_detail(html, url):
    bsObj = BeautifulSoup(html, 'html.parser')
    print(bsObj)
    # title = bsObj.select('title')[0].get_text()
    # print(title)
    # #数据不在正常的标签里，只能正则匹配了
    # imgPattern = re.compile("gallery: JSON.parse\(\"(.*?)\"\),", re.S)
    # result = re.search(imgPattern, html)
    # if result is not None:
    #     #匹配json串数据，并解析
    #     #格式调整
    #     newResult = result.group(1).replace('\\\\', '#')
    #     newResult = newResult.replace('\\', '')
    #     newResult = newResult.replace('#', '\\\\')
    #     newResult = newResult.replace('\/', '/')
    #     #print(newResult)
    #     data = json.loads(newResult)
    #     #print(data)
    #     if data and 'sub_images' in data.keys():
    #         sub_images = data.get('sub_images')
    #         #print(sub_images)
    #         images = [item.get('url') for item in sub_images]
    #         print(images)
    #         # for image in images: download_image(image)
    #         return {
    #             'title': title,
    #             'url': url,
    #             'images': images,
    #         }

def main():
    html = get_page_index(0, "街拍")
    # print(html)
    for url in parse_page_index(html):
        # print(url)
        if url:
            html = get_page_detail(url)
            # print(html)
            result = parse_page_detail(html, url)

if __name__ == '__main__':
    main()







