
import functools
from clockdeco import clock


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


@functools.lru_cache()  
# 注意，必须像常规函数那样调用 lru_cache。这一行中有一对括号：@functools.lru_cache()。
# 这么做的原因是，lru_cache 可以接受配置参数，稍后说明。
@clock  
# 这里叠放了装饰器：@lru_cache() 应用到 @clock 返回的函数上。
# 这样一来，执行时间减少了，而且 n 的每个值只调用一次函数：
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)

# 除了优化递归算法之外，lru_cache 在从 Web 中获取信息的应用中也能发挥巨大作用。
# 特别要注意，lru_cache 可以使用两个可选的参数来配置。它的签名是：
# functools.lru_cache(maxsize=128, typed=False)
# maxsize 参数指定存储多少个调用的结果。缓存满了之后，旧的结果会被扔掉，腾出空间。
# 为了得到最佳性能，maxsize 应该设为 2 的幂。
# typed 参数如果设为 True，把不同参数类型得到的结果分开保存，即把通常认为相等的浮点数和整数参数（如 1 和 1.0）区分开。
# lru_cache 使用字典存储结果，而且键根据调用时传入的定位参数和关键字参数创建，所以被 lru_cache 装饰的函数，它的所有参数都必须是可散列的。
if __name__ == '__main__':
    # print(fibonacci(6))
    print(fibonacci2(6))

# 接下来讨论吸引人的 functools.singledispatch 装饰器。