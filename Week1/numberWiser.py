__author__ = 'Administrator'

import random

count = 1
min=1
max=100

while True:
    num=min+max
    num=num>>1
    print(num)
    print("정답입니까?")
    userResp=input("정답보다크면H, 정답보다 작으면L, 정답이면O 를 입력하세요")
#만일 정답이면 break
    if userResp=="H":
        min=num+1
        count += 1
    if userResp=="L":
        max=num-1
        count += 1
    if userResp=="O":
        print(str(count)+"번째 정답을 맞췄습니다.")
        break
    else:
        print("H,L,O 중 하나를 입력해 주세요")
"""


def getMidValue(min, max):
    num=min+max
    num=num>>1
    return num


def main():
    print("main function")
    num = getMidValue(1,100)
    print(getMidValue(1,100))
    print("정답입니까?")
    userResp=input("정답보다크면H, 정답보다 작으면L, 정답이면O 를 입력하세요")
#만일 정답이면 break
    while True:
        if userResp=='H':
            min=num+1
            getMidValue()
        if userResp=='L':
         max=num-1
        if userResp=='O':
            print("정답입니다.")
            break
        else:
            print("H,L,O 중 하나를 입력해 주세요")
            continue


if __name__ == '__main__':
    main()
    """