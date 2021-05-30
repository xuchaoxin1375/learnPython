import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import logging as l
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
l.basicConfig(level=l.INFO)
import sklearn
prefix="D:/OneDrive - pop.zjgsu.edu.cn/PythonPath/exp9/"
train_data=prefix+"train_data.csv"
test_data=prefix+"test_data.csv"
emotion = {0: 'Angry', 1: 'Disgust', 2: 'Fear',
           3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}
''' get dateFrame(contain strings)(the whole data) '''
g_train_data_df = pd.read_csv(train_data, dtype='a')
g_test_data_df=pd.read_csv(test_data,dtype='a')
    # l.debug(f"\n{data}")
g_label_str = np.array(g_train_data_df['emotion'])
    #get the float lable array
g_label_int=g_label_str.astype(int)
    # l.debug(f"\n{type(label)}\n{label}")

g_train_img_data_str = np.array(g_train_data_df['pixels'])
g_test_img_data_str=np.array(g_test_data_df['pixels'])

    # l.debug(f"\n{img_data}")
    # l.debug(f"\n{train_img_data_str.shape}")  # （170，）

g_clf_GNB=GaussianNB()
g_clf_KNN=KNeighborsClassifier()
g_train_img_data_float=[]
g_test_img_data_float=[]
# train_img_data_float=train_img_data_str.astype(float)
def nd_to_float(img_data_str,img_data_float):
    for str2float in img_data_str:
        np_float=np.fromstring(str2float,dtype=float,sep=' ')
        img_data_float.append(np_float)
def g_nds_to_float():
    nd_to_float(g_train_img_data_str,g_train_img_data_float)
    nd_to_float(g_test_img_data_str,g_test_img_data_float)
    
def predict(train_img_data_float,train_label_int,test_img_data_float,classifier):
    #训练数据和对应的标签
    classifier.fit(train_img_data_float,train_label_int)
    #return ndarray_int(返回预测结果)
    return classifier.predict(test_img_data_float)

# # 显示人脸以及对应表情
def show_pictures(img_data_float,label_int):
    
    #show the images
    size=len(img_data_float)
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
        
        item_float=img_data_float[index]
        # l.debug(f"\n{item_float.shape}")
        # this is a good idea to make the values to range in (0,1)
        item_float = item_float/item_float.max()
        img_x = np.reshape(item_float, (48, 48))
        # the loaction of the pictrue will show
        plt.subplot(7, 7, index+1)

        plt.axis('off')
        plt.title(emotion[(label_int[index])])

        # print(emotion[(label_int[index])])
        # Display data as an image, i.e., on a 2D regular raster.:image_show
        ''' 
            The input may either be actual RGB(A) data, or 2D scalar data, which will be rendered as a pseudocolor image. For displaying a grayscale image set up the colormapping using the parameters cmap='gray', vmin=0, vmax=255.

            The number of pixels used to render an image is set by the Axes size and the dpi of the figure. This can lead to aliasing artifacts when the image is resampled because the displayed image size will usually not match the size of X (see Image antialiasing). The resampling can be controlled via the interpolation parameter and/or rcParams["image.interpolation"] (default: 'antialiased').
            输入可以是实际的RGB（A）数据，也可以是2D标量数据，它们将被呈现为伪彩色图像。 为了显示灰度图像，请使用参数cmap ='gray'，vmin = 0，vmax = 255设置颜色映射。
            用于渲染图像的像素数由图形的轴大小和dpi设置。 当重新采样图像时，这可能会导致混淆现象，因为显示的图像大小通常将与X的大小不匹配（请参阅图像抗锯齿）。 可以通过插值参数和/或rcParams [“ image.interpolation”]（默认值：“ antialiased”）控制重采样。  '''
        plt.imshow(img_x, plt.cm.gray)
    # present the result:
    plt.pause(15)
    
    # print(label)
def exec(train_img_data_float,train_label_int,test_img_data_float):
    g_nds_to_float()
    predict_label_int=predict(train_img_data_float,train_label_int,test_img_data_float,g_clf_GNB)
    with open(prefix+"preds.txt","w") as fos:
        for label_int in predict_label_int:
            fos.write(str(label_int)+"\n")
        
    show_pictures(test_img_data_float,predict_label_int)
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
def estimate_accuracy():
    ''' 调用本函数前,请确保执行了nds_to_flaot()方法,得到数值化数据集 '''
    g_nds_to_float()
    estimate_scale=int(len(g_train_img_data_float)*0.75)
    #截取估算子集
    estimate_train_data_float=g_train_img_data_float[:estimate_scale]
    global g_label_int
    estimate_train_label=g_label_int[:estimate_scale]
    estimate_test_data_float=g_train_img_data_float[estimate_scale:]
    estiamte_real_data_int=g_label_int[estimate_scale:]
    estimate_predict_labels_int= predict(estimate_train_data_float,estimate_train_label,estimate_test_data_float,g_clf_GNB)
    show_pictures(estimate_test_data_float,estimate_predict_labels_int) 
    
    count=0
    be_predict=len(estimate_predict_labels_int)
    for pred,real in zip(estimate_predict_labels_int,estiamte_real_data_int):
        print(emotion[pred],emotion[real])
        if pred==real:
            count+=1
    print(be_predict,"were predicted","the expecting accuracy is :",count/be_predict)
    print(f"{be_predict}were predicted,{count} hit,the expecting accuracy is :{count/be_predict}")
        
    
    

    
if __name__ =="__main__":
    exec(g_train_img_data_float,g_label_int,g_test_img_data_float)
# exec(g_test_img_data_float,g_label_int)
# estimate_accuracy()
# exec(g_)
    