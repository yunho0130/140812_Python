__author__ = 'Administrator'
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

    def setNext(self, nextQuiz):
        self.next = nextQuiz

    def setNextYes(self, nextQuiz1):
        self.nextYes = nextQuiz1

    def setNextNo(self, nextQuiz2):
        self.nextNo = nextQuiz2

    def setNext3(self, nextQuiz3):
        self.next3 = nextQuiz3

    def setNext4(self, nextQuiz4):
        self.next4= nextQuiz4

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
qEndB = Quiz("[B type] 러브지수 30~50% 사랑? 그게 뭔데! 겉으로만 천상천하 유아독존형 언젠가는 누군가를 만날 것 같다는 확신이 있지만 현재 연인의 부재에 약간은 불안하고 외로운 당신. 주위에서 소개팅이라도 주선할라치면 만나볼까? 귀찮아! 사이에서 고민한다. 커플을 부러워하는 경우가 종종 있으며 가끔 커플들 사이에서 소외감을 느끼기도 한다. 하지만 자신이 좋아하는 일에 집중하면 모든 근심걱정이 사라지므로 몸을 힘들게 만들려고 노력하는 형이다. 누군가를 만나고 싶은 욕심은 있지만 언젠가는 자신에게 맞는 상대가 저절로 나타날 것이라는 허황된 꿈을 안고 사는 덕에 웬만한 남자는 눈에 차지 않는다. 사람을 만날 때 이것저것 따지는 것이 많고 사랑 앞에 강한 척하는 것이 특징이다. 한마디로 속 다르고 겉 다른 형. 이런 유형의 사람들에게 가장 위험한 것은 자포자기로 발전할 가능성은 크다. 가장 먼저 해야 할 일은 자신에게 맞는 상대가 어떤지 체크해보는 것. 내가 만나고 싶은 남자 정말 기피하고 싶은 남자 남자를 볼 때 가장 중요하게 생각하는 것 현재 주위에 있는 사람들에 대한 호감도 등 연애를 하기 위한 준비를 꼼꼼히 해본다. 여행지나 놀거리를 살피며 남자친구와 하고 싶은 일들을 생각해보는 것도 러브지수를 충만하게 해줄 수 있는 좋은 방법이다. 누군가가 옆에 있었으면 좋겠다는 인식은 충분히 하고 있는 상태이므로 조금만 불을 지펴주면 다음부터는 일사천리로 진행된다. 이런 사람들이 사랑하는 사람을 만나면 가장 성실하고 오래간다.",["1.종료", "2.다시"])
qEndC = Quiz("[C type] 러브지수 60~80% '거기 누구 없나요?' 킬리만자로의 표범형 러브필이 충만한 당신. 누군가가 옆에 있었으면 하는 생각을 수시로 하며 길거리를 지나다 괜찮은 남자를 보면 눈을 떼지 못한다. 못 먹는 감이라도 어떻게 안 될까 호시탐탐 노리기도 하지만 생각에 그치는 것이 어찌 보면 다행. 남의 연애담 듣기를 좋아하며 내가 이 상황이라면 이렇게 했을 것이라는 충고에 열 올리기도 한다. 하지만 정작 자신은 내실이 없다. 이렇게 러브필이 충만한데도 결실이 없는 사람들의 가장 큰 문제는 이리 재고 저리 재는 버릇이다. 처음 소개받을 때는 '이러면 어떻고 저러면 어떠니'라고 말하면서도 '아무나 만날 순 없잖아'를 입버릇처럼 내뱉으며 사람을 내치는 나쁜 습성도 있다. 영혼이 통하는 사람, 혹은 조건이 딱 맞는 사람을 원하는 통에 시작도 해보기 전에 지레 안 된다고 결단 내리는 경우가 많다. 혹은 반대로 상대방이 마음에 들어도 자신을 내 보이길 쑥스러워 하는 경우가 있다. 이런 유형들은 1차적으로 철저한 자기 분석이 필요하다. 나는 현재 어떤 생각을 하고 있고 어떤 위치에 있으며 남들에게 보이는 나는 어떨까를 생각하며 자만심을 버리거나 자신감을 채워야 한다. '그동안 너무 나 자신을 과대평가했군' 혹은 '나도 꽤 괜찮은 사람이었어'라고 생각할 수 있다면 자신과 맞는 사람을 좀더 쉽게 만날 수 있다. 여러 남자들에게 가능성을 열어두고 사랑할 기회를 호시탐탐 노리는 당신의 모습은 그대로 가져가되 현실적인 자기 파악에 들어가보자는 말씀.",["1.종료", "2.다시"])
qEndD = Quiz("[D type] 러브지수 90~100% '끓어오르는 피를 주체할 수 없어!' 활화산형 사랑할 준비도, 확실하게 타오를 준비도 확실히 돼 있는 당신. 그런데 왜 남자가 없는 걸까? 과도한 에너지가 문제일 수 있다. 사람과 사람이 만나면, 특히 호감 가는 사람들끼리 마주하면 일종의 전파 같은 것이 흐르는데 그것으로 이 사람이 나에게 얼마나 관심이 있는지 무관심한지 알 수 있다고 한다. 좋은 티 팍팍 내는 당신, 말하지 않아도 얼굴에 사랑에 빠졌다고 써 있다. 누군가에게 빠지는 것을 나쁘다고 할 수만은 없다. 문제는 그런 감정이 자주 일어난다는 것. 애정이 흘러넘치다 보니 이 남자 저 남자 건드리다가 한 명도 못 건지는 불상사가 일어나기도 한다. 열정적인 연애를 하지 못하는 상황이라면 보험적인 의미로라도 남자를 곁에 두었으면 좋겠다는 당신의 욕심은 자칫 당신을 한없이 외롭게 만들 수도 있다. 이런 유형에게 가장 필요한 것은 그를 만났을 때 느끼는 감정이 진짜 사랑인지 가슴에 손을 얹고 냉정하게 판단해보는 것. 얘를 만나면 이래서 좋고 쟤를 만나면 저래서 좋다는 공식은 사랑하는 사람을 만드는 공식에 적용되지 않는다. 또 하나, 사랑에 충만한 사람일수록 외로움도 많이 탄다는 사실. 옆에 누군가가 없으면 우울증에 걸리기 십상이므로 사랑이 아닌 다른 것에 열정을 쏟는 마음가짐이 필요하다.",["1.종료", "2.다시"])

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