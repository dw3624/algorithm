import sys
sys.stdin = open('input.txt')


def square(r1, c1, r2, c2):
    for r in range(r1, r2):
        for c in range(c1, c2):
            mat[r][c] = 1


def bfs(sr, sc):
    res = 1
    visit[sr][sc] = 1
    q = [(sr, sc)]
    while q:
        r, c = q.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and not visit[nr][nc] and not mat[nr][nc]:
                q.append((nr, nc))
                res += 1
                visit[nr][nc] = 1
    return res

m, n, k = map(int, input().split())
mat = [[0] * n for _ in range(m)]
visit = [[0] * n for _ in range(m)]
cnt = 0
results = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    r1, c1, r2, c2 = m - y2, x1, m - y1, x2
    square(r1, c1, r2, c2)

for r in range(m):
    for c in range(n):
        if not mat[r][c] and not visit[r][c]:
            result = bfs(r, c)
            results.append(result)
            cnt += 1
results.sort()

print(cnt)
print(*results)
