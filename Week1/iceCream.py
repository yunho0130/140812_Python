__author__ = 'Administrator'
# 1등 5000원 2등 3000원 3등은 심부름 해야하는 아이스크림 복불복게임.
# 조원들의 이름을 입력. 섞어.딕셔너리와 튜플, 딕셔너리와 리스트. 아이스크림 사는 프로그램. 딕셔너리를 이용. 이름과 결과를 담는다. 5명. 섞어요. 1등은 5천원 2등은 3천원 3등은 심부름. 절차지향으로 일단.
# 람다 식이라는 게 있다는 거. 아이스크림 만드는 프로그램에 적용.

import random

global totalPenalty
totalPenalty = []
global totalPerson
totalPerson = []
global dic
dic = []

def add(*nums):
    # 반복이 가능하다고 간주.
    # list도 던지면 된다.
    # 아스테리크는 파라미터 갯수를 여러개를 입력받을 때 사용한다.
    for val in nums:
        if val == 'X':
            print("종료합니다.")
            return
        if val == 'O':
            print("벌칙입력이 완료되었습니다.")
            print("벌칙은"+str(totalPenalty)+"입니다.")
            return 9
        totalPenalty.append(nums)
        print(str(val)+"입력")
        print("현재까지 DB: "+str(totalPenalty))

def add2(*nums):
    for val in nums:
        if val == 'X':
            print("종료합니다.")
            return
        if val == 'O':
            print("참가자 입력이 완료되었습니다.")
            print("참가자는"+str(totalPerson)+"입니다.")
            return 9
        if len(totalPenalty) > len(totalPerson):
            print("참가자 숫자가 적습니다. 참가자를 더 입력해주세요.")
            continue
        totalPerson.append(nums)
        print(str(val)+"입력")
        print("현재까지 DB: "+str(totalPerson))

def main():

    while True:
        condition = add(input("벌칙을 입력하세요. \n종료는 X, 입력완료는 O를 입력하세요: "))
        if condition == 9:
            break
    while True:
        condition2 = add2(input("참가자를 입력하세요. \n종료는 X, 입력완료는 O를 입력하세요: "))
        if condition2 == 9:
            break



"""
    for i in range(inputNum):
        inputName = input("이름을 입력해 주세요") #listA 에 사용자 입력값 추가
        inputHeight = int(input("키를 입력해 주세요"))
        dic.append({'name':inputName,'penalty':inputHeight})
"""

if __name__ == '__main__':
    main()
"""
personList=[] #List 생성
personList.append({'이름':'A', '결과':'O'}) # list에 Dic 넣기, Dic={}
personList.append({'이름':'B', '결과':'O'})
personList.append({'이름':'C', '결과':'O'})
personList.append({'이름':'D', '결과':'O'})
personList.append({'이름':'E', '결과':'O'})

target1=random.randint(0,100) % 5

personList[target1]['결과'] = 'X'

print(personList)
"""

"""
#  순서대로 나와서 엔터를 눌러. x가 나오면 당첨
target = random.randint(0,100) % 5

print(target)

list = ['o','o','o','o','o']

list[target] = 'x'

for item in list:
    input("당황하지 말고 enter")
    print(item)

"""