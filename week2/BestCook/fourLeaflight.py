__author__ = 'Administrator'

import random
import copy

totalList = []
secondList = []
thirdList = []
tempList = []
firstFloor = []
secondFloor = []
thirdFloor = []
firthFloor = []
fifthFloor = []

global totalMoveNum
#주사위 갯수를 입력받아 몬스터가 가지고 있는 주사위 개수 생성

class Monster:

    def __init__(self, mNum=0, mFloor=0, mRow=0 ,dicNum=0):
        self.mNum =mNum         #몬스터 ID
        self.mFloor =mFloor     #몬스터 층위치
        self.mRow = mRow        #몬스터 열위치
        self.diceNum = dicNum   #몬스터가 가지고 있는 주사위 개수
        self.rollResult = 0
        self.totalMoveNum = 0   #총 이동주사위 던진횟수
        self.tempRow = 0
        self.tempFloor = 0
        self.tempValue = None
        self.dicResult = 0

    #몬스터 주사위 개수 초기화
    def countDiceNum(self, diceNum):
        self.dicNum = diceNum
        # self.dicNum = int(input("몬스터 주사위 개수를 입력해 주세요 \n"))
        # self.rollDie(self.dicNum)

    #주사위 개수 입력 받은만큼 늘리기
    def addDiceNum(self, diceNum):
        num= self.diceNum
        return num+diceNum

    def rollDie(self):
        for i in range(self.dicNum):
            roll = random.randint(1,6)
            self.rollResult += roll
        return self.rollResult

    # 전투 주사위
    def rollFightDice(self):
        for i in range(self.dicNum):
            roll = random.randint(1,6)
            self.rollResult += roll
        # print("전투 주사위를 굴렸습니다. 주사위 값: ")
        return self.rollResult

    def userFirstMove(self, map):
        dicResult = self.rollResult
        self.mRow += dicResult
        if self.mRow > 5:
            self.mRow -= 5
            self.mFloor += 1
        self.tempRow = self.mRow
        self.tempFloor = self.mFloor
        self.tempValue = map[self.tempFloor][self.tempRow]
        map[self.mFloor][self.mRow] = "[User]"

    def userMove(self, map):
        print("테스트")
        print(self.tempValue)
        map[self.mRow][self.mFloor] = self.tempValue
        dicResult = self.rollResult
        self.mRow += dicResult
        if self.mRow > 5:
            self.mRow -= 5
            self.mFloor += 1
        self.tempRow = self.mRow
        self.tempFloor = self.mFloor
        self.tempValue = map[self.tempFloor][self.tempRow]
        map[self.mFloor][self.mRow] = "[User2]"

        # 일반 주사위
    def rollMoveDice(self, dicNum):
        for i in range(dicNum):
            roll = random.randint(1,6)
            self.rollResult += roll
        # print("주사위를 굴렸습니다. 주사위 값: ")
        self.totalMoveNum += 1
        return self.rollResult

def copyMap(map):
    return map

def makeAList(i,list):
    tempList = range(i)
    for k in tempList:
        list.append('빈 칸')
    return list

def addAList(list1,list2):
    tempList = range(len(list1))
    for k in tempList:
        list1[k] = list2
    return list1

def printAList (list):
    countFloor = 1
    for i in list:
        print("----- 지하 "+str(countFloor)+" 층 -----")
        countFloor += 1
        print(i)

def blankMapData(firstFloor=firstFloor, secondFloor= secondFloor, thirdFloor=thirdFloor, firthFloor= firthFloor, fifthFloor=fifthFloor ):

    firstFloor = makeAList(5,firstFloor)
    secondFloor = makeAList(5,secondFloor)
    thirdFloor = makeAList(5,thirdFloor)
    firthFloor = makeAList(5,firthFloor)
    fifthFloor = makeAList(5,fifthFloor)
    totalList = [firstFloor, secondFloor, thirdFloor, firthFloor, fifthFloor]
    return totalList

def defaultMapSetting (map):
    # map[층][칸]
    map[4][1] = "[몬스터]" # 주사위 1개
    map[3][3] = "[몬스터]" # 주사위 1개
    map[2][3] = "[몬스터]" # 주사위 2개
    map[1][2] = "[몬스터]" # 주사위 2개
    map[0][1] = "[몬스터]" # 주사위 3개

    map[4][2] = "[사다리1]" # 이동장소: map[2][0]
    map[3][4] = "[사다리5]" # 이동장소: map[1][3]
    map[2][2] = "[사다리4]" # 이동장소: map[0][2]
    map[1][1] = "[사다리3]" # 이동장소: map[3][0]
    map[0][3] = "[사다리2]" # 이동장소: map[4][3]

    map[4][0] = '+1'
    map[3][2] = '+1'
    map[2][1] = '+2'
    map[2][4] = '-1'
    map[1][0] = '+2'
    map[1][4] = '-2'
    map[0][0] = '[시작]'
    map[4][4] = '[도착]'

    return map


# firstList = makeAList(4,firstList)
# secondList = makeAList(7,secondList)
# thirdList = addAList(firstList, secondList)
# firstList = [1,2,3]
# secondList = [1,2,3]
# print(thirdList)

# main 시작

print("===비트 던전에 오신것을 환영합니다 ===")

map = blankMapData()
defaultMapSetting(map)

#! printAList(map)
mon = Monster()  # 몬스터 생성
mon.countDiceNum(2) # 몬스터 주사위 갯수 설정
b= mon.rollFightDice() # 전투주사위 굴리기
# c = mon.rollMoveDice(2) # 이동주사위 굴리기
# d = mon.totalMoveNum # 총 주사위 굴린 횟수

mon1 = Monster()
mon1.countDiceNum(1)
mon2 = Monster()
mon2.countDiceNum(2)
mon3 = Monster()
mon3.countDiceNum(3)
user = Monster()
mon2.countDiceNum(1)

user.rollMoveDice(1)
user.userFirstMove(map)
printAList(map)
print("======")
user.rollMoveDice(1)
user.userMove(map)
printAList(map)
print("======")
user.rollMoveDice(1)
user.userMove(map)
printAList(map)


# map[4][1] = "[몬스터]" # 주사위 1개
# map[3][3] = "[몬스터]" # 주사위 1개
# map[2][3] = "[몬스터]" # 주사위 2개
# map[1][2] = "[몬스터]" # 주사위 2개
# map[0][1] = "[몬스터]" # 주사위 3개

# def __init__(self, mNum=0, mFloor=0, mRow=0 ,dicNum=0):
#     self.mNum =mNum         #몬스터 ID
#     self.mFloor =mFloor     #몬스터 층위치
#     self.mRow = mRow        #몬스터 열위치
#     self.diceNum = dicNum   #몬스터가 가지고 있는 주사위 개수
#     self.rollResult = 0
#     self.totalMoveNum = 0   #총 이동주사위 던진횟수