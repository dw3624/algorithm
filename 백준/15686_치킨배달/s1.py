# 시간초과

import sys
sys.stdin = open('input.txt')


from copy import deepcopy


def distance(q, m):
    global res
    total_dist = 0
    visit = [[0] * N for _ in range(N)]
    for sr, sc, sd in q:
        visit[sr][sc] = 1
    while q:
        sr, sc, dist = q.pop(0)
        for d in range(4):
            nr, nc = sr + dr[d], sc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                visit[nr][nc] = 1
                q.append((nr, nc, dist+1))
                if m[nr][nc] == 1:
                    total_dist += dist+1
                if total_dist > res:
                    return
    res = min(res, total_dist)
    return


def close(lst):
    if len(lst) == M:
        q = lst.copy()
        tmp_mat = deepcopy(mat)
        distance(q, tmp_mat)
        return
    for chick in chicken:
        if chick not in lst:
            lst.append(chick)
            close(lst)
            lst.pop()


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
res = 1e9
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
chicken = []
for r in range(N):
    for c in range(N):
        if mat[r][c] == 2:
            chicken.append((r, c, 0))

close([])
print(res)