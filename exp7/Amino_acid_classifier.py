from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import numpy as np

''' 本程序采用python3的注解,标记出变量/函数的类型,提高可读性 '''
def get_percents(protein)->list:
    ''' according the protein to calculate the percentes: '''
    aa20:tuple = ('A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
            'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V')
    result_list = []
    protein_len:int = len(protein)
    for amino in aa20:
        # print(amino,end=" ")
        # dict={amino:protein.count(amino)/protein_len}
        percent = protein.count(amino)/protein_len
        result_list.append(percent)
    return result_list


def get_protein_sequences1(file:str)->list[str]:
    ''' get protein sequences from file '''
    sequences = []
    with open(file, "r") as file_input_stream:
        # 从文件中读取蛋白质序列
        for line in file_input_stream:
            # 每次读取一行(str)
            line = line.split(" ")
            sequences.append(line[2].strip())
    return sequences

def get_protein_sequences2(file):
    ''' get protein sequences from file '''
    sequences = []
    with open(file, "r") as file_input_stream:
        for line in file_input_stream:
            line = line.split(" ")
            sequences.append(line[1].strip())
    return sequences

def get_protein_labels(file):
    ''' get labels of each protein from file '''
    labels = []
    with open(file, "r") as file_input_stream:
        for line in file_input_stream:
            # the line is <class 'str'>
            line = line.split(" ")
            labels.append(int(line[1]))
    return labels


def output_file(result_list, result_file, classifier=""):
    with open(result_file, "w") as fos:
        result = ""
        # print(str(result_list))
        # fos.write(classifier+str(result_list))
        for char in result_list:
            result = result+(str(char)+'\n')
        print(result)
        result.strip()
        fos.write(result)


prefix = "D:/OneDrive - pop.zjgsu.edu.cn/PythonPath/exp7/"
ProSeqs_Test = prefix+"ProSeqs_Test.txt"
ProSeqs_Train = prefix+"ProSeqs_Train.txt"
x_list = get_protein_sequences1(ProSeqs_Train)
y_list = get_protein_labels(ProSeqs_Train)
# print(y_list)

# with open(ProSeqs_Train, "r") as file_input_stream:
    # # line=file_input_stream.readline()
    # for line in file_input_stream:
    #     # the line is <class 'str'>
    #     line = line.split(" ")
    #     input_list.append(line[2].strip())
    #     # print(line)
    #     # print(type(line))
    #     # break
    #     y.append(int(line[1]))
# debug
    # file_input_stream.close()
    # print(input_list)
    # print(x_list)
x_percents = [get_percents(protein) for protein in x_list]
# print(x_percents)
# print(len(x_percents))

x_array = np.array(x_percents)  # 注意不是用ndarray()
y_array = np.array(y_list)
#degug
    # print(len(x_array))
    # print(x_array, "\n\n", y_array)

    # print(len(x))
    # print(x)
    # print(y)
x_list_test = get_protein_sequences2(ProSeqs_Test)
x_percents_test = [get_percents(protein) for protein in x_list_test]
x_array_test = np.array(x_percents_test)
# print(x_array_test)

clf = GaussianNB()
# clf=KNeighborsClassifier(n_neighbors=55)

def estimate_accuracy(x_array,y_array,sample_num=1500):
    sample_num=1500
    estimate_accuracy_x=x_array[:sample_num]
    estimate_accuracy_y=y_array[:sample_num]
    # print(estimate_accuracy_x,estimate_accuracy_y)
    # print(len(estimate_accuracy_x))

    #fit the modle(classifier)
    clf.fit(estimate_accuracy_x,estimate_accuracy_y)

    estimate_accuracy_x_test=x_array[sample_num:]
    real_result=y_array[sample_num:]
    # predict according the x segment:
    estimate_result=clf.predict(estimate_accuracy_x_test)
    # calculate the accuracy:
    ''' the GNB will be expecting has the 80% accuracy or so: '''
    length=len(estimate_result)
    count=0
    for label1,label2 in zip(estimate_result,real_result):
        if label1==label2:
            count+=1
        else :
            # print(label1," ",label2)
            pass
    # print the len to certain the result is calculate the proper case:
    print(count/length,length,"elements were predicted")
    

# print(len(x_array), len(y_array))
clf.fit(x_array, y_array)
result_list = clf.predict(x_array_test)
print(result_list)
prediction_result = prefix+"preds.txt"
output_file(result_list, prediction_result)
