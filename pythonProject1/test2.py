class Cal():
    def __init__(self,result=0):
        self.result = result
    def plus(self, num):
        self.result += num
    def minus(self,num):
        self.result -= num
    def cross(self, num):
        self.result = self.result*num
    def div(self, num):
        self.result = self.result/num
    def clear(self):
        self.result = 0

c1 = Cal()
c1.plus(3)

print(c1.result)
c1.minus(1)

print(c1.result)
c1.cross(5)

print(c1.result)
c1.div(2)
print(c1.result)
c1.clear()

print(c1.result)