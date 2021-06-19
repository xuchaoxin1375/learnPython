# -*- coding: utf-8 -*-
# re_find.py
import re

p = re.compile('\d+')


def test_findall():
    f1 = re.findall(p, 'one1two2three3four4')
    print('findall:', f1)


def test_finditer():
    result_match_ite = re.finditer(p, 'one1two2three3four4')
    print('finditer:', result_match_ite)
    for item_match in result_match_ite:
        print(item_match, ':', item_match.group())


if __name__ == "__main__":
    test_findall()
    test_finditer()
