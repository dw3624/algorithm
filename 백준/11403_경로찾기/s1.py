import sys
sys.stdin = open('input.txt')

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

def dfs(r):
    for c in range(N):
        if mat[r][c] and not visit[c]:
            visit[c] = 1
            dfs(c)


for r in range(N):
    visit = [0] * N
    dfs(r)
    for c in range(N):
        if visit[c]: print(1, end=' ')
        else: print(0, end=' ')
    print()