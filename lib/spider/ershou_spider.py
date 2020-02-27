from lib.utility.path import *
from lib.zone.city import *
from lib.spider.base_spider import *
import threadpool

st_dic = {}

class ErShouSpider(BaseSpider):
	

	def start(self):
		city = get_city()
		#创建保存数据的目录
		self.today_path = create_date_path('{0}/ershou'.format(SPIDER_NAME),city,self.date_string)
		
		# t1 = time.time()

		# 获取到某个城市有多少个行政区
		districts = get_districs(city)
		print('City:{0}'.format(city))
		print('Districts:{0}'.format(districts))

		# 获取某个行政区有多少个街道
		streetlist = []
		# st_dic = {}
		for district in districts:
			streets = get_streets(district)
			print('District {0}: Streets: {1}'.format(district,streets))
			streetlist.extend(streets)
			for item in streets:
				st_dic[item] = district
		print('streetlist:{0}'.format(streetlist))
		print('st_dic:{0}'.format(st_dic))
		# 准备参数
		nones = [None for i in range(len(streetlist))]
		city_list = [city for i in range(len(streetlist))]
		args = zip(zip(city_list,streetlist),nones)
		# print(list(args))
		# args: [(('bj', '安贞'), None), (('bj', '朝阳门'), None), (('bj', '新街口'), None), (('bj', '西四'), None)]

		pool_size = THREAD_POOL_SIZE
		pool = threadpool.ThreadPool(pool_size)
		my_requests = threadpool.makeRequests(self.save_data, args)
		[pool.putRequest(req) for req in my_requests]
		pool.wait()
		pool.dismissWorkers(pool_size, do_join=True)  # 完成后退出

	# 保存文件
	def save_data(self,city_name,street_name,fmt='csv'):
		# district_name = st_dic.get(street_name)
		# csvfilename = self.today_path + '/{0}_{1}.'.format(district_name,street_name) + fmt
		# with open(csvfilename,'w') as f:
		# 	results = self.collect_data(city_name,street_name)
		# 	for result in results:
		# 		f.write(result+'\n')
		# print('ok')
		print('cityname:{0}'.format(city_name))
		print('streetname:{0}'.format(street_name))

	# 爬取內容
	def collect_data(self,city_name,street_name):
		return ['hello' for item in range(10)]

if __name__ == '__main__':
	pass