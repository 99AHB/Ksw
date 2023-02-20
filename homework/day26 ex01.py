import random

def binSearch(array, fData):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if fData == array[mid]:
            return mid
        elif fData > array[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

data_array = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell_array = [random.choice(data_array) for _ in range(20)]

print('#오늘 판매된 전체 물건(중복O, 정렬X) -->', sell_array)
sell_array.sort()
print('#오늘 판매된 전체 물건(중복O, 정렬O) -->', sell_array)
sellProduct = list(set(sell_array))
print('#오늘 판매된 물품 종류(중복x) -->', sellProduct)

countList = []
for product in sellProduct:
    count = 0
    pos = 0
    while pos != -1:
        pos = binSearch(sell_array, product)
        if pos != -1:
            count += 1
            del (sell_array[pos])
    countList.append((product, count))

print()
print("결산 결과 ==>", countList)
