import hashlib
import datetime
import re
from douban.settings import *


def get_md5(url):
	if isinstance(url,str):#isinstance会判断url是否为unicode编码方式（python3默认都是unicode），unicode编码方式是不可以用在哈系中的
		url = url.encode("utf-8")#将uncoide编码的url转化为utf-8
	m = hashlib.md5()
	m.update(url)
	return m.hexdigest()#提取出md5的值




def delete_useless_str(obj):
	#对字符串进行过滤，选出有用的data
	if obj:
		nbsp = '&nbsp;'
		if nbsp in obj:
			str = obj.replace(nbsp, "").strip()
			str = obj.replace(" ",'')
		else:
			str = obj.strip()
			str = obj.replace(" ", '')
		return str
	else:
		return "None"


def get_num1(obj):
	#对数字进行处理，主要用于com_num,page等等
	if isinstance(obj,list):
		str = delete_useless_str(obj[0])
		str = re.compile('(\d+)').findall(str)
		if str:
			if'.'in obj[0]:
				num = int(0)
			else:
				num = int(str[0])
			return num
		else:
			return int(0)
	else:
		return int(0)

def get_num2(obj):
	#用于float数字
	if isinstance(obj,list):
		str = delete_useless_str(obj[0])
		str = re.compile('(\d+\.{0,1}\d+)').findall(str)
		if str:
			if '.' in obj[0]:
				num = float(str[0])
			else:
				num = float(str[0]+'.00')
			return num
		else:
			return float(0.0)
	else:
		return float(0.0)



def get_hot_comments(obj):
	#对热评进行整合提取
	comments = []
	if isinstance(obj,list):
		for x,comment in enumerate(obj):
			comment = str(x+1)+' '+delete_useless_str(comment)+'\n'
			comments.append(comment)
		comments="".join(comments)
		return comments
	else:
		return "None"


def get_ration_element(obj):
	#对个元素的list进行字符串整合，用于导演，演员等可能出现多个值的对象
	if isinstance(obj,list):
		if len(obj)==1:
			str = delete_useless_str(obj[0])
			return str

		if len(obj)>=2:
			str1,str2 =delete_useless_str(obj[0]),delete_useless_str(obj[1])
			str ="{0},{1}".format(str1,str2)
			return str
	else:
		return "None"


def now():
	#返回现在的时间
	return datetime.datetime.now().strftime(DATETIME_TYPE2)


def get_date(obj):
	#对抓取到的各种类型的datetime进行整合输出
	if isinstance(obj,list):
		str = delete_useless_str(obj[0])
		str_time = re.compile('(\d{3,5}-{0,1}\d{0,2}-{0,1}\d{0,2})').findall(str)
		flag = re.compile('(-)').findall(str)
		if str_time and len(flag)==0:
			create_time = str_time[0]+'-1-1'
			try:
				return datetime.datetime.strptime(create_time,DATETIME_TYPE).date()
			except:
				return datetime.datetime.strptime(ERROR_DATETIME,DATETIME_TYPE).date()
		if str_time and len(flag)==1:
			create_time = str_time[0]+'-1'
			try:
				return datetime.datetime.strptime(create_time,DATETIME_TYPE).date()
			except:
				return datetime.datetime.strptime(ERROR_DATETIME, DATETIME_TYPE).date()
		if str_time and len(flag)==2:
			try:
				return datetime.datetime.strptime(str_time[0], DATETIME_TYPE).date()
			except:
				return datetime.datetime.strptime(ERROR_DATETIME, DATETIME_TYPE).date()
	else:
		return datetime.datetime.strptime(ERROR_DATETIME, DATETIME_TYPE).date()


#获取作者
def get_writer(obj):
	if isinstance(obj,list):
		if len(obj)==1:
			if len(obj[0][0])>len(obj[0][1]):
				str = delete_useless_str(obj[0][0])
			elif len(obj[0][0])<len(obj[0][1]):
				str = delete_useless_str(obj[0][0])
			else:
				str = delete_useless_str(obj[0][0])
			return str

		if len(obj)>=2:
			if len(obj[0][0])>len(obj[0][1]):
				str1 = delete_useless_str(obj[0][0])
			elif len(obj[0][0])<len(obj[0][1]):
				str1 = delete_useless_str(obj[0][0])
			else:
				str1 = delete_useless_str(obj[0][0])

			if len(obj[1][0])>len(obj[1][1]):
				str2 = delete_useless_str(obj[1][0])
			elif len(obj[1][0])<len(obj[1][1]):
				str2 = delete_useless_str(obj[1][0])
			else:
				str2 = delete_useless_str(obj[1][0])
			str1,str2 =delete_useless_str(obj[0]),delete_useless_str(obj[1])
			str ="{0},{1}".format(str1,str2)
			return str
	else:
		return "None"
