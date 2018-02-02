import random,linecache
#随机返回ua
def ua():
    this_ua = linecache.getline("ua.txt",random.randrange(1,251))
    return this_ua

if __name__ =="__main__":
    print(ua())
