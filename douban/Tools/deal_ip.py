import random,linecache,requests,time

def return_txt():
    #大象代理
    url = "http://tvp.daxiangdaili.com/ip/?tid=558931260013284&num=10"
    response = requests.get(url)
    if len(response.text)>100:
        print("ip_pool ready!")
        with open("ua.txt",'w')as f:
            f.write(response.text)
            f.close()
        if "ERROR" in response.text:
            raise Exception("api关闭")
        time.sleep(150)
        return_txt()



def product_xiongmao_ip():
    #返回熊猫代理的ip
    ip = linecache.getline("/home/hl/桌面/ubuntu/MINE/douban/douban/Tools/ua.txt",random.randrange(1,11))
    proxy = "http://"+str(ip)
    return proxy


if __name__=="__main__":
    return_txt()