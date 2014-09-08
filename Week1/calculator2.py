__author__ = 'BIT'
# global total
total=0

def add(value) :    #더하기 연산
    global total
    total = total + value
    return total

def sub(value) :    #빼기 연산
    global total
    total = total - value
    return total

def multiply(value) :   #곱하기 연산
    global total
    total = total * value
    return total

def divide(value) :     #나누기 연산
    global total
    total = total / value
    return total

def calculator():

        inputFunction = input("")   #기능:숫자로 입력
        print(inputFunction [0])
       # print(float(inputFunction [2:]))
        if inputFunction[0] == "A":
            total = add(float(inputFunction [2:]))
            print(float(inputFunction [2:]))
        elif inputFunction[0] == "S":
            total = sub(float(inputFunction [2:]))
            print(float(inputFunction [2:]))
        elif inputFunction[0] == "M":
            total = multiply(float(inputFunction [2:]))
            print(float(inputFunction [2:]))
        elif inputFunction[0] == "D":
            total = divide(float(inputFunction [2:]))
            print(float(inputFunction [2:]))
        elif inputFunction[0] == "T":
            global total
            print(total)
        elif inputFunction[0] == "X":
            return 1

def main(): #main 함수 정의하기

    print ("연산 할 기능과 숫자(기능:숫자)를 입력해 주세요(+:A, -:S, *:M, /:D, 총합:T, 종료:X)")

    while True :
        if calculator() == 1:
            break


if __name__ =='__main__':
    main()



"""
        elif inputFuntion == "S":
            inputNum = float(input("연산 할 수를 입력해 주세요"))
            total = sub(inputNum)

        elif inputFuntion == "M":
            inputNum = float(input("연산 할 수를 입력해 주세요"))
            total = multiply(inputNum)

        elif inputFuntion == "D":
            inputNum = float(input("연산 할 수를 입력해 주세요"))
            total = divide(inputNum)

        elif inputFuntion == "T":
            print("총합은", total, "입니다.")
"""