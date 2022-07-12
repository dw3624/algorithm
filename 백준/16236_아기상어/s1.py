import sys
sys.stdin = open('input.txt')


def bfs(r, c):
    global size
    visit = [[0] * N for _ in range(N)]
    visit[r][c] = 1
    dist = [[0] * N for _ in range(N)]
    fish = []

    q = [(r, c)]
    while q:
        r, c = q.pop(0)
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                if mat[nr][nc] <= size or not mat[nr][nc]:
                    visit[nr][nc] = 1
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                if 0 < mat[nr][nc] < size:
                    fish.append((nr, nc, dist[nr][nc]))
    if not fish:
        return -1, -1, -1
    fish.sort(key=lambda x: (x[2], x[0], x[1]))
    return fish[0][0], fish[0][1], fish[0][2]


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
size = 2

for r in range(N):
    for c in range(N):
        if mat[r][c] == 9:
            sr, sc = r, c
            break

eat = 0
res = 0
while True:
    mat[sr][sc] = 0
    nr, nc, dist = bfs(sr, sc)
    if nr == -1:
        break
    mat[nr][nc] = 9
    sr, sc = nr, nc
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    res += dist
print(res)