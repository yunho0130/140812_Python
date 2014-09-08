__author__ = 'Administrator'

import math

#person = [국어, 영어, 수학, 과학, 선택]
person1 = [74, 65, 82, 79, '이공계']
person2 = [83, 77, 65, 64, '인문계']
person3 = [93, 92, 91, 89, '이공계']
person4 = [91, 56, 51, 65, '인문계']
person5 = [89, 86, 64, 54, '인문계']
person6 = [90, 76, 53, 56, '인문계']


myScore = []
myScoreAnalysis1 = []
myScoreAnalysis2 = []
myScoreAnalysis3 = []
myScoreAnalysis4 = []
myScoreAnalysis5 = []
myScoreAnalysis6 = []

myScoreResult1 = 0
myScoreResult2 = 0
myScoreResult3 = 0
myScoreResult4 = 0
myScoreResult5 = 0
myScoreResult6 = 0

myResultList = []

myScore.append(int(input("국어점수입력: ")))
myScore.append(int(input("영어점수입력: ")))
myScore.append(int(input("수학점수입력: ")))
myScore.append(int(input("과학점수입력: ")))

print("내가 입력한 값")
print(myScore)

for i in range(4):
    myScoreAnalysis1.append(pow((person1[i]-myScore[i]),2))
    myScoreAnalysis2.append(pow((person2[i]-myScore[i]),2))
    myScoreAnalysis3.append(pow((person3[i]-myScore[i]),2))
    myScoreAnalysis4.append(pow((person4[i]-myScore[i]),2))
    myScoreAnalysis5.append(pow((person5[i]-myScore[i]),2))
    myScoreAnalysis6.append(pow((person6[i]-myScore[i]),2))

print("내 점수와 각 과목이 얼마나 떨어져 있는지")
print(myScoreAnalysis1)
print(myScoreAnalysis2)
print(myScoreAnalysis3)
print(myScoreAnalysis4)
print(myScoreAnalysis5)
print(myScoreAnalysis6)

for i in range(4):
    myScoreResult1 += myScoreAnalysis1[i]
    myScoreResult2 += myScoreAnalysis2[i]
    myScoreResult3 += myScoreAnalysis3[i]
    myScoreResult4 += myScoreAnalysis4[i]
    myScoreResult5 += myScoreAnalysis5[i]
    myScoreResult6 += myScoreAnalysis6[i]

print("내 점수와 각 과목이 얼마나 떨어져 있는지에 대한 합")

print(myScoreResult1)
print(myScoreResult2)
print(myScoreResult3)
print(myScoreResult4)
print(myScoreResult5)
print(myScoreResult6)

newScoreList = []

newScoreList.append(myScoreResult1)
newScoreList.append(myScoreResult2)
newScoreList.append(myScoreResult3)
newScoreList.append(myScoreResult4)
newScoreList.append(myScoreResult5)
newScoreList.append(myScoreResult6)

newScoreList2 = []

newScoreList2.append(myScoreResult1)
newScoreList2.append(myScoreResult2)
newScoreList2.append(myScoreResult3)
newScoreList2.append(myScoreResult4)
newScoreList2.append(myScoreResult5)
newScoreList2.append(myScoreResult6)


print(newScoreList)
newScoreList2.sort()
print(newScoreList2)

indexNum1 = 9
indexNum2 = 9
indexNum3 = 9

for k in range(6):
    if newScoreList2[0] == newScoreList[k]:
        indexNum1 = k
    elif newScoreList2[1] == newScoreList[k]:
        indexNum2 = k
    elif newScoreList2[2] == newScoreList[k]:
        indexNum3 = k



print(indexNum1)
print(indexNum2)
print(indexNum3)

Result1 = None
Result2 = None
Result3 = None

# person1 = [74, 65, 82, 79, '이공계']
# person2 = [83, 77, 65, 64, '인문계']
# person3 = [93, 92, 91, 89, '이공계']
# person4 = [91, 56, 51, 65, '인문계']
# person5 = [89, 86, 64, 54, '인문계']
# person6 = [90, 76, 53, 56, '인문계']

if indexNum1 == 0:
    Result1 = '이공계'
if indexNum1 == 1:
    Result1 = '인문계'
if indexNum1 == 2:
    Result1 = '이공계'
if indexNum1 == 3:
    Result1 = '인문계'
if indexNum1 == 4:
    Result1 = '인문계'
if indexNum1 == 5:
    Result1 = '인문계'

if indexNum2 == 0:
    Result2 = '이공계'
if indexNum2 == 1:
    Result2 = '인문계'
if indexNum2 == 2:
    Result2 = '이공계'
if indexNum2 == 3:
    Result2 = '인문계'
if indexNum2 == 4:
    Result2 = '인문계'
if indexNum2 == 5:
    Result2 = '인문계'

if indexNum3 == 0:
    Result3 = '이공계'
if indexNum3 == 1:
    Result3 = '인문계'
if indexNum3 == 2:
    Result3 = '이공계'
if indexNum3 == 3:
    Result3 = '인문계'
if indexNum3 == 4:
    Result3 = '인문계'
if indexNum3 == 5:
    Result3 = '인문계'

finalResultList = [Result1, Result2, Result3]

if finalResultList.count('이공계') == 0:
    print("당신은 인문계 입니다.")
if finalResultList.count('이공계') == 1:
    print("당신은 인문계 입니다.")
if finalResultList.count('이공계') == 2:
    print("당신은 이공계 입니다.")


#
#
#
#
#
#
#
#
# myDicResult[myScoreResult1] = person1[4]
# myDicResult[myScoreResult2] = person2[4]
# myDicResult[myScoreResult3] = person3[4]
# myDicResult[myScoreResult4] = person4[4]
# myDicResult[myScoreResult5] = person5[4]
# myDicResult[myScoreResult6] = person6[4]
#
# print(myDicResult)
#
#

#
# myResultList = [myScoreResult1, myScoreResult2, myScoreResult3, myScoreResult4, myScoreResult5, myScoreResult6]
#
#


