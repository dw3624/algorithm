import sys
sys.stdin = open('input.txt')


import sys
from heapq import heappush, heappop


input = sys.stdin.readline
n = int(input())
m = int(input())
nodes = [[] for _ in range(n+1)]
costs = [1e9] * (n + 1)
for _ in range(m):
    a, b, w = map(int, input().split())
    nodes[a].append([b, w])
start, end = map(int, input().split())


def dijkstra(s):
    costs[s] = 0
    heap = []
    heappush(heap, [0, s])
    while heap:
        w, s = heappop(heap)
        if costs[s] < w:
            continue
        for ns, nw in nodes[s]:
            if costs[ns] > w + nw:
                costs[ns] = w + nw
                heappush(heap, [w + nw, ns])


dijkstra(start)
print(costs[end])