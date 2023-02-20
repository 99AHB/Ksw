import random

def seqSearch(ary, fData):
    global count
    position = -1
    for i in range(len(ary)):
        count += 1
        if ary[i] == fData:
            position = i
            break
    return position


def binSearch(ary, fData):
    global count
    start = 0
    end = len(ary) - 1

    while start <= end:
        count += 1
        mid = (start + end) // 2

        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


dataArray, sortedArray = [], []
findData = 7878
count = 0

dataArray = [random.randint(0, 999999) for _ in range(1000000)]
dataArray.insert(random.randint(0, 1000000), findData)
sortedArray = sorted(dataArray)

print('#비정렬 배열(100만개) -->', dataArray[0:5], '~~~~', dataArray[-5:len(dataArray)])
print('#정렬 배열(100만개) -->', sortedArray[0:5], '~~~~', sortedArray[-5:len(sortedArray)])

count = 0
pos = seqSearch(dataArray, findData)
if pos != -1:
    print('순차 검색(비정렬 데이터) -->', count, '회')

count = 0
pos = binSearch(sortedArray, findData)
if pos != -1:
    print('이진 검색(정렬 데이터) -->', count, '회')
