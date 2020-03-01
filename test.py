import os

l1 = ['a','b','c','d']
l2 = ['aaa']

print('l1:{0}'.format(l1))
print('l2:{0}'.format(l2))
l2.extend(l1)
print(l2)

dic1 = {'dongchengqu':'bj','xichengqu':'bj'}

print(dic1.keys(),dic1.values())

temp = ['hello' for i in range(3)]
print(temp)



# temp = [None for i in range(len(areas))]
