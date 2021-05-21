def naive_string_match(string, pattern):
    len_string = len(string)
    len_pattern = len(pattern)
    delta = len_string-len_pattern

    for s in range(delta+1):
        if string[s:s+len_pattern] == pattern:
            print(s)
# naive_string_match("teaae","a")


def kmp(string, pattern):
    len_string = len(string)
    len_pattern = len(pattern)
    pre_calculate_list = compute_prefix(pattern)
    
    q = 0  # number of characters matched
    for i in range(len_string):  # scan the string from left to right

        while q > 0 and pattern[q+1] != string[i]:
            q = pre_calculate_list[q]  # next charactor does not match

        if pattern[q+1] == string[i]:
            q += 1  # next charactor matches
        if q == len_pattern:# is all of pattern matched?
            print(i-len_pattern)
        q = pre_calculate_list[q]# look for the next match


def compute_prefix(pattern):
    len_pattern = len(pattern)
    list = [0 for i in range(len_pattern)]
    list[0] = 0
    k = 0# the length of the prefix(maximum each case)
    # the q  is to visit the pattern string charactors
    # the more specific meaning is the index of the mismatched charactor(in each cases)
    for q in range(1, len_pattern):
        # the while loop will not executed until the k>0(to make the list[k] meaningful)
        while k > 0 and pattern[k] != pattern[q]:#if the next character mismatched
            k = list[k]
            #after out of the while loop,it means the pattern[k+1]== pattern[q](or k==0,this is only for the frist execution)
        
        if pattern[k+1] == pattern[q]:
            k += 1
        list[q] = k
    return list


string = "teaaeeaae"
# pattern = "ea"
pattern="eaeaakke"
# kmp(string, pattern)
list=compute_prefix( pattern)
print(list)
