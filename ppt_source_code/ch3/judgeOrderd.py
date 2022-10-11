# l=list(range(10))
# print(l)
# disorder_list=rand.shuffle(order_list)
# print(order_list)
import random as rand

ordered_list = list(range(4))
# ordered_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# d1 = [2, 1, 0, 8, 9, 5, 7, 6, 3, 4]
# disorder_list=[d1,d2,d3]
# print(ordered_list)

# def judgeOrder(l, i=0, ascend=True, asc_mark=0, dsc_mark=0):
#     len_l = len(l)
#     print(asc_mark,dsc_mark)
#     if asc_mark and dsc_mark:
#         print("disorder!!")
#         return False

#     if i >= len_l - 1:
#         print(l, "orderd!")
#         return True

#     elif l[i] <= l[i + 1]:
#         asc_mark += 1
#     else:
#         dsc_mark += 1
#     judgeOrder(l, i + 1,asc_mark,dsc_mark)


def judgeOrder(l, i=0, order=0,log=0):
    len_l = len(l)
    asc_mark = 0
    dsc_mark = 0

    while (i < len_l - 1):
        # print(asc_mark, dsc_mark)
        if l[i] <= l[i + 1]:
            asc_mark += 1
        else:
            dsc_mark += 1
        if asc_mark and dsc_mark:
            if log:
                print(l, "disorder!!")
            return False
        else:
            i += 1

    # if(log):
    print(l, "ascend👆" if asc_mark else "dscend⏬", "orderd!")
    if (not order):
        return True
    elif (order == 1 and asc_mark):
        return True

    elif (order == -1 and dsc_mark):
        return True
    return False


# def judgeOrderRecursiveDescend(l, i=0):

if __name__ == "__main__":
    n=40
    print(ordered_list)
    # ordered_list=[42,311,111,110]
    judgeOrder(ordered_list)
    for i in range(n):
        rand.shuffle(ordered_list)
        judgeOrder(ordered_list,log=1)
    print("--------------------升序----------------")

    for i in range(n):
        rand.shuffle(ordered_list)
        if(judgeOrder(ordered_list,order=1)):
            print("True")
    print("-------------------降序-----------------")
    for i in range(n):
        rand.shuffle(ordered_list)
        if(judgeOrder(ordered_list,order=-1)):
            print("True")