def factorial(n):

    if(n<0):
        # 对于非法输入(负数,我们抛出异常)
        raise ValueError(f"{n} must be a positive number!!")
    f=1
    while(n):
       f*=n
       n-=1
    return f

# print(factorial(5))
def catalan(n):
    # c=1/(n+1)*(factorial(2*n))/(factorial(n)**2)
    c=factorial(2*n)/(factorial(n+1)*factorial(n))
    return int(c)
# print(catalan(4))

# 打印前n个catalan数
def get_catalan_seq_tops(n):
    # l=[catalan(i) for i in range(1,n+1)]
    print("n:catalan(n)")
    for i in range(0,n+1):
        c=catalan(i)
        print(f"{i}:{c}")    
if __name__=="__main__":
    get_catalan_seq_tops(10)
#前十个: [1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]
# PS D:\repos\PythonLearn>  py catalan.py
# n:catalan(n)
# 0:1
# 1:1
# 2:2
# 3:5
# 4:14
# 5:42
# 6:132
# 7:429
# 8:1430
# 9:4862
# 10:16796