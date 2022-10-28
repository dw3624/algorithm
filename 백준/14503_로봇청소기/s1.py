# 런타임 에러 (RecursionError)
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
sr, sc, sd = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
ds = [
    [(0, -1, 3), (-1, 0, 0), (0, 1, 1), (1, 0, 2)],  # 북: 좌상우하
    [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)],  # 동: 상우하좌
    [(0, 1, 1), (1, 0, 2), (0, -1, 3), (-1, 0, 0)],  # 남: 우하좌상
    [(1, 0, 2), (0, -1, 3), (-1, 0, 0), (0, 1, 1)]  # 서: 하좌상우
]


def clean(r, c, d, cnt):
    mat[r][c] = 2
    dirs = ds[d]

    if cnt >= 4:
        bdr, bdc = dirs[-1][0], dirs[-1][1]
        bnr, bnc = r + bdr, c + bdc
        if 0 <= bnr < n and 0 <= bnc < m:
            if mat[bnr][bnc] != 1:
                return clean(bnr, bnc, d, 0)
            else:
                return

    for dr, dc, dd in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if not mat[nr][nc]:
                return clean(nr, nc, dd, 0)
            else:
                return clean(r, c, dd, cnt + 1)


clean(sr, sc, sd, 0)

res = 0
for row in mat:
    res += row.count(2)
print(res)