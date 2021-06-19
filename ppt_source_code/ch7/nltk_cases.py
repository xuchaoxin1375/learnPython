# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:44:18 2021

@author: zero
"""

#import nltk
#nltk.download()

#ch7: nltk_cases.py
# ========== 1.分句与分词 =================
# 分句
from nltk.tokenize import sent_tokenize
text = "Hello Adam, how are you? \
          I hope everything is going well.\
          Today is a good day, see you dude."
print("分句:", sent_tokenize(text))
# 分词
from nltk.tokenize import word_tokenize
text = "Hello Mr. Adam, how are you?\
          I hope everything is going well.\
          Today is a good day, see you dude."
print("分词:", word_tokenize(text))

# ============ 2.词性标注 =================
import nltk
text=nltk.word_tokenize('what does the fox say')
print("词性标注:",nltk.pos_tag(text))


# ============ 3.命名实体识别 =======================
#sentence = "I am very excited about the next generation of Apple products."
sentence = "Edison went to Tsinghua University today."
tokens = nltk.word_tokenize(sentence)  # 分词
tags = nltk.pos_tag(tokens)  # 词性标注
ners = nltk.ne_chunk(tags)  # 利用词性标注结果，进行NER,返回一种树结构
print(ners)
for i,tree in enumerate(ners.subtrees()):
    if tree.label()=="S":
        continue
    print("NE%d:"%(i),tree)

# ============= 4.去除停用词 =======================
from nltk.corpus import stopwords

tokens = ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please',
          'maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid',
          'my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him']
clean_tokens = tokens[:]
stwords = stopwords.words('english')
for token in tokens:
    if token in stwords:
        clean_tokens.remove(token)
print("去除停用词后:",clean_tokens)
print("全部停用词:",stwords)

# ============= 5.情感分析 =======================
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentences = ['this is a good book',  # 正面情感
            'this is a awesome book']  # 正面情感
sid = SentimentIntensityAnalyzer()  # 创建分类器
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)  # 对句子进行情感分析
    print("情感得分：", ss)  # 其中，compound表示复杂程度，neu表示中性，
                            #      neg表示负面情绪，pos表示正面情绪
    print('-----------------------------')
