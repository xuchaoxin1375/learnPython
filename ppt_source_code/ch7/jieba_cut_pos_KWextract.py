
#ch7: jieba_cut_pos_KWextract.py
# ============ 1.分词 =======================
import jieba
text = "文本分析涵盖了许多研究方向。"
# 精确模式
seg1 = jieba.cut(text, cut_all=False) #返回迭代器
print("seg1:",seg1)
print("精确模式:","/ ".join(seg1))
seg2 = jieba.lcut(text, cut_all=False)#返回列表
print("精确模式list:",seg2)

# 全模式：将句子中所有可能的词都列举出来
seg3 = jieba.cut(text, cut_all=True)
print("seg3:",seg3)
print("全模式:","/ ".join(seg3))
seg4 = jieba.lcut(text, cut_all=True)
print("全模式list:",seg4)

# 搜索引擎模式：适用于搜索引擎使用
seg5 = jieba.cut_for_search(text)
print("seg5:",seg5)
print("seg5:","/ ".join(seg5))
seg6 = jieba.lcut_for_search(text)
print("seg6:",seg6)


# ============ 2.词性标注 ===============
import jieba.posseg as pseg

text = "文本分析涵盖了许多研究方向。"
seg = pseg.cut(text)
print("seg:",seg)
print([word for word in seg])


# ============= 3.关键词抽取 ==========
import jieba.analyse as an

# 基于TF-IDF算法
result = an.extract_tags(text, topK=3)  #指定抽取topK个关键词
print(result)

# 基于TextRank算法
result = an.textrank(text, topK=3)
print(result)



