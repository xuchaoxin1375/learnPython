# -*- coding: utf-8 -*-
#rematch_search.py
import re
pattern=re.compile('h.llo')
result1=re.match(pattern,'hello C') #1
result2=re.match(pattern,'C hello') #2
result3=re.match(pattern,'helo') #3
result4=re.match(pattern,'hello world') #4
print(result1)
if result1: print('1匹配:',result1.group())
else: print('1匹配:失败')
if result2: print('2匹配:',result2.group())
else: print('2匹配:失败')
if result3: print('3匹配:',result3.group())
else: print('3匹配:失败')
if result4: print('4匹配:',result4.group())
else: print('4匹配:失败')

#rematch_search.py
import re
res1=re.match('[a-z]oo','seafood')
print('match匹配:',res1)
if res1: print(res1.group())
res2=re.search('[a-z]oo','seafood')
print('search匹配:',res2)
if res2: print(res2.group())


xx = re.match(r"(..)+", "a1b2c3")
yy = re.match(r"(..)..(..)", "a1b2c3")
print(xx.group(0),xx.group(1),xx.groups())
print(yy.group(0),yy.group(1),yy.groups())

m=re.match(r'(\w+) (\w+)(?P<char>.*)','hello world djkfa fjkda!')
print(m.groups())
print(m.group(0))