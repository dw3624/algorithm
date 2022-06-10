import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int, input().split())
q = deque([N])
visit = [0] * 100001

while q:
    v = q.popleft()

    if v == K:
        print(visit[v])
        break

    for i in (v-1, v+1, v*2):
        if 0 <= i <= 100000 and not visit[i]:
            visit[i] = visit[v] + 1
            q.append(i)