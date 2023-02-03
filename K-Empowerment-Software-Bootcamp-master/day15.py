def find_and_insert_data(friend, K_count):
    findPos = -1
    for i in range(len(kakao)):
        pair = kakao[i]
        if K_count > pair[1]:  #pair는 숫자를 의미한다
            findPos = i
            break
        if findPos == -1:
            findPos = len(kakao)

        insert_data(findPos, (friend, K_count))


def insert_data(position, friend):
    if position < 0 or position > len(kakao):
        print("데이터 삽입 범위를 초과하였습니다.")
        return

    kakao.append(None)
    kLen = len(kakao)

    for i in range(kLen -1, position -1):
        kakao[i] = kakao[i-1]
        kakao[i-1] = None

    kakao[position] = friend


kakao = [('다현', 200),('정현',150),('쯔위', 90),('사나', 30),('지효',150)]


if __name__ == "__main__":

    while True:
        data = input("추가할 친구 --> ")
        count = int(input("카톡 횟수__> "))
        find_and_insert_data(data, count)
        print(kakao)