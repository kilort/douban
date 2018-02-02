import random,linecache
#随机返回ua
def ua():
    this_ua = linecache.getline("/home/hl/桌面/ubuntu/MINE/douban/douban/Tools/ua.txt",random.randrange(1,250))
    return this_ua

if __name__ =="__main__":
    ua()
