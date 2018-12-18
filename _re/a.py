import re

import requests

content = requests.get("https://book.douban.com/").text
# print(content)
p = re.compile('<li.*?cover.*?href="(.*?)".*?</li>', re.S)

a= re.findall(p, content)
print(a)