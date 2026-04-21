############################## 20260420
# import random
# print("欢迎来到猜数字游戏！")
# 
# secret = random.randint(1, 10)
# temp = input("猜一下心中的数字：")
# guess = int(temp)
# times = 1
# 
# while (guess != secret) and (times < 3):
#     if guess > secret:
#         print("哥，大了大了~~")
#     else:        
#         print("哥，小了小了~~")
#     temp = input("请再试试吧：")
#     guess = int(temp)
#     times += 1
# if (guess == secret) and (times <= 3):
#     print("猜对了，游戏结束，不玩了！")
# else:
#     print("哥，三次机会用完了，游戏结束，不玩了！")


# for year in range(2020, 2031):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         break
# print(year, "是第一个闰年")


############################## 20260421
# 序列：列表、元组、字符串
# 都可以通过索引得到每一个元素、索引值从0开始、切片得到任意范围元素、共同的操作符
############################# 列表
# 列表从0开始计数，eggs[0]是第一个元素，eggs[1]是第二个元素，以此类推
# eggs = [1, 2, [3,"随意"], 4, 5]
# eggs.append(6) # 在列表末尾添加一个元素
# print(eggs)
# eggs.extend([7, 8, 9]) # 在列表末尾添加多个元素
# print(eggs)
# print(eggs[len(eggs) - 1])
# print(eggs[-1]) # 负数索引，-1表示最后一个元素，-2表示倒数第二个元素，以此类推
# print(eggs[0]) # 第一个元素
# print(eggs[2][1]) # 第三个元素的第二个元素
# eggs.remove(1) # 删除列表中的元素1
# print(eggs)
# eggs.pop(1) # 删除列表中的第二个位置元素
# print(eggs)
# eggs1 = eggs[2:5] # 切片，获取列表中的一部分，eggs[2:5]表示从第三个元素开始到第六个元素结束（不包括第六个元素）
# print(eggs1)
# eggs2 = eggs[:2] # 切片，获取列表中的一部分，eggs[:2]表示从第一个元素开始到第三个元素结束（不包括第三个元素）
# print(eggs2)
# eggs3 = eggs[2:] # 切片，获取列表中的一部分，eggs[2:]表示从第三个元素开始到最后一个元素结束
# print(eggs3)
# eggs4 = eggs[:] # 复制列表 
# print(eggs4)
# eggs5 = eggs[-2:] # 切片，获取列表中的一部分，eggs[-2:]表示从倒数第二个元素开始到最后一个元素结束
# print(eggs5)
# eggs6 = eggs[::-1] # 切片，-1表示倒叙，eggs[::1]表示从第一个元素开始到最后一个元素结束，步长为1，以此类推
# print(eggs6)

# 元组、字符串一旦确认就不能修改了，列表可以修改。可以使用切片操作拼接达到修改目的。

############################# 字符串
# str1 = 'Hello World'
# str1 = str1.casefold()
# print(str1)
# str2 = "{0}, 你好吗？{a}".format("小明", a="我是小红") # format方法，{0}表示第一个参数，{a}表示命名参数a
# print(str2)
# str3 = "{0}: {1:.2f}".format("圆周率", 3.1415926) # format方法，{0}表示第一个参数，{1:.2f}表示第二个参数保留两位小数
# print(str3)
# str4 = "%s;%s;%5.1f;%10d;%010d" % (str2, str3, 3.1415926, 123, 123) # %s表示字符串，%f表示浮点数，%d表示整数，%5.1f表示保留一位小数，宽度为5，%10d表示宽度为10，右对齐，%010d表示宽度为10，右对齐，前面补0
# print(str4)
# str5 = list(str1) # 将字符串转换为列表，字符串是不可变的，列表是可变的，可以修改列表中的元素
# print(str5)

#############################自定义函数
# def divide(a, b):
#     """
#     除法函数，返回a除以b的结果
#     :param a: 被除数
#     :param b: 除数
#     :return: a除以b的结果，如果除数为0，返回错误信息
#     """
#     if b == 0:
#         return "除数不能为0"
#     else:
#         return a / b
# 
# print(divide(10, 0))
# print(divide.__doc__) # 输出函数的文档字符串，帮助用户理解函数的作用和使用方法
# 
# # 位置参数必须在关键字参数或默认参数前面，否则会报错
# 
# def watchMovie(name="张三", cigarette=True, drink=True, girlFriend=True):
#     sentence = name + "带着"
#     if cigarette:
#         sentence = sentence + "香烟"
#     if drink:
#         sentence = sentence + "啤酒"
#     if girlFriend:
#         if cigarette or drink:
#             sentence = sentence + "和女朋友"
#         else:
#             sentence = sentence + "女朋友"
#     sentence = sentence + "去看电影"
#     return sentence
# 
# print(watchMovie())
# print(watchMovie("李四", cigarette=False, drink=False, girlFriend=True))  #“李四”这个位置参数必须放在前面，否则会报错
# 
# #收集参数  会打包成元组
# def test(*params, extra):
#     print("收集参数是：", params)
#     print("位置参数：", extra)
# print(test(1, 2, 3, extra=4)) # 收集参数必须放在位置参数前面，否则会报错
# # * 在形参中是打包，在实参中是解包
# name = "fishC"
# print(*name) # 解包字符串，输出每个字符
# numbers = [1, 2, 3, 4, 5]
# print(*numbers) # 解包列表，输出每个元素

############################# 知识
# 如果在函数内部试图修改外部的全局变量，必须使用global关键字声明该变量为全局变量，
# 否则会创建一个新的局部变量，导致外部的全局变量无法被修改。

# 内嵌函数：在一个函数内部定义另一个函数，内嵌函数可以访问外部函数的变量，但外部函数无法访问内嵌函数的变量。

# LEGB规则：Local（局部作用域） -> Enclosing（嵌套作用域） -> Global（全局作用域） -> Built-in（内置作用域）
# ，Python会按照这个顺序查找变量。

# str1 = "Hello World"
# x = 5
# def test():
#     x = 10
#     print(x) # 输出局部变量x
# test()
# print(x)
# print(len(str1))


############################## 闭包
# def funX(x):
#     def funY(y):
#         return x + y
#     return funY
# temp = funX(10) # funX返回funY函数对象，temp指向funY函数对象
# print(temp(5)) # 调用funY函数，输出15
# 
# # 由于内部函数只能访问外部变量，不能修改，以往方式是通过容器间接实现，容器不会被屏蔽
# def funA():
#     x = [5]
#     def funB():
#         x[0] = x[0] + 1
#         return x[0]
#     return funB
# temp = funA() # funA返回funB函数对象，temp指向funB函数对象
# print(temp()) # 调用funB函数，输出6
# 
# # python 3引入了nonlocal关键字，允许在内嵌函数中修改外部函数的变量
# def funC():
#     x = 5
#     def funD():
#         nonlocal x # 声明x为外部函数的变量，允许修改
#         x = x + 1
#         return x
#     return funD
# temp = funC()
# print(temp()) # 调用funD函数，输出6


############################## 装饰器
def log(func):
    def wrapper(*params):
        print("开始调用eat()函数...")
        func(*params)
        print("结束调用eat()函数...")
        return "都吃过了" # 这里不加return，最后打印的结果就是None，因为wrapper函数没有返回值，默认返回None
    return wrapper

@log  # @log是装饰器语法糖，等价于eat = log(eat)，将eat函数作为参数传递给log函数，返回wrapper函数对象，eat指向wrapper函数对象
def eat(*names):  # 支持任意数量的人
    for name in names:
        print("%s正在吃饭..." % name)

print(eat("小明", "小红"))