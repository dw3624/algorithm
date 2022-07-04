import sys
sys.stdin = open('input.txt')

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

def bfs(r):
    q = [r]
    visit = [0]*N
    while q:
        r = q.pop(0)
        for c in range(N):
            if mat[r][c] and not visit[c]:
                visit[c] = 1
                q.append(c)
    print(*visit)

for r in range(N):
    bfs(r)

