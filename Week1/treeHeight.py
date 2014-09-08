__author__ = 'Administrator'
import math
# a는 높이,
atreew = 150
# atreeh = atreew * 0.5317
print("math.tan((28/180.0)*math.pi)의 값 ")
print(math.tan((28/180.0)*math.pi))
atreeh = atreew * math.tan((28/180.0)*math.pi)
print("A나무의 높이")
print(atreeh+1.8)

btreew = 100
# btreeh = btreew * 0.6249
print("math.tan((32/180.0)*math.pi)의 값")
print(math.tan((32/180.0)*math.pi))
btreeh = btreew * math.tan((32/180.0)*math.pi)
print("B나무의 높이")
print(btreeh+1.8)

if atreeh > btreeh:
    print("A나무의 높이가 더 큽니다.")
if atreeh == btreeh:
    print("A나무와 B나무의 높이가 같습니다.")
# else:
if atreeh < btreeh:
    print("B나무의 높이가 더 큽니다.")
