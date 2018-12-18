from bs4 import BeautifulSoup

import requests

baidu = requests.get("https://www.baidu.com")

baidu.encoding = 'utf-8'

soup = BeautifulSoup(baidu.text, 'html.parser')

# print(soup.prettify())

print(soup.title)
print(soup.title.text)
print(soup.title.string)
print(soup.head)
print(soup.div)
print(soup.div["id"])


for item in soup.find_all("a"):
    print(item.get("href"))
    print(item.get_text())




print(soup.select('title')[0].text)


