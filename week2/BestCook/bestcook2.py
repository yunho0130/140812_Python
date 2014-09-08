__author__ = 'Administrator'
__author__ = 'Administrator'

class FoodStore :
    def __init__(self,name, menu, lat, lng):
        self.name = name
        self.menu= menu
        self.lat= lat
        self.lng= lng

class BestCookService:

    def __init__(self):
        self.storeList = []

    def registFoodStore(self, newFoodStore):
        self.storeList.append(newFoodStore)

class BestCookUI:

    def __init__(self):
        self.service = BestCookService()

    def registNewFoodStore(self):
        print("Name, Menu, lat, lng")
        name = input()
        menu = input()
        lat = float(input())
        lng = float(input())

        foodStore = FoodStore(name,menu,lat,lng)
        self.service.registFoodStore(foodStore)


 def main():
     newUI = BestCookUI()
     newUI.registNewFoodStore()


 if __name__ =='__main__':
     main()