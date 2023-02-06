class Node:
	def __init__(self):
		self.data = data
		self.link = None

def print_nodes(start):
    current = start
    if current == None :
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link  # 다음 노드로 이동
        print(current.data, end=' ')
    print()

def insert(find_data, insert_data):
    global memory, head, current, property
    if head.data == find_data:  # 첫 번째 노드 삽입
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        return

    current = head
    while current.link != None:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()  # 마지막 노드 삽입
    node.data = insert_data
    current.link = node

def delete_nodes(delelt_data):
    global memory, head, current, pre

    if head.data == delelt_data:
        current = head
        print("첫번쨰 노드가 삭제됨")
        head = head.link
        del current
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == delelt_data:
            print("중간 노드가 삭제됨")
            pre.link = current.link
            del current
            return

    print("삭제할 노드를 찾기 못함")

    # 삭제할 데이터를 못찾는 경우 함수 종료

def find_nodes(find_data):
    global memory, head, current, pre

    current = head
    if current.data == find_data:
        return current

    while current.link !=None:
        current = current.link



memory = []
head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]

if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node
    memory.append(node)

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    print_nodes(head)
    insert_nodes("피카츄", "잠만보")
    print_nodes(head)
    insert_nodes("파이리", "어니부기")
    print_nodes(head)
    insert_nodes("성윤모", "거북왕")
    delete_nodes("잠만보")
    print_nodes(head)
    delete_nodes("어니부기")
    print_nodes(head)
    delete_nodes("강찬석")
    print_nodes(head)
    print_nodes(find_nodes("파이리"))
    print_nodes(find_nodes("박민석"))
