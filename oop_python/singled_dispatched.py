import html

def htmlize0(obj):
    """ 生成 HTML，显示不同类型的 Python 对象。 """
    """ 这个函数适用于任何 Python 类型，但是现在我们想做个扩展，让它使用特别的方式显示某些类型。
str：把内部的换行符替换为 '<br>\n'；且不使用 <pre>，而是使用 <p>。
int：以十进制和十六进制显示数字。
list：输出一个 HTML 列表，根据各个元素的类型进行格式化。 """
    content = html.escape(str(obj))
    # content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

print(type({1,2,3}))
print(htmlize0({1,2,3}))
print(htmlize0(abs))
## 
from functools import singledispatch
from collections import abc
import numbers
import html
# 定义单分派函数:利用@singledispatch 创建一个自定义的 htmlize.register 装饰器，把多个函数绑在一起组成一个泛函数
@singledispatch  # @singledispatch 标记处理 object 类型的基函数。
def htmlize(obj):
    # 由于本函数被singledispatch所修饰,因此可能在调用的时候因遇到不同类型的参数,函数体(函数行为)被替换为对应的专门函数来处理,下面的逻辑是一种可能的执行方式
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)
#各个专门函数使用 @<base_function>.register(<type>) 装饰。
# 专门函数的名称无关紧要；_ 是个不错的选择，简单明了
@htmlize.register(str)  
def _(text):            
    # 如果传入的参数是str(字符串型),尝试将`\n`替换为<br>,并且标签要从默认的<pre>改为<p>
    content = html.escape(text).replace('\n', '<br>')
    return '<p>{0}</p>'.format(content)
# 为每个需要特殊处理的类型注册一个函数。numbers.Integral 是 int 的虚拟超类。
@htmlize.register(numbers.Integral)  
def _(n):
    # return '<pre>{0} (0x{0:x})</pre>'.format(n)
    return '<pre>{0} ({0:#x})</pre>'.format(n)

# 可以叠放多个 register 装饰器，让同一个函数支持不同类型。
@htmlize.register(tuple)  
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '\n\t</li>\n\n\t<li>\n\t\t🎈'.join(''+htmlize(item) for item in seq)
    return '<ul>\n\t<li>' + inner + '\n\t</li>\n</ul>'
# 只要可能，注册的专门函数应该处理抽象基类（如 numbers.Integral和 abc.MutableSequence），不要处理具体实现（如 int 和list）。
# 这样，代码支持的兼容类型更广泛。例如，Python 扩展可以子类化 numbers.Integral，使用固定的位数实现 int 类型。
# 　使用抽象基类检查类型，可以让代码支持这些抽象基类现有和未来的具体子类或虚拟子类。
# singledispatch 机制的一个显著特征是，你可以在系统的任何地方和任何模块中注册专门函数。如果后来在新的模块中定义了新的类型，可以轻松地添加一个新的专门函数来处理那个类型。
# 此外，你还可以为不是自己编写的或者不能修改的类添加自定义函数。
# singledispatch 是经过深思熟虑之后才添加到标准库中的，它提供的特性很多，这里无法一一说明。这个机制最好的文档是“PEP 443 —Single-dispatch generic functions”（https://www.python.org/dev/peps/pep-0443/）。
# @singledispatch 不是为了把 Java 的那种方法重载带入Python。
# 在一个类中为同一个方法定义多个重载变体，比在一个函数中使用一长串 if/elif/elif/elif 块要更好。
# 但是这两种方案都有缺陷，因为它们让代码单元（类或函数）承担的职责太多。
# @singledispath 的优点是支持模块化扩展：各个模块可以为它支持的各个类型注册一个专门函数。
##测试用例
print(htmlize('Heimlich & Co.\n- a game'))
print(htmlize(['alpha', 66, {3, 2, 1}]))
print(htmlize(15))
print(htmlize(1))
print(htmlize(True))
print(htmlize(1.1))

##
