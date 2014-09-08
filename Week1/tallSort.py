__author__ = 'Administrator'
## 기능 단위가 아니라 사람 단위로 함수를 나눠봤습니다.
## 제가 단 주석은 #이 두 개에요

## 태윤누나 코드
def start():
    myName=input("이름을 입력하세요.:")
    myTall=int(input("키를 입력하세요.:"))
    print("내 이름은" + myName + "이고," + "키는" + str(myTall) + "입니다")
    return [myName, myTall]

## 윤호 팀 코드 1
def sort(dic, myInfo):
    dic.sort(key= lambda obj: abs(myInfo[1]-obj['height']))
    print(myInfo[0]+"님의 키와 비슷한 순서대로 정렬하였습니다.")
    print(dic)
    return dic

## 은애 팀 코드
## cf. 딕셔너리로 입력 받는 방식이 어떤 차이를 지니는지 print(dic)으로 확인하고
## ',' 위치를 유심히 확인하세요.

def compareObj():
    #    listName = []   #입력 받을 이름 List
    #    listHeight = [] #입력 받을 키 List
    #    dic = {'이름':listName, '키':listHeight}
    inputNum = int(input("몇명의 키를 입력 하실건가요?"))
    ## 키는 정렬을 해야하기 때문에 인트값으로 형변환이 필요해요
    #일때 실행을 계속해
    inputNum = int(input("몇명의 키를 입력 하실건가요?"))
    dic = []
    for i in range(inputNum):
        inputName = input("이름을 입력해 주세요") #listA 에 사용자 입력값 추가
        inputHeight = int(input("키를 입력해 주세요"))
        dic.append({'name':inputName,'height':inputHeight})
#        listHeight.append(inputHeight)
#    for i in range(1):
    return dic

# 윤호 팀 코드 2
def main():
    myInfo = start()
    dic = compareObj()
    sort(dic, myInfo)

if __name__ == '__main__':
    main()