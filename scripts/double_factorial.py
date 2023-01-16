# importing functools for reduce()
# import functools as ft
##
from functools import reduce


def product(x, y):
    return x*y


def df_reduce(n):
    l = range(n, 0, -2)
    res = reduce(lambda x, y: x * y, l)
    #     print("n=%-3d-->" % n, "{:-^30}".format(list_str), "product_res=%d" % res)

    return res


def df_while(n):
    res = 1
    while (n > 0):
        res *= n
        n = n-2
    return res


def df_k(n):
    q = n//2
    r = n % 2
    k = q-1+r
    l = range(0, k+1)
    res_list = [n-2*i for i in l]
    res = reduce(product, res_list)
    return res


def df_recursive(n):
    # if (n == 1 or n == 2):
    #     return n
    # return n*df_recursive(n-2)
    return n if n == 1 or n == 2 else n*df_recursive(n-2)


def df_print(df_fun, n):
    res = df_fun(n)
    print("n=%-3d-->" % n, "product_res=%d" % res)


def df_reduce_print(n):
    df_print(df_reduce, n)


def df_while_print(n):
    df_print(df_while, n)


def df_k_print(n):
    df_print(df_k, n)


def df_recursive_print(n):
    df_print(df_recursive, n)


def test(df_implements):
    for df_fun in df_implements:
        print("{:*^70}".format(str(df_fun)))
        list(map(df_fun, test_list))


##
test_list = [3, 4, 5, 8, 9, 16]
if __name__ == "__main__":
    # res = list(map(df_while_print, test_list))
    df_implements = [df_k_print, df_while_print, df_reduce_print,df_recursive_print]
    test(df_implements)
    # list(map(df_recursive_print,test_list))
    # print(df_k(5))
    # df_implements = [df_k, df_while,  df_reduce, df_recursive]
    

##
