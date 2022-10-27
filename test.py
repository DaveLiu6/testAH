import numpy as np
import torch

num1 = np.ones(9).reshape(3, 3)
print(num1)
num2 = np.ones(16).reshape(4, 4)
print(num2)

n1 = num1.flatten()
n2 = num2.flatten()
print(n1)
print(n2)

count = 0
for i in range(len(n1)):
       if n1[i] == n2[i]:
              count += 1
print(count)



