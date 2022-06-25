import sys
sys.stdin = open('input.txt')

import sys
from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append([i, j, k])

dl = [0, 0, 0, 0, -1, 1]  # level
dr = [-1, 1, 0, 0, 0, 0]  # row
dc = [0, 0, -1, 1, 0, 0]  # column
while q:
    l, r, c = q.popleft()

    for d in range(6):
        nl = l + dl[d]
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nl < H and 0 <= nr < N and 0 <= nc < M and box[nl][nr][nc] == 0:
            box[nl][nr][nc] = box[l][r][c] + 1
            q.append([nl, nr, nc])

day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
        day = max(day, max(box[i][j]))
print(day-1)
