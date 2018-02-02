import requests
from http import cookiejar

session = requests.session()
session.cookies = cookiejar.LWPCookieJar('cookie.txt')
try:
	session.cookies.load(ignore_discard=True)
	proxy_dict={"http":"http://60.167.20.32:22477"}
	response = session.get("https://movie.douban.com/subject/26612285/?from=showing",proxies = proxy_dict, headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)"})
	print(response.status_code)
except:
	proxy_dict = {"http": "http://60.167.20.32:22477"}
	response = session.get("https://movie.douban.com/subject/26612285/?from=showing", proxies=proxy_dict, headers={
		"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)"})
	session.cookies.save()
	print(response.status_code)

