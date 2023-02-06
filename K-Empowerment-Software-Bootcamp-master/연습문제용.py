# # 5-1 편의점 관리하기
# import random
# import math
#
# class Node():
#     def __init__(self):
#         self.data = None
#         self.link = None
#
# def printStores(start):
#     current = start
#     if current == None:
#         return
#
#     while current.link != head :
#         current = current.link
#         x, y = current.data[1:]
#         print(current.data[0], '편의점, 거리:', math.sqrt(x*x + y*y))
#     print()
#
# def makeStoreList(store) :
#     global memory,head,current,pre
#
#     node = Node()
#     node.data = store
#     memory.append(node)
#
#     if head == None:
#         head = Node
#         node.link = head
#         return
#
#     nodeX, nodeY = node.data[1:]
#     nodeDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
#     headX, headY = head.data[1:]
#     headDist = math.sqrt(headX*headX + headY*headY)
#
#     if headDist > nodeDist:
#         node.link = head
#         last = head
#         while last.link != head:
#             last = last.link
#         last.link = node
#         head = node
#         return
#
#     current = head
#     while current.link != head:
#         pre = current
#         current = current.link
#         currentX,currentY = current.data[1:]
#         currentDist = math.sqrt(currentX*currentX + currentY*currentY)
#         if currentDist > nodeDist :
#             pre.link = node
#             node.link = current
#             return
#
#     current.link = node
#     node.link = head
#
# memory = []
# head, current, pre = None, None, None
#
# if __name__ == "__main__":
#
#     storeArray = []
#     storeName = 'A'
#     for _ in range(10):
#         store = (storeName, random.randint(1,100), random.randint(1,100))
#         storeArray.append(store)
#         storeName = chr(ord(storeName) + 1)
#
#     for store in storeArray:
#         makeStoreList(store)
#
#     printStores(head)








