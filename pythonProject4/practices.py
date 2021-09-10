

a = input("값을 입력 : ")
all_str = []
for i in range(65,91) :
    all_str.append(chr(i))
for i in range(97,123) :
    all_str.append(chr(i))


numalpha = 0
space = 0
num = 0
for i in a :
    if i in all_str :
        numalpha +=1
    if i.isnumeric() :
        num +=1
    if i == " " :
        space +=1
print("알파벳 수 : ", numalpha)
print("빈칸 수 :",space)
print("숫자 수 : ",num)