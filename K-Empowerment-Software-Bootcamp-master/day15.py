def insert_data(idx, pokemon):
    if idx < 0 or idx > len():
        print("Out of range!")
        return

    pokemons.append(None)

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon


def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None

    # self 3-1
    # for i in range(len_pokemons - idx):
    #     pokemons.pop()
    for i in range(idx + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None

    pokemons.pop()



def add_data(pokemon):
    """
    선형 리스트의 맨 뒤에 원소 삽입
    :param pokemon:str
    :return:
    """
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemons

pokemons=[]

if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]
    print(pokemons)
    #insert_data(3, '어니부기')
    delete_data(1)
    print(pokemons)
    # #insert_data(6, '거북왕')
    delete_data(3)
    print(pokemons)
    add_data('터검니')
    print(pokemons)
    while True:
        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

        if (select == 1):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif (select == 2):
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(pokemons)
        elif (select == 3):
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(pokemons)
        elif (select == 4):
            print(pokemons)
            # exit()
            break
        else:
            print("menu에서 고르세요.")
            continue