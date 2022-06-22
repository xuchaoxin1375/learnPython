# -*- coding: utf-8 -*-
# re @overload def split(pattern: Pattern[AnyStr],
#           string: AnyStr,
#           maxsplit: int = ...,
#           flags: Union[int, RegexFlag] = ...) -> list[AnyStr]
# Split the source string by the occurrences of the pattern, returning a list containing the resulting substrings. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list.
#re_split.py
import re
p=re.compile(r'\d+')
print(p.split('one1two2three3four4'))

s="str1:str2:str3"
print(re.split(':',s))
print(s.split(':'))


#re_split.py
import re
print(re.split(',','a,s,d,**asd'))#返回列表
pat = re.compile(',')
print(pat.split('a,s,d,**asd'))
print(re.split('[, *]+','a ,  s  ,d ,,**asd')) 
#正则匹配：[, *]+,1个或多个逗号、空格、*等符号均可作为分隔符。
print(re.split('[, *]+','a ,  s  ,d ,,**asd',maxsplit=2)) 
# maxsplit 最多分割次数

