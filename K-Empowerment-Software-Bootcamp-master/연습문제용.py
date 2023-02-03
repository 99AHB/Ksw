# ex
def find_and_insert_data(pokemons,h_count) :
    findPos = -1
    for i in range(len(hp)):
        pair = hp[i]
        if h_count >= pair[1]:
            findPos = i
            break
    if findPos == -1 :
        findPos = len(hp)

    insert_data(findPos, (pokemons, h_count))


def insert_data(position,pokemons):
    if position < 0 or position > len(hp):
        print("입력값을 다시 입력해주세요")
        return

    hp.append(None)
    hLen = len(hp)

    for i in range(hLen -1, position, -1):
        hp[i] = hp[i-1]
        hp[i-1] = None

    hp[position] = pokemons

hp = {"라이츄":200 , "피카츄":150, "파이리":100, "꼬부기":70, "치코리타":1}
sort_hp =sorted(hp.items(),key=lambda x:x[1], reverse=True)
# print(sort_hp)

if __name__ == "__main__":

    while True :
        data = input("추가할 pokemons--> ")
        count = int(input("포켓몬의 체력 입력-->"))
        find_and_insert_data(data,count)
print(sort_hp)















# 1. 선형리스트
# 2. 1
# 3. 4->2->3->1
# 4.