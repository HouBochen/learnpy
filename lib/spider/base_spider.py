from lib.utility.date import *

SPIDER_NAME = 'ke'

class BaseSpider(object):

	def __init__(self,name):
		self.name = name
		self.date_string = get_date_string()


