from lib.utility.date import *

SPIDER_NAME = 'ke'
THREAD_POOL_SIZE = 10

class BaseSpider(object):

	def __init__(self,name):
		self.spider_name = name
		self.date_string = get_date_string()
