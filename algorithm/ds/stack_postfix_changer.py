s1 = "a+b-a*((c+d)/e-f)+g"
res1 = "ab+acd+e/f-*-g+"
s2 = "a+b-a*((c+d*a)/e-f)+g"
res2 = "ab+acda*+e/f-*-g+"
s3 = "(a+b)-a*((c+d-f))+g"
s_illegal_bracktes = "(c-f))+g"
sl = [s1, s2, s3,s_illegal_bracktes]

prior_d = {"+": 2, "-": 2}
lbs = ("(")
rbs = (")")


def isp_prior(ch):
    p = 0
    if ch in ["+", "-"]:
        p = 2
    elif ch in ["*", "/"]:
        p = 3
    elif ch in ["", "#"]:
        p = 0
    elif ch in rbs:
        p = 1

    elif ch in lbs:
        # 左括号入栈的时候是无条件的
        #但是要让左括号出栈,则只有右括号才可以,而遇到其他运算符是不出栈的!
        #这是为了让括号的作用:提升其包裹的表达式内的计算优先级)
        p = 1
    return p


def get_top_ch(op_stack):
    r = ""
    if len(op_stack):
        r = op_stack[-1]
    return r


def putchar(s):
    print(s, end='')


def pupo_next(op_stack, ch_now):
    """ 这是一个递归函数
    """
    top_ch = get_top_ch(op_stack)
    if top_ch + ch_now in ["()", "[]", "\{\}"]:  #出口1
        op_stack.pop()
    else:  #ch_now 不是右括号
        push_judger = (isp_prior(top_ch) < isp_prior(ch_now))
        push_judger = push_judger or (ch_now in lbs)  #ch_now是一个左括号
        push_judger = push_judger or (top_ch in lbs)  #ch_now是跟在左括号后面的运算符
        if push_judger:  #出口2
            # 注意右括号和左括号相邻的robust
            #入栈每次最多一个
            op_stack.append(ch_now)
        else:
            # 出栈可能一口气出多个(这依赖于递归调用本函数)
            if (len(op_stack)):
                op = op_stack.pop()
                if op not in lbs:
                    putchar(op)

                top = get_top_ch(op_stack)
                pupo_next(op_stack, ch_now)


def infix2postfix(s):
    op_stack = []
    for c in s:
        if c.isalpha():
            print(c, end='')
        else:
            # top_ch = get_top_ch(op_stack)
            pupo_next(op_stack, c)
    # if len(op_stack):
    #     putchar(op_stack[-1])
    # print("".join(op_stack))
    print(op_stack[0])


def is_legal_brackets(s):
    """ 本函数利用栈检查一个表达式(中缀表达式)的括号是否是符合规范的 """
    brackets_dict = {"(": ")", "[": "]", "{": "}"}
    lbs = brackets_dict.keys()  #左括号
    rbs = brackets_dict.values()  #有括号
    # print(keys)
    stack = []
    i = 0
    for c in s:
        if c in lbs:
            stack.append(c)
            # continue
        # if c not in lbs:
        elif c in rbs:

            if len(stack):
                lb = stack.pop()
            else:
                return False
            if c == brackets_dict[lb]:
                # print(f"matched{i}:{lb}{c}")
                i += 1
            else:
                # print("illegal brackets!!!")
                return False
    if len(stack) == 0:
        # print("😊great!the string is legal brackets char sequence")
        return True
    else:
        return False
    # else:
    #     print("illegal brackets!!!")
    # print(stack)

    # if brackets_dict[c]:


if __name__ == "__main__":
    # infix2postfix(s)
    i=1
    for s in sl:
        if(not is_legal_brackets(s)):
            print(i,":😡😠illegal infix expression")
            break
        print(i,":",s, "😁😀--> ", end='')
        i+=1
        infix2postfix(s)