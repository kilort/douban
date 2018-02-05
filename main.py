from scrapy.cmdline import execute
import sys,os
#debug
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
execute(["scrapy","crawl","basic_douban"])