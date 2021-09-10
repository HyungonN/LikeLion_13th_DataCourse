
def cal(op,num1,num2) :
    if op == "+" :
        print("양 값의 합은 ", num1+num2)
    if op =="-" :
        print("양 값의 차는 : ", num1-num2)
    if op == "*":
        print("양 값의 곲은 : ", num1*num2)
    if op == "/" :
        print("양 값의 나눈값은 :", num1/num2)

a = int(input("값1입력 :"))
b = int(input("값2입력 :"))

cal("+",a,b)
cal("-",a,b)
cal("*",a,b)
cal("/",a,b)