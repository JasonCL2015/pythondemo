# -*-coding:utf-8-*-
# -------------------------tuple的使用--------------------------

tuple1 = ('两点水', 'twowater', 'liangdishui', 123, 456)
tuple2 = '两点水', 'twowater', 'liangdishui', 123, 456
tuple3 = ()
tuple4 = (123,)
tuple5 = (123)
# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(tuple4)
# print(tuple5)

# print(tuple1[4])
# print(tuple1.count(123))
# print(len(tuple1))
# print(tuple1 + tuple2)
# print(tuple1*3)

# for x in tuple1:
#     print(x)
#
# print(tuple(tuple1))

name1 = ('一点水', '两点水', '三点水', '四点水', '五点水')

name2 = ('1点水', '2点水', '3点水', '4点水', '5点水')

list1 = [1, 2, 3, 4, 5]

# 计算元素个数
print(len(name1))
# 连接,两个元组相加
print(name1 + name2)
# 复制元组
print(name1*2)
# 元素是否存在 (name1 这个元组中是否含有一点水这个元素)
print('一点水' in name1)
# 元素的最大值
print(max(name1))
# 元素的最小值
print(min(name1))
# 将列表转换为元组
print(list1)
t1 = tuple(list1)
print(t1)
print(list1)