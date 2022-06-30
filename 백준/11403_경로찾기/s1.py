import sys
sys.stdin = open('input.txt')

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
res = [[0]*(N) for _ in range(N)]

def dfs(r):
    for c in range(N):
        if mat[r][c] and not visit[c]:
            visit[c] = 1
            dfs(c)

visit = [0]*N
for r in range(N):
    dfs(r)
    for c in range(N):
        if visit[c]: res[r][c] = 1
    visit = [0]*N

[print(r) for r in res]