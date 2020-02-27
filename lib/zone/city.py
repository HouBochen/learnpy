cities = {
    'bj': '北京',
    'cd': '成都',
    'cq': '重庆',
    'cs': '长沙',
    'dg': '东莞',
    'dl': '大连',
    'fs': '佛山',
    'gz': '广州',
    'hz': '杭州',
    'hf': '合肥',
    'jn': '济南',
    'nj': '南京',
    'qd': '青岛',
    'sh': '上海',
    'sz': '深圳',
    'su': '苏州',
    'sy': '沈阳',
    'tj': '天津',
    'wh': '武汉',
    'xm': '厦门',
    'yt': '烟台',
}

dis_temp = {
    'bj':['东城','西城'],
    'sz':['福田','南山']
}

str_temp = {
    '南山':['粤海','蛇口'],
    '福田':['梅林','福田中心'],
    '东城':['安贞','朝阳门'],
    '西城':['新街口','西四']
}


# 通过命令指定爬取哪些城市
def get_city():
    return 'bj'

# 爬取某个城市的行政区,返回行政区列表    
def get_districs(city):
    return dis_temp[city]
# 爬取街道的名称，返回街道列表
def get_streets(district,city='sz'):
    return str_temp[district]

if __name__ == '__main__':
    print(get_streets('南山'))