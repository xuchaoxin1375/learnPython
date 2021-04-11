'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-02-04 11:33:14
LastEditors: xuchaoxin
LastEditTime: 2021-02-04 11:40:23
'''
import unittest
"""注意:
python -m unittest .\mydict_test.py
和
python -m unittest mydict_test
两者的不同(当需要带参数运行时,就不要带有文件名意外的符号了(无参数时执行效果一般相同))
"""
from mydict import Dict

class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')
    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty