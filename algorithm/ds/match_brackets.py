s = "((1)((2))[3])[4]"
s1=")"
s2="(()"
s3="())"
s4="[([)"
s5 = "[()[]]"
s6 = "(()[])[\{\}]"#python中匹配{}需要转义
s7 = "a+b-a*((c+d)/e-f)+g"
test_list=[s,s1,s2,s3,s4,s5,s6,s7]


def is_legal_brackets(s):
    brackets_dict = {"(": ")", "[": "]", "{": "}"}
    lbs = brackets_dict.keys()#左括号
    rbs = brackets_dict.values()#有括号
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


for t in test_list:
    res = is_legal_brackets(t)
    print(t,":",res)