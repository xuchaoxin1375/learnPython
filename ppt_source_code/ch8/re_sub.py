# -*- coding: utf-8 -*-
# 在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string，不要转译反斜杠 '\' 。
# 例如，\n 在raw string中，是两个字符，\和n， 而不会转译为换行符。
# 由于正则表达式和\会有冲突，因此，当一个字符串使用了正则表达式后，最好在前面加上'r'。

# 与大多数编程语言相同，正则表达式里使用"\"作为转义字符，这就可能造成反斜杠困扰。
# 假如你需要匹配文本中的字符"\"，那么使用编程语言表示的正则表达式里将需要4个反斜杠"\\\\"：
# 前两个和后两个分别用于在编程语言里转义成反斜杠，转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。
# Python里的原生字符串很好地解决了这个问题，这个例子中的正则表达式可以使用r"\\"表示。
# 同样，匹配一个数字的"\\d"可以写成r"\d"。
# 有了原生字符串，你再也不用担心是不是漏写了反斜杠，写出来的表达式也更直观。

# 不是说 加了r \就没有转译功能，好乱，就直接记住1句话：
# 当一个字符串使用了正则表达式后，最好在前面加上'r'，这样你再也不用担心是不是漏写了反斜杠，写出来的表达式也更直观
# re_sub.py
import re


def test1():
    pattern_str = "a"
    to_str = "A"
    be_placed_str = "abcasd"
    re_pattern = re.compile("a")
    result = re_pattern.sub(to_str, be_placed_str)
    # rex=re.compile()
    # result=re.sub()m
    print(result)
    r1 = re.sub('a', 'A', 'abcasd')  # 找到a用A替换
    print(r1)
    pat = re.compile('a')
    r2 = pat.sub('A', 'abcasd')
    print(r2)
    pat = re.compile('(blue|white|red)')
    r3 = pat.sub('colour', 'blue socks and red shoes')
    print(r3)


def test2():
    pat = re.compile(r'www\.(.*)\..{3}')  # 正则表达式
    r4 = pat.match('www.dxy.com').group(1)
    print(r4)  # dxy
    r5 = re.sub(r'www\.(.*)\..{3}', r'\1', 'hello,www.dxy.com')  # r'1'是第一组的意思
    print(r5)  # hello,dxy
    # 同样的:用模式串对象来操作
    r6 = pat.sub(r'\1', 'hello,www.dxy.com')
    print(r6)  # hello,dxy
    # 该匹配中,找到符合规则的子字符串是"www.dxy.com",借助sub(),
    # 达到用组1字符串(这里组1(第一个括号)匹配到的字符串是dxy,dxy去替换匹配的整个被匹配到的字符串(www.dxy.com被替换为dxy,而hello由于没有被模式串匹配到,
    # 所以得到保留)
    pat = re.compile(r'(\w+) (\w+)')  # 正则表达式
    s = 'hello world ! hello hz !'
    r7 = pat.findall('hello world ! hello hz !')
    print(r7)
    r8 = pat.sub(r'\2 \1', s)
    # 通过正则得到组1(hello)，组2(world)
    # 再通过sub去替换。即组1替换组2，组2替换组1，调换位置。
    print(r8)


# 这种的函数repl参数可以起到一个将被匹配的串做一个映射,然后将映射结果替换掉原来的部分
def _add111_map_method(match):
    # print(type(match))#re.Match<>
    intStr = match.group("number")  # group(name),由?P<name>定义
    intValue = int(intStr)
    addedValue = intValue + 111
    addedValueStr = str(addedValue)
    return addedValueStr


inputStr = "hello 123 world 456"
# 类似于filter/map()操作
replacedStr = re.sub("(?P<number>\d+)", _add111_map_method, inputStr)
# 模式字符串中?P<name>是给正则匹配中的组起一个名字:name of group(i)
# 这种方式的好处是于序号无关，都是这个名字，与圆括号的顺序无关，
# 它出现在的那对括号内，就表示这个括号内匹配的内容就是group(name)
print("replacedStr=", replacedStr)  # 结果：hello 234 world 567
