'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-03-23 22:23:38
LastEditors: xuchaoxin
LastEditTime: 2021-03-24 22:24:26
'''
# """ a=input('请输入省份:')
# b=input('请输入城市:')
# c=input('请输入景点:')
# s=a+'省'+b+'市'+c+'景点!'
# print('欢迎来到:',s) """

# a=((1,2,3,6),(4,5,6,8),(7,8,9,6),(5,2,8,7))
# max=a[0][0]
# min=max
# average=min
# sum=0

# list=[j for i in a for j in i]
# for i in list:
#     if i>max:
#         max=i
#     elif i<min:
#         min=i
#     sum+=i
a = [1, 6, 3]
# b=a.sort()
# b = a
# a.sort()
c=a
# print(b)
print(a.sort())
# print(c)

# print(a.sort())

# print("max=%d,min=%d,average=%s"%(max,min,sum/len(list)))
# s = {'学号': ['姓名', '性别', '年龄', '婚否', ('高数', '英语', '体育', '软件')],
#      '1901': ['张三', '男', 19, True, (90, 92, 98, 96)],
#      '1902': ['李四', '女', 16, False, (95, 96, 99, 97)],
#      '1903': ['王五', '男', 18, True, (97, 91, 95, 98)]}
# print(s)
# for x in s.keys():
#     print(x, s[x])
# s['1904'] = ['孙六', '女', 20, False, None]
# s['1905'] = ['赵七', '女', 22, True]
# for x in s.keys():
#     print(x, s[x])
# s['1904'] = ['孙六', '女', 20, False, (99, 99, 99, 99)]
# for x in s.keys():
#     print(x, s[x])
# s.pop('1905')
# for x in s.keys():
#     print(x, s[x])
# if '1904' in s.keys():
#     print('1904', s['1904'])
# if '1905' not in s.keys():
#     print('查无此人!')
# print('学生人数：', len(s)-1)

# u = {1, 2, 3, 4, 5, 6}
# v = {5, 6, 7, 8, 9}
# w = {'a', 'b', 'c', 5, 6, 7, True}
# # union=u.union(v).union(w)
# union=u|v|w
# print(union)
# # mix=u.intersection(v).union(w)
# mix=u&v|w
# print(mix)
# sub=u-v-w
# print(sub)
# print(u^v)
# print(v^w)

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={}\t'.format(j, i, i*j), end='')
    print() 
