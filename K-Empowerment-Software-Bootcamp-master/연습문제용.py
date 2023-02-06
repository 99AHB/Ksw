# 5-2 이중 연결 리스트 구현
class NodeA():
    def __init__(self):
        self.Alink=None
        self.data=None
        self.Zlink=None

def printNodes(start):
    current = start
    if current.Alink ==None:
        return
    print("정방향-->", end=' ')
    print(current.data,end = ' ')
    while current.Alink !=None:
        current = current.Alink
        print(current.data, end=' ')
    print()
    print("역방항-->", end=' ')
    print(current.data,end=' ')
    while current.Zlink !=None:
        current = current.Zlink
        print(current.data, end=' ')


    memory = []
    head, current, pre = None, None, None
    dataName = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__ == "__name__":

    node = NodeA()
    node.data = dataArray[0]
    head= node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = NodeA()
        node.data = data
        pre.Alink = node
        pre.Zlink = pre
        memory.append(node)

    printNodes(head)











