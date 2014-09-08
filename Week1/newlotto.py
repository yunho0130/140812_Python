__author__ = 'Ray Kang'
 
import random
 
class LottoBall:
 
    def __init__(self, num):
        self.num = num
 
class LottoMachine:
 
    def __init__(self, ballsNum = 45):
        self.ballList = []
        self.reset(ballsNum)
 
    def reset(self, ballsNum = 45):
        self.ballList.clear()
        for num in range(1, ballsNum):
            self.ballList.append(LottoBall(num))
 
    def selectLotto(self, count = 6):
 
        resultList = []
 
        for cnt in range(0,count):
            random.shuffle(self.ballList)
            resultList.append(self.ballList[0])
            del self.ballList[0]
 
        return resultList
 
    def selectMulti(self, selectCount = 1):
 
        totalList = []
 
        for cnt in range(0, selectCount):
            totalList.append(self.selectLotto())
            self.reset()
 
        return totalList
 
def main():
 
    machine = LottoMachine()
    #result = machine.selectLotto()
    #for ball in result:
    #    print(str(ball.num), end=",")
 
    totalResult = machine.selectMulti(3)
 
    for result in totalResult:
        for aResult in result:
            print(str( aResult.num ), end =",")
        print("\n----------")
 
 
 
if __name__ == '__main__':
    main()
