# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 22:44:33 2021

@author: zero
"""
#ch7: ner.py
import nltk
import pandas as pd
text = """
FIFA was founded in 1904 to oversee international competition among the national 
associations of Belgium, Denmark, France, Germany, the Netherlands, Spain, 
Sweden, and Switzerland. Headquartered in Zürich, its membership now comprises 
211 national associations. Member countries must each also be members of one of 
the six regional confederations into which the world is divided: Africa, Asia, 
Europe, North & Central America and the Caribbean, Oceania, and South America.
"""
sentences = nltk.sent_tokenize(text) # 分句
tokenized_sentences=[nltk.word_tokenize(sentence) for sentence in sentences] #分词
tagged_sentences=[nltk.pos_tag(sentence) for sentence in tokenized_sentences]#标注
ne_chunked_sents=[nltk.ne_chunk(tagged) for tagged in tagged_sentences]#命名实体识别
named_entities = []
for ne_taged_sentence in ne_chunked_sents:
    for tagged_tree in ne_taged_sentence:
       if hasattr(tagged_tree, 'label'):
         name = tagged_tree[0][0]
         C = tagged_tree.label()
         named_entities.append((name,C))
entity_frame = pd.DataFrame(named_entities, columns=['Entity Name', 'Entity Type'])
print(entity_frame)

