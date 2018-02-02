import requests,re
from scrapy.selector import Selector

url = [
# 	   "https://movie.douban.com/subject/27617323/",
# 	   "https://movie.douban.com/subject/27091600/",
# 	   "https://movie.douban.com/subject/26994754/",
# 	   "https://movie.douban.com/subject/26764928/",
# 	   "https://movie.douban.com/subject/27591954/"
# 	'https://book.douban.com/subject/6709783/',
# 	'https://book.douban.com/subject/27021786/',
# 	'https://book.douban.com/subject/26657570/',
# 	'https://book.douban.com/subject/1476651/',
# 	'https://book.douban.com/subject/24754316/',
# 	'https://book.douban.com/subject/26822709/']
	'https://music.douban.com/subject/6064884/',
	'https://music.douban.com/subject/27200370/',
	'https://music.douban.com/subject/1407624/',
	'https://music.douban.com/subject/26915671/',
	'https://music.douban.com/subject/19967501/',
	'https://music.douban.com/subject/4894045/'
     ]
headers={"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)"}


for i in url:
	response = requests.get(i, headers=headers)
	selector = Selector(text=response.text)
	music=selector.xpath('//div[@id="wrapper"]/h1/span/text()').extract()
	performer=re.compile('表演者:.*?>(.*?)<', re.DOTALL).findall(response.text)
	# classify= response.meta.get("tag2", "")
	media=re.compile('介质:.*?>(.*?)<', re.DOTALL).findall(response.text)
	release_time=re.compile('发行时间:.*?(.*?)<', re.DOTALL).findall(response.text)
	# publisher=re.compile().findall(response.text)
	score= selector.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()
	comments_num=selector.xpath('//div[@class="rating_self clearfix"]/div[@class="rating_right "]/div[@class="rating_sum"]/a/span/text()').extract()
	hot_comments=selector.xpath('//div[@class="comment-list hot show"]/ul/li/div/p/text()').extract()


	###################################################################################################################

	# response = requests.get(i,headers=headers)
	# selector = Selector(text=response.text)
	# book=selector.xpath('//div[@id="wrapper"]/h1/span/text()').extract()
	# writer= selector.xpath('//div[@class="subject clearfix"]/div[@id="info"]/a/text()').extract()
	# publish=re.compile('<span.*?>出版社:</span>(.*?)<br/>.*?<span', re.DOTALL).findall(response.text)
	# publish_time=re.compile('<span class="pl">出版年:</span>(.*?)<br/>.*?<span', re.DOTALL).findall(response.text)
	# pages=re.compile('<span class="pl">页数:</span>(.*?)<br/>.*?<span', re.DOTALL).findall(response.text)
	# price=re.compile('<span class="pl">定价:</span>(.*?)<br/>.*?<span', re.DOTALL).findall(response.text)
	# type= re.compile('<span class="pl">装帧:</span>(.*?)<br/>.*?<span', re.DOTALL).findall(response.text)
	# ISBN= re.compile('<span class="pl">ISBN:</span>(.*?)<br/>.*?<span', re.DOTALL).findall(response.text)
	# score= selector.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()
	# comments_num=selector.xpath('//div[@class="rating_self clearfix"]/div[@class="rating_right "]/div[@class="rating_sum"]/span/a/span/text()').extract()
	# hot_comments=selector.xpath('//div[@class="comment-list hot show"]/ul/li/div/p/text()').extract()
	#

	######################################################################################################

	# country = re.compile(r'<span class="pl">制片国家/地区:</span>(.*?)<br/>.*?<span',re.DOTALL).findall(response.text)
	# language=re.compile(r'<span class="pl">语言:</span>(.*?)<br/>.*?<span', re.DOTALL).findall(response.text)
	# screen_time= selector.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()
	# score=selector.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()
	# comments_num=selector.xpath('//div[@class="rating_self clearfix"]/div/div/a/span/text()').extract()
	# hot_comments=selector.xpath('//div[@id="hot-comments"]/div/div/p/text()').extract()
	print(music)