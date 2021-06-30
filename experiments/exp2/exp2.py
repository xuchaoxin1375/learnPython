
# string_list=["test1", "test2", "test3"]
# for i in map(lambda string: string+"_good",string_list):
#     print(i)


# from functools import reduce

# """ the function just to ignore the float point to turn to a integer number:  """


# def strToInteger(s):
#     def fn(x, y):
#         return x * 10 + y

#     def char2num(s):
#         """ create a built-in dict to deal with map references """
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     """ use map and reduce: """
#     """ use: map(char2num, s.replace(".","") to transfor the digit char to int digit
#     use: the reduce to iterate(reduce) the scale of the input """
#     return reduce(fn, map(char2num, s.replace(".", "")))


# def str2float(s):
#     """ if you meet the float ,turn make a divide by a proper number to convert it to a float correctly"""
#     if s.find(".") != -1:
#         print('str2float(\'%s\') =' % s, strToInteger(
#             s)/pow(10, (len(s)-s.find(".")-1)))
#     else:
#         print('str2float(\'%s\') =' % s, strToInteger(s))

# s = "1234.56"
# str2float(s)


# dict=[{'id':'4','name':'b'},{'id':'6','name':'c'},{'id':'3','name':'a'},{'id':'1','name':'g'},{'id':'8','name':'f'}]
# dict.sort(key=lambda dict:(int)(dict['id']))
# print(dict)


# def extrem_value_dict(list):
#     dict={}
#     dict['min']=min(list)
#     dict['max']=max(list)
#     return dict

# test_list=[5,7,4,2,7,899,0]
# print(extrem_value_dict(test_list))


# people = [('牛牛', 'F', 15), ('道长', 'M', 12), ('大师兄','M', 10), ('小师妹','F', 13)]
# people.sort(key=lambda tuple:tuple[2])
# print(people)

# def classifier(ls):
#     list_small = []
#     list_big = []
#     list_odd = []
#     dict = {'k1': list_small, 'k2': list_big, 'k3': list_odd}
#     for i in ls:
#         if i <= 66:
#             list_small.append(i)
#         elif i > 66:
#             list_big.append(i)
#         if i % 2 == 1:
#             list_odd.append(i)
#     return dict


# ls = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 200, 230, 330]


# def sum_of_squares(odd_dict):
#     return sum(([i*i for i in odd_dict["k3"]]))

# dict = classifier(ls)
# print(dict)
# print("sum_of_squares(dict)=",sum_of_squares(dict),sep="")

# def deal_dict(dict):
#     """ result_dict: """
#     ret = {}
#     for key,value in dict.items():
#         if len(value) > 2:
#             """ use section """
#             ret[key] = value[0:2]
#         else:
#             """ the length doesn't longer than 2,return directly: """
#             ret[key] = value
#     """ return the finally result_dict """
#     return  ret

# dict = {"key1": "v0v1", "key2": [11, 22, 33, 44],"k3":"1sdf2"}
# r = deal_dict(dict)
# print(r)

# def func(*list_args):

#     all_list = []  # test
#     for i in list_args:
#         """ (function) isinstance: (__obj: object, __class_or_tuple: type | Tuple[type | Tuple, ...]) -> bool;
#         Return whether an object is an instance of a class or of a subclass thereof.
#         A tuple, as in isinstance(x, (A, B, ...)), may be given as the target to check against. This is equivalent to isinstance(x, A) or isinstance(x, B) or ... etc. """
#         if isinstance(i, list):
#             """
#             (method) extend: (__iterable: Iterable) -> None
#             Extend list by appending elements from the iterable. """
#             all_list.extend(i)
#         else:
#             return "列表参数有错误，请重新输入列表："
#     all_list.sort()
#     return all_list[-1]
# tempString=func([178, 29, 579, 13], [900, 454, 65, 445], [12, 54, 2980, 72])
# print(tempString)
""" 函数func()可以接受不定数量的各种参数,但是如果传入了非list类型的实参,那么就会返回:"列表参数有错误，请重新输入列表：";func内部将对输入的参数中list类型的参数进行处理,利用isinstance()来判断各个参数是否为list类型,如果是list类型,那么对list实参中的数字元素通过extend()方法批量的添加到all_list列表中,然后对all_list中的元素进行排序,左后使用all_list[-1]将其中的最大元素打印出来(即2980) """

