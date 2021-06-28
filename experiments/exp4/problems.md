(5)类的定义以及实例化测试。
定义一个列表的操作类Listinfo，包括的方法:
(a)列表元素添加: add_elem (elename)  [elename: 字符串或者整数类型]
(b)列表元素取值：get_ elem(num)   [num: 整数类型]
(c)列表合并：merge_list(ls)	  [ls: 列表类型]
(d)删除最后一个元素，并返回这个元素：del_lastone()
写好这个类之后，进行实例化测试，某个实例对象创建可以如下：
********list_info = Listinfo([44,222,111,333,454,'sss','333'])
源代码：

源代码截图：

运行结果截图：

(6)通过Python包与模块的创建，理解Python项目的组织结构。
创建一个包（Package），并命名为“mypack”，注意包的目录下需要包含“__init__. py”文件。在“mypack”目录下创建“aa.py”文件以及一个名为“subpack”的子包，在子包“subpack”下创建“bb.py”文件。最后创建一个和“mypack”同级的“test.py”文件。项目结构如下:
test.py
mypack
|-- __init__.py
|-- aa.py
|-- subpack
|-- __init__.py
|-- bb.py
其中， 需将各个“*.py”源代码具体定义为：
(i)在“aa.py”中定义一个函数add(x, y)，该方法能够打印输出x、y的两数之和；
(ii) 在“bb.py”中定义一个函数sub(x, y)，该方法能够打印输出x、y的两数之差；(iii)在“mypack”的“__init__. py”文件中定义两个变量a和b，并为其赋值a=2, b=1；(iv)在“test.py”文件中定义两个变量m和n，并为其赋值m=4, n=3。且要求在“test.py”文件中，进行如下操作：
(a)使用from ... import ...的方式导入模块“bb.py”中的sub(x, y)方法，将m、n传入sub(x,y)方法中，得到输出结果；
(b)使用from ... import ...的方式导入模块“aa.py”中的add(x,y)方法，将m、n传入add(x,y)方法中，得到输出结果；
(c)使用from ... import ...的方式导入“mypack”里“__init__. py”文件的a、b，将a、b传入add(x,y)方法中，得到输出结果。
源代码(test.py)：

源代码(test.py)截图：

运行结果截图：

项目实际目录截图：

(7)类的继承及其实例化测试。
定义一个类Human，包括的方法: (i) 构造函数__init__()：包含参数name、age; (ii) get_name(): 打印输出name的内容; (iii) do_homework()：打印输出语句‘There is no homework from the parent!’;
另外再定义一个类Student，让其继承Human类，包含的方法：(i)构造函数__init__()：包含参数name、age、homework; (ii) do_homework()：打印输出属性homework内容的语句，如print(“作业为:”+ self.homework)，并利用super()方法继承Human类的do_homework()方法。
接下来，进行实例化测试，如stu = Student(‘John’, 20, ‘Python实验’)，进一步引用并打印输出对象stu的三个属性name、age、homework的内容，然后调用方法do_homework()和get_name()，查看运行结果。
源代码：

源代码截图：

运行结果截图：

(8)类成员的访问以及实例化测试。
定义一个计数器类Counter，包括的变量及方法: (i)首先定义两个类变量，分别为：公开变量publicCount，为其赋初始值0；私有变量secretCount（私有变量的命名方式为：__variableName），为其赋初始值0；(ii)定义方法count()：能够使得私有变量secretCount和共有变量publicCount都自增1，并打印输出私有变量secretCount的值。
接下来，进行实例化测试，创建类的实例对象，形如counter = Counter()，并进行以下操作：
(a)使用类对象调用count()方法；
(b)尝试使用类对象直接调用私有变量secretCount。如果报错，思考如何使用类对象直接调用私有属性，并打印输出结果。
源代码：

源代码截图：

运行结果截图：

(9) 模块文件中定义类及其实例化。
首先，创建一个名为“mc.py”的模块文件。在该模块文件中，编写一个通用的人员类（person），该类具有姓名（Name）、年龄（Age）、性别（Sex）等私有属性，如Name的私有属性可以写为“self.__name”。为保护个人隐私，person类的所有数据属性均需定义为私有属性。然后，对person 类进行继承得到一个学生类（student），该类能够存放学生任意多门课的成绩（这里门数不定），并能求出平均成绩。
最后，另外创建一个主文件“test.py”，以from…import…方式导入student类，并给出三位学生的student实例，要求他们的课程门数不同，在实例化测试中对student类的功能进行验证。
源代码(mc.py)：

源代码(test.py)：

源代码截图(mc.py)：

源代码截图(test.py)：

运行结果截图：

(10) 定义一个高维空间样本点集类HDPoints，须包含以下数据属性与方法属性：
(a)数据属性self.points：类型为列表，由多个子列表构成，每个子列表表示高维空间中的一个数据点，且数据维度可以任意，并通过初始化构造函数获得。
(b)方法属性centerpoint(self)：计算点集的中心点。
(c)方法属性minkowski (self, x, y, p)：计算两点x和y之间的闵可夫斯基距离，p为非负整数，用p=0情形表示切比雪夫距离。由此定义的距离称为p-闵氏距离，其数学定义如下：

(d)方法属性farthestpoint(self, p)：找出离中心点p-闵氏距离最远的点，返回在self.points中的下标以及最大距离。
(e)方法属性farthest2points(self, p)：找出点集self.points中p-闵氏距离最远的两点，返回两点在self.points中的下标及其最大距离。
接一下来，实例化类HDPoints，利用random模块，随机产生至少50个高维空间数据点，样本点的维度至少在5以上，且每个分量取值服从区间[0,1]上的均匀分布。同时，随机产生一个0~5之间的一个非负整数，赋值传递给p-闵氏距离函数中的参数p，对HDPoints实例对象的全部自定义方法属性（即centerpoint()、minkowski()、farthestpoint()和farthest2points()）进行功能测试。
源代码：

源代码截图：

运行结果截图：
