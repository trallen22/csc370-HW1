from random import random
from math import floor





y = [0, 0, 0, 0]

for i in range(100):
    x = floor(random() * 4)
    y[x] += 1
    
print(y)