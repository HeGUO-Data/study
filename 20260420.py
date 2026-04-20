import random
print("欢迎来到猜数字游戏！")

secret = random.randint(1, 10)
temp = input("猜一下心中的数字：")
guess = int(temp)
times = 1

while (guess != secret) and (times < 3):
    if guess > secret:
        print("哥，大了大了~~")
    else:        
        print("哥，小了小了~~")
    temp = input("请再试试吧：")
    guess = int(temp)
    times += 1
if (guess == secret) and (times <= 3):
    print("猜对了，游戏结束，不玩了！")
else:
    print("哥，三次机会用完了，游戏结束，不玩了！")