import requests, json
 
#  定义python 字典
d = {'name':'jod'}
# 字典d序列化成json字符串
d2j = json.dumps(d)
print("d2j",d2j,type(d2j))
 
#json反序列化成字典
j2d=json.loads(d2j)
print ("j2d",j2d,type(j2d))
