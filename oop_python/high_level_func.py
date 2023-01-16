##



def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


avg = make_averager()
##
# dis(avg)
##

avg(10)
avg(11)
##
series = []


def make_averager2(new_value):
    series.append(new_value)
    total = sum(series)
    return total/len(series)

    # return averager


print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
# 综上，闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定。注意，只有嵌套在其他函数中的函数才可能需要处理不在全局作用域中的外部变量。
# 其实，闭包指延伸了作用域的函数，其中包含:函数定义体中`引用`但是不在定义体中`定义`的非全局变量。
# 函数是不是匿名的没有关系，关键是它能访问定义体之外定义的非全局变量。
##


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


avg2 = Averager()

avg2(10)
avg2(11)
##
# 自由变量:nonlocal声明


def make_averager_nonlocal():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total  # 显式将两个变量指定为nonlocal
        count += 1
        total += new_value
        return total / count
        # 当 count 是数字或任何不可变类型时，count += 1 语句的作用其实与 count = count + 1 一样。因此，我们在 averager 的定义体中为 count 赋值了，这会把 count 变成局部变量。total 变量也受这个问题影响。为了解决这个问题，Python 3 引入了 nonlocal 声明。
        # 它的作用是把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量。如果为 nonlocal 声明的变量赋予新值，闭包中保存的绑定会更新。
        # python中的变量主要有local,global,nonlocal类型,其中nonlocal类型在python2中是没有的
    return averager


avg3 = make_averager_nonlocal()
avg3(4)
avg3(8)
##

