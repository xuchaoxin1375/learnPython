from dis import dis

b = 1


def test0(a):
    print(a)
    print(b)
    b = 100
    print("---")


def test1(a):
    print(a)
    print(b)
    # b=100
    print("---")


def test2(a):
    print(a)
    global b
    b = 20
    print(b)
    print("---")





def byte_codes(func):
    print("========```````oooooooo",func.__name__,"oooooooo`````````=======")
    dis(func)


if __name__ == "__main__":
    test1(3)
    test2(3)
    print(b)
    print("---")
    # dis(test0)

    list(map(byte_codes, [test0, test1, test2]))
