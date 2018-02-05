import random

def product_ip():
    #返回代理ip
    with open("/home/my_Tools/share_ip.txt") as f:
     ip = random.choice(f.readlines())
    proxy = "http://"+str(ip)
    return proxy

if __name__=="__main__":
    product_ip()