import random,linecache

def product_xiongmao_ip():
    #返回熊猫代理的ip
    ip = linecache.getline("/home/hl/桌面/docker_share/share_ip.txt",random.randrange(1,11))
    proxy = "http://"+str(ip)
    print(proxy)
    return proxy


if __name__=="__main__":
    product_xiongmao_ip()