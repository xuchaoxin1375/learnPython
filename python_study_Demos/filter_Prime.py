'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-01 20:30:12
LastEditors: xuchaoxin
LastEditTime: 2021-03-24 17:25:49
'''
""" 用Python来实现这个算法，可以先构造一个从3开始的奇数序列： 
首先,任何一个数n都给可以表示成一系列仅包含质数(的幂)的乘积,并且这些质因子不大于n(这很重要)
此外,如果某个数n是一个质数,那么它只有其本身和1这两个因子
从最小质数集{2},用第一个质数2去筛选自然数,得到的序列中的最小者(第一个元素3),3的质因子表达式中没有比它小质数2(因为含有因子2的数被筛掉了),
又因为3的质因子不能大于3本身,所以3本身就是下一个质数,同理,用3去筛,得到的新序列中的第一个元素5的质因子展开式中必然没有比5本身小的质因子2,3(其他小于5的数被作为合数被筛掉了,这些书必然不是它的因子,如果是,它也在之前就被筛掉,不会留到当下再判断了)
而5的质因子不大于5,所以5本身就是质数...,对于
"""


def _odd_iter():
    """产生序列:3,5,7,9,11,13,15,17.....(从3开始的奇数序列
    弄清某个迭代器(生成器)的作用的一个较好方法时枚举出前几项(有比较直观的感受)

    可以通过手工枚举,也可以通过for来枚举(注意break 的条件编写))

    Yields:
        [int]: [奇数序列中的元素]
    """
    n = 1
    while True:
        n = n + 2
        yield n
# 测试生成器（methond1：using debug to set breakpoint)
# for i in _odd_iter():
#     print(i)


""" 注意这是一个生成器函数(函数生成器)，并且是一个无限序列。
"""
""" 枚举出一部分迭代器产生的元素以观察其功能 """
# method2(recommended)
# for i in _odd_iter():
# #print the element smaller than 100:
#     if(i > 100):
#         break
#     print(i)

"""
然后定义一个筛选函数： """


def _not_divisible(divisor):
    """the higherOrder function return a lambda function

    Args:
        n (int): divisor(is used for judging the integer x whether could be divisible by n)

    Returns:
        a lambda function: to judge the divisible(return the bool value(True/False),we want to filter the integer which couldn't be divisible by n,to make up(generate) the new sequence)
    """
    """ return the lambda function:x is the parameter of the lambda expression 
    because we need to pass two parameter :element from iterator;the prime number to be the divisor
    we could return a lambda function to achieve it:the lambda contains two variable:x(passed from the iterator to be the divisor),n(passed from _not_divisible())"""
    """ write the doc for the lambda:
    x:the element of the iterator"""
    return lambda x: x % divisor > 0


""" 最后，定义一个生成器，不断返回下一个素数： """


def primes():
    """calculate the prime number   

    Yields:
        [int]: [the calculate result ]
    """
    """ initial return(yield) the specific prime :2 """
    yield 2
    """bind the odd integers generator to the variable it
    """
    it = _odd_iter()  # 初始序列(iterator) the statement will just be execute once,then the while loop will update the iterator
    while True:
        # 返回序列的第一个数(this number will be the screen(filter) to be the parameter of the _notdivisible())
        """  get a element from the _odd_iter() ,assign to it(int type) """
        n = next(it)
        """ pop the first element of the number sequence--the next prime number"""
        yield n
        # 通过筛选函数,再次执行以n为筛子进行筛选,构造新序列(update the iterator to iterate the process)
        """ update the iterator :use the prime founded (it is:n)just now to be the divisor to generator a new iterator represent the new sequence
        the filter is:judge the element of iterator which make the filter function return True"""
        it = filter(_not_divisible(n), it)
        """ TypeError: <lambda>() missing 1 required positional argument: 'n'
        we need a highorder function to utilize the filter() to pass n and the element of the iterator"""
        # it=filter((lambda x,n:x%n>0),it)


""" 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件 """
# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
""" 注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。 """
