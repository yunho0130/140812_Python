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

# global totalMoveNum
# totalMoveNum = 1
#주사위 갯수를 입력받아 몬스터가 가지고 있는 주사위 개수 생성

class Monster:

    def __init__(self, mNum=0, mFloor=0, mRow=0 ,dicNum=0):
        self.mNum =mNum         #몬스터 ID
        self.mFloor =mFloor     #몬스터 층위치
        self.mRow = mRow        #몬스터 열위치
        # self.diceNum = dicNum   #몬스터가 가지고 있는 주사위 개수
        self.rollResult = 0
        self.totalMoveNum = 1   #총 이동주사위 던진횟수
        self.tempRow = 0
        self.tempFloor = 0
        self.tempValue = None
        self.myDicNum = 1
        self.monDicNum = 1
        self.tempList2 = []
    #몬스터 주사위 개수 초기화
    def countDiceNum(self, diceNum):
        self.dicNum = diceNum
        # self.dicNum = int(input("몬스터 주사위 개수를 입력해 주세요 \n"))
        # self.rollDie(self.dicNum)
    #주사위 개수 입력 받은만큼 늘리기
    def addDiceNum(self, diceNum):
        num= self.diceNum
        return num+diceNum
    def rollFightDice(self, diceNum1):
        self.rollResult = 0
        for i in range(diceNum1):
            self.roll = [1,2,3,4,5,6]
            random.shuffle(self.roll)
            self.rollValue = self.roll[0]
            self.rollResult += self.rollValue
        # print("전투 주사위를 굴렸습니다. 주사위 값: ")
        return self.rollResult

class User(Monster) :

    def userMove(self, map):
        map[self.mFloor][self.mRow] = self.tempValue
        self.diceValue1 = self.rollMoveDice()
        print(str(self.diceValue1)+" 나왔습니다.")
        dicResult = self.rollResult
        self.mRow += dicResult
        if self.mRow > 4:
            self.mRow -= 5
            self.mFloor += 1
            if self.mRow > 4:
                self.mRow -= 5
                self.mFloor += 1
        self.ready()
        self.readyTwo()
        if self.mFloor == 5:
            self.lastFight()
            return
        self.tempFloor = self.mFloor
        self.tempRow = self.mRow
        self.tempValue = map[self.tempFloor][self.tempRow]
        map[self.mFloor][self.mRow]="★"
        self.totalMoveNum += 1
        return self.mFloor,self.mRow

    def setGameLevel(self):
        self.gameLevel = 1
        self.gameLevel = int(input("====난이도를 선택하세요==== \n 0. 쉬움, 1. 보통, 2. 어려움 : "))

    def startFight(self):
        print("몬스터를 만났습니다.")
        input("Enter를 누르면 전투용 주사위를 굴립니다.")
        print("2 개의 주사위를 내가 던진 값: ")
        self.temp1 = self.rollFightDice(2)
        print(self.temp1)
        self.resultLevel1 = 2+self.gameLevel-1
        print(str(self.resultLevel1)+" 개의 주사위를 몬스터가 던진 값: ")
        self.temp2 = self.rollFightDice(self.resultLevel1)
        print(self.temp2)
        if self.temp2 >= self.temp1:
            print("전투에서 패배했습니다. 처음으로갑니다.")
            self.mRow = 0
            self.mFloor = 0
            return 0
            # map[self.mFloor, self.mRow] = '시 작'
        else:
            print("전투에서 승리했습니다.")
            return 1

    def lastFight(self):
        print("보스몬스터를 만났습니다.")
        input("Enter를 누르면 전투용 주사위를 굴립니다.")
        print("2 개의 주사위를 내가 던진 값: ")
        self.temp1 = self.rollFightDice(2)
        print(self.temp1)
        self.resultLevel2 = 2+self.gameLevel
        print(str(self.resultLevel2)+" 개의 주사위를 보스 몬스터가 던진 값: ")
        self.temp2 = self.rollFightDice(self.resultLevel2)
        print(self.temp2)
        if self.temp2 >= self.temp1:
            print("전투에서 패배했습니다. 처음으로 되돌아갑니다.")
            self.setGameLevel()
            self.mRow = 0
            self.mFloor = 0
            return 0
            # map[self.mFloor, self.mRow] = '시 작'
        else:
            print("축하합니다. 마지막 전투에서 승리했습니다.")
            if self.gameLevel == 0:
                print("당신은 쉬움 난이도를 클리어했습니다.")
            if self.gameLevel == 1:
                print("당신은 보통 난이도를 클리어했습니다.")
            if self.gameLevel == 2:
                print("당신은 어려움 난이도를 클리어했습니다.")
            print("종료 되었습니다. 당신은 "+str(self.totalMoveNum)+"번 주사위를 던졌습니다.")
            input("(난이도가 어려울 수록, 주사위 횟수가 적을수록 승리)")
            return 1

    def changeLocation(self, floor, row):
        self.mFloor = int(floor)
        self.mRow = int(row)
        print("!!! 순간이동을 했습니다. !!! ")
        return self.mFloor, self.mRow

    def ready(self):
        if self.mFloor == 0:
            if self.mRow == 1:
                self.startFight()
            else:
                return

        if self.mFloor == 1:
            if self.mRow == 2:
                self.startFight()
            else:
                return

        if self.mFloor == 2:
            if self.mRow == 3:
                self.startFight()
            else:
                return

        if self.mFloor == 3:
            if self.mRow == 3:
                self.startFight()
            else:
                return

        if self.mFloor == 4:
            if self.mRow == 1:
                self.startFight()
            else:
                return
        else:
            return

    def readyTwo(self):
        if self.mFloor == 4:
            if self.mRow == 2:
                self.changeLocation(2,0)
            else:
                return

        if self.mFloor == 3:
            if self.mRow == 4:
                self.changeLocation(1,3)
            else:
                return

        if self.mFloor == 2:
            if self.mRow == 2:
                self.changeLocation(0,2)
            else:
                return

        if self.mFloor == 1:
            if self.mRow == 1:
                self.changeLocation(3,0)
            else:
                return

        if self.mFloor == 0:
            if self.mRow == 3:
                self.changeLocation(4,3)
            else:
                return
        else:
            return

            #        일반 주사위
    def rollMoveDice(self):
        self.roll = [1,2,3,4,5,6]
        random.shuffle(self.roll)
        self.rollValue2 = self.roll[0]
        self.rollResult = self.rollValue2
        # print("주사위를 굴렸습니다. 주사위 값: ")
        self.totalMoveNum += 1
        return self.rollResult
