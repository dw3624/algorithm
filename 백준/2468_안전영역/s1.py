import sys
sys.stdin = open('input.txt')


def cnt(sr, sc, height):
    q = [(sr, sc)]
    visit[sr][sc] = 1
    while q:
        r, c = q.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0<=nr<n and 0<= nc < n and not visit[nr][nc] and area[nr][nc] > height:
                visit[nr][nc] = 1
                q.append((nr, nc))


n = int(input())
rains = []
area = []
res = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    area.append(tmp)
    rains.extend(tmp)
rains = list(set(rains))
rains.sort()

for rain in rains:
    visit = [[0] * n for _ in range(n)]
    tmp_cnt = 0
    for r in range(n):
        for c in range(n):
            if area[r][c] > rain and not visit[r][c]:
                cnt(r, c, rain)
                tmp_cnt += 1
    res = max(res, tmp_cnt)
print(res) if res else print(1)