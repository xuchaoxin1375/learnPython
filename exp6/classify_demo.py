from typing import Tuple
import numpy as np
from numpy.lib.function_base import average
import pandas as pd
import random
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

""" the exp6 """


def output_file(result_list, result_file, method):
    ''' 输出预测结果 '''
    with open(result_file, "w") as fos:
        result = ""
        # print(str(result_list))
        for char in result_list:
            result = result+(str(char)+'\n')
        # print(result)
        result.strip()
        # fos.write(method+str(result_list))
        fos.write(result)


data_train = 'data-train.csv'
data_test = 'data-test.csv'
# gnb predicion:
clf_GNB = GaussianNB()
clf_KNN = KNeighborsClassifier()
clf_LR = LogisticRegression()
clf_MLP = MLPClassifier(max_iter=10000)  # max_iter=1000最高迭代1000次
clf_RF = RandomForestClassifier()
clf_GB = GradientBoostingClassifier()
df_train_df = pd.read_csv(data_train, encoding='utf-8')
# 取得本征数据集条目
x_arrays_train = np.array(df_train_df.iloc[:, :-1])
# 取得对应的标签集
y_array_train = np.array(df_train_df.iloc[:, -1])


def generate_random_bools(x_array: np.ndarray, estimate_scale: float = 90):
    """ 通过随机化手段(将产生一系列的随机索引,方便对多组执行同样的随机选择(保持配套),
    这种做法相较于直接再数据容器(比如ndarray上直接抽取子集要来的灵活方便:引入第三方中介)) """
    size = len(x_array)
    estimate_scale_int = int(size/100*estimate_scale)
    real_scale = size-estimate_scale_int
    true_list = [True for index in range(estimate_scale_int)]
    false_list = [False for index in range(real_scale)]
    bools = true_list+false_list
    random.shuffle(bools)
    return bools


def estimate_accuracy(bools: list[bool], x_array: np.ndarray, y_array: np.ndarray, clf=clf_GNB):

    # 读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
    # print(bools)

    estimate_accuracy_x_train: np.ndarray = x_array[bools]
    estimate_accuracy_y_train: np.ndarray = y_array[bools]
    # fit the modle(classifier)
    clf.fit(estimate_accuracy_x_train, estimate_accuracy_y_train)
    # get the data set to be predict(estimate)
    bools_reverse = [not bool_ for bool_ in bools]
    estimate_accuracy_x_test = x_array[bools_reverse]
    real_result = y_array[bools_reverse]

    estimate_predict_result = clf.predict(estimate_accuracy_x_test)
    # calculate the accuracy:
    length = len(estimate_predict_result)
    count = 0
    for label1, label2 in zip(estimate_predict_result, real_result):
        if label1 == label2:
            count += 1
        else:
            ...
    # print the len to certain the result is calculate the proper case:
    accuracy = count/length

    # print(accuracy)
    # print(length, "elements were predicted with model:", clf)
    return accuracy


def estimate_by_k_fold(index_tuple:Tuple, x_arrays_train: np.ndarray = x_arrays_train,
                       y_array_train: np.ndarray = y_array_train, clf=clf_GNB):
    estimate_accuracy_x_train: np.ndarray = x_arrays_train[index_tuple[1]]
    estimate_accuracy_y_train: np.ndarray = y_array_train[index_tuple[1]]
    clf.fit(estimate_accuracy_x_train, estimate_accuracy_y_train)
    real_result = y_array_train[index_tuple[0]]
    estimate_accuracy_x_test = x_arrays_train[index_tuple[0]]
    estimate_predict_result = clf.predict(estimate_accuracy_x_test)
    # calculate the accuracy:
    length = len(estimate_predict_result)
    count = 0
    for label1, label2 in zip(estimate_predict_result, real_result):
        if label1 == label2:
            count += 1
        else:
            ...
    # print the len to certain the result is calculate the proper case:
    accuracy = count/length

    # print(accuracy)
    # print(length, "elements were predicted with model:", clf)
    return accuracy


