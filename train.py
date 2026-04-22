# try:
#     # 可能会引发异常的代码
#     result = 10 / 0
# except ZeroDivisionError as e:
#     # 处理异常的代码
#     print("发生了零除错误：", e)
# else:
#     # 没有发生异常时执行的代码
#     print("结果是：", result)


class Turtle:
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    __mouth = '大嘴'

    def __init__(self, name): 
        # 构造方法，初始化实例对象的属性，self表示实例对象本身，name是一个参数，用于初始化实例对象的name1属性
        # 自动调用，创建实例对象时必须传入name参数，否则会报错
        self.name1 = name

    def climb(self):
        print("我%s会爬树了！" % self.name1)
    
    def run(self):
        print("我会跑了！")
    
turtle1 = Turtle("小猪") # 创建一个Turtle类的实例对象turtle1
print(turtle1.color) # 访问实例对象的属性
print(turtle1._Turtle__mouth) # 访问实例对象的私有属性，私有属性在类外部不能直接访问，但是可以通过 _类名__属性名 的方式访问
turtle1.climb() # 调用实例对象的方法
turtle1.run() # 调用实例对象的方法