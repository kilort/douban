import random,linecache,requests,time

#通过本地的ip文件池，随机生成调用ip
def produce_ip():
	# line = random.randrange(1,100)
	# this_ip = linecache.getline('/home/hl/桌面/MINE/douban/douban/Tools/my_IP.txt',line)
	api = 'http://tvp.daxiangdaili.com/ip/?tid=558931260013284&num=1&protocol=https&filter=on&category=2&sortby=speed'
	time.sleep(1)
	response = requests.get(api)
	ip = 'http://'+str(response.text)
	print(ip)
	return  ip



