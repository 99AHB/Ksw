import random

small = random.choice([True, False])
print(small)
green = random.choice([True, False])
print(green)

# small = False
# green = False

if small:
    if green:
        print('완두콩')
    else:
        print('체리')
else:
    if green:
        print('수박')
    else:
        print('호박')


# import random
#
# secret = random.randint(1, 10)
# guess = int(input('정답은 ? '))
#
# if secret == guess:
#     print("정답 입니다!")
# elif guess > secret:
#     print(f"정답 보다 큰 수 입니다. 정답은 {secret}")
# else:
#     print(f"정답 보다 작은 수 입니다. 정답은 {secret}")
