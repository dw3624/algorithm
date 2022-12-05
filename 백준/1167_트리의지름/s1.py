# 임의의 두 점 사이의 길이 중 가장 긴 트리의 지름을 구하는 문제입니다.
# 다음과 같은 순서로 생각해볼 수 있습니다.
# 1. 입력값을 바탕으로 트리를 생성합니다.
# 2. 임의의 점/시작 정점에서 가장 먼 정점을 탐색하고 거리를 계산합니다.
# 3. 찾은 정점으로부터 가장 먼 정점을 탐색해 거리를 계산합니다.

import sys
sys.stdin = open('input.txt')

from collections import defaultdict
v = int(input())
trees = defaultdict(list)

for _ in range(v):
    input_lst = list(map(int, input().split()))
    for i in range(1, len(input_lst) - 1, 2):
        trees[input_lst[0]].append((input_lst[i], input_lst[i + 1]))

def dfs(sn):
    for nv, w in trees[sn]:
        if visit[nv] == -1:
            visit[nv] = visit[sn] + w
            dfs(nv)
    return

visit = [-1] * (v + 1)
visit[1] = 0
dfs(1)
sr = visit.index(max(visit))

visit = [-1] * (v + 1)
visit[sr] = 0
dfs(sr)
print(max(visit))