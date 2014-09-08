__author__ = 'Administrator'

value1 = 0
power = 0
totalMoney = 0
temp = 0
total = 0


def addValue(totalMoney):

    value1 = int(input("금액의 증감을 입력하세요: "))
    totalMoney = totalMoney + value1
    print("총금액:"),
    print(totalMoney)
    return totalMoney
    # print("총금액:")
    # print(totalMoney)
    #      return totalMoney

while True:
    totalMoney= addValue(totalMoney)


    print("종료하시겠습니까? 종료는 0번을 입력하세요")
    power = int(input())
    if power == 0:
        print("종료하겠습니다")

        break
#    else :
    else :
        print("계속하겠습니다")








