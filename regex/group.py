import re
p = re.compile(r'(?P<word>\b\w+\b)')
# test text:
txt='((((Lots of punctuation)))'
m = p.search(txt)
# "word" 对应的分组正则规则:\b\w+\b
# 取出匹配对象m中的子组("word"规则对应的子组)
result1=m.group("word")
result2=m.groups("word")
print(result1)
print(result2)
result_findall = p.findall(txt)

print(result_findall)

##
m = re.match("([abc])+", "abc")
m.groups()

##
m=re.match(r"[abc]","aa")
m.groups()
m=re.findall(r"[abc]+","pabbpcc cbacbaa")
m
##
