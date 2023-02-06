class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def print_nodes(start):
    current = start
    if current == None :
        return
    print(current.data, end=' ')
    while current.link != start:  #
        current = current.link
        print(current.data, end=' ')
    print()


def insert_nodes(find_data, insert_data):
    global head, current, pre
    if head.data == find_data:
        node = Node(insert_data)
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(insert_data)
            node.link = current
            pre.link = node
            return

    node = Node(insert_data)
    current.link = node
    node.link = head


def delete_nodes(delete_data):
    global head, current, pre

    if head.data == delete_data:
        current = head
        head = head.link
        last = head  #
        while last.link != current:  #
            last = last.link  #
        last.link = head  #
        del current
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del current
            return


def find_nodes(find_data):
    global head, current, pre

    current = head
    if current.data == find_data:
        return current

    while current.link != head:  #
        current = current.link
        if current.data == find_data:
            return current

    return Node(None)


def is_find(find_data):
    """
    연결 리스트안에서 원소 존재 여부 판정 함수
    :param find_data: 찾고자 하는 원소. str
    :return: 연결 리스트안에서 원소가 존재하면 True리턴 아니면 False
    """

    global head, current, pre

    current = head
    if current.data == find_data:
        return True

    while current.link != head:  #
        current = current.link
        if current.data == find_data:
            return True

    return False

head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


if __name__ == "__main__":
    node = Node(data_array[0])
    head = node
    node.link = head

    for data in data_array[1:]:
        pre = node
        node = Node(data)
        pre.link = node
        node.link = head


    print(is_find('꼬부기'))
    print(is_find('성윤모'))
    print(find_nodes('꼬부기').data)
    print(find_nodes('김인하').data)
    print(find_nodes('피카츄').data)

    # print_nodes(head)
    # delete_nodes("피카츄")
    # print_nodes(head)
    # delete_nodes("파이리")
    # print_nodes(head)
    # delete_nodes("김인하")
    # print_nodes(head)

    # print_nodes(head)
    # insert_nodes("피카츄", "잠만보")
    # print_nodes(head)
    # insert_nodes("파이리", "어니부기")
    # print_nodes(head)
    # insert_nodes("성윤모", "거북왕")
    # print_nodes(head)