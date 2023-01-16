import functools
import time
from dis import dis
def clock(func):
    """ 定义了一个装饰器，它会在每次调用被装饰的函数时计时，然后把经过的时间、传入的参数和调用的结果打印出来。 """
    def clocked(*args):  # 定义内部函数 clocked，它接受任意个定位参数。
        t0 = time.perf_counter()
        result = func(*args)  # clocked 的闭包中包含自由变量 func,来自clock函数的形参。
        # 执行完func指定的任务,再次计时,计算任务耗时
        elapsed = time.perf_counter() - t0
        # 函数调用信息:函数名和函数func的参数值检查
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        # 还原打印调用的语句
        print('time elapsed:[%0.8fs] funcName: %s(arg:%s) -> %r' %
              (elapsed, name, arg_str, result))
        return result
    return clocked  # 返回内部函数，取代被装饰的函数。


def border(func):
    """打印边界

    Parameters
    ----------
    func : str
        边界字符

    Returns
    -------
    Function
        边界打印逻辑函数对象
    """
    def printer_with(*args):
        print("-"*40)
        result = func(*args)
        print("result=%d" % result)
        print("`"*40)
        return result
    return printer_with


##
# clockdeco_demo.py


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

# 工作原理

# @clock
# def factorial(n):
#     return 1 if n < 2 else n*factorial(n-1)

# 其实等价于：


def factorial2(n):
    return 1 if n < 2 else n*factorial(n-1)


factorialk = clock(factorial2)


@border
def df_recursive(n):
    return n if n == 1 or n == 2 else n*df_recursive(n-2)

# clockdeco2.py

##


def clock2(func):
    # @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock2
def factorial3(n=3):
    return 1 if n < 2 else n*factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    df_recursive(8)
    factorial3(n=6)


# 将clock函数作为factorial函数的装饰器:将是的factorial会作为 func 参数传给 clock .
# 这个过程不像手动传参那样处理,而是通过@decorator语法在定义带装饰器函数的时候指定的
# 然后， clock 函数会返回 clocked 函数，Python 解释器在背后会把 clocked 赋值给 factorial。
# 所以，现在 factorial 保存的是 clocked 函数的引用。自此之后，每次调用 factorial(n)，执行的都是 clocked(n)。
# clocked 大致做了下面几件事。
# (1) 记录初始时间 t0。
# (2) 调用原来的 factorial 函数，保存结果result。
# (3) 计算经过的时间。
# (4) 格式化收集的数据，然后打印出来。
# (5) 返回第 2 步保存的结果result。
# 这是装饰器的典型行为：把被装饰的函数替换成新函数，二者接受相同的参数，
# 而且（通常）返回被装饰的函数(func)本该返回的值，同时还会做些额外操作。
# 在clock2函数的定义中,使用了functools
# functools.wraps 只是标准库中拿来即用的装饰器之一。
# functools 模块中最让人印象深刻的两个装饰器：lru_cache 和 singledispatch。
