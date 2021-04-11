'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-04-07 10:14:46
LastEditors: xuchaoxin
LastEditTime: 2021-04-07 11:23:36
'''
ls=[["'name': 'IBM'", " 'shares': 100", " 'price': 91.1"], ["'name': 'AAPL'", " 'shares': 50", " 'price': 543.22"], ["'name': 'FB'", " 'shares': 200", " 'price': 21.09"], ["'name': 'HPQ'", " 'shares': 35", " 'price': 31.75"], ["'name': 'YHOO'", " 'shares': 45", " 'price': 16.35"], ["'name': 'ACME'", " 'shares': 75", " 'price': 115.65"]]
print(int(ls[0][1].split(":")[1]))
print(float(ls[0][2].split(":")[1]))
print(int(ls[0][1].split(":")[1])*float(ls[0][2].split(":")[1]))