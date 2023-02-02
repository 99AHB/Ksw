import random

limits = 20
tweets = "pass" * random.randint(1, 10)  # 1에서 10 사이의 정수가 임의로 발생
diff = limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f'글자 수 {abs(diff)}초과')
