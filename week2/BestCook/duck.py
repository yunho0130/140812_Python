__author__ = 'Administrator'

class ASample:
    def doJob(self):
        print("ASample")

class BSample:

    def doJob(self):
        print("BSample")

list = [ASample(), BSample()]
print(list)

for i in list:
    print(i)