import sklearn
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging as l
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
l.basicConfig(level=l.INFO)
prefix = "D:/OneDrive - pop.zjgsu.edu.cn/PythonPath/exp9/"
train_data = prefix+"train_data.csv"
test_data = prefix+"test_data.csv"
emotion = {0: 'Angry', 1: 'Disgust', 2: 'Fear',
           3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}

''' get dateFrame(contain strings)(the whole data) '''
g_train_data_df = pd.read_csv(train_data, dtype='a')
g_test_data_df = pd.read_csv(test_data, dtype='a')
# l.debug(f"\n{data}")

g_label_str_nd = np.array(g_train_data_df['emotion'])
# get the float lable array:利用ndarray的astype方法,将元素转为int类型
g_label_int_nd = g_label_str_nd.astype(int)
# l.debug(f"\n{type(label)}\n{label}")

g_train_img_data_str_nd = np.array(g_train_data_df['pixels'])
g_test_img_data_str_nd = np.array(g_test_data_df['pixels'])

g_clf_GNB = GaussianNB()
g_clf_KNN = KNeighborsClassifier()
# g_clf_svm=svm.SVR()
# g_clf_reg=LinearRegression()
g_clf_logistic = LogisticRegression()
# g_clf_MLP=MLPClassifier()
# g_clf_RF=RandomForestClassifier()
# g_clf_GB=GradientBoostingClassifier()
g_clf_DT = DecisionTreeClassifier()

''' 获取可以用sklearn直接计算的数值类型输入 '''
g_train_img_data: list[list[float]] = []
g_test_img_data: list[list[float]] = []
# train_img_data_float=train_img_data_str.astype(float)


def nd_to_float(img_data_str_nd: np.ndarray, img_data: list[list[float]]):
    for str2float in img_data_str_nd:
        np_float = np.fromstring(str2float, dtype=float, sep=' ')
        img_data.append(np_float)


def g_nds_to_float():
    nd_to_float(g_train_img_data_str_nd, g_train_img_data)
    nd_to_float(g_test_img_data_str_nd, g_test_img_data)


def predict(train_img_data_float , train_label_int, test_img_data_float, classifier):
    """[summary:根据传入的训练数据集和标签来训练模型,在根据带预测输入执行预测操作]

    Parameters
    ----------
    train_img_data_float : np.ndarray_like
        训练数据集
    train_label_int : np.ndarray_like
        训练数据解对应的标签(真)
    test_img_data_float : np.ndarray_like
        待预测数据集
    classifier : 分类器
        例如GNB,KNN分类器

    Returns
    -------
    [Iterable:list[int]]
        [分类结果]
    """
    print("fitting...")
    classifier.fit(train_img_data_float, train_label_int)
    print("almost to complete...")
    # return ndarray_int(返回预测结果)
    predict_result_int = [int(item)
                          for item in classifier.predict(test_img_data_float)]
    return predict_result_int

# # 显示人脸以及对应表情


def show_pictures(img_data_float, labels_int):
    """显示图像

    Parameters
    ----------
    img_data_float : np.ndarray_like
        需要被显示的图像的pixels
    labels_int : array_like
        [各图像表情的类别代号]
    """    
    # show the images
    size = len(img_data_float)
    l.debug(f"\nsize={size}")
    for index in range(size):
        # get the i_th picture's gray value description:
        # x = train_img_data[i]
        # l.debug(f"\ni={index}")

        # item_str=test_img_data_str[index]
        #     # l.debug(f"\n{type(item_str)}")  # str
        #     # turn to ndarray type:
        #     # A new 1-D array initialized from text data in a string.the digital string will be turn to float
        # item_float = np.fromstring(item_str, dtype=float, sep=' ')

        item_float = img_data_float[index]
        # l.debug(f"\n{item_float.shape}")
        # this is a good idea to make the values to range in (0,1)
        item_float = item_float/item_float.max()
        img_x = np.reshape(item_float, (48, 48))
        # the loaction of the pictrue will show
        plt.subplot(7, 7, index+1)

        plt.axis('off')
        plt.title(emotion[(labels_int[index])])

        # print(emotion[(label_int[index])])
        # Display data as an image, i.e., on a 2D regular raster.:image_show
        ''' 
            The input may either be actual RGB(A) data, or 2D scalar data, which will be rendered as a pseudocolor image. For displaying a grayscale image set up the colormapping using the parameters cmap='gray', vmin=0, vmax=255.

            The number of pixels used to render an image is set by the Axes size and the dpi of the figure. This can lead to aliasing artifacts when the image is resampled because the displayed image size will usually not match the size of X (see Image antialiasing). The resampling can be controlled via the interpolation parameter and/or rcParams["image.interpolation"] (default: 'antialiased').
            输入可以是实际的RGB（A）数据，也可以是2D标量数据，它们将被呈现为伪彩色图像。 为了显示灰度图像，请使用参数cmap ='gray'，vmin = 0，vmax = 255设置颜色映射。
            用于渲染图像的像素数由图形的轴大小和dpi设置。 当重新采样图像时，这可能会导致混淆现象，因为显示的图像大小通常将与X的大小不匹配（请参阅图像抗锯齿）。 可以通过插值参数和/或rcParams [“ image.interpolation”]（默认值：“ antialiased”）控制重采样。  '''
        plt.imshow(img_x)
    # present the result:
    plt.pause(5)

    # print(label)


