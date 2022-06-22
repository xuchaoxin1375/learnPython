

def factorial(n):
    """传统递归方式编写计算阶乘的函数

    Parameters
    ----------
    n : int
        速度较慢,譬如(n=100)

    Returns
    -------
    计算结果
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fact_iter(num, product=1):
    """尾递归的形式实现阶乘

    Parameters
    ----------
    num : int
        表示需要计算的阶乘的数
        同时表征递归出口(运算次数)
    product : int
        累计计算结果,最终在递归出口返回
        在本调用的执行过程中,后面的函数调用传入的参数累计了上一次调用的计算结果

    Returns
    -------
    int
        计算结果
    """
    # 定义递归出口
    if num == 1:
        return product
    # num * product是计算关键
    # num-1是通往出口的关键
    return fact_iter(num - 1, num * product)
def factorail(n):
    return fact_iter(n, 1)
print(factorial(1000))

factorial_d=[1]
def factorial_speed(n):
    """fast factorial

    Parameters
    ----------
    n : int
        需要计算阶乘的整数

    Returns
    -------
    int
        calculate result
    """
    for n in range(1,n+1):
        factorial_d.append( n * factorial_d[n - 1])
    return factorial_d[n]
if __name__=="__main__":
    # res=factorial(100)
    # print("res1:",res)

    # res=factorial_speed(50)
    # print("res2:",res)
    pass