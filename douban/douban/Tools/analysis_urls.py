import requests
from scrapy.selector import Selector


url ='https://book.douban.com/subject/26692203/'
headers = {'User-Agent':':Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

response = requests.get(url=url,headers=headers)
# selector = Selector(text=response.text)
# links = selector.xpath('//a/@href').extract()
# for i in links :
# 	print(i)


import re
url = ['https://book.douban.com/tag/%E6%95%A3%E6%96%87',
	   'https://music.douban.com/tag/Electronic?start=40&type=T',
	   'https://book.douban.com/tag/%E6%95%A3%E6%96%87?start=100&type=T']

for i in url:
	a = re.compile("tag/(.*?)($|\?.*)").findall(i)
	print(a[0][0])

print(re.compile('作者</span>.*?<a.*?>(.*?)<', re.DOTALL).findall(response.text))