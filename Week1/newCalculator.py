__author__ = 'Administrator'

global totalNum
totalNum = []

def add(*nums):
    # 반복이 가능하다고 간주.
    # list도 던지면 된다.
    # 아스테리크는 파라미터 갯수를 여러개를 입력받을 때 사용한다.
    for val in nums:
        totalNum.append(nums)
        print(str(val)+"입력")
        print("현재까지 DB: "+str(totalNum))

def main():
    while True:
        add(input("입력해봐: "))


    """
    print('main')
    # add(1,2,3,4,6)
    listObj = list(range(1,100,2))
    add(listObj)
    tObj = (1,2,3,4,5)
    add(tObj)
    """

if __name__ == '__main__':
    main()
