tion will continuosly to match 
    next_list = pre_calculate_next_list(pattern)
    while s < len(string):
        # matched! 
        #   if two charactor are identical ,step the index (s and pos)
        if string[s] == pattern[pos]:
            s += 1
            pos += 1
        elif pos:# mismatched!