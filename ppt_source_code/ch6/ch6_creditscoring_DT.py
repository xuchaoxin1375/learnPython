# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:26:40 2021

@author: zero
"""
#ch6_creditscoring.py
import numpy as np
from sklearn import linear_model
from math import sqrt

data1=np.loadtxt('AustralianCredit_train600.txt') # trainset
train_features=data1[:,:-1] # features
train_labels=data1[:,-1].astype(int) # labels
data2=np.loadtxt('AustralianCredit_test90.txt') # testset
test_features=data2[:,:-1]  # features
test_labels=data2[:,-1].astype(int) # labels

clf = linear_model.LogisticRegression() #classifier
clf.fit(train_features, train_labels)
pred_labels=clf.predict(test_features) # predicted labels
print("真实类别:\n",test_labels)
print("预测类别:\n",pred_labels)

TP,TN,FP,FN=0,0,0,0   # 1: positive, 0: negative
for x,y in zip(test_labels,pred_labels):
    if x==1 and y==1: TP+=1
    if x==0 and y==0: TN+=1
    if x==1 and y==0: FN+=1
    if x==0 and y==1: FP+=1
print("混淆矩阵：","TP=",TP,"TN=",TN,"FP=",FP,"FN=",FN)
sen,spe,pre=TP/(TP+FN),TN/(TN+FP),TP/(TP+FP)  #sensitivity,specificity,precision
acc=(TP+TN)/(TP+TN+FN+FP) #accuracy
MCC=(TP*TN-FP*FN)/sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))  #MCC
print("sen:%.4f"%sen,"spe:%.4f"%spe,"pre:%.4f"%pre,"acc:%.4f"%acc,"mcc:%.4f"%MCC)



#调用sklearn自带的性能指标计算方法
from sklearn import metrics
print("混淆矩阵：\n",metrics.confusion_matrix(test_labels,pred_labels))
print("准确率：%.4f"%metrics.accuracy_score(test_labels,pred_labels))
print("精度：%.4f"%metrics.precision_score(test_labels,pred_labels,pos_label=1))
print("召回率：%.4f"%metrics.recall_score(test_labels,pred_labels,pos_label=1))
print("F1 score:%.4f"%metrics.f1_score(test_labels,pred_labels))
print("MCC:%.4f"%metrics.matthews_corrcoef(test_labels,pred_labels))

pred_prob=clf.predict_proba(test_features)
auc=metrics.roc_auc_score(test_labels,pred_prob[:,1])
print('AUC:%.4f'%auc)
fpr, tpr, thresholds = metrics.roc_curve(test_labels, pred_prob[:,1], pos_label=1)
#print(fpr,tpr,thresholds)

import matplotlib.pyplot as plt
plt.figure()
plt.plot(fpr,tpr,label='ROC curve (area= %0.2f)'%auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()


