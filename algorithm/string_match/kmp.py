# def kmp(text, p):
#     len_text = len(text)
#     len_p = len(text)


def pre_calculate_next_recursive(p):
    #build the next array(the position update guider when the 'matche failed' events occur. )
    len_list = len(p)
    next = [0]  #next[0]总是0
    match_lenx = 1  #从next[1]开始求(区分不同的头部串)(指示next数组的填充进度)
    now = 0  #保存next数组的各个元素的值
    #注意两组关系:
    # p[x]&p[x-1];相邻的串尾两字符
    # 其中,p[0]~p[x-1]所对应最长相等前后缀长度为now=next[x-1]#next元素的简写
    #now=next[x-1]代表已知解的问题规模;next[x]是尚未求解的
    #字符p[now]=?=p[x]将决定next[x]=now+1=next[x-1]是否成立

    while match_lenx < len_list:  #需要填充len(p)个值才算完成next数组的构建
        # 下面三个分支两两互斥，每次循环只会进入其中的一条逻辑！！！
        if p[now] == p[match_lenx]:  # matched!(走运)
            #注意,在这个循环中,p[now] == p[match_lenx]的左边p[now]会在关系表达式False
            # 的时候变发生变化,直到这个比较表达式为True,match_lenx才会+1
            #或者now=0,单独强制让match_lenx+=1
            now += 1
            match_lenx += 1
            # this new  scale is calculated! it could be recorded into the next
            next.append(now)
        # mismatched:(不走运)
        # 尝试缩小now,然后进入到下一轮的比较计算
        elif now > 0:  # to iterate the length value
            now = next[now - 1]  # the now>=0
            #修改now,然后重新进入循环再判断
        else:  #now=0,意味着p[0]~p[match_lenx]前缀不可能在有能够和某个后缀相等了(或者说这是个相等缀长度为0)
            # explictly set the length value as 0 in this case
            next.append(0)
            match_lenx += 1

    return next


def kmp_all(text, p):
    s = 0  # offset
    pp = 0  #模式串内字符的指针postion_to_continue(pointer_p)
    #首先要明确,pp的取值范围是0~len(p)-1
    len_p = len(p)
    cnt = 1  #计数匹配位成功的次数
    matched_locations = []  #收集匹配成功的位序字符位序(而非下标)
    next = pre_calculate_next_recursive(p)
    while s < len(text):
        # matched!
        #在这个循环体中,需要明确:
        # 我们把逻辑分为两大块
        #第一块中包含三小块互斥的分支(它们构成所有情况的集合的一种划分,囊括了所有可能)
        #因此,循环每趟执行只会且一定会,进入其中的一个分支
        #第二块代码和第一块代码相对独立(作为单独的一段逻辑存在)
        if text[s] == p[pp]:  #模式串的第[pp]处字符成功匹配
            # 准备比较下一位字符
            s += 1
            pp += 1
        #pp处失配,每前进一个字符,就需要检查整个模式串是否已经都匹配上了(第二块代码)
        #本循环的后面部分仅仅调整指针而不做比较操作(指针调整好后,比较留给下轮循环的开头代码)
        #那么p[:pp]段字符是成功匹配的(右开)从字符p[0]~p[pp-1]
        #通过访问next[pp-1],拿到k=lepp(p[:pp])
        #下一趟比较中,模式串的这部分长度p[:k](p[0]~p[k-1])不需要再比较了
        #直接从p[k]开始和主串(T[s]比较(这是新一轮循环的任务了)
        elif pp:  #pp>0
            # mismatched!模式串在下标为pp处的字符失配!
            # 借助于next数组调整下一次比较的字符位置指针(pp)
            pp = next[pp - 1]
            # 如果失配发生在pp==0的地方,那么lepp==0(next[0]==0总是确定的)
            #发生失配,并且,模式串的指针跳转到下一个合理位置(next[continue-1]),作为下次继续比较的地方
            # 注意到,这里的下标表达式pp-1>=0就要求pp>0
            #pp==0的时候要额外处理
        else:  #pp=0
            #第一个字符(p[pp]就失配了,那么主串的指示指针向后移动一个字符)
            s += 1
        # 判断是否已经找到了模式串要匹配的位置

        if pp == len(p):  #其中pp是指向下一位要比较的字符,如果匹配完成,那么pp=len(p)
            # print("place%d:" % cnt, (s - pp) + 1)
            #其中s-pp是匹配点的下标,转换为位置+1(从1开始计数)
            matched_locations.append(s - pp + 1)
            cnt += 1
            # 开始寻找下一个能够匹配模式串的位置
            pp = next[pp - 1]
            #或者 pp=next[len_p-1]#因为此时pp==len_p
    if matched_locations == []:
        print("matched failed!")
    return matched_locations


def naive_text_matcher(str, p):
    len_str = len(str)
    len_p = len(p)
    matched_locations = []
    # for c in t[:n-m]:
    # start = 0
    last_start = len_str - len_p  #最后一趟需要比较的主串字符的下标
    for start in range(last_start + 1):
        if p == text[start:start + len_p]:
            # print("Matched!")
            res = start + 1  #返回的数值为从1开始计数的字符位置(order not index)
            # print(res)
            # return res
            matched_locations.append(res)
    if len(matched_locations) == 0:
        print("matched failed!")
        # return -1
    return matched_locations
    # 切片左闭右开区间


def get_next_naive_bad(p):
    # 性能较差的next元素计算函数/构建函数
    len_p = len(p) - 1
    for i in range(len_p - 1):  #0,1,2,3,...
        print(i)
        print("p[len_p-i]", p[0:len_p - i], "p[i:len_p]", p[i + 1:])
        if p[:len_p - i] == p[i + 1:]:
            break
    res = len_p - i
    print("res", res)
    return res


def get_next_naive(p, matched_size):
    """ 用户逐个计算next数组中的元素(相对对立地计算)next[x] 的函数调用
    从最长相等前后缀,从长试验到短,比较合适
    prefix=p[:size-1]->p[0:0]=''
    postfix=p[1:]->p[size-1:]
    """
    # x=len(p)
    for i in range(matched_size, 0, -1):
        # i=size,size-1,...,1
        if p[0:i] == p[matched_size - i + 1:matched_size + 1]:
            return i
            # break
    # 不存在相等前后缀,返回0
    return 0


def test_by_naive():
    print("test by naive:")
    naive_text_matcher(text, p1)
    naive_text_matcher(text, p2)


def test_by_kmp():
    print("test by kmp:")
    kmp(text, p4)
    kmp(text, p1)
    # kmp(text, p2)


text = "teababaca_aaaeeaae_abaabac_1234_abaabac"
# p = "ea"
p1 = "eea"
# p="aacaa"
# p="aadabaadaadaa"
# p = "acbabaca"
p2 = "ababaca"
p3 = "ababa"  #lepp=3
p4 = "abaabac"
ps = [p1, p2, p3, p4]


# print(pre_calculate_next_recursive(p1))
# print(kmp())
def puts(s):
    print(s, end='')


if __name__ == "__main__":
    # test_by_naive()
    # test_by_kmp()

    p = p4
    # next = [get_next_naive(p, x) for x in range(len(p))]
    # print(next)
    for p in ps:
        puts("by kmp: ")
        print(kmp_all(text, p))
        puts("by naive: ")
        print(naive_text_matcher(text, p))