def estimate_by_k_fold_times(index_tuples, clf=clf_GNB):
    count_probiblity=0
    for index_tuple in index_tuples:
        result = estimate_by_k_fold(index_tuple, clf=clf)
        count_probiblity+=result
        # print(result)
        # 返回平均值
    return count_probiblity/len(index_tuples)
    


# defind  series of k_fold related method:
""" 产生原问题的训练数据集x_array_train元素的索引构成的随机化序列,这些索引值构成一个索引序列列表index_list
k等分索引序列,得到k各区间,分别收集索引列表各区间的起始索引start_index和终止索引end_index;
range(start_index,end_index)产生的序列可以取得的index_list中的连续的若干个元素,按照这些元素可以取得x_array_train中的对应的一系列元素
这些元素将作为测试集;同时,range(0,start_index)和range(end_index,)
然而,更好的描述是:对于分组start_index,end_index,对于index_list的切片[start_index,end_index],[:start_index]和[end_index:]
两个切片之和作为对应的训练集(中元素的索引)

 """


def get_random_indexes(x_arrays_train=x_arrays_train) -> list:
    size = len(x_arrays_train)
    indexes = [i for i in range(size)]
    random.shuffle(indexes)
    # print(np.ndarray(indexes))
    return indexes


def get_k_fold_test_indexes(random_indexes:list[int], k=5) -> list:
    test_index_tuples: list = []
    size=len(random_indexes)
    array_size = size//k
    for i in range(k):
        array_start = i*array_size
        array_end = array_start+array_size
        # 左闭右开
        # test_index_tuples.append(indexs[array_start:array_end])
        # test_index_tuples.append((array_start,array_end))
        test_index_tuples.append(
            (random_indexes[array_start: array_end], random_indexes[:array_start]+random_indexes[array_end:]))
    return test_index_tuples


# def get_k_fold_train_indexes(test_index_tuples, length, k=10) -> list:
#     for tuple in test_index_tuples:
# def k_fold_estimate(x_array_train, k=10):


def random_reservation():
    classifiers: list = [clf_GNB, clf_KNN, clf_RF, clf_GB, clf_MLP]
    sort_list = []
    times = 10
    count_prob = [0.0 for i in range(len(classifiers))]
    for index in range(times):
        bools = generate_random_bools(x_arrays_train, 90)
        clf_index = 0
        for clf_i in classifiers:
            count_prob[clf_index] += estimate_accuracy(
                bools, x_arrays_train, y_array_train, clf=clf_i)
            clf_index += 1
            
    average_probs: np.ndarray = np.array(count_prob)/times

    # clf_index=0
    for clf_perform in zip(classifiers, average_probs):
        print("in average result with:", clf_perform[0], clf_perform[1])
        sort_list.append(clf_perform)
    # print(sort_list)
    sort_list.sort(key=lambda tuple: tuple[1], reverse=True)
    for item in sort_list:
        print(item)

def k_fold():
    classifiers: list = [clf_GNB, clf_KNN, clf_RF, clf_GB, clf_MLP]
    sort_list = []
    times = 10
    count_prob = [0.0 for i in range(len(classifiers))]
    for index in range(times):
        index_tuples = get_k_fold_test_indexes(get_random_indexes(x_arrays_train))
        clf_index = 0
        for clf_i in classifiers:
            
            count_prob[clf_index] += estimate_by_k_fold_times(
                index_tuples, clf=clf_i)
            clf_index += 1
            
    average_probs: np.ndarray = np.array(count_prob)/times

    # clf_index=0
    for clf_perform in zip(classifiers, average_probs):
        print("in average result with:", clf_perform[0], clf_perform[1])
        sort_list.append(clf_perform)
    # print(sort_list)
    sort_list.sort(key=lambda tuple: tuple[1], reverse=True)
    for item in sort_list:
        print(item)

if "__main__" == __name__:
    k_fold()
