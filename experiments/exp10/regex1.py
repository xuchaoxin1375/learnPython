s = "I like Python programming 123 because it is 456 simple and elegant."
s = '''see 123, 1987-02-09 07:30:00
    1987-02-15 07:25:00'''
s = """xiasd@163.com, sdlfkj@.com sdflkj@180.com solodfdsf@123.com sdlfjxiaori@139.com saldkfj.com oisdfo@.sodf.com.com"""
# pattern_str=r"\b[A-Za-z_-]+\b"
# pattern_str=r"[\d]{4}-[0|1][\d]-[0|1|2|3][\d] [\d]{2}:[\d]{2}:[\d]{2}"
s = "see 123, 1987-02-09 07:30:00, 1986-02-15 07:25:00"
s = """hi69@qq.com, werksdf@163.com, sdf@sina.com
    sfjsdf@139.com, soifsdfj@134.com
    pwoeir23@126.com"""

import re

field_alnum = "[a-z0-9A-Z]"
pattern_str=f"{field_alnum}+@{field_alnum}+\.com"
# pattern_str = "(?P<number>\d+)"
s_pattern = re.compile(pattern_str)

# substitute_result = s_pattern.sub(repl=add_212_method, string=s)
# substitute_result=re.sub("(?P<number>\d+)",add_212_method,s)
substitute_result=s_pattern.sub("hime@163.com",s)
print(substitute_result)

def add_212_method(match):
    """
    :param match: Match
    :return: sum_result Str
    """
    int_str = match.group("number")
    value_int = int(int_str)
    sum_result = value_int + 212
    return str(sum_result)
# fa1=re.findall("\d+-\d+-\d+",s)
# # ['1987-02-09', '1986-02-15'];整个字符处匹配,返回完整的被匹配值
# fa2=re.findall("(\d+)-\d+-\d+",s)
# #['1987', '1986'];可以匹配到未分组时同样的字符串,但是返回值是返回的括号内(分组)的所匹配到的那部分内容(截取),这里只有一个组,所以每个返回值只有一个子串
# fa3=re.findall("(\d+)-(\d+)-(\d+)",s)
# #[('1987', '02', '09'), ('1986', '02', '15')];可以匹配到未分组时同样的字符串,但是此处分了三组,且仅截取其个括号组匹配到的内容返回
# # 元组的个数有被完全匹配的串决定(但内容由分组情况分别截取构成)
