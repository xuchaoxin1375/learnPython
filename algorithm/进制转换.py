#本代码试图实现16进制内的数进制转换(r1->r2)
##包括对整数部分和小数部分的处理
## 基础函数包括是10进制转r进制
## r进制转10进制
#基本思想是,将r1进制转换为10进制,在从10进制转为r2进制
d_16 = {10: "A", 11: "B"}
for i in range(10, 16):
    c = chr(ord('A') - 10 + i)
    d_16[i] = c
    d_16[c] = i
print(d_16)
# 对十进制内的各进制数进行转换
#16进制由于引入了A~F6个英文字母,需要额外处理,但是算法核心没有变
dotted_line = "\n============================\n"


def separate_outputs(separator=dotted_line):
    print(dotted_line)


def puts(strx):
    print(strx, end="")
def ten_to_r_Z(Z, r):
    """十进制数的小数部分转换为为r进制

    Parameters
    ----------
    F : int
        被转换的十进制数的小数部分
    r : int
        目标进制数(基数)

    Returns
    -------
    list
        目标进制(r)的结果(各个数位上的数码)
    """
    i = 0
    res = []
    remainder = Z // r**i
    while (remainder):
        next_bit = remainder % r
        if (next_bit > 9):
            next_bit = d_16[next_bit]
        res.append(next_bit)
        i += 1
        remainder = Z // r**i
    res.reverse()
    return res
    # puts(res)


def ten_to_r_F(F, r):
    """十进制数的小数部分转换为为r进制

    Parameters
    ----------
    F : float
        被转换的十进制数的小数部分
    r : int
        目标进制数(基数)
        

    Returns
    -------
    list
        目标进制(r)的结果(各个数位上的数码)
    """
    i = 1
    # print(F)
    res = []
    remainder = 1
    while (remainder):
        dividend = F * r**i
        next_bit = (int(dividend) % r)
        if (next_bit > 9):
            next_bit = d_16[next_bit]
        res.append(next_bit)
        i += 1
        # is_continue = F * r**i % r
        remainder = dividend - int(dividend)
    return res
    # puts(res)


def ten_to_r(S, r):
    """将十进制数转换为r进制数

    Parameters
    ----------
    S : float(int)
        被转换的十进制数数
    r : int
        目标进制
        

    Returns
    -------
    list
        转换完成后的r进制数的各个数码(从高位到低位,列表中包含一个小数点(字符))
    """
    Z = int(S)
    F = S - Z
    Zr = ten_to_r_Z(Z, r)
    # puts(".")
    Fr = ten_to_r_F(F, r)
    res = Zr + ["."] + Fr
    # print(res)
    return res


def r_to_ten(S, r):
    """将r进制数转换为10进制数r不超过16

    Parameters
    ----------
    S : list
        需要转换的数的字符化列表
    r : int
        被转换的数的进制
    Returns
    -------
    float
        r进制数(列表)转换为十进制数的结果
    """

    # Sr=list(Sr)
    index_dot = len(S)
    if ('.' in S):
        index_dot = S.index(".")
        S.remove(".")
    # Z=S[:index_dot]
    # F=S[index_dot+1:]
    # print(Z,F)
    S10 = 0
    # i=1
    # for zi in Z:
    #     S10+=r**(len(Z)-i)*int(zi)
    #     i+=1
    i = 1
    for si in S:
        # print("current:si=:",si)
        if (si in d_16.keys()):
            si = d_16[si]
            # print("changed to ten si:=",si)

        S10 += r**(index_dot - i) * int(si)
        # puts(S10)
        i += 1
    # print(S10)
    return S10


def r1_to_r2(Sr1, r1=16, r2=10):
    """r1进制转为r2进制(不超过16进制)

    Parameters
    ----------
    Sr1 : float(int) 
        被转换的r1进制数
    r1 : int
        Sr1的进制
    r2 : int
        转换目标进制

    Returns
    -------
    list[str]
        转换结果(各个位上的数码(以及小数点))
    """
    Sr1 = list(str(Sr1))
    # print(Sr1)
    S10 = r_to_ten(Sr1, r1)
    res = ten_to_r(S10, r2)
    # print("res:",res)
    return res


def test(S10):
    print("example :将10进制的", S10, "转换为二进制和八进制")
    print("")
    puts("2进制:")
    S2 = ten_to_r(S10, 2)
    generator_S2 = map(lambda i: puts(i), S2)
    list(generator_S2)
    separate_outputs()
    puts("8进制:")
    S8 = ten_to_r(S10, 8)
    list(map(lambda i: puts(i), S8))
    separate_outputs()
    puts("16进制:")
    S16 = ten_to_r(S10, 16)
    list(map(lambda i: puts(i), S16))
    separate_outputs()
    print("将上述结果转换为十进制来验证:")
    puts("2->10:")
    print(r_to_ten(S2, 2))
    puts("8->10:")
    print(r_to_ten(S8, 8))
    puts("16->10:")
    print(r_to_ten(S16, 16))

if __name__ == "__main__":
    # ten_to_r_Z(Z, r2)
    # ten_to_r_F(F, r)
    S10 = 123.6875
    S10=0.05
    S2_1 = 11111
    S2_2 = 1.1
    S16 = "7B.B"
    test(S10)

    separate_outputs()

    #todo 解决123.88问题(16进制)
    # res = r1_to_r2(S, 2, 13)
    print("r1进制转换为r2进制:")
    print(S16, "16->8:")
    res = r1_to_r2(S16, r1=16, r2=8)
    res_str = "".join(map(lambda x: str(x), res))
    print(res_str)
    print(S2_1, "2->8:")
    res = r1_to_r2(S2_1, 2, 8)
    res_str = "".join(map(lambda x: str(x), res))
    print(S2_2, "2->10:")
    res = r1_to_r2(S2_2, 2, 10)
    res_str = "".join(map(lambda x: str(x), res))
    print(res_str)
