import numpy as np
import random
a = np.random.normal()
b = np.random.normal()
c = np.random.normal()
#y=2 * (x1) + (x2) + 3
rate = 0.001
x_train = np.array([    [1, 2],    [2, 1],    [2, 3],    [3, 5],    [1, 3],    [4, 2],    [7, 3],    [4, 5],    [11, 3],    [8, 7]    ])
y_train = np.array([7, 8, 10, 14, 8, 13, 20, 16, 28, 26])
x_test  = np.array([    [1, 4],    [2, 2],    [2, 5],    [5, 3],    [1, 5],    [4, 1]    ])
def h(x):
    return a*x[0]+b*x[1]+c

for i in range(10000):
    for x, y in zip(x_train, y_train):
#        flag = random.randint(0,1)
#        if flag > 0:

            a = a - rate * (h(x)-y) * x[0]
            b = b - rate * (h(x)-y) * x[1]
            c = c - rate * (h(x)-y)
            #print ("sum_a param: ", rate * (y-h(x)) * x[0])
            #print ("sum_b param: ", rate * (y-h(x)) * x[1])
            #print ("sum_c param: ", rate * (y-h(x)))
            #print ("current sum a,b,c: ",sum_a, sum_b, sum_c)
    
print("a =", a)
print("b =", b)
print("c =", c)

result = [h(xi) for xi in x_train]
print(result)

result = [h(xi) for xi in x_test]
print(result)
