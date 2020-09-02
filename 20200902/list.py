# -*-coding:utf-8-*-
# ----------------------list的使用---------------------------

# 1.一个产品，需要列出产品的用户，这时候就可以使用一个 list 来表示
user = ['liangdianshui', 'twowater', '两点水']
print('1.产品用户')
print(user)

# 2.如果需要统计有多少个用户，这时候 len() 函数可以获的 list 里元素的个数
print('\n 2.有多少个用户')
print(len(user))

# 3.此时，如果需要知道具体的用户呢？可以用过索引来访问 list 中每一个位置的元素，索引是0从开始的
print('\n 3.第二个用户名称')
print(user[1])

# 4.突然来了一个新的用户，这时我们需要在原有的 list 末尾加一个用户
print('\n 4.在列表末尾添加用户三点水')
user.append('三点水')
print(user)

# 5.又新增了一个用户，可是这个用户是 VIP 级别的学生，需要放在第一位，可以通过 insert 方法插入到指定的位置
print('\n 5.在列表第一位添加学生一点水')
user.insert(0, '一点水')
print(user)

# 6.突然发现之前弄错了，“茵茵”就是'VIP用户'，因此，需要删除“茵茵”；pop() 删除 list 末尾的元素
print('\n 6.删除列表末尾的学生')
user.pop()
print(user)

# 7.过了一段时间，用户“liangdianshui”不玩这个产品，删除了账号
print('\n 7.删除liangdianshui')
user.remove('liangdianshui')
print(user)

# 8.用户“两点水”想修改自己的昵称了
print('\n 8.修改两点水名称为两滴水')
user[user.index('两点水')] = '两滴水'
print(user)

# 9.单单保存用户昵称好像不够好，最好把账号也放进去
print('\n 9.把两点水放进列表')
user.append('两点水')
print(user)