#변수, 클래스, 함수

likecolor = 'navy'

def mydream(a):
    return a*1

class myact1():
    def __init__(self,result=0):
        self.result = result
    def walk(self):
        action = "걷는다"
        return action
class myact2():
    def __init__(self, rest):
        self.rest = rest
    def sleep(self):
        sleeptime = self.rest
        return sleeptime
if __name__ == "__main__":
    print('mydream 시작')