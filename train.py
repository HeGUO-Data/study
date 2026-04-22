try:
    # 可能会引发异常的代码
    result = 10 / 0
except ZeroDivisionError as e:
    # 处理异常的代码
    print("发生了零除错误：", e)
else:
    # 没有发生异常时执行的代码
    print("结果是：", result)