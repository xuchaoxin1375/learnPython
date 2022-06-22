# -*- coding: utf-8 -*-
#ch3:break_continue.py
#while True:
#    s = input('Enter something : ')
#    if s == 'quit':
#        break
#    print('Length of the string is', len(s))
#print('Done')

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print ('length is not sufficient')
        continue
    print('Length of the string is', len(s))
