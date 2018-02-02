import datetime
# print(datetime.datetime.strptime("","%Y-%m-%d"))
# a = {"qqq":['qqq']}
# print(a.get("qq",""))
# # if a["dasdad"]:
# # 	print(a["dasda"])
# # else:
# # 	print("qqqq")
# print(len([""]))
# import re
# a = re.compile('(\d+\.\d+)').findall("45.00")
# print(a)
# print(float(1.0))
import pymysql
conn = pymysql.connect(
            host ="localhost",
            db = "test",
            user = "root",
            password = "1127",
            charset = "utf8",
            port = 3306,
            use_unicode=True)

cursor = conn.cursor()


inser_sql  ='select * from yu'
cursor.execute(inser_sql)
result =cursor.fetchone()
print(result)
conn.commit()
conn.close()



