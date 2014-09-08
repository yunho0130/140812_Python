__author__ = 'Ray Kang'
 
import random
 
class Member:
 
    def __init__(self,name , money = 0):
        self.name = name
        self.money = money
 
class IcecreamSelector:
 
    def __init__(self):
        self.memberList  = []
 
    def addMember(self, member):
        self.memberList.append(member)
 
    def selectOne(self):
        print(self.memberList)
 
    def selectMoney(self, info):
        random.shuffle(self.memberList)
 
        num = 0
        for data in info:
            memberObj = self.memberList[num]
            memberObj.money = data
            num = num+1
 
    def printResult(self):
 
        for member in self.memberList:
            print(member.name +  "   :  "+ str(member.money))
 
 
 
 
 
def main():
 
    selector = IcecreamSelector()
    selector.addMember(Member("Kim"))
    selector.addMember(Member("Maegn"))
    selector.addMember(Member("Park"))
    selector.addMember(Member("Kim"))
    selector.addMember(Member("Park2"))
 
    moneyList = [3000, 2000, '심부름']
    selector.selectMoney(moneyList)
    selector.printResult()
 
 
 
 
 
if __name__ =='__main__':
    main()