# def print_up_triangle(n):
#     """ to count the space of each line: """
#     j=n-1
#     for i in range(0,n):
#         print(j*' '+(i*2+1)*'*')
#         j-=1

# def print_down_triangle(n):
#     """ to count the space of each line: """
#     j=1
#     for i in range(n-2,-1,-1):
#         print(j*' '+(2*i+1)*'*')
#         j+=1
# """ the scale n is the sequence:n= 0,1,2,3,...n """
# def print_diamond(n):
#     print_up_triangle(n)
#     print_down_triangle(n)
# scale=input("input a integer to specify the scale of the diamond to be print: ")
# scale=(int)(scale)
# print_diamond(scale)


# import math
# from math import e
# def calculate(a,b,c):
#     return e**b**((math.pi/2)**0.5)+(-b+(b**2-4*a*c)**0.5)/2*a+(math.log10(abs(a+b))+a/b)/math.log(a**b+100,e)
# print("calculate(1,2,3)=%s"%calculate(1,2,3))
# """ test: """
# # print(math.e)
# # print(e)
# # x=math.log(100,10)
# # print(x)


# def count(string):
#     count=0
#     # count=string.replace('ab','AB');
#     while 'ab' in string:
#         string=string.replace('ab','AB',1)
#         count+=1
#     return count
# string=input("input a string contains several 'ab':")
# print("the string contains:%d'ab'\n"%count(string))
# string=string.split(sep='ab')
# print("split as 'ab' result：")
# for i in string:
#     if i.strip():
#         print(i)
# print(string)

# """ iterator """
# def fib_variant(generate_max_times):
#     count = 0
#     a, b = 2, 3
#     while count < generate_max_times:
#         yield a
#         a, b = b, a+b
#         count += 1
#     return "end"

# def fib_variant2(generate_max_times):
#     count = 0
#     a, b = 1, 2
#     while count < generate_max_times:
#         yield a
#         a, b = b, a+b
#         count += 1
# """ test the iterator: """
# # for i in fib_variant(10):
# #     print(i)
# # for i in fib_variant2(10):
# #     print(i)
# """ calculate:sum: 2/1，3/2，5/3，8/5，13/8，21/13."""
# def sum_fib_variant(bound):
#     count = 0
#     f1 = fib_variant(bound)
#     f2 = fib_variant2(bound)

#     """ range from 0(not 1) """
#     for i in range(0, bound):
#         count += next(f1)/next(f2)
#         # print(count)
#     return count

# print("sum_10=%.4f" % sum_fib_variant(10))
# print("sum_20=%.4f" % sum_fib_variant(20))

# def isprime(n):
#     if n==1 or n==0:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return n
# def decompose():
#     n=(int)(input("input a positive integer:"))
#     list_factor=[]
#     list_power=[]
#     list=[list_factor,list_power]

#     """ python3:the dict is ordered! """
#     # dict={}
#     """ use the index variable to guide the power update operation """
#     j=-1
#     i=2
#     # for i in range(2,n):
#     while n>1:
#         # if n==1:
#         #     break
#         if n%i==0:
#             if isprime(i):
#                 """ iterate n: """
#                 n=n//i
#                 """ update the prime factor and its correspondent power  """
#                 if(i not in list_factor):
#                     list_factor.append(i)
#                     list_power.append(1)
#                     j+=1
#                 else:
#                     list_power[j]+=1
#             else:
#                 i+=1
#         else:
#             i+=1
#     return list
# print(decompose())


# print(isprime(7))


# def count(string):

#     count_lowercase=0
#     count_uppercase=0
#     count_digit=0
#     count_others=0

#     for i in string:
#         if i.islower():
#             count_lowercase+=1
#         elif i.isupper():
#             count_uppercase+=1
#         elif i.isdigit():
#             count_digit+=1
#         else:
#             count_others+=1
#     return count_uppercase,count_lowercase,count_digit,count_others
# string= string=input("input a string:")
# """
# 23u0jnd;gjaSSS
# """
# result_tuple=count(string)
# print(result_tuple)
# print(f"count_uppercase={result_tuple[0]},count_lowercase={result_tuple[1]},count_digit={result_tuple[0]},count_others={result_tuple[2]}")
