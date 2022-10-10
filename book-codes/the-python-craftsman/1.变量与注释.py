"""
变量与注释之禅：

何为变量？变量就是用来从内存中找个某个东西的标记；
何为注释？注释就是用来描述代码的；
对于计算机而言，变量定义的好坏，注释的有无，都不会影响到程序正常的执行
对于读代码的人而言，直接决定了读者对代码的第一印象，也影响了读者对代码质量的判断;

禅：变量和注释是程序员表达思想的基础，故好的变量和注释并非为计算机而写，而是为每个阅读代码的人而写。
"""

# 【变量的常见用法】
# 定义变量
author = 'sswang'
print('Hello, {}'.format(author))  # 输出打印方式一
print("Hello, %s" % author)  # 输出打印方式二 
print(f"author is {author}")  # 输出打印方式三【目前最常用的方式】


# 交换变量
author, reader = 'ssw', 'sswang'
author, reader = reader, author
print(f"author: {author} reader: {reader}")


# 变量解包
## 普通解包
## 技巧：解包是python里的一种特殊的赋值操作，允许我们把一个可迭代对象的所有成员，一次性赋值给多个变量
usernames = ['sswang1', 'sswang2']
author, reader = usernames
print(f"author: {author} reader: {reader}")

attrs = [1, ['sswang',100]]
user_id, (username, score)= attrs
print(f"user_id:{user_id}", f"username:{username}", f"score:{score}")


## 动态解包
## 技巧：只要使用*号表达式（*variables）作为变量名，它便会贪婪地捕获多个值对象，并将捕获到的内容作为列表赋值给variables
data = ['sswang','apple', 'orange', 'banana', 100]
username, *fruits, score = data
print(f"username:{username}", f"fruits:{fruits}", f"score:{score}")

# 切片
username, fruits, score = data[0], data[1:-1], data[-1]
print(f"username:{username}", f"fruits:{fruits}", f"score:{score}")
# 可以看出，相对于切片，动态解包看上去会更优雅

# 上述解包操作可以在任务循环语句中使用：
for username, score in [("sswang1",'99'), ("sswang2",'98')]:
    print(f"username:{username}", f"score:{score}")


# 单下划线变量名 _
## 技巧：常被用作一个无意义的占位符，若在解包赋值时忽略某些变量，可以使用 _
author, _ = usernames  # 忽略展开时的第二个变量；
username, *_, score = data  # 忽略第一个和最后一个变量之间的所有变量

## 在python的交互式环境中，_ 变量还有另外一个含义：默认保存我们输入的上个表达式的返回值
In [1]: "data".upper()
Out[1]: 'DATA'
In [2]: print(_)
DATA


# 【给变量注明类型】
## 分析：动态语言在使用变量不需要做任何的类型声明，对于开发者来说是优势，但对于读者来说，其实是一个劣势，因为让代码可读性变差了
## 技巧: 在编码时建议尽可能多的使用类型注解，具体的做法就是：在变量名后添加类型，使用冒号分隔
def remove_invalid(items):
    """剔除items中无效项"""
    ...

# Sphinx格式（函数）文档
def remove_invalid(items):
    """剔除items里无效的元素
    :param items: 待剔除对象
    type items: 包含整个的列表， [int, ...]
    """
    ...

# 类型注解
from concurrent.futures import process
from typing import List
def remove_invalid(items: List[int]):
    """剔除items里无效的元素
    """
    ...


# 注释基础知识
# 用户输入可能会有空格，使用strip去掉空格
# 1. 数据库保存占用空间更小
# 2. 不必因为用户多打了一个空格而要求用户重新输入
username = extract_username(input_string.strip())


class Person:
    """人
    
    param name: 姓名
    param age: 年龄
    param favorite_color: 最喜欢的颜色
    """
    def __init__(self, name, age, favorite_color) -> None:
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
        
# 坏的注释方式
# 1. 用注释屏蔽代码
# 源码里有大段暂时不需要执行的代码
# trip = get_trip(request)
# trip.refresh()
# ...

# 2. 用注释复述代码
# bad
# 调用strip()去掉空格
input_string = input_string.strip()

# good
# 如果直接把空格的输入传递到后端处理，可能会造成后端服务崩溃
# 因此使用strip()去掉首尾空格
input_string = input_string.strip()

# 3. 弄错接口注释的受众
# bad
def resize_image(image, size):
    """将图片缩放到指定尺寸，并返回新的图片
    
    该函数将使用Pilot模块读取对象，然后调用.resize()方法将其缩放到指定尺寸。
    但由于Pilot模块自身限制，这个函数不能很好的处理过大的文件，当文件大小超过5MB时，
    resize()方法的性能会因为内存分配问题急剧下降，对于超过5MB的图片文件，请使用resize_big_iamge()替代
    
    :param iamge: 图片文件对象
    :param size: 包含宽高的元组：（width, height）
    :return : 新图片对象
    """
    ...

# good
def resize_image(image, size):
    """将图片缩放到指定尺寸，并返回新的图片
    
    注意： 当文件超过5MB时，请使用resize_big_image()
    
    :param iamge: 图片文件对象
    :param size: 包含宽高的元组：（width, height）
    :return : 新图片对象
    """
    ...




if __name__ == '__main__':
    pass