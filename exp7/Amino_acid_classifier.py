from typing import Iterable
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import random
''' 本程序采用python3的注解,标记出变量/函数的类型,提高可读性 '''


def get_percents(protein: str) -> list[float]:
    ''' 
    计算蛋白质序列上各种氨基酸占该氨基酸的比例，以此提取特征值做归一化处理
    according the protein to calculate the percentes: '''
    aa20: tuple = ('A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
                   'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V')
    result_list: list[float] = []
    protein_len: int = len(protein)
    # We do the normalization by counting the animo ratio:
    for amino in aa20:
        # print(amino,end=" ")
        # dict={amino:protein.count(amino)/protein_len}
        percent: float = protein.count(amino)/protein_len
        result_list.append(percent)
    return result_list


def get_protein_sequences1(file: str) -> list[str]:
    ''' get protein sequences from file '''
    sequences: list[str] = []
    with open(file, "r") as file_input_stream:
        # 从文件中读取蛋白质序列
        for line in file_input_stream:
            # 每次读取一行(str)
            line = line.split(" ")
            sequences.append(line[2].strip())
    return sequences


def get_protein_sequences2(file: str) -> list[str]:
    ''' get protein sequences from file2 '''
    sequences: list[str] = []
    with open(file, "r") as file_input_stream:
        for line in file_input_stream:
            line = line.split(" ")
            sequences.append(line[1].strip())
    return sequences


def get_protein_labels(file: str):
    ''' get labels of each protein from file '''
    labels: list[int] = []
    with open(file, "r") as file_input_stream:
        for line in file_input_stream:
            # the line is <class 'str'>
            line = line.split(" ")
            labels.append(int(line[1]))
    return labels


def output_file(result_iterable: Iterable, result_file: str, classifier=""):
    with open(result_file, "w") as fos:
        result = ""
        # print(str(result_list))
        # fos.write(classifier+str(result_list))
        print(classifier)
        for char in result_iterable:
            result = result+(str(char)+'\n')
        print(result)
        result.strip()
        fos.write(result)


prefix = "D:/OneDrive - pop.zjgsu.edu.cn/PythonPath/exp7/"
ProSeqs_Test = prefix+"ProSeqs_Test.txt"
ProSeqs_Train = prefix+"ProSeqs_Train.txt"
x_list: list[str] = get_protein_sequences1(ProSeqs_Train)
y_list: list[int] = get_protein_labels(ProSeqs_Train)
x_percents = [get_percents(protein) for protein in x_list]
x_list_test = get_protein_sequences2(ProSeqs_Test)
x_percents_test = [get_percents(protein) for protein in x_list_test]
""" get the numerical data set and corresponding labels: """
x_array: np.ndarray = np.array(
    x_percents)  # 注意,ndarry类型的对象构造函数这里不是用ndarray(),而是numpy.array()
y_array: np.ndarray = np.array(y_list)
x_array_test: np.ndarray = np.array(x_percents_test)

# print(x_array_test)

clf_GNB = GaussianNB()
clf_KNN = KNeighborsClassifier()
clf_LR = LogisticRegression()
clf_MLP = MLPClassifier()
clf_RF = RandomForestClassifier()
clf_GB = GradientBoostingClassifier()


def estimate_accuracy(x_array: np.ndarray, y_array: np.ndarray, estimate_scale: float, clf):
    """ 通过随机化手段(将产生一系列的随机索引,方便对多组执行同样的随机选择(保持配套),
    这种做法相较于直接再数据容器(比如ndarray上直接抽取子集要来的灵活方便:引入第三方中介)) """
    size = len(x_array)
    estimate_scale_int = int(size/100*estimate_scale)
    real_scale = size-estimate_scale_int
    true_list = [True for index in range(estimate_scale_int)]
    false_list = [False for index in range(real_scale)]
    bools = true_list+false_list
    random.shuffle(bools)
    # print(bools)
    
    estimate_accuracy_x: np.ndarray = x_array[bools]
    estimate_accuracy_y: np.ndarray = y_array[bools]
    # fit the modle(classifier)
    clf.fit(estimate_accuracy_x, estimate_accuracy_y)
    # get the data set to be predict(estimate)
    bools_reverse = [not bool_ for bool_ in bools]
    estimate_accuracy_x_test = x_array[bools_reverse]
    real_result = y_array[bools_reverse]
    
    
    # predict according the x segment:
    estimate_predict_result = clf.predict(estimate_accuracy_x_test)
    # calculate the accuracy:
    ''' the GNB will be expecting has the 80% accuracy or so: '''
    length = len(estimate_predict_result)
    count = 0
    for label1, label2 in zip(estimate_predict_result, real_result):
        if label1 == label2:
            count += 1
        else:
            # print(label1," ",label2)
            pass
    # print the len to certain the result is calculate the proper case:
    accuracy = count/length
    
    # print(accuracy)
    # print(length, "elements were predicted with model:", clf)
    return accuracy


def get_average_accuracy(clf=clf_GNB, times: int = 10, estimate_scale=95):
    count_probility = 0
    count = times
    while count:
        count_probility += estimate_accuracy(x_array,
                                             y_array, estimate_scale, clf)
        count -= 1
    return count_probility/times

""" 将结果写入文件: """
# print(len(x_array), len(y_array))

# clf.fit(x_array, y_array)
# result_iterable = clf.predict(x_array_test)
# print(result_iterable)

# prediction_result = prefix+"preds.txt"
# output_file(result_iterable, prediction_result)


if __name__ == "__main__":
    # estimate_accuracy(x_array,y_array,95.5,clf_KNN)
    # """ clf_MLP, """
    classifiers: list = [clf_GNB, clf_KNN, clf_LR,  clf_RF, clf_GB]
    sort_list = []
    for clf in classifiers:
        result = get_average_accuracy(times=10,estimate_scale=98,clf=clf)
        print("in average result with:", clf, result)
        sort_list.append((result, clf))
    # print(sort_list)
    sort_list.sort(key=lambda tuple: tuple[0], reverse=True)
    for item in sort_list:
        print(item)
