import sys
sys.stdin = open('input.txt')


def bfs(sr, sc):
    global s1
    q = [(sr, sc)]

    while q:
        r, c = q.pop(0)
        visit[r][c] = 1

        dr = [0, 0, -1, 1]
        dc = [-1, 1, 0, 0]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and mat[r][c]==mat[nr][nc]:
                q.append((nr, nc))
                visit[nr][nc] = 1
    return 1


N = int(input())
mat = []
for _ in range(N):
    mat.append([t for t in input()])

s1 = 0
visit = [[0]*(N) for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visit[r][c]:
            s1 += bfs(r, c)

for r in range(N):
    for c in range(N):
        if mat[r][c] == 'G':
            mat[r][c] = 'R'

s2 = 0
visit = [[0]*(N) for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visit[r][c]:
            s2 += bfs(r, c)

print(s1, s2)