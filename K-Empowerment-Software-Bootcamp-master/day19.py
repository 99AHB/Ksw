def fibo_recu(n) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibo_recu(n-1) + fibo_recu(n-2)


def fibo_iter(n):
    r = list()
    p1, p2 = 1, 1
    for _ in range(n-2):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]


print('피보나치 수 --> 0 1 ')
for i in range(2, 10) :
    #print(fibo_iter(i))   # 빠르게 가능
    print(fibo_recu(i))    # 가면 갈수록 느리다
