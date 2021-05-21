import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
""" KNN  """


def test_KNN():
    # prepare the fiting data set(including the intrinsic data x and  tag data y )
    from sklearn.neighbors import KNeighborsClassifier
    x = [[0.2, 1, 1.5], [1.2, 3.1, 0.8], [2, 3.2, 1], [3, 2, 0.3]]
    # with the corresponding tag data collection
    y = [0, 0, 1, 1]
    # import the classify algorithm from sklearn package
    # get the corresponding classifier instance with specific classify algorithm:
    # (there may need parameters to generate the specified classifier)
    neigh = KNeighborsClassifier(n_neighbors=3)
    # use the classifier instance to fit the module
    neigh.fit(x, y)
    # prepare the new test data set:
    newx = [[1.1, -1.2, 2.3]]
    # do the predict work and get the result:
    print("Predict_KNN:", neigh.predict(newx))
    print("Probability_KNN:", neigh.predict_proba(newx))


""" Gaussian naive bayes """


def test_GNB():
    import numpy as np
    x = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    y = np.array([1, 1, 1, 2, 2, 2])
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(x, y)
    newx = [[0.8, -1], [1, 1.2]]
    print("predict_GNB:", clf.predict(newx))
    print("prob_GNB:", clf.predict_proba(newx))


""" the exp6 """


def output_file(result_list, result_file,method):
    with open(result_file, "w") as fos:
        result=""
        # print(str(result_list))
        for char in result_list:
            result=result+(str(char)+'\n')
        print(result)
        result.strip()
        # fos.write(method+str(result_list))
        fos.write(result)


def exp6():
    from re import T
    from openpyxl import Workbook
    from openpyxl.utils.dataframe import dataframe_to_rows
    import pandas as pd
    import numpy as np
    prefix = "./exp6/"
    data_train = 'data-train.csv'  
    data_test = 'data-test.csv'

    data_train = prefix+data_train
    data_test = prefix+data_test
    prediction_result = prefix+'prediction.txt'  
    # 读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
    """   # print(data_table)
        # print(data_table.loc[0:3])
        # print("\n"*3)
        # list=np.array(data_table.iloc[:,:]).tolist()
        # print(list[0])
        # lists=np.array(data_table.iloc[:,:-1]).tolist()
        # print(lists[0])
        # print(list[0]) """
    df_train = pd.read_csv(data_train, encoding='utf-8')
    # x_arrays = np.array(df_train.iloc[:, :-1])
    # y_array = np.array(df_train['target'])
    x_arrays = np.array(df_train.iloc[:180, :-1])
    y_array = np.array(df_train.iloc[:180, -1])
    
    # print(x_arrays,"\n",y_array)
   
    #the original prediction 
    # df_test = pd.read_csv(data_test, encoding='utf-8')
    # newx = np.array(df_test.iloc[:, :-1])
    #estimate the accuracy
    # df_estimate =pd.read_csv(data_train,encoding='utf-8')
    newx=np.array(df_train.iloc[181:,:-1])
    newx_real=np.array(df_train.iloc[181:,-1])

    # KNN_exp6(x_arrays,y_array,newx,prediction_result)
    # GNB_exp6(x_arrays,y_array,newx,prediction_result)

    #gnb predicion:
    clf= GaussianNB()
    clf.fit(x_arrays,y_array)
    newx_predict=clf.predict(newx)
    # print(newx_predict,"\n",newx_real)
    
    count=0
    for label1,label2 in  zip(newx_predict,newx_real):
        if label1==label2:
            count+=1
        else:
            print(label1,label2)
    print(len(newx_predict))
    print(count/len(newx_predict))
    
    
    # print("predict_GNB:",clf.predict((newx)))
    # print("probability_GNB:",clf.predict_proba(newx))

def KNN_exp6(x,y,newx,prediction_result):
    # the default n_neightbors=5
    clf=KNeighborsClassifier(n_neighbors=7)
    clf.fit(x,y)
    result_list=clf.predict(newx)
    output_file(result_list, prediction_result,"KNN")
def GNB_exp6(x,y,newx,prediction_result):
    clf= GaussianNB()
    clf.fit(x, y)
    result_list=clf.predict(newx)
    output_file(result_list, prediction_result,"GNB")
    
exp6()