def exec(train_img_data_float, train_label_int, test_img_data_float, classifier):
    """[summary]

    Parameters
    ----------
    train_img_data_float : np.ndarray
        [description]
    train_label_int : np.ndarray
        [description]
    test_img_data_float : np.ndarray
        [description]
    classifier : [type]
        [description]
    """
    g_nds_to_float()
    predict_label_int = predict(
        train_img_data_float, train_label_int, test_img_data_float, classifier)

    with open(prefix+"preds.txt", "w") as fos:
        for label_int in predict_label_int:
            fos.write(str(label_int)+"\n")

    show_pictures(test_img_data_float, predict_label_int)

# g_nds_to_float()
# exec(g_train_img_data_float,g_label_int,g_test_img_data_float)
''' 关于估算准确度:
    相对于直接的预测,在准确度估算中,
    需要执行训练数据集的变化(缩减)和测试数据的变化操作:
    您应当注意,使用sklearn的分类器做训练,需要将被测试集抽象成数值类型
    同时,如果您在读入训练/测试数据集的时候,是以字符串的形式,那么需要通过一定的步骤获得可处理的数值数组(或者其他的array-like isntance)
    此外,当您是在预测后才做准确度估算,那么就可以直接利用已经转换好的数值数据集对象(一般是截取其中的一部分数据,而用重新做数值化操作)
    确定截取的测试集部分(estimate_scale_select)
    estimate_train_data_Number
    estimate_train_data_Number
    estiamte_test_data_Number
    calculate the accuracy:
    estimate_real_data_Number

    '''


def estimate_accuracy(classifier):
    """[summary]
    ''' 调用本函数前,请确保执行了nds_to_flaot()方法,得到数值化数据集 '''

    Parameters
    ----------
    classifier : [type]
        [您要使用的分类器]
    """    
    
    g_nds_to_float()
    estimate_scale = int(len(g_train_img_data)*0.75)
    # 截取估算子集
    estimate_train_data_float = g_train_img_data[:estimate_scale]
    global g_label_int_nd
    estimate_train_label = g_label_int_nd[:estimate_scale]
    estimate_test_data_float = g_train_img_data[estimate_scale:]
    estiamte_real_data_int = g_label_int_nd[estimate_scale:]
    estimate_predict_labels_int = predict(
        estimate_train_data_float, estimate_train_label, estimate_test_data_float, classifier)
    show_pictures(estimate_test_data_float, estimate_predict_labels_int)

    count = 0
    be_predict = len(estimate_predict_labels_int)
    for pred, real in zip(estimate_predict_labels_int, estiamte_real_data_int):
        print(emotion[pred], emotion[real])
        if pred == real:
            count += 1
    print(be_predict, "were predicted",
          "the expecting accuracy is :", count/be_predict)
    print(f"{be_predict}were predicted,{count} hit,the expecting accuracy is :{count/be_predict}")


if __name__ == "__main__":
    exec(g_train_img_data, g_label_int_nd,
         g_test_img_data, g_clf_logistic)
    # estimate_accuracy(g_clf_logistic)
