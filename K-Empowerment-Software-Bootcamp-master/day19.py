## 함수 선언 부분 ##
import random
def quickSort(ary) :
    global count

    n = len(ary)
    if n <= 1:  # 정렬할 리스트의 개수가 1개 이하면
        return ary

    pivot = ary[n // 2]  # 기준값을 중간값으로 지정
    leftAry, rightAry = [], []

    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)

    return quickSort(leftAry) + [pivot] + quickSort(rightAry)


## 전역 변수 선언 부분 ##
dataAry = []
count = 0

## 메인 코드 부분 ##
dataAry=[random.randint(0,200)for _ in range(20)]
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)
print('##', count, "회 로 정렬 완성")




