name = ['一点水', '两点水', '三点水', '四点水', '五点水']
print(name)
print(name[0])
print(name[0:2])
print(name[2:5])
# 更改元素
name[1] = '新两点水'
print(name)
# 复制列表
name2 = name.copy()
print(name2)
# 指定位置插入元素
name.insert(2, "aaa")
print(name)
# 列表末尾添加元素
name.append('六点水')
print(name)
# 删除指定位置元素
del name[2]
print(name)
# 删除指定元素，列表倒序
name.remove('六点水')
name.reverse()
print(name)

# 列表长度
print(len(name))
# 列表元素最大值、最小值
print(max(name))
print(min(name))

name.extend(name2)
print(name)

print(name2.pop(1))
print(name2)
