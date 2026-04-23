class New_int(int):
    def __add__(self, other):
        return int(self) + int(other)

a = New_int(5)
b = New_int(3)
print(a + b) # 输出8，调用__add__方法，返回5+3
print(a.__add__(b))

print(type(a))
print(type(b))
print(type(a.__add__(b)))