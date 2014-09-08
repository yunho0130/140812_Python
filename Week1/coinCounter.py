__author__ = 'Administrator'
# 동전계산 프로그램 함수와 리스트를 사용해서 만들어보기.
# 리스트에 1000원권을 추가해도 코드의 수정이 필요 없을 것
# 100원짜리만 있을 때 다른 주화는 물어보지 않는 것. 입금할 주화를 선택. 총계.

"""
c10=10
c50=50
c100=100
c500=500
"""

# calcValue (10)
total = 0
coinValue = 0
coinTable = [10, 50, 100, 500,1000]
length = len(coinTable)

def multipleVal (coinValue, coinNum):
    return coinValue*coinNum

def choiceCoin ():
    choice = int(input("입금할 주화의 번호를 선택해주세요 \n 1. 10원 2. 50원 3. 100원 4. 500원 5. 1000원 \n"))
    if choice < 0:
        print("값을 잘못입력하셨습니다. 프로그램을 종료합니다.")

    elif choice > length:
        print("값을 잘못입력하셨습니다. 프로그램을 종료합니다.")

    else:
        coinNum = int(input("갯수를 입력해주세요: "))
        return multipleVal(coinTable[choice-1],coinNum)

def myExit ():
    print("종료하시겠습니까? 종료는 0번 계속은 1번을 입력하세요")
    power = int(input())
    if power == 0:
        print("종료하겠습니다 정산금액은 아래와 같습니다.")
        print(total)
        return 1
    else :
        print("계속하겠습니다")

def main():
    while True:
        global total
        total = total+ choiceCoin()
        if myExit() == 1:
            break



if __name__ == '__main__':
    main()

"""
while i<length

    total = total+ multipleVal(coinTable[i],coinNum)
    i += 1
    print (total)

choice = int(input("입금할 주화를 선택해주세요: "))
"""

"""
while True:
    total = total+ 1
    print("종료하시겠습니까? 종료는 0번을 입력하세요")
    power = int(input())
    if power == 0:
        print("종료하겠습니다")

        break
    else :
        print("계속하겠습니다")



# coin = [c10Num,c50Num,c100Num,c500Num]

c10Num=int(input("10원짜리의 개수를 입력"))
c50Num=int(input("50원짜리의 개수를 입력"))
c100Num=int(input("100원짜리의 개수를 입력"))
c500Num=int(input("500원짜리의 개수를 입력"))

total=((coinValue[0]*c10Num)+(coinValue[1]*c50Num)+(coinValue[2]*c100Num)+(coinValue[3]*c500Num))
print(total)
"""