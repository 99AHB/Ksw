# def find_and_insert_data(pokemon, k_count) :
# 	findPos = -1
# 	for i in range(len(pokemons)):
# 		pair = pokemons[i]
# 		if k_count <= pair[1]:
# 			findPos = i
# 			break
# 	if findPos == -1:
# 		findPos = len(pokemons)
#
# 	insert_data(findPos, [pokemon, k_count])
#
#
# def insert_data(position, pokemon):
# 	if position < 0 or position > len(pokemons):
# 		print("데이터를 삽입할 범위를 벗어났습니다.")
# 		return
#
# 	pokemons.append(None)
# 	kLen = len(pokemons)
#
# 	for i in range(kLen - 1, position, -1):
# 		pokemons[i] = pokemons[i - 1]
# 		pokemons[i - 1] = None
#
# 	pokemons[position] = pokemon
#
#
#
# pokemons = [['피카츄', 300], ['꼬부기', 500], ['어니부기', 700], ['거북왕', 1000]]
#
# ## 메인 코드 부분 ##
# if __name__ == "__main__":
#
# 	while True:
# 		pokemon = input("새로운 몬스터 : ")
# 		hp = int(input("체력 : "))
# 		find_and_insert_data(pokemon, hp)
# 		print(pokemons)

class Node:
	def __init__(self):
		self.data = None
		self.link = None

	# def __repr__(self):
	# 	return f'포켓몬스터!'


def print_nodes(start):
    current = start
    if current == None :
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link  # 다음 노드로 이동
        print(current.data, end=' ')
    print()


memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_nodes(head)
    print(memory)
    # print(node.data)
    # print(pre.data)