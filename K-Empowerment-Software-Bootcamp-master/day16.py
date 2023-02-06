def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    return False


def is_stack_empty():
    global SIZE, stack, top
    if top >= SIZE - 1:
        return True
    return False


def push():
    global SIZE, stack, top
    if is_stack_full():
        print("Stack is FULL!")
        return
    top = top + 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack ifs EMPTY~")
        return
    temp = stack[top]
    stack[top] = None
    top = top - 1
    return temp

def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack ifs EMPTY~")
        return None
    return stack[top]


SIZE = int(input("Stack Size : "))
stack = [None for _ in range(SIZE)]
top = -1


if __name__ == "__main__":
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

        while (select != 'X' and select != 'x'):
            if select == 'I' or select == 'i':
                data = input("입력할 데이터 ==> ")
                push()
                print("스택 상태 : ", stack)
            elif select == 'E' or select == 'e':
                data = pop()
                print("추출된 데이터 ==> ", data)
                print("스택 상태 : ", stack)
            elif select == 'V' or select == 'v':
                data = peek()
                print("확인된 데이터 ==> ", data)
                print("스택 상태 : ", stack)
            else:
                print("입력이 잘못됨")

            select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

        print("프로그램 종료!")