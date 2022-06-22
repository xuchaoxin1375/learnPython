##
import numpy as np
a=np.array([1,2,3])


[
    [1., 0., 0.],
    [0., 1., 2.]
]

# 两个包含基本元素的向量a1,a2 
a1=[1,0,0]
a2=[1,0,0]
#最外层的向量维度,包含两个元素a1,a2;其中a1,a2又都是一个包含三个基本元素的向量
nd_list=[a1,a2]
# 将以上组织结构实例化一个相对应的numpy的ndarray对象
nd=np.array(nd_list)
print("@nd:\n",nd)
print("@nd.shape:",nd.shape)
print("@nd.dtype:",nd.dtype)
##
b1=[1,2]
b2=[3,4]
b3=[5,6]
nd2_list=[b1,b2,b3]
nd2=np.array(nd2_list)
print("@nd:\n",nd2)
print("@nd.shape:",nd2.shape)
print("@nd.dtype:",nd2.dtype)
# 同等体量(包含相同基本元素的向量,正如nd.size属性所指示的那样)的ndarray经过不同的组织,可以得到不同的规格的ndarray
##
print("@nd.size",nd.size)
print("@nd2:",nd2.size)

##
# 设定nd一级元素有100个,每个一级元素包含100个二级元素(这里二级元素已经是最低级元素(基本元素)),总共2个维度;共计10000个基本元素
nd=np.arange(10000).reshape(100, 100)
print("@nd:\n",nd)
##
#设定一级元素10个,每个一级元素10个二级元素,每个二级元素包含100个三级元素(这里的三级元素为最低级别元素,基本元素),总共3个维度;共计10000个基本元素
nd=np.arange(10000).reshape(10,10,100)
print("@nd:\n",nd)
##
nd=np.arange(1000).reshape(10,10,10)
print("@nd:\n",nd)


##
b = np.arange(4)
bb=b**2
print("@b:\n",b)
print("@bb:\n",bb)
##
b = np.arange(-4,4,0.5)
print("@b:\n",b)
sin_b=np.sin(b)
print("@sin_b:\n",sin_b)
sin_b_ten=np.sin(b)*10
print("@sin_b_ten:\n",sin_b_ten)

##
#随机数模块
# 实例化一个默认的随机数产生器
rng=np.random.default_rng()
print("@rng:",rng)
##

rfloat=rng.random()
print("@rfloat:",rfloat)
##
rints = rng.integers(low=0, high=10, size=3)
print("@rints:",rints)
##
#产生随机数矩阵(shape=(3,3))
arr1 = rng.random((3, 3))
print("@arr1:\n",arr1)
##

arr2=rng.integers(low=-3, high=3, size=(3,4))
print("@arr2:\n",arr2)
##
arr3=rng.random((3,3))+10
print("@arr3:\n",arr3)
##
#生成0~10间的随机数
arr4=rng.random((3,3))*10
print("@arr4:\n",arr4)

## 
# 概率论&数理统计:符合泊松分布的数据集使用案例
import numpy as np
rng = np.random.default_rng()
s = rng.poisson(5, 10000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 14, density=True)
plt.show()