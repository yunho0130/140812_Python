__author__ = 'Administrator'

import random

#  순서대로 나와서 엔터를 눌러. x가 나오면 당첨
target = random.randint(0,100) % 5

print(target)

list = ['o','o','o','o','o']

list[target] = 'x'

for item in list:
    input("당황하지 말고 enter")
    print(item)