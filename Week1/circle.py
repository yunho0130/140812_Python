__author__ = 'Administrator'

# print(__name__)

def getArea(radius):
    area = radius * radius * math.pi
    return area

def main():
    print("main function")
    firstArea = getArea(10)
    secondArea = getArea(5)

if __name__ == '__main__':
    main()