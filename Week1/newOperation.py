__author__ = 'Administrator'


num1 = int (input("첫 번째 숫자를 입력하세요:"))
num2 = int (input("두 번째 숫자를 입력하세요:"))
total = 0
# num1 = 5, num2 = 2 => 5+ 6
i = 0
while i < num2 :
    total = total + num1 + i
    i = i+1

print ("토탈값:")
print (total)




