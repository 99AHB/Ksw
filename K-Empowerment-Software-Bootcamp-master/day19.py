import tkinter as tk

memos = [None for _ in range(100)]  # 전역 리스트
memos[0], memos[1] = 0, 1


def fibo_memo_recu(n):
    """
    재귀함수에 Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global memos

    if n <= 1:
        return memos[n]

    if memos[n] is not None:  # 전역 메모리 memos에 이전에 계산한 결과 값이 존재하면
        return memos[n]

    memos[n] = fibo_memo_recu(n-2) + fibo_memo_recu(n-1)  # 처음 방문하는 n이면
    return memos[n]


def fact_recu(n):
    if n == 1 :
        return 1
    else:
        return n * fact_recu(n-1)


def factorial_input():
    lbl_result.config(text=f"팩토리얼 출력 결과 : {fact_recu(int(en_num_input.get()))}")
    input_number = int(en_num_input.get())

def fibonacci_input():
    lbl_result.config(text=f"피보나치 출력 결과 : {fibo_memo_recu(int(en_num_input.get()))}")
    input_number = int(en_num_input.get())

win = tk.Tk() # 윈도우 생성
win.title("Calculator") # 피보나치, 팩토리얼 계산기
win.geometry("250x150")


en_num_input = tk.Entry() # 텍스트 입력 상자
lbl_result = tk.Label(text="계산기 출력 결과 : ")
btn_fact = tk.Button(text="팩토리얼", command=factorial_input)
btn_fibo = tk.Button(text="피보나치", command=fibonacci_input)

en_num_input.pack()
lbl_result.pack()
btn_fact.pack(fill='x')
btn_fibo.pack(fill='x')

win.mainloop()




