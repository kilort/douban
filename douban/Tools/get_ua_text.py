import requests,json
#同感fake的api接口 将其api_ua数据写入本地文本中
url = "https://fake-useragent.herokuapp.com/browsers/0.1.6"
response = requests.get(url)
print(response.text)
response_json = json.loads(response.text)
for type in response_json["browsers"]:
    for ua in response_json["browsers"]["%s"%type]:
        with open("ua.txt","a",encoding="utf-8")as f:
            f.write(ua+'\n')

