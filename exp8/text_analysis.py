from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
import logging as l
l.basicConfig(level=l.DEBUG)
prefix = "./exp8/"
news_train = 'news_train.csv'  
news_train_subset = "news_train_subset.csv"
news_test = "news_test.csv"

''' use the small scale input to test the process  '''
# news_train = news_train_subset

# 读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
news_train_df = pd.read_csv(prefix + news_train, encoding='utf-8')
news_test_df = pd.read_csv(prefix+news_test, encoding="utf-8")


x_train = news_train_df['text']
len_train=len(x_train)
# print(len_train)
x_test=news_test_df['text']
# print(x_test)
# x=pd.merge(x,x_test,how="cross")
''' concat the two files 
because the tf-idf algorithm reference to the corpus,so if you want to predict the news' validity ,you should create a corpus base all sentences'''
x_whole=pd.concat([x_train,x_test])

# print("new shape of x:")
    # print(news_train_series)
    # l.debug(f"{x}")
y = news_train_df['label']
#get the numeric label vector
y=[1 if validity=='REAL'  else 0 for validity in y  ]

# news_test_series = news_test_df['text']
    # print(label_train_series)
    # label_test_series=news_test_df['label']#this is waiting for solve(predict)

    # news_train_series = np.array(news_train_series)
    # print(news_train_series.shape)
    # print(news_train_series)
    # label_train_series = np.array(label_train_series)
    # print(label_train_nd[1])

corpus = x_whole
# corpus_test=x_test
vectorizer = TfidfVectorizer()
# vectorizer_test=TfidfVectorizer()
v = vectorizer.fit_transform(corpus)
# v_test=vectorizer_test.fit_transform(corpus_test)
#get numeric x vector(ndarry)
x_whole_vectors=v.toarray()
# print(x_whole_vectors)
x_train_vectors=x_whole_vectors[:len_train]
x_test_vectors=x_whole_vectors[len_train:]


clf_GNB = GaussianNB()
y_test_estimate_real=[]
def estimate_accuracy():
    ''' estimate the accuracy: '''
    estimate_number = int(0.9*len_train)
    x_estimate = x_whole_vectors[:estimate_number]
    y_estimate = y[:estimate_number]
    # #fix the shape
    x_test_estimate = x_whole_vectors[estimate_number:len_train]
    global y_test_estimate_real
    y_test_estimate_real = y[estimate_number:len_train]
    ''' estimate clf and operation:,if you want predict the finally result,the comment the  following lines '''
    clf_GNB.fit(x_estimate,y_estimate)
    global y_predict
    y_predict=clf_GNB.predict(x_test_estimate)

''' # change the references to estimate '''
# x = x_estimate
# y = y_estimate
y_predict=[]
def predict():
    ''' the ultimately prediction classifer and predict operation '''
    clf_GNB.fit(x_train_vectors, y)
    global y_predict
    y_predict = clf_GNB.predict(x_test_vectors)


print("prediction:")
def output_prediction():
    with open(prefix+"pred.txt","w") as fos:
        for validity in y_predict:
            if validity==1:
                fos.write("REAL\n")
                print("REAL",end=" ") 
            else:
                fos.write("FAKE\n")
                print("FAKE",end=" ") 
        print()

estimate_accuracy()
# predict()
output_prediction()

def print_for_estimate_accuracy():
    ''' begin estimate the prediction accuracy:80% or so '''
    count=0
    for i,j in zip(y_test_estimate_real,y_predict):
        if i!=j:
            count+=1
            # print(i,j)
    predicts_numbers=len(y_predict)
    print(predicts_numbers)
    print((predicts_numbers-count)/predicts_numbers)
print_for_estimate_accuracy()