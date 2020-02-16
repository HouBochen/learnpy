from lib.spider.base_spider import *
from lib.utility.path import *

class ErShouSpider(BaseSpider):
	def start():
		city = 'bj'
		self.today_path = create_date_path('{0}/ershou'.format(SPIDER_NAME),city,self.date_string)


if __name__ == '__main__':
	ershou = ErShouSpider('bj')