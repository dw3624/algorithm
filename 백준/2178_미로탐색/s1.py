import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
mat = [[0]*(M+1)]
for _ in range(N):
    mat.append([0]+list(map(int, input())))
visit = [[0]*(M+1) for _ in range(N+1)]
visit[1][1] = 1

q = [(1, 1)]
while q:
    r, c = q.pop(0)
    if r == N and c == M:
        break

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 1 <= nr <= N and 1 <= nc <= M and mat[nr][nc] and not visit[nr][nc]:
            q.append((nr, nc))
            visit[nr][nc] = visit[r][c] + 1

print(visit[N][M])