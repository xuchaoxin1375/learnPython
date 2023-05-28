##


def iter_table_output(lst, row_len=3, cell_width="20"):
    for i in range(len(lst)):
        print(format(str(lst[i]), cell_width), end="\t")
        if (i + 1) % row_len == 0:
            print()


def iter_output_1(lst):
    for i in lst:
        print(i)


def sayHellow():
    print("\n🎈hellow! package by cxxu for output contents formatter")


def testPackage():
    print("\n😊test package!")


# def get_attrs_magic(obj):


def get_attrs(obj, magic=True):
    """获取对象的属性Key:Value
    key是不可调用的属性(成员变量而非成员方法)

    Parameters
    ----------
    obj : any
        需要查询对象属性key:value的对象
    magic: bool
        是否包括魔术属性`__doc__`这类属性
    Returns
    -------
    list[tuple[str, any]]

    """
    res = []
    if "__dict__" in dir(obj):
        res =[('__dict__',vars(obj))]
    if magic:
        print(
            "[I] obj does not exsit does not have __dict__ attribute to be argument of vars()!\n"
        )
        # res=get_attrs_magic(obj)
        res = [
            (attr, getattr(obj, attr))
            for attr in dir(obj)
            if not callable(getattr(obj, attr))
        ]
    return res


def get_methods(obj, magic=False):
    """获取对象的属性Key:Value
    key是可调用的属性(成员方法)

    Parameters
    ----------
    obj : any
        需要查询对象属性key:value的对象
    magic: bool
        是否包括魔术属性`__xx__`这可调用属性
    Returns
    -------
    list[str]

    """
    # res = [attr for attr in dir(obj) if callable(getattr(obj, attr)) and magic and attr.startswith("__")]
    res = []

    for attr_name in dir(obj):
        if callable(getattr(obj, attr_name)):
            if magic == False:
                if attr_name.startswith("__"):
                    continue
            res.append(attr_name)

    return res


class DemoClass:
    """用于测试用的类,包含简单的属性和方法"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
def print_dict_in_lines(result_dict):
    """Print key value pairs in the dictionary line by line

    Parameters
    ----------
    result_dict : dict
        the dict to be print in lines
    """
    for key,value in result_dict.items():
        print(f'{key}:{value}')

if __name__ == "__main__":
    obj = DemoClass("John", 30)
    # res=get_attrs("good")
    attrs = get_attrs(obj,magic=False)
    methods = get_methods(obj, magic=False)
    print("res: ", attrs)
