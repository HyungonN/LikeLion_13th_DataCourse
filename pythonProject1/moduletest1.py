###
### 함수 < 클래스(객체) < 모듈(함수, 클래스의 모음) < 라이브러리(패키지)

loc = [0,0] #현재 위치

def forward_move():
    print("앞으로 이동")
    loc[0] +=1

def back_move():
    print("뒤로 이동")
    loc[0] -= 1
