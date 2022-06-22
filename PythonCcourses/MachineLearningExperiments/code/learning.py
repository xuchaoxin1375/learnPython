import csv
import numpy as np
from sklearn import linear_model
from sklearn.metrics import classification_report


def empty(obj):
    pass


if __name__ == '__main__':
    """ 调试打印使用d;
    正常输出打印使用print
    这样一来，可以通过对d所指向的对象进行修改，可以方便控制输出中间结果（当然也可以使用专业的debug库） """
    # d = print
    d = empty
    # 数据文件所在路径
    file_dir = './Data_students_new.csv'
    # 数据一共10列，名称分别为：'used_time', 'height', 'weight', 'consumption', 'sleeping_time','character', 'gift_language', 'gift_sport', 'gift_music', 'gift_logic', 'gender'
    # X_valid_list = [0, 2, 3, 4, 5, 6, 7, 8, 9]
    X_list_hw = [1, 2]
    # X_valid_list=X_list_hw
    X_list_all = list(range(10))
    X_valid_list = X_list_all
    Y_valid_index = 10
    # 读取数据
    with open(file_dir, encoding='UTF8') as f:
        reader = csv.reader(f)
        d(type(reader))
        name = next(reader)
        # X 将作为一个二维向量
        X = list()
        Y = list()
        line_index = 0
        # 数据填充到x,y向量
        for line in reader:
            X.append(list())
            Y.append(float(line[Y_valid_index]))
            # 写入到X向量中,每次处理掉一个line(一条数据记录)
            # 在10个字段中将第`1`作为待预测字段
            d(line)
            d(type(line))
            # eg: ['48.0', '180.0', '100.0', '1500.0', '8.0', '0.0', '8.0', '6.0', '6.0', '6.0', '1.0']
            # have more effect method to do the filling.
            for item_index in X_valid_list:
                X[line_index].append(float(line[item_index]))
            line_index = line_index + 1
        # 封装成numpy数组
        X = np.array(X)
        Y = np.array(Y)
    print(X.size)
    # 按比例拆分数据，50%用作训练
    train_data = []
    train_label = []
    # 保存待预测部分的数据
    test_data = []
    test_label = []
    # 划分训练集和测试集
    for i in range(len(X)):
        if i % 2 == 0:
            test_data.append(X[i])
            test_label.append(Y[i])
        else:
            train_data.append(X[i])
            train_label.append(Y[i])
    # penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True,
    #                                     intercept_scaling=1, class_weight=None, random_state=None, solver='liblinear',
    #                                     max_iter=100, multi_class='ovr', verbose=0, warm_start=False, n_jobs=1
    # 惩罚函数/正则(L)
    clf = linear_model.LogisticRegression(
        penalty='l2', dual=False, tol=1e-4, C=1000, class_weight=None, random_state=None,
        solver='newton-cg', max_iter=10000, verbose=0, warm_start=False, n_jobs=1,
    )
    # 根据训练数据集来训练算法模型
    clf.fit(train_data, train_label)
    # 利用训练好的模型来执行预测计算
    predict = clf.predict(test_data)
    print(classification_report(test_label, predict))
    # print(list(predict))

""" 
~$Chp3_LogisticRegression.pptx

 """
