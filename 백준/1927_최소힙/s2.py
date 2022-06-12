# import sys
# sys.stdin = open('input.txt')

import sys
import heapq

# N = int(input())
N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    # x = int(input())
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)