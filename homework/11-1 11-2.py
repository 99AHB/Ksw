# # 성적별로 조 편성하기
# def scoreSort(ary):
#     n = len(ary)
#     for end in range(1,n):
#         for cur in range(end,0,-1):
#             if (ary[cur-1][1] > ary[cur][1]):
#                 ary[cur-1],ary[cur]=ary[cur],ary[cur-1]
#     return ary
#
# scoreAry = [['선미',88],['초아',99],['화사',71],['영탁',78],['영웅',67],['민호',92]]
#
# print('정렬 전 -->',scoreAry)
# scoreAry = scoreSort(scoreAry)
# print('정렬 후-->', scoreAry)
#
# print('##성적별 조 편성표##')
# for i in range(len(scoreAry)//2):
#     print(scoreAry[i][0], ':',scoreAry[len(scoreAry)-1-i][0])

# # 2차원 배열의 중앙값 찾기
# def selectionSort(ary):
#     n=len(ary)
#     for i in range(0,n-1):
#         Idx = i
#         for k in range(i+1,n):
#             if (ary[Idx] > ary[k]):
#                 Idx = k
#         tmp = ary[i]
#         ary[i] = ary[Idx]
#         ary[Idx] = tmp
#
#     return ary
#
# ary2 = [[55, 33, 250, 44],
#         [88, 1, 76, 23],
#         [199, 222, 38, 47],
#         [155,145,20,99]]
# ary1 = []
#
#
# for i in range(len(ary2)):
#     for k in range(len(ary2[i])):
#         ary1.append(ary2[i][k])
#
# print('1차원 변경 후,정렬 전-->',ary1)
# ary1 = selectionSort(ary1)
# print('1차원 변경 후, 정렬 후-->', ary1)
# print('중앙값--> ',ary1[len(ary1)//2])