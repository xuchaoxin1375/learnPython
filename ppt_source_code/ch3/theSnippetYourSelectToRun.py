    print("--------------------升序----------------")

    for i in range(n):
        rand.shuffle(ordered_list)
        if(judgeOrder(ordered_list,order=1)):
            print("True")