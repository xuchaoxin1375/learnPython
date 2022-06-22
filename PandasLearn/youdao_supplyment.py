# -*- coding: utf-8 -*-

##
from itertools import count
import sys
import uuid
import requests
import hashlib
import time
from imp import reload
from importlib import reload
# import json 
import time
import numpy as np
import pandas as pd


""" 准备有道api """
reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '2be31bd18122436f'
APP_SECRET = 'xb8r8ATirfHuGMiNrFX9kJ99wndQ5CqM'
""" 指定文件来源和输出文件名 """
dir="./raw_word_data/"
dir_out="./mini_dicts/"
# fileNamebase="outline5500_sorted.xlsx"
fileNamebase="delta_cet46_gre.xlsx"

fileSource=dir+fileNamebase
fileOut=dir_out+"/basic_words.xlsx"

def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)

resJson=""

def query(spelling="do"):

##
    # spelling = "do"
    data = {}
    data['from'] = 'auto'
    data['to'] = 'auto'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    print(f"@spelling={spelling}")
    spelling=str(spelling)
    signStr = APP_KEY + truncate(spelling) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = spelling
    data['salt'] = salt
    data['sign'] = sign
    data['vocabId'] = "您的用户词表ID"
    response = do_request(data)
    return response
##  
    # contentType = response.headers['Content-Type']
"""     if contentType == "audio/mp3":
        millis = int(round(time.time() * 1000))
        filePath = "./" + str(millis) + ".mp3"
        fo = open(filePath, 'wb')
        fo.write(response.content)
        fo.close() """
def get_word_list():
    """ 指定文件源 """

    word_list_df=pd.read_excel(fileSource)
    # word_list=word_list_df.values.tolist()
    s=word_list_df.squeeze()
    word_list=s.tolist()
    # print first 5 to preview outline
    print(word_list[:5])
    # print(type(s))
    # t=type(word_list_df)
    return word_list
def get_words_round(word_list,size=100):
    length=len(word_list)
    round=length//size
    remain=length%size
    end=length-remain
    return word_list[:end]
def get_words_tail(word_list,size=100):
    length=len(word_list)
    round=length//size
    remain=length%size
    start=length-remain
    return word_list[start:]
        
def get_record(word):
    " excel version """
    response=query(word)
    # global resJson
    # 得到字典对象
    res_d=response.json()
    #wordForms
    basic_d=res_d.get('basic',"NULL")
    if(basic_d=="NULL"):
        basic_d={}
    
    wfs=basic_d.get('wfs',"NULL")
    if(wfs=="NULL"):
        wfs={}

    wfs_list=[]
    
    wfs_d={}
    for item in wfs:    
        pair=item.get('wf',"NULL")
        field=pair.get('name')
        value=pair.get('value')
        # wfs_str+=value
        # fs_list.append({field,value})
        wfs_d[field]=value
        # 过去
    # index=5
    forms=["复数","第三人称单数","现在分词","过去式","过去分词"]
    # for item in wfs_d:
    for i in range(5):
        wfs_list.append(wfs_d.get(forms[i],"NULL"))
    # return wfs_list

    
    phonetic=[basic_d.get('phonetic',"NULL")]
    explains=[basic_d.get('explains',"NULL")]
    record_list=[word]+phonetic+wfs_list+explains
    # print(record_list)
    return record_list
def query_batch(word_list,size=100):
    # 
    # dir="./out/"
    ext=".xlsx"
    # record=''
    record_batch=[]
    # record_list=[]
    i=0
    cnt=0
    for word in word_list:
        # 分批写入文件
        record_batch.append(get_record(word))
        i+=1
        if (i%size==0):
            # generate()
            # return record_batch
            start=cnt*size
            end=start+size
            cnt+=1
            out_path_name=dir_out+str(start)+"~"+str(end)+ext
            export_to_excel(out_path_name,record_batch)
            record_batch=[]
def query_tail(word_list):
    # dir="./out/"
    ext=".xlsx"
    # record=''
    record_batch=[]
    # record_list=[]
    i=0
    cnt=0
    for word in word_list:
        # 分批写入文件
        record_batch.append(get_record(word))
        # i+=1
        # if (i%size==0):
            # generate()
            # return record_batch
            # cnt+=1
    start=1
    end=len(word_list)
    out_path_name=dir_out+str(start)+"~"+str(end)+ext
    export_to_excel(out_path_name,record_batch)
    # record_batch=[]

def export_to_excel(out_path_name,records_batch):
    # print(records_batch)
    records_pd=pd.DataFrame(records_batch,columns=["spelling","phonetic","plurality","thirdpp","present_participle","past_tense","past_participle","explains"])
    records_pd.to_excel(out_path_name)
    print(records_pd)
# export_to_excel(query_batch(get_word_list()))

# if __name__ == '__main__':
##
# query_batch(get_word_list())
word_tail_list=get_words_tail(get_word_list())
query_tail(word_tail_list)
query_batch(get_words_round(get_word_list()))

##
