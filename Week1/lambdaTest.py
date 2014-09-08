__author__ = 'Administrator'

import math

list = [1,3,2,5,6,3,9,4,0]

target = 5

list.sort(key= lambda x : math.fabs(x-target))

print(list)