#
# class Location(User):
#
#     def __init__(self, map , mFloor2, mRow2 ):
#         self.mFloor = mFloor2
#         self.mRow = mRow2
#         self.map = map
#
#     def setLocation(self, location, user):
#         # map[user.mFloor][user.mRow] = self.tempValue
#         user.mFloor = location.mFloor
#         user.mRow = location.mRow
#         print("순간이동을 했습니다.")
#         self.tempValue = map[user.mFloor][user.mRow]
#         map[user.mFloor][user.mRow] = "[User]"
#
#     def getLocation(self):
#         return map[self.mFloor][self.mRow]

# lo1_2 = lo1_2.setLocation(lo2_4) 이런걸 하고 싶다.

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
    return list
def blankMapData(firstFloor=firstFloor, secondFloor= secondFloor, thirdFloor=thirdFloor, firthFloor= firthFloor, fifthFloor=fifthFloor ):

    firstFloor = makeAList(5,firstFloor)
    random.shuffle(firstFloor)
    secondFloor = makeAList(5,secondFloor)
    random.shuffle(secondFloor)
    thirdFloor = makeAList(5,thirdFloor)
    random.shuffle(thirdFloor)
    firthFloor = makeAList(5,firthFloor)
    random.shuffle(firthFloor)
    fifthFloor = makeAList(5,fifthFloor)
    random.shuffle(fifthFloor)
    totalList = [firstFloor, secondFloor, thirdFloor, firthFloor, fifthFloor]
    return totalList

def defaultMapSetting (map):
    # map[층][칸]
    map[4][1] = "몬스터" # 주사위 1개
    map[3][3] = "몬스터" # 주사위 1개
    map[2][3] = "몬스터" # 주사위 2개
    map[1][2] = "몬스터" # 주사위 2개
    map[0][1] = "몬스터" # 주사위 3개

    map[4][2] = "워프 1" # 이동장소: map[2][0]
    map[3][4] = "워프 5" # 이동장소: map[1][3]
    map[2][2] = "워프 4" # 이동장소: map[0][2]
    map[1][1] = "워프 3" # 이동장소: map[3][0]
    map[0][3] = "워프 2" # 이동장소: map[4][3]

    # map[4][0] = '+1'
    # map[3][2] = '+1'
    # map[2][1] = '+2'
    # map[2][4] = '-1'
    # map[1][0] = '+2'
    # map[1][4] = '-2'
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
printAList(map)
mon = Monster()  # 몬스터 생성
mon.countDiceNum(1) # 몬스터 주사위 갯수 설정
mon1 = Monster()
mon2 = Monster()
mon3 = Monster()
user = User()
user.setGameLevel()
# user.userFirstMove(map)
# printAList(map)
# print("----")
while True:
    input("Enter를 누르면 주사위를 굴립니다.")
    user.userMove(map)
    printAList(map)
    print("----")

