## 시간초과

import sys
sys.stdin = open('input.txt')


def bfs(n, k):
    q = [(n, 0)]
    while q:
        x, time = q.pop(0)
        if x == k:
            return time

        q.append((x + 1, time + 1))
        q.append((x - 1, time + 1))
        q.append((x * 2, time))
    return


N, K = map(int, input().split())
res = bfs(N, K)
print(res)