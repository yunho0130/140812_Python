__author__ = 'Administrator'

class TestUI:
    pass

# class TestProvider:
#
#     def getFirstQuiz(self):
#
#     pass

class Quiz:

    def __init__(self, question, options):
        self.question = question
        # self.answer = answer
        self.options = options
        # self.next = None
        self.nextYes = None
        self.nextNo = None
        self.next3 = None
        self.next4 = None

    # def setNext(self, nextQuiz):
    #     self.next = nextQuiz

    def setNextYes(self, nextQuiz1):
        self.nextYes = nextQuiz1

    def setNextNo(self, nextQuiz2):
        self.nextNo = nextQuiz2

    def setNext3(self, nextQuiz3):
        self.next3 = nextQuiz3

    def setNext4(self, nextQuiz4):
        self.next4 = nextQuiz4

    # def checkAnswer(self, userAnswer):
    #     if self.answer == userAnswer:
    #         return self.next
    def checkYesOrNo(self, userAnswer):
        if userAnswer == '1':
            return self.nextYes
        if userAnswer == '2':
            return self.nextNo
        if userAnswer == '3':
            return self.next3
        if userAnswer == '4':
            return self.next4

q0 = Quiz("당신의 혈액형을 입력하세요: ", ["1.A형","2.B형","3.AB형","4.O형"])
q1_1 = Quiz("시간 체크와 일정체크에 둔감해져 약속을 자꾸 잊어버린다.",["1.Yes", "2.No"])
q1_2 = Quiz("컴퓨터나 TV앞에 앉아 있는 시간이 부쩍 많아졌다.",["1.Yes", "2.No"])
q1_3 = Quiz("혼자서 할수있는 운동이나 문화 생활을 즐긴다.",["1.Yes", "2.No"])
q2_1 = Quiz("술자리나 모임이 잦고 사람들과 어울리는 자리를 찾는다.",["1.Yes", "2.No"])
q2_2 = Quiz("가끔씩 애인이 생기면 하고 싶은 일들을 생각해본다.",["1.Yes", "2.No"])
q2_3 = Quiz("연예인이나 드라마, 만화 속 주인공 등 비현실적인 인물에 열광하는 경우가 많다.",["1.Yes", "2.No"])
q3_1 = Quiz("심심한 겻을 견딜 수가 없고 혼자 있는 시간이 무료하다 못해 화가 난다.",["1.Yes", "2.No"])
q3_2 = Quiz("쇼핑으로 스트레스를 푸는 버릇이 생겼다.",["1.Yes", "2.No"])
q3_3 = Quiz("커플인 친구들이 부럽고 그 속에서 가끔 외로움을 느낀다.",["1.Yes", "2.No"])
q4_1 = Quiz("재미있는 일, 재미없는 일에 대한 구분이 모호해져 특별한 일을 계획하지 않는다.",["1.Yes", "2.No"])
q4_2 = Quiz("휴일이나 긴 휴가기간이 돌아오면 적극적으로 계획을 세운다.",["1.Yes", "2.No"])
q4_3 = Quiz("남의 연애담을 잘 들어주고 상담해주는 것을 좋아한다.",["1.Yes", "2.No"])
qEndA = Quiz("[A type] 러브지수 0~20% '평생 혼자 살 수도 있는 것 아냐?' 자포자기형" ,["1.종료", "2.다시"])
qEndB = Quiz("[B type] 러브지수 30~50% 사랑? 그게 뭔데! 겉으로만 천상천하 유아독존형",["1.종료", "2.다시"])
qEndC = Quiz("[C type] 러브지수 60~80% '거기 누구 없나요?' 킬리만자로의 표범형",["1.종료", "2.다시"])
qEndD = Quiz("[D type] 러브지수 90~100% '끓어오르는 피를 주체할 수 없어!' 활화산형",["1.종료", "2.다시"])

q0.setNextYes(q1_1)
q0.setNextNo(q2_1)
q0.setNext3(q3_1)
q0.setNext4(q4_1)
q1_1.setNextYes(q1_2)
q1_1.setNextNo(q2_2)
q1_2.setNextYes(q1_3)
q1_2.setNextNo(q2_3)
q1_3.setNextYes(qEndA)
q1_3.setNextNo(q2_3)
q2_1.setNextYes(q1_1)
q2_1.setNextNo(q2_2)
q2_2.setNextYes(q3_2)
q2_2.setNextNo(q2_3)
q2_3.setNextYes(q3_3)
q2_3.setNextNo(qEndB)
q3_1.setNextYes(q4_1)
q3_1.setNextNo(q3_2)
q3_2.setNextYes(q3_3)
q3_2.setNextNo(q2_3)
q3_3.setNextYes(qEndC)
q3_3.setNextNo(qEndB)
q4_1.setNextYes(q3_2)
q4_1.setNextNo(q4_2)
q4_2.setNextYes(q4_3)
q4_2.setNextNo(q3_3)
q4_3.setNextYes(qEndD)
q4_3.setNextNo(q3_3)
qEndA.setNextNo(q0)
qEndB.setNextNo(q0)
qEndC.setNextNo(q0)
qEndD.setNextNo(q0)



print("========================")

quiz = q0

while True:
    print(quiz.question)
    print(quiz.options)
    userAnswer = input("선택지 번호를 입력하세요: ")
    quiz = quiz.checkYesOrNo(userAnswer)
    if quiz == None:
        print("테스트를 종료합니다. 수고하셨습니다.")
        break

        # quiz = quiz.checkAnswer(userAnswer)
        #
        # if quiz == None:
        #     print("탈락!")
        #     break