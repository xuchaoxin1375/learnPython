registry_list = []


def register(func):
    print('🎈running register(%s)🎈' % func)
    registry_list.append(func)
    return func




@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')

##
def f3():
    print('running f3()')


def main():
    print('running main()...')
    print('\tregistry =', registry_list)
    f1()
    f2()
    f3()



if __name__ == '__main__':
    main()

##
