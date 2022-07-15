import sys
sys.stdin = open('input.txt')

# 시간초과
# N = int(input())
# heap = []
# for _ in range(N):
#     x = int(input())
#     if x == 0:
#         # 배열에서 절댓값 가장 작은 값 출력
#         # 해당 값 배열에서 제거
#         if heap:
#             print(heap.pop(0)[0])
#         else:
#             print(0)
#     else:
#         # x 배열에 추가
#         heap.append((x, x**2))
#         heap.sort(key = lambda x: (x[1], x[0]))

import sys
import heapq

N = int(input())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        # 배열에서 절댓값 가장 작은 값 출력
        # 해당 값 배열에서 제거
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        # x 배열에 추가
        heapq.heappush(heap, (x**2, x))
