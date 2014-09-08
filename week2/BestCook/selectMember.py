__author__ = 'Administrator'

import random
import pickle



#
# 비트58기_이판호   010-6530-5168
# 비트58기_오지선   010-3220-0362
# 비트58기_오가현   010-4907-1311
# 비트58기_김은애   010-8880-7298
# 비트58기_김동혁   010-2357-0709
# 비트58기_황명화   010-2397-0916
# 비트58기_김윤형   010-9522-3689
# 비트58기_박상호   010-9689-2741
# 비트58기_서준형   010-6292-1260
# 비트58기_김진영(청각장애-문자연락부탁드려요)   010-7774-1186
# 비트58기_최명진   010-3862-0623
# 비트58기_임성민   010-6228-2851
# 비트58기_김인수   010-3330-6701
# 비트58기_모종현   010-4935-3595
# 비트58기_박봉재   010-8920-5140
# 비트58기_박태은   010-9268-9860
# 비트58기_김태윤   010-7308-3321
# 비트58기_심후섭   010-4252-1741
# # 비트58기_양동훈   010-2189-8995
# 비트58기_맹윤호   010-2815-9190
# # 비트_송승환 과장님   010-8912-8086
# 박준일

mem1 = '박봉재'
mem2 = '김은애'
mem3 = '김태윤'
mem4 = '박상호'
mem5 = '맹윤호'
mem6 = '모종현'
mem7 = '오가현'
mem8 = '임성민'
mem9 = '이판호'
mem10 = '김인수'
mem11 = '박준일'
mem12 = '황명화'
mem13 = '김진영'
mem14 = '서준형'
mem15 = '심후섭'
mem16 = '오지선'
mem17 = '김동혁'
mem18 = '최명진'
mem19 = '박태은'
mem20 = '김윤형'
shuffleList2 = []
# memList = [mem1,mem2,mem3,mem4,mem5,mem6,mem7,mem8,mem9,mem10,mem11,mem12,mem13,mem14,mem15,mem16,mem17,mem18,mem19,mem20]
#
# shuffleList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

memList1 =[mem1,mem2,mem3,mem4,mem5]
memList2 =[mem6,mem7,mem8,mem9,mem10]
memList3 =[mem11,mem12,mem13,mem14,mem15]
memList4 =[mem16,mem17,mem18,mem19,mem20]
###
##newfile1 = open("group1.txt", 'rb')
##memList1 = pickle.load(newfile1)
#
# newfile2 = open("group2.txt", 'rb')
# memList2 = pickle.load(newfile2)
#
# newfile3 = open("group3.txt", 'rb')
# memList3 = pickle.load(newfile3)
#
# newfile4 = open("group4.txt", 'rb')
# memList4 = pickle.load(newfile4)
# ###

print("피클링 호출완료")


print("=== 자바 58기 고급자 과정 조원 편성기 ===")
print("<멤버리스트>")
print("1조")
print(memList1)
print("2조")
print(memList2)
print("3조")
print(memList3)
print("4조")
print(memList4)
input("Enter를 입력하면 조를 편성")



random.shuffle(memList1)
random.shuffle(memList2)
random.shuffle(memList3)
random.shuffle(memList4)
print("섞었습니다.")
print(memList1)
print(memList2)
print(memList3)
print(memList4)

newMemlist1 = []
newMemlist2 = []
newMemlist3 = []
newMemlist4 = []
newPickleList = []
# for i in range(4):
#     newMemlist1.append(memList1[i])
# newMemlist1.append(memList1[4])
# for i in range(4):
#     newMemlist2.append(memList2[i])
# newMemlist2.append(memList2[4])
# for i in range(4):
#     newMemlist3.append(memList3[i])
# newMemlist3.append(memList3[4])
# for i in range(4):
#     newMemlist4.append(memList4[i])
# newMemlist4.append(memList4[4])

#
#
newMemlist1 = [memList1[4], memList1[0], memList2[0], memList3[0], memList4[0]]
newMemlist2 = [memList2[4], memList1[1], memList2[1], memList3[1], memList4[1]]
newMemlist3 = [memList3[4], memList1[2], memList2[2], memList3[2], memList4[2]]
newMemlist4 = [memList4[4], memList1[3], memList2[3], memList3[3], memList4[3]]
print("조원간의 중복을 최소화 하여 조를 분배합니다.")

print("=== 자바 58기 고급자 과정 조원 편성기 ===")
print("<멤버리스트>")
print("1조")
print(newMemlist1)
print("2조")
print(newMemlist2)
print("3조")
print(newMemlist3)
print("4조")
print(newMemlist4)
print("조별활동 하면서 열공하세요 ^-^*")

input("조편성 결과를 저장하시려면 Enter를 눌러주세요. ")

file1 = open("group1.txt",'wb')
pickle.dump(newMemlist1, file1)
file1.close()

file2 = open("group2.txt",'wb')
pickle.dump(newMemlist2, file2)
file2.close()

file3 = open("group3.txt",'wb')
pickle.dump(newMemlist3, file3)
file3.close()

file4 = open("group4.txt",'wb')
pickle.dump(newMemlist4, file4)
file4.close()


print("피클링 저장완료")





# >>> import pickle
# >>> f = open("test.txt", 'wb')
# >>> data = {1: 'python', 2: 'you need'}
# >>> pickle.dump(data, f)
# >>> f.close()
# pickle.dump에 의해 저장된 파일을 열어 원래 있던 딕셔너리 객체(data)를 그대로 가져오는 전형적인 예이다.
#
# >>> import pickle
# >>> f = open("test.txt", 'rb')
# >>> data = pickle.load(f)
# >>> print(data)