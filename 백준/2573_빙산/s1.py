import sys
sys.stdin = open('input.txt')


def bfs(sr, sc):
    del_lst = []
    visit[sr][sc] = 1
    q = [(sr, sc)]
    while q:
        r, c = q.pop(0)
        sea = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if mat[nr][nc] and not visit[nr][nc]:
                    q.append((nr, nc))
                    visit[nr][nc] = 1
                if not mat[nr][nc]:
                    sea += 1
        del_lst.append((r, c, sea))
    for r, c, sea in del_lst:
        mat[r][c] = max(0, mat[r][c] - sea)


n, m = map(int, input().split())
ice = []
mat = []
for r in range(n):
    row = list(map(int, input().split()))
    for c in range(m):
        if row[c]:
            ice.append((r, c))
    mat.append(row)

year = 0
while ice:
    no_ice = []
    group = 0
    visit = [[0] * m for _ in range(n)]
    for r, c in ice:
        if not visit[r][c]:
            bfs(r, c)
            group += 1
        if not mat[r][c]:
            no_ice.append((r, c))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(no_ice)))
    year += 1

if group <= 1:
    print(0)