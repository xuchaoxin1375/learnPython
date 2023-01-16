

registry = set()  
def register(active=True):  #register 接受一个可选的关键字参数。
    def decorate(func):  # decorate 这个内部函数是真正的装饰器；注意，它的参数是一个函数。
        print('running register(active=%s)=decorate(%s)'
              % (active, func))
        if active:   
            registry.add(func)
        else:
            registry.discard(func)  
        return func  # decorate 是装饰器，必须返回一个函数。
    return decorate  #register 是装饰器工厂函数，因此返回真正装饰器函数:decorate。
@register(active=False) 
def f1():
    print('running f1()')
@register()  
def f2():
    print('running f2()')

def f3():
    print('running f3()')
    
    
##
import time

DEFAULT_FMT = '[{elapsed:0.8f}s😁] {name}({args}) -> {result}'
def clock(fmt=DEFAULT_FMT):   #clock 是参数化装饰器工厂函数
    # print("工厂接受到的参数",fmt)
    def decorate(func):#decorate 是真正的装饰器。
        def clocked(*_args):  #clocked 包装被装饰的函数。#_args 是 clocked 的参数
            t0 = time.time()
            _result = func(*_args)  #_result 是被装饰的函数返回的真正结果。
            #显示内容:
            elapsed = time.time() - t0
            name = func.__name__+"🤣"
            args = "🎈 ".join(repr(arg) for arg in _args)  #_args 是 clocked 的参数，args 是用于显示的字符串。
            result = repr(_result)  #result 是 _result 的字符串表示形式，也是用于显示。
            #显示全部内容:
            # print(elapsed,name,args,result)
            #显示格式控制,显示部分内容(locals()函数会以字典类型返回当前位置的全部局部变量。fmt字符串则指定了哪些变量要被以某种格式打印出来)
            print(fmt.format(**locals())) 
            return _result  #返回被装饰的函数func的结果
        return clocked  #真正装饰器decorate返回函数clocked(替代被装饰函数func的逻辑/函数体)
    return decorate  #装饰器工厂函数返回真正的装饰器函数decorate
if __name__ == '__main__':

    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
    # 格式控制1
    @clock('{name}: {elapsed}s')#clock这里是装饰器工厂,格式控制字符串作为工厂函数的参数;而真正的装饰器有该工厂函数的调用(@句法)返回,该返回结果decorate作为下方被修饰的snooze1函数的直接装饰器;snooze1作为decorate的参数;而snooze1的参数seconds则被传给最内的clocked作为参数(snooze1和它的代替者clocked共享参数seconds)
    def snooze1(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze1(.123)
    # 格式控制2
    @clock('{name}({args}) dt={elapsed:^12.3f}s')
    def snooze2(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze2(.123)

