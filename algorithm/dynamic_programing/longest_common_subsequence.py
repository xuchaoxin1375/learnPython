''' about the index of the lists(or arrays) to visit elements,we should realize that
    when we desing or understand the process of a algorithm,we usually base on the elements
    themselves to calculate or mark them,we needn't too care the index of the elements
    the regularity of the index counting is depends on the specific programming language
    when we do the code implements works,just according to the processing !
    on the other hand,we reference the pseudocodes to help design the architecture of the code writing,
    don't to be too careful about the specific index of the pseudocodes,if you want reference furtherly,you can
    calculate the gap/times the loops executed'''


def get_lcs_tables(x, y):
    """return the lenth of the longest subsequence of sequence x and y 

    Args:
        x ([list]): sequence x
        y (list)): sequence y
    return: the lenth of the longest subsequence,the mark of the last element of the get_lcs_tables 
    before the latest one 

    """
    m = len(x)
    n = len(y)
    ''' calculate the index from 0 
    carefully to use the list resolution expression to create two dimension list'''
    b = [["" for i in range(0, n)] for j in range(0, m)]
    c = [[0 for i in range(n+1)] for j in range(m+1)]

    # for i in range(m+1):
    ''' the i,j index variable is to primary for traverse the table c and b 
    the i=1,...,m;j=1,...n
    '''
    for i in range(1, m+1):
        for j in range(1, n+1):
            ''' debug :index out of range '''
            # print('x[i]=',x[i],'i=',i,"y[j]=",y[j],"j=",j)

            ''' traverse the x,y sequence
            index_x=0,...,m-1,so make a offset:-1'''
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                b[i-1][j-1] = "diagonal"
            # the compare the length of the lcs currently
            # if the up element >= the left element:
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "up"
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "left"
    return c[m][n], b


def length_table_lcs(x, y):
    """return the table  of the length information of subsequences(processing) of sequence x and y 

    Args:
        x ([list]): sequence x
        y (list)): sequence y
    return the table  of the length information of subsequences(processing) of sequence x and y 
    """
    m = len(x)
    n = len(y)
    ''' calculate the index from 0 
    carefully to use the list resolution expression to create two dimension list'''
    c = [[0 for i in range(n+1)] for j in range(m+1)]

    # for i in range(m+1):
    ''' the i,j index variable is to primary for traverse the table c and b 
    the i=1,...,m;j=1,...n
    '''
    for i in range(1, m+1):
        for j in range(1, n+1):
            ''' debug :index out of range '''
            # print('x[i]=',x[i],'i=',i,"y[j]=",y[j],"j=",j)

            ''' traverse the x,y sequence
            index_x=0,...,m-1,so make a offset:-1'''
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
            # the compare the length of the lcs currently
            # if the up element >= the left element:
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return c


''' the first invoke of the print_lcs_by_mark is :print_lcs_by_mark(b,x,b_row_index_max,b_col_index_max)'''


def print_lcs_by_mark(b, x, i, j):
    """[summary]

    Args:
        b (table): [description]
        x (list): sequence
        i (int): [from 0 count]
        j (int): [from 0 count]
    """
    if i == -1 or j == -1:
        return
    if b[i][j] == "diagonal":
        print_lcs_by_mark(b, x, i-1, j-1)
        print(x[i], end=" ")
    elif b[i][j] == "up":
        print_lcs_by_mark(b, x, i-1, j)
    else:
        print_lcs_by_mark(b, x, i, j-1)


def print_lcs_single(c, x, y, i, j):
    # ''' without the table c,the sequence may not be a longest one ! '''
    # ''' initailly invoke is print_lcs_single(c,x,len(c),len(c[0])) '''
    # index variable i,j is primaryly to visit the table c:
    string = ""
    while(i > 0 and j > 0):
        # for j in range(1, j+1):
        while(i > 0 and j > 0):
            #     ''' debug :index out of range '''
            # # print('x[i]=',x[i],'i=',i,"y[j]=",y[j],"j=",j)

            # # ''' traverse the x,y sequence index_x=0,...,m-1,so make a offset:-1'''
            if x[i-1] == y[j-1]:
                # c[i][j] = c[i-1][j-1]+1
                # print(x[i-1])
                string += x[i-1]
                i -= 1
                j -= 1
            else:
                # i-=1
                if c[i-1][j] >= c[i][j-1]:
                    i -= 1
                else:
                    j -= 1
    # print("over!")
    print(string[::-1])


def get_lcs(c, x, y, i, j, lcs_sequences_set, cs=""):
    # ''' without the table c,the sequence may not be a longest one ! '''
    # ''' initailly invoke is print_lcs_single(c,x,len(c),len(c[0])) '''
    # index variable i,j is primaryly to visit the table c:
    """get all largest common subsequnces without repeating

    Args:
        c (list): two dimension list(as a table)
        x (str): sequence x
        y (str): sequence y
        i (int): size of the table's rows
        j (int): size of the table's column
        lcs_sequences_set (str): contain all lcs
        cs (str, optional): accumulate the common subsequence before recursively invoke the function. Defaults to ""(empty string).
    """
    while(i > 0 and j > 0):
        # for j in range(1, j+1):
        while(i > 0 and j > 0):
            #     ''' debug :index out of range '''
            # # print('x[i]=',x[i],'i=',i,"y[j]=",y[j],"j=",j)

            # # ''' traverse the x,y sequence index_x=0,...,m-1,so make a offset:-1'''
            if x[i-1] == y[j-1]:
                # c[i][j] = c[i-1][j-1]+1
                # print(x[i-1])
                cs += x[i-1]
                # print(x[i-1],end=" ")
                i -= 1
                j -= 1
            else:
                # i-=1
                ''' there will hit one case following: '''
                if c[i-1][j] > c[i][j-1]:
                    i -= 1
                elif c[i-1][j] == c[i][j]:
                    # pass
                    get_lcs(c, x, y, i, j-1, lcs_sequences_set, cs)
                    get_lcs(c, x, y, i-1, j, lcs_sequences_set, cs)
                    # i=i-1
                    # j=j-1
                    # return cs[::-1]
                    return
                else:
                    j -= 1
    # print(cs[::-1])
    lcs_sequences_set.add(cs[::-1])
    # print("over!")
    # print (string[::-1])
    # return cs[::-1]


# x=['a', 'b', 'c', 'b', 'd', 'a', 'b']
# y=['b', 'd', 'c', 'a', 'b', 'a']
''' test data x,y: '''
x = "abcbdab"
y = "bdcaba"

''' data2: '''
# x="_12_34_5"
# y="_1_2545_"
''' test data 3: 
输入：两个字符串为 X={A, B, C, B, D, A, B}和Y={B, D, C, A, B, A}
输出结果：
'''
X="ABCBADA"
Y="BDCABA"



def version1_0():
    c = length_table_lcs(x, y)
    print_lcs_single(c, x, y, len(x), len(y))
    # print(get_lcs_tables(x,y))
    # tuple=length_table_lcs(x,y)
    # print(tuple[0])
    # b=tuple[1]
    # print_lcs_single(b,x)


# b = get_lcs_tables(x, y)[1]
# print_lcs(b, x, len(b)-1, len(b[0])-1)
''' invoke version 1.5 '''


def version1_5(x,y):
    ltl = length_table_lcs(x, y)
    print("lcs=", ltl[len(x)][len(y)], sep="")
    lcs_sequences_set = set()
    get_lcs(ltl, x, y, len(x), len(y), lcs_sequences_set)
    print(lcs_sequences_set)


# version1_0()
version1_5(X,Y)
