from scrapy.cmdline import execute
import sys,os
# print(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
execute(["scrapy","crawl","basic_douban"])