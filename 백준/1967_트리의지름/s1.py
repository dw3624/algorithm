import sys
sys.stdin = open('input.txt')


from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 트리 탐색 후 리스트에 길이 저장
def dfs(x, w):
    for t, total in trees[x]:
        if dists[t] == -1:
            dists[t] = total + w
            dfs(t, total + w)

n = int(input())
trees = defaultdict(list)
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    trees[a].append((b, c))
    trees[b].append((a, c))

# 1번 노드에서 가장 먼 노드 탐색
dists = [-1] * (n + 1)
dists[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에서 가장 먼 노드 탐색
start = dists.index(max(dists))
dists = [-1] * (n + 1)
dists[start] = 0
dfs(start, 0)
print(max(dists))