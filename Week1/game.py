__author__ = 'Administrator'

import random

class Member:
    def __init__(self, name, money = 0):
    # __init__ 클래스 초기값 설정.
    # 반드시 name과 money를 가지게 하고 싶다.
    # 0은 줘도 되고 안줘도 되는 값이 되었다.
        self.name = name
        self.money = money

class IcecreamSelector:

    def __init__(self):
        self.memberList = []

    def addMember(self, member):
        self.memberList.append(member)

    def printMember(self):
        print(self.memberList)

    # def selectOne(self):
    #     random.shuffle(self.memberList)
    #     return self.memberList

    def selectMoney(self, info):
        random.shuffle(self.memberList)
        num = 0
        for choice in info:
            memberObj = self.memberList[num]
            memberObj.money = data

    def printResult(self):
        for member in self.memberList:
            print(member.name + str(member.money))

def main():
    selector = IcecreamSelector()
    for i in range(5):
        selector.addMember(input("멤버를 입력하세요:"))
    selector.printMember()
    # one = selector.selectOne()
    # print("당첨!!")
    # print(one[0])
    selector.printResult()


if __name__ == '__main__':
    main()



# obj1.name = 'Hong gil dong'
# obj1['name'] = "Kim"

# print(obj1.name)