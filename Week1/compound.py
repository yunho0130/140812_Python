__author__ = 'Administrator'
# ▷ 단리 : S = A(1+rn)
# ▷ 복리 : S = S+A(1+r)ⁿ
# ( S : 원리금 합계 / A : 원금 / r : 이자율 / n : 기간)

total = 0


def compound ():

    money = float(input("원금을 입력: "))
    rate = float(input("이자율 입력: "))
    period = float(input("기간을 입력: "))
    global total
    total += money * ((1 + rate) ** period)
    print(total)
    return total

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
        compound ()
        if myExit() == 1:
            break




if  __name__ == '__main__':
    main()