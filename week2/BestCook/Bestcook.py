#거리순서대로 출력
#음식점데이터에 리뷰데이터 추가/익명코멘트/self.reviewList 작성

__author__ = 'Administrator'

import math

class FoodStore :
    def __init__(self, name, menu, lat, lng, review = 0):
        self.name = name
        self.menu= menu
        self.lat= lat
        self.lng= lng
        self.review = []
        self.review = review

    def __str__(self):
        return self.name+":" +self.menu + ":"+str(self.lat) + ","+str(self.lng)

            # sortedStore.append(self.menu)
            # sortedStore.append(self.lat)
            # sortedStore.append(self.lng)

class BestCookService:

    def __init__(self):
        self.storeList = []
        self.storeList.append(FoodStore("평래옥", "냉면", 37.565267, 126.990344))
        self.storeList.append(FoodStore("동경식당", "우동", 37.565548, 126.993059))
        self.storeList.append(FoodStore("김가네", "우동", 37.565549, 126.993059))
        self.sortedStore = []

    def registFoodStore(self, newFoodStore):
        self.storeList.append(newFoodStore)

    def sortStore(self, menu1):
        for i in self.storeList:
            if i.menu == menu1:
                self.sortedStore.append(FoodStore(i.name, i.menu, i.lat, i.lng))
        self.sortByDistance(self.sortedStore)
        # for i2 in self.sortedStore:
        #     print(i2.name+":" +i2.menu + ":"+str(i2.lat) + ","+str(i2.lng))

    def calcDistance(self, lat, lng):
        # 솔로몬 빌딩
        basicLat = 37.564212
        basicLng = 126.991639
        result = math.sqrt(pow((basicLat - lat),2)+pow((basicLng - lng),2))
        return result

    def sortByDistance (self, distanceDataList):
        dic = {}
        for i in distanceDataList:
            # print(i)
            dicT = self.calcDistance(i.lat, i.lng)
            dic[dicT] = i
        keyList = list(dic.keys())
        keyList.sort()
        for i3 in keyList:
            print("거리: "+ str(i3))
            print(dic[i3])
        # return dic

    def createReview(self, YesOrNo):
        if (YesOrNo == '1'):
            self.review = Review()
            # self.review.displayReview()
                # for i in self.storeList
                #     i.review
            # self.service.storeList[4].append(self.review.userComments)
            # print(self.service.storeList[4])

    def selectCurrentNumber(self, currentNumber):
        cNum = currentNumber-1
        print(self.storeList[cNum])


class BestCookUI:

    def __init__(self):
        self.service = BestCookService()
        self.orderNum = 1
        self.testReviewList = []
        self.test2ReviewList = []
        self.currentNum = 0

    def registNewFoodStore(self):
        print("Name, Menu, lat, lng")
        name = input()
        menu = input()
        lat = float(input())
        lng = float(input())

        foodStore = FoodStore(name, menu, lat, lng)
        self.service.registFoodStore(foodStore)

    def findNearestFoodStore(self, lat, lng, list = None):
        min = 100
        nearestStore = None

        if list == None:
            targetList = self.storeList
        else:
            targetList = list

        for store in self.storeList:
            distance = math.sqrt(
                math.pow((lat - store.lat), 2) +
                math.pow((lng - store.lng), 2)
            )
            if min > distance:
                nearestStore = store
                min = distance
            return nearestStore


        """
        self.basicLat = 37.564567
        self.basicLng = 126.991545
        self.nearestDistance = math.sqrt(pow(lat - self.basicLat)+pow(lng -self.basicLng))
        """

    def showListAll(self):
        for store in self.service.storeList:
            print(str(self.orderNum)+"번", store)
            # print(store)
            self.orderNum += 1
        self.orderNum = 1

    def returnListAll(self):
       for store2 in self.service.storeList:
           return store2

    def showUsage(self):
        oper = input("1.등록 2. 전체 리스트 3. 메뉴검색 4. 거리순 정렬 5. 리뷰작성")
        if oper == '1':
            self.registNewFoodStore()
        elif oper == '2':
            self.showListAll()
            currentNum = int(input("정보를 보고싶은 리스트 번호를 입력하세요: "))
            self.service.selectCurrentNumber(currentNum)
            self.service.createReview(input("리뷰를 남기시려면 1을 입력: "))
            self.testReviewList.append(self.service.review.returnReview())
            for i in self.testReviewList:
                print("----------------" )
                print("작성자: "+i[0]+" 별점: "+i[2]+"\n Re: "+i[3])

        elif oper == '3':
            self.service.sortStore(input("메뉴검색: "))
        elif oper == '4':
            print("거리순으로 정렬했습니다.")
            self.service.sortByDistance(self.service.storeList)
 #            print(self.service.sortByDistance())
        elif oper == '5':
            self.service.createReview(input("리뷰를 남기시려면 1을 입력: "))

        print("=================")
        self.showUsage()
    # def service.FoodStore.__str__(self):
    #     self.service.storeList
    #     return self.name+":" +self.menu + ":"+str(self.lat) + ","+str(self.lng)

class Review:
    def __init__(self, starScore = 0 , userComments = None ):
        self.userID = input("아이디를 입력하세요: ")
        self.passWord = input("비밀번호를 입력하세요: ")
        self.starScore = input("별점을 입력하세요: ")
        self.userComments = input("덧글을 입력하세요: ")
        self.contentReview = []
        self.reviewList = []

    def returnReview(self):
        self.contentReview.append(self.userID)
        self.contentReview.append(self.passWord)
        self.contentReview.append(self.starScore)
        self.contentReview.append(self.userComments)
        return self.contentReview


    def displayReview(self):
        print("작성된 덧글 확인 === ")
        print("작성자: "+self.userID+" 별점: "+self.starScore+"\n 덧글내용 \n "+self.userComments)


def main():
    newUI = BestCookUI()
    newUI.showListAll()
    newUI.showUsage()
    # print("거리계산 테스트")
    # print(newUI.service.calcDistance(37.565267, 126.990344))

if __name__ == '__main__':
    main()