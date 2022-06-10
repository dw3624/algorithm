import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
visit = [0] * 100001
q = [N]


def bfs(v):
    q = [v]
    while q:
        v = q.pop(0)
        if v == K:
            return visit[v]

        for i in (v-1, v+1, v*2):
            if 0 <= i <= 100000 and not visit[i]:
                visit[i] = visit[v] + 1
                q.append(i)

print(bfs(N))