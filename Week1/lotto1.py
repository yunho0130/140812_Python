__author__ = 'Administrator'
# 로또를 만든다. 1.공을 뽑고 표본에서 지운다. 2.섞고shuffle 6개를 뽑아. 2.1. 데이터를 뽑아서 표본에서 지운다. 2.2. 데이터를 카피해서 뽑는다. 동전 프로그램이랑 결합. 거스름돈(과제) 리스트 데이터를 훼손하지 않고 6개 데이터를 추출. 뽑은 숫자가 정렬이 되어.
# 코드를 짤 때, 변하지 않는 것으로 짜야 정상.
# 로또 프로그램 함수형으로 바꾸는 것.
## 로또 일련번호를 생성. 가상의 서버와 통신.
## 가상의 서버에서 지난주 당첨번호를 받아와서

import random


def putTheBall():
    ballList = list(range(1, 45))
    random.shuffle(ballList)
    result = ballList[:6]
    result.sort()
    print(result)


def printResult(rest):
    print("거스름돈은 아래와 같습니다.")
    print(rest)


def calcRest(inputMoney, oneGame):
    global rest
    rest = inputMoney % oneGame
    return rest


def defaultSetting():
    global oneGame
    oneGame = 1000
    print("===== 비트 컴퓨터 로또 =====")
    print("한 게임은 "+str(int(oneGame))+"원 입니다.")
    global inputMoney
    inputMoney = int(input("금액을 입력해주세요: "))
    gameOpt = input("게임종류를 입력해주세요. 오토는 A를 수동은 M을 :  입력해주세요: ")
    gameNum = input("게임횟수를 입력해주세요: ")
    return [inputMoney, gameOpt]

def repeatCalc(gameOpt):
    if gameOpt == 'A':
        rest = calcRest(inputMoney, oneGame)
        autoGameNum = (inputMoney - rest) / oneGame
        print("자동으로 총"+str(int(autoGameNum))+"게임 진행합니다.")
        repeatNum = 0
        while repeatNum < autoGameNum:
            putTheBall()
            repeatNum += 1
        return rest
    else:
        print("자동으로 총"+str(int(gameOpt))+"게임 진행합니다.")
        rest = inputMoney - oneGame*int(gameOpt)
        for i in range(int(gameOpt)):
            putTheBall()
        return rest


def main():
    default = defaultSetting()
    rest = repeatCalc(default[1])
    printResult(rest)

if __name__ == '__main__':
    main()

