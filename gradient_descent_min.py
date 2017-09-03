import numpy as np

#用梯度下降求解目标函数的最小值
#y = (x-3)^2 +3
rate = 0.001
count = 0
max_times = 10000

def target_func(x):

    y = np.square(x - 3) + 3
    return y

f_change = 1
f_current = 10
x = 2

while count < max_times:
    x = x - rate * 2 * (x-3)
    print (count, "training-----current x is: ",x)
    count = count + 1

# 大约提供17位有效数字
print (x, target_func(x))
