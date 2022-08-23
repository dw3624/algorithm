# 시간초과

import sys
sys.stdin = open('input.txt')


def distance(chicken_lst):
    global res
    dist = 0
    for house_r, house_c in house:
        tmp_dist = 1e9
        for chicken_r, chicken_c in chicken_lst:
            tmp = abs(chicken_r - house_r) + abs(chicken_c - house_c)
            tmp_dist = min(tmp_dist, tmp)
        dist += tmp_dist
        if dist > res:
            return
    res = min(res, dist)
    return


def close(lst):
    if len(lst) == M:
        distance(lst)
        return
    for c in chicken:
        if c not in lst:
            lst.append(c)
            close(lst)
            lst.pop()


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
res = 1e9
house = []
chicken = []
for r in range(N):
    for c in range(N):
        if mat[r][c] == 1:
            house.append((r, c))
        elif mat[r][c] == 2:
            chicken.append((r, c))

close([])
print(res)
