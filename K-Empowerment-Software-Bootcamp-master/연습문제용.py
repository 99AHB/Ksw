# 6-1 헨젤과 그레텔
import random

def isStackFull():
    global SIZE,stack,top
    if (top >= SIZE - 1) :
        return True
    else :
        return False

def isStackEmpty():
    global SIZE, stack, top
    if (top == - 1) :
        return
    else :
        return False

def push(data):
    global SIZE,stack,top
    if (isStackFull()) :
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        return None
    return stack[top]

SIZE = 10
stack = [None for i in range(SIZE)]
top = -1

if __name__=="__name__":

    stonecl = ["빨강", "주황", "노랑", "초록", "파랑", "보라"]
    random.shuffle(stonecl)

    print("과자집으로 가는길 : ", end='  ')
    for stone in stonecl:
        push(stone)
        print(stone, "-->", end=' ')
    print("과자집")

    print("우리집으로 돌아 가는길 : ", end='  ')
    while True:
        stone = pop()
        if stone== None:
            break
        print(stone, "-->", end=' ')
    print("우리집")











