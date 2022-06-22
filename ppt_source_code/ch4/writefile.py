# -*- coding: utf-8 -*-

fout=open("data.txt",'a')
for x in "Python":
    for y in range(10):
        fout.write("%2s,%10d\n"%(x,y))
fout.close()