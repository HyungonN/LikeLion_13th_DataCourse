import moduletest1
def right_move():
    print("오른쪽 이동")
    moduletest1.loc[1] +=1
def left_move():
    print("왼쪽 이동")
    moduletest1.loc[1] -=1