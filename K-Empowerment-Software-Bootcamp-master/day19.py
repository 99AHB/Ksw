memo = list() # 전역 변수를 한 번 처리한 결과 값을 저장
def fibo_memo(n) :
    global memo
    memo = [1, 1]
    """
    Memoization(DP)를 사용한 피보나치 수열 처리 함수
    :param n: 
    :return: 
    """
    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n+1):
            memo.append(memo[i-1]+ memo[i-2])
        return memo[n]

def fibo_recu(n):
    r = list()
    p1, p2 = 1, 1
    for _ in range(n-2):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]


print('피보나치 수 --> 0 1 ')
for i in range(2, 10) :
    # print(fibo_iter(i))   # 빠르게 가능
    print(fibo_recu(i))    # 가면 갈수록 느리다
