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

# 列表从0开始计数，eggs[0]是第一个元素，eggs[1]是第二个元素，以此类推
eggs = [1, 2, [3,"随意"], 4, 5]
eggs.append(6) # 在列表末尾添加一个元素
print(eggs)
eggs.extend([7, 8, 9]) # 在列表末尾添加多个元素
print(eggs)
print(eggs[len(eggs) - 1])
print(eggs[-1]) # 负数索引，-1表示最后一个元素，-2表示倒数第二个元素，以此类推
print(eggs[0]) # 第一个元素
print(eggs[2][1]) # 第三个元素的第二个元素
eggs.remove(1) # 删除列表中的元素1
print(eggs)
eggs.pop(1) # 删除列表中的第二个位置元素
print(eggs)
eggs1 = eggs[2:5] # 切片，获取列表中的一部分，eggs[2:5]表示从第三个元素开始到第六个元素结束（不包括第六个元素）
print(eggs1)
eggs2 = eggs[:2] # 切片，获取列表中的一部分，eggs[:2]表示从第一个元素开始到第三个元素结束（不包括第三个元素）
print(eggs2)
eggs3 = eggs[2:] # 切片，获取列表中的一部分，eggs[2:]表示从第三个元素开始到最后一个元素结束
print(eggs3)
eggs4 = eggs[:] # 复制列表 
print(eggs4)
eggs5 = eggs[-2:] # 切片，获取列表中的一部分，eggs[-2:]表示从倒数第二个元素开始到最后一个元素结束
print(eggs5)
eggs6 = eggs[::-1] # 切片，-1表示倒叙，eggs[::1]表示从第一个元素开始到最后一个元素结束，步长为1，以此类推
print(eggs6)