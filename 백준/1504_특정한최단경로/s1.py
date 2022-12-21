import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import defaultdict
from heapq import heappush, heappop


n, e = map(int, input().split())
nodes = defaultdict(list)
for _ in range(e):
    a, b, c = map(int, input().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))
v1, v2 = map(int, input().split())


def dijkstra(start):
    dists = [1e9] * (n + 1)
    dists[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)

        if dists[now] < dist:
            continue

        for i, cost in nodes[now]:
            if dist + cost < dists[i]:
                dists[i] = dist + cost
                heappush(q, (dist + cost, i))

    return dists


one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
ans = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(ans if ans < 1e9 else -1)
